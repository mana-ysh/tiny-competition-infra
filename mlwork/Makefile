
PREDICT_INPUT := ./data/test.txt
PREDICT_OUTPUT := ./data/test.pred.txt

EVALUATION_API_HOST := localhost
EVALUATION_API_PORT := 8000
EVALUATION_API_ENDPOINT := ${EVALUATION_API_HOST}:${EVALUATION_API_PORT}/api/v1/evaluation_batch_sync
EXPERIMENT_NAME := kakki-v2



predict:
	python predict.py --pred_in ${PREDICT_INPUT} --pred_out ${PREDICT_OUTPUT}


submit:
	curl -XPOST -F file=@${PREDICT_OUTPUT} ${EVALUATION_API_ENDPOINT}/${EXPERIMENT_NAME}
