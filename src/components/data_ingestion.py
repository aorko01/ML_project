import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_trasformation import DataTransformationConfig
from src.components.data_trasformation import DataTransformation
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

#all the inputs that are required for data ingestion are stored in a dataclass
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingstion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            # this is the part where we read the dataset
            #we might use a different source in the future for this template code
            
            
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(
                os.path.dirname(self.ingstion_config.train_data_path), exist_ok=True
            )

            df.to_csv(self.ingstion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(
                self.ingstion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.ingstion_config.test_data_path, index=False, header=True
            )

            logging.info("Ingestion of data is completed")

            return (
                self.ingstion_config.train_data_path,
                self.ingstion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys) from e
            logging.info("Exited the data ingestion method or component")


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data, test_data)
    modeltrainer= ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))