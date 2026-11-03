import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Giovane Abrantes Bonache")
n = st.slider("Tamanho", 2, 64, 8)
img = np.random.randint(0, 256, (n, n), dtype=np.uint8)
st.image(img, caption=f"Imagem {n}x{n}", width=300)
st.write(img)