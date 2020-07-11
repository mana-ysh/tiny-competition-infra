# tiny-competition-infra

Tiny experiment manager with mlflow.   
The source codes in mlflow-related parts are based on [mlflow-docker-compose](https://github.com/ymym3412/mlflow-docker-compose)

## Quick start

1. start applications via `docker-compose up`
2. do inference with your own methods, and submit results into evaluation server
    1. `cd mlwork`
    2. `poetry shell`
    3. `make predict && make submit EXPERIMENT_NAME=hello-initial-experiment`
3. then check results on mlflow UI at `localhost:5000`
