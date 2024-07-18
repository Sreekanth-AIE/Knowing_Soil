from Soil_Types import logger
from Soil_Types.pipeline.data_ingestion_stage import DataIngestionPipeline
from Soil_Types.pipeline.base_model_stage import BuildBaseModelPipeline
from Soil_Types.pipeline.training_stage import ModelTrainingPipeline
from Soil_Types.pipeline.evaluation_stage import EvaluationPipeline


if __name__ == '__main__':
    try:
        data_ingestion_instance = DataIngestionPipeline()
        logger.info(f">>>>>> stage {data_ingestion_instance.STAGE_NAME} started <<<<<<")
        data_ingestion_instance.execute_stage()
        logger.info(f">>>>>> stage {data_ingestion_instance.STAGE_NAME} completed <<<<<<\n\nx==========x")

        base_model_instance = BuildBaseModelPipeline()
        logger.info(f">>>>>> stage {base_model_instance.STAGE_NAME} started <<<<<<")
        base_model_instance.execute_stage()
        logger.info(f">>>>>> stage {base_model_instance.STAGE_NAME} completed <<<<<<\n\nx==========x")

        model_training_instance = ModelTrainingPipeline()
        logger.info(f">>>>>> stage {model_training_instance.STAGE_NAME} started <<<<<<")
        model_training_instance.execute_stage()
        logger.info(f">>>>>> stage {model_training_instance.STAGE_NAME} completed <<<<<<\n\nx==========x")

        evaluation_instance = EvaluationPipeline()
        logger.info(f">>>>>> stage {evaluation_instance.STAGE_NAME} started <<<<<<")
        evaluation_instance.execute_stage()
        logger.info(f">>>>>> stage {evaluation_instance.STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

