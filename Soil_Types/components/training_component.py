import tensorflow as tf
from pathlib import Path
from Soil_Types.entity.config_entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
    
    def get_untrained_model(self):
        # Feteching the  saved untrained model from artifacts after Building_base_model pipeline is executed
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
    
    def train_valid_data_generator(self):
        # setting up **kwargs for Image_Data_Generator from Keras(main config)
        image_data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        # setting up **kwargs for data_flow_from_directory from Keras(secondary config)
        dataflow_form_directory_kwargs = dict(
            directory=self.config.training_data,
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            class_mode='categorical',
            shuffle=True,
            interpolation="bilinear"
        )

        # For datasets that require Augmentation
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **image_data_generator_kwargs
            )
        else:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                **image_data_generator_kwargs
            )

        # Executing the Data Acquisition process for training set
        self.train_set_generator_inst = train_datagenerator.flow_from_directory(
            subset="training",
            **dataflow_form_directory_kwargs
        )
        # executing the Data Acquisition process for validation set
        self.val_set_generator_inst = train_datagenerator.flow_from_directory(
            subset="validation",
            **dataflow_form_directory_kwargs
        )
      

    def train(self, callback_list: list):
        # training the updated base model with the training data and validation data with callbacks
        self.model.fit(
            self.train_set_generator_inst,
            epochs=self.config.params_epochs,
            validation_data=self.val_set_generator_inst,
            callbacks=callback_list
        )
