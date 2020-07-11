import os

import mlflow
from fastapi import APIRouter, FastAPI, UploadFile, File
from pydantic import BaseModel

from evalapp.data import read_gold_data, read_pred_data
from evalapp.metrics import do_evaluation


TEST_GOLD_PATH = os.path.join(os.path.dirname(__file__), "./test.gold.txt")
TEST_GOLD_DATA = read_gold_data(TEST_GOLD_PATH)

mlflow.set_experiment(os.environ["COMPETITION_NAME"])
api_v1_router = APIRouter()


class MessageResponse(BaseModel):
    msg: str


@api_v1_router.post("/evaluation_batch_sync/{run_name}")
def evaluation_batch_sync(run_name: str, file: UploadFile = File(...)) -> MessageResponse:
    try:
        pred_ys = read_pred_data(file.file.read().decode("utf-8"))
        assert len(pred_ys) == len(TEST_GOLD_DATA), \
            "Inconsistent length between prediction/gold data: len prediction={}, len gold={}".format(
                len(pred_ys), len(TEST_GOLD_DATA))
        eval_metrics = do_evaluation(TEST_GOLD_DATA, pred_ys)
        with mlflow.start_run(run_name=run_name):
            for (k, v) in eval_metrics.items():
                mlflow.log_metric(k, v)
        return MessageResponse(msg="success: metrics={}".format(eval_metrics))
    except Exception as e:
        return MessageResponse(msg="fail to evaluate because...{}".format(str(e)))


def create_app() -> FastAPI:
    app = FastAPI(title="App")

    app.include_router(api_v1_router, prefix="/api/v1")

    @app.get("/health")
    def health() -> MessageResponse:
        return MessageResponse(msg="I'm healthy")

    return app
