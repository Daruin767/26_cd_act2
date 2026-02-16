import streamlit as st

st.subheader("Ejercicio 1: Saludo Simple",divider="rainbow")
st.write(
    """
    Crea una campo de entrada de texto para que el usuario escriba su nombre.
    - Si el nombre no esta vacio, muestra un mensaje de bienvenida: "Hola, [nombre]!"
    """
)

name = st.text_input("Escribe tu nombre:")
st.write(f"Hola, {name}!") 

st.divider()



st.subheader("Ejercicio 2: Calculadora de Producto", divider="rainbow")

st.write(
    """
    Pide al usuario dos numeros (usando `st.number_input`)
    - muestra el resultado de su multiplicación.
    - Si alguno de los números es mayor a 100, muestra un `st.warning` indicando "Números grandes".
    """
)

num1 = st.number_input("Número 1:", step=1)
num2 = st.number_input("Número 2:", step=1)

result = num1 * num2
st.write(f"El resultado de la multiplicación es: {result}")

if num1 > 100 or num2 > 100:
    st.warning("Números grandes")

st.divider()



st.subheader("Ejercicio 3: Convertidor de Temperatura (Radio Buttons)", divider="rainbow")

st.write(
    """
    *   Usa un `st.radio` para elegir la dirección de la conversión: "Celsius a Fahrenheit" o "Fahrenheit a Celsius".
*   Usa un `st.number_input` para ingresar la temperatura.
*   Muestra el resultado calculado.
    *   *Fórmula C a F*: `(C * 9/5) + 32`
    *   *Fórmula F a C*: `(F - 32) * 5/9`.
    """
)

conversor = st.radio("Selecciona la conversión:", ("Celsius a Fahrenheit", "Fahrenheit a Celsius"))

temperatura = st.number_input("Ingresa la temperatura:", step=0.1)
if conversor == "Celsius a Fahrenheit":
    resultado = (temperatura * 9/5) + 32
    st.write(f"{temperatura} °C es igual a {resultado} °F")
else:
    resultado = (temperatura - 32) * 5/9
    st.write(f"{temperatura} °F es igual a {resultado} °C")

    
st.divider()



st.subheader("Ejercicio 4: Galerí­a de Mascotas (Tabs)", divider="rainbow")

st.write(
    """
   *   Crea 3 pestañas: "Gatos", "Perros", "Aves".
*   En cada pestaña muestra una imagen diferente (puedes usar URLs públicas) y un botón de "Me gusta" que, al ser presionado, muestre un `st.toast` diciendo "Te gusta esta mascota".
    """
)

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.header("Gatos")
    st.image("https://staticprd.minuto30.com/wp-content/uploads/2023/11/c6e853f81c831f5b8ba90c7a6106708bd22fe879.jpg", width=200)

    if st.button("Me gusta ♥", key="gato"):
        st.toast("Te gusta esta mascota")

with tab2:
    st.header("Perros")
    st.image("https://content.elmueble.com/medio/2023/06/20/perro-terranova_2757464b_230620110906_2000x1500.jpg", width=200)

    if st.button("Me gusta ♥", key="perro"):
        st.toast("Te gusta esta mascota")

with tab3:
    st.header("Aves")
    st.image("https://hotelrurallascorchuelas.com/wp-content/uploads/2025/04/Halcon-peregrino_22J2697-Editar.jpeg", width=200)

    if st.button("Me gusta ♥", key="ave"):
        st.toast("Te gusta esta mascota")
    
st.divider()




st.subheader("Ejercicio 5: Caja de Comentarios (Formulario)", divider="rainbow")

st.write(
    """
Crea un formulario con:
*   Un campo de texto para el asunto.
*   Un área de texto para el mensaje.
*   Un botón de envío.
*   Al enviar, muestra los datos ingresados en un `st.json` o `st.write` solo si el mensaje no está vacío.  .
    """
)

asunto = st.text_input("Asunto:")
mensaje = st.text_area("Mensaje:")



st.divider()