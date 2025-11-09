import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt


@st.cache_resource
def carregar_modelo():
    modelo = load_model("./my_model.h5")  
    return modelo


def preprocessar_imagem(img, tamanho=(224, 224)):
    img = img.resize(tamanho)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0 
    return img_array


def prever_pneumonia(modelo, imagem_processada):
    resultado = modelo.predict(imagem_processada)
    return resultado[0][0]  


def pneumonia_detector():
    st.set_page_config(page_title="Pneumonia Detector", layout="centered")
    st.title("🫁 Pneumonia Detector")

    st.markdown("Envie uma radiografia de tórax para detectar pneumonia com Inteligência Artificial.")

    modelo = carregar_modelo()

    imagem_up = st.file_uploader("📤 Faça upload da imagem (.jpg ou .png)", type=["jpg", "jpeg", "png"])

    if imagem_up is not None:
        imagem = Image.open(imagem_up).convert("RGB")
        st.image(imagem, caption="🖼️ Imagem enviada", use_container_width=True)

        imagem_processada = preprocessar_imagem(imagem, tamanho=(150, 150))
        prob = prever_pneumonia(modelo, imagem_processada)
        percentual = prob * 100

        if prob > 0.5:
            diagnostico = "⚠️ **Pneumonia detectada!**"
            cor = "red"
        else:
            diagnostico = "✅ **Sem sinais de pneumonia.**"
            cor = "green"

        st.markdown(f"<h3 style='color:{cor};'>Probabilidade de pneumonia: {percentual:.2f}%</h3>", unsafe_allow_html=True)
        st.markdown(diagnostico)

        # Gráfico de pizza
        labels = ['Pneumonia', 'Saudável']
        values = [percentual, 100 - percentual]
        colors = ['#ff4d4d', '#4da6ff']

        fig, ax = plt.subplots()
        bars = ax.bar(labels, values, color=colors)
        ax.set_ylim(0, 100)
        ax.set_ylabel("Probabilidade (%)")
        ax.set_title("Resultado da Análise")

        # Exibe valores nas barras
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # deslocamento vertical
                        textcoords="offset points",
                        ha='center', va='bottom')

        st.pyplot(fig)



if __name__ == "__main__" or True:
    pneumonia_detector()
