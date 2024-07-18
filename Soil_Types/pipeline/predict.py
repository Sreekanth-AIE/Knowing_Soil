import os
import numpy as np
from pathlib import Path
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from Soil_Types.constants import *
from Soil_Types.utils.common import read_yaml

print("lo")
class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename
        
    @staticmethod
    def get_required_data():
        config_data = read_yaml(CONFIG_FILE_PATH)
        params_data = read_yaml(PARAMS_FILE_PATH)
        return config_data.prepare_callbacks.checkpoint_model_filepath,\
               config_data.data_ingestion.train_dir,\
               params_data.IMAGE_SIZE[:-1]

    def predict(self):
        model_path, train_dir, img_size = self.get_required_data()
        
        # load model
        model = load_model(model_path)

        test_image = image.load_img(self.filename, target_size = img_size)
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result_idx = np.argmax(model.predict(test_image), axis=1)
        
        classes = os.listdir(Path(train_dir))

        return classes[result_idx]
