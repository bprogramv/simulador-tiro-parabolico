import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Proyecto - Simulador de Tiro Parabólico")

# Velocidad & Ángulo

v0 = st.slider("Velocidad inicial (m/s)", 0, 100, 50)
angle = st.slider("Ángulo de lanzamiento (grados)", 0, 90, 45)
g = 9.81

# Cálculos

theta = np.radians(angle)
t_flight = 2 * v0 * np.sin(theta) / g
t = np.linspace(0, t_flight, num=100)
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Mostrar resultados numéricos

alcance = max(x)
altura_maxima = max(y)


st.subheader("Resultados")
st.write(f"Tiempo total de vuelo: {t_flight:.2f} segundos")
st.write(f"Alcance horizontal máximo: {alcance:.2f} metros")
st.write(f"Altura máxima alcanzada: {altura_maxima:.2f} metros")


# Mostrar la gráfica

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Distancia (m)")
ax.set_ylabel("Altura (m)")
ax.set_title("Trayectoria del proyectil")
st.pyplot(fig)

# Firma

st.write(f"Brandon Paredes - 5990 24 23242")
