from src.chicken_classifier import logger
from src.chicken_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.chicken_classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.chicken_classifier.pipeline.stage_03_training import TrainingPipeline
from src.chicken_classifier.pipeline.stage_04_evaluation import EvaluationPipeline
STAGE_NAME =  "Data Ingestion Stage"
try:
    logger.info(f">>>>>  {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>   {STAGE_NAME} completed succesfully <<<<<<<<")
except Exception as e:
        logger.exception(e) 


STAGE_NAME =  "BASE MODEL PREPRATION"
try:
    logger.info(f"**********************************************************************************")
    logger.info(f">>>>>>{STAGE_NAME} stage started <<<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "TRAINING"
try:
    logger.info(f"**********************************************************************************")
    logger.info(f">>>>>>{STAGE_NAME} stage started <<<<<<<") 
    obj = TrainingPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<<\n\n=======================================================================")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "EVALUATION"


try:
    logger.info(f"**********************************************************************************")
    logger.info(f">>>>>>{STAGE_NAME} stage started <<<<<<<") 
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<<\n\n=======================================================================")
except Exception as e:
    logger.exception(e)
    raise e