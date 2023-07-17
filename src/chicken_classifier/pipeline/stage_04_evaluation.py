from src.chicken_classifier import logger
from src.chicken_classifier.components.prepare_callbacks import PrepareCallback
from src.chicken_classifier.config.configuration import ConfigurationManager
from src.chicken_classifier.components.evaluation import Evaluation

STAGE_NAME =  "EVALUATION"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == '__main__':
    try:
        logger.info(f"**********************************************************************************")
        logger.info(f">>>>>>{STAGE_NAME} stage started <<<<<<<") 
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<<\n\n=======================================================================")
    except Exception as e:
        logger.exception(e)
        raise e


