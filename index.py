

def main():
    print('Classificador de Pneumonia em Raios-X de Pulmão')

    # Imports necessários dentro da função para garantir escopo
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    import numpy as np
    from tensorflow.keras.utils import load_img, img_to_array

    # Diretórios do dataset
    train_dir = 'dataset/train'
    img_height, img_width = 150, 150
    batch_size = 32

    # Geradores de dados
    train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='binary',
        subset='training'
    )
    validation_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='binary',
        subset='validation'
    )

    # Modelo simples
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    print('Treinando modelo...')
    history = model.fit(
        train_generator,
        epochs=5,
        validation_data=validation_generator
    )
    print('Treinamento finalizado!')

    # Avaliação
    loss, acc = model.evaluate(validation_generator)
    print(f'Acurácia na validação: {acc*100:.2f}%')

    # Predição em uma imagem
    img_path = input('Digite o caminho de uma imagem para testar: ')
    if img_path:
        img = load_img(img_path, target_size=(150, 150))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        prob = model.predict(img_array)[0][0]
        print(f'Probabilidade de pneumonia: {prob*100:.2f}%')
        if prob > 0.5:
            print('Pneumonia detectada!')
        else:
            print('Sem pneumonia detectada.')

if __name__ == '__main__':
    main()


import os
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Diretórios do dataset
train_dir = 'dataset/train'
test_dir = 'dataset/test'

# Parâmetros
img_height, img_width = 150, 150
batch_size = 32

# Geradores de dados
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

data_dir = './dataset'
img_height, img_width = 150, 150
batch_size = 32
epochs = 10
num_classes = 2

train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2), 
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(
     optimizer='adam',
     loss='sparse_categorical_crossentropy', 
     metrics=['accuracy']
     )

history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)          

model.save('my_model.h5')

print('Modelo trainado e slavo comn sucesso')

