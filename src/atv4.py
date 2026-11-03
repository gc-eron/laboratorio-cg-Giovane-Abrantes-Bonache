import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

st.header("1. Leitura da foto")
col1, col2 = st.columns(2)

foto = Image.open("imagens/gato.jpg")
img = np.array(foto)

foto2 = Image.open("imagens/que mario.jpg")
img2 = np.array(foto2)
col1.image(img)
col2.text(img.shape)
col2.text(img[430, 250])

st.header("2. Canais")
col1, col2 = st.columns(2)

col1.image(img[:, :, 0], caption="R")
col1.image(img[:, :, 1], caption="G")
col1.image(img[:, :, 2], caption="B")

r = np.zeros_like(img)
r[:, :, 0] = img[:, :, 0]

g = np.zeros_like(img)
g[:, :, 1] = img[:, :, 1]

b = np.zeros_like(img)
b[:, :, 2] = img[:, :, 2]

col2.image(r, caption="R")
col2.image(g, caption="G")
col2.image(b, caption="B")

st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (255, 255, 0)
col1.image(quadrado, caption="amarelo")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (100, 155, 50)
col1.image(quadrado, caption="verde")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (150, 105, 150)
col1.image(quadrado, caption="roxo")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (250, 0, 250)
col1.image(quadrado, caption="rosa")

quadrado = np.zeros((80, 80, 3), dtype=np.uint8)
quadrado[:, :] = (0, 100, 150)
col1.image(quadrado, caption="azul")

col2.image(img2, channels="BGR", caption="mario capitalista")

st.header("4. Tons de cinza")
col1, col2 = st.columns(2)


r = img2[:, :, 0].astype(float)
g = img2[:, :, 1].astype(float)
b = img2[:, :, 2].astype(float)

soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média")

ponderada = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
col2.image(ponderada, caption="ponderada")