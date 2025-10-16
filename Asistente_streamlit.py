
import streamlit as st
from datetime import datetime
import random


st.set_page_config(page_title="Asistente Par e Impar", page_icon="🤖")


def frases_bienvenida():
    frases = [
        "Bienvenido al asistente personal",
        "Qué gusto tenerte aquí. Siéntete como en casa",
        "¡Hola! Gracias por elegirnos. Estás en buenas manos"
    ]
    return random.choice(frases)


def mostrar_titulo():
    st.title("Par_Impar_bot | Asistente personal")
    st.markdown(f"🕒 Sesión iniciada: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    st.markdown(f"📍 Ubicación: Valencia, Venezuela")
    st.markdown(f"💬 {frases_bienvenida()}")


def capturar_numero():
    num = st.number_input("Ingrese un número positivo menor a 5 cifras:", step=1.0)

    if num == 0:
        st.info("El número ingresado es cero. Todo comienza aquí.")
        return None

    if num < 0:
        st.error("Por favor, ingrese un número positivo.")
        return None

    if len(str(int(num))) > 5:
        st.error("El número tiene más de 5 cifras.")
        return None

    if num.is_integer():
        st.success(f"El número {int(num)} es entero. ¡Perfecto para cálculos exactos!")
    else:
        st.success(f"El número {num} es decimal. Ideal para medidas precisas.")

    return num


def mostrar_par_impar(num):
    if not num.is_integer():
        st.warning("No se puede determinar si es par o impar porque es decimal.")
        return

    num = int(num)
    frases_par = [
        f"El {num} es Par. Felicidades 🎉",
        f"El {num} ingresado es Par. Gracias por elegirnos 🙌",
        f"{num} es Par. Estamos para servirle 🤝"
    ]
    frases_impar = [
        f"El {num} es Impar. Felicidades 🎉",
        f"El {num} ingresado es Impar. Gracias por elegirnos 🙌",
        f"{num} es Impar. Estamos para servirle 🤝"
    ]

    if num % 2 == 0:
        st.success(random.choice(frases_par))
    else:
        st.success(random.choice(frases_impar))

def ejecutar():
    mostrar_titulo()
    num = capturar_numero()
    if num:
        mostrar_par_impar(num)


ejecutar()

    




