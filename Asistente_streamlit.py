
import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title= "Asistente Par e Impar", page_icon= "")

def frases_bienvenida():

    frases = [
        "Bienvenido al asistente personal",
        "Que gusto tenerte aquí. Sientete como en casa",
        "¡Hola! Gracias por elegirnos. Estas en buenas manos"
    ]
    return random.choice(frases)

def mostrar_titulo():

    st.title("Par_Impar_bot | Asistente personal")
    st.markdown(f"Sesión Iniciada: {datetime.now().strftime("%d/%m/%Y %H:%M")}")
    st.markdown(frases_bienvenida())

def capturar_numero():
    
    while True:
        try:
            num = st.number_input("Ingrese un número cualquiera: ") 

            if num <= 0:
                st.error("Por favor, ingrese un número válido")
                continue
            
            if len(str(int(num))) > 5:
                st.error("Por favor, ingrese un número menor a 5 cifras")
                continue
                
            if num.is_integer():
                st.success("Es un número entero")
                
            else:
                st.success("Es un número decimal")
            return num
        except ValueError:
            st.error("Por favor, ingrese números")

def par_impar(num):

    if not num.is_integer():
        st.error("No se puede determinar si es par o impar porque es un número decimal")
        return

    num = int(num)

    if num % 2 == 0:
        frases = [

            f"El {num} es Par. Felicidades",
            f"El {num} ingresado es Par. Gracias por elegirnos",
            f"{num} es Par. Estamos para servirle"
        ]
        st.success(random.choice(frases))
    
    else:
        frases_impar = [

            f"El {num} es impar. Felicidades",
            f"El {num} ingresado es Impar. Gracias por elegirnos",
            f"{num} es Impar. Estamos para servirle"
        ]
        st.success(random.choice(frases_impar))

        
def ejecutar():
    mostrar_titulo()
    num = capturar_numero()
    if num:
        par_impar(num)
    


