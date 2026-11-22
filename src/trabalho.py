
import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/gato.jpg")
img = np.array(foto.convert("RGB"))

foto2 = Image.open("imagens/que mario.jpg") # melhor visibilidade para a media ponderada la
img2 = np.array(foto2.convert("RGB"))



#-------------------------------------------------------------------
st.header("1. Brilho")
col1, col2 = st.columns(2)

brilho = st.slider("Brilho", -255, 255, 0)

imagem_brilho = img.astype(float) + brilho
imagem_brilho = np.clip(imagem_brilho, 0, 255).astype(np.uint8)

col1.image(img, caption="Original")
col2.image(imagem_brilho, caption="Brilho alterado")





#-------------------------------------------------------------------
st.header("2. Tons de cinza")
col1, col2 = st.columns(2)

r = img2[:, :, 0].astype(float)
g = img2[:, :, 1].astype(float)
b = img2[:, :, 2].astype(float)

soma = r + g + b
media = (soma / 3).astype(np.uint8)

ponderada = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)

col1.image(media, caption="Média")
col2.image(ponderada, caption="Ponderada")




#-------------------------------------------------------------------
st.header("3. Troca de canais")
col1, col2 = st.columns(2)

imagem_canais = np.zeros_like(img)

imagem_canais[:, :, 0] = img[:, :, 2]
imagem_canais[:, :, 1] = img[:, :, 1]
imagem_canais[:, :, 2] = img[:, :, 0]

col1.image(img, caption="Original")
col2.image(imagem_canais, caption="R e B trocados")


#-------------------------------------------------------------------
st.header("4. Espelhamento")
col1, col2 = st.columns(2)

tipo = st.selectbox("Tipo de espelhamento", ["Horizontal", "Vertical"])

if tipo == "Horizontal":
    imagem_espelhada = img[:, ::-1]
else:
    imagem_espelhada = img[::-1, :]

col1.image(img, caption="Original")
col2.image(imagem_espelhada, caption="Espelhada")






#-------------------------------------------------------------------
st.header("5. Pixel art")
col1, col2 = st.columns(2)

k = st.slider("Tamanho dos pixels", 2, 30, 8)

imagem_pequena = img[::k, ::k]
imagem_pixel = imagem_pequena.repeat(k, axis=0).repeat(k, axis=1)

col1.image(img, caption="Original")
col2.image(imagem_pixel, caption="Pixel art")
