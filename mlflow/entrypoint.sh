#/bin/sh

set -eu

DB_URI=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgresql:5432/mlflow-db
DEFAULT_ARTIFACT_ROOT=./artifacts

mlflow server \
    --backend-store-uri ${DB_URI} \
    --default-artifact-root ${DEFAULT_ARTIFACT_ROOT} \
    --host 0.0.0.0 \
    --port 5000
