from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Starting Data Ingestion: {STAGE_NAME} <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Completed Data Ingestion: {STAGE_NAME} <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

