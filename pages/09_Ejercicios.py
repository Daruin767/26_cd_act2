import streamlit as st
import random

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



st.subheader("Ejercicio 4: Galería de Mascotas (Tabs)", divider="rainbow")

st.write(
    """
*   Crea 3 pestañas: "Gatos", "Perros", "Aves".
*   En cada pestaña muestra una imagen diferente (puedes usar URLs públicas) y un botón de "Me gusta" que, al ser presionado, muestre un `st.toast` diciendo "Te gusta esta mascota".

    """
)

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.header("Gatos")
    st.image("https://cdn.pixabay.com/photo/2017/11/09/21/41/cat-2934720_1280.jpg", width=300)

    if st.button("Me gusta ♥", key="gato"):
        st.toast("Te gusta esta mascota ")

with tab2:
    st.header("Perros")
    st.image("https://www.hola.com/horizon/original_aspect_ratio/b0ee803a6e46-razas-de-perros-raras-a.jpg", width=300)

    if st.button("Me gusta ♥", key="perro"):
        st.toast("Te gusta esta mascota ")

with tab3:
    st.header("Aves")
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/c2/Maakotka_%28Aquila_chrysaetos%29_by_Jarkko_J%C3%A4rvinen.jpg", width=300)

    if st.button("Me gusta ♥", key="ave"):
        st.toast("Te gusta esta mascota ")

st.divider()




st.subheader("Ejercicio 5: Caja de Comentarios (Formulario)", divider="rainbow")

st.write(
    """
Crea un formulario con:
*   Un campo de texto para el asunto.
*   Un área de texto para el mensaje.
*   Un botón de envío.
*   Al enviar, muestra los datos ingresados en un `st.json` o `st.write` solo si el mensaje no está vacío.
    """
)

with st.form("formulario_comentarios"):
    asunto = st.text_input("Asunto:")
    mensaje = st.text_area("Mensaje:")
    enviar = st.form_submit_button("Enviar")

    if enviar:
        if mensaje.strip() == "":
            st.error("El mensaje no puede estar vacío ")
        else:
            st.success("Comentario enviado correctamente ")
            st.json({
                "Asunto": asunto,
                "Mensaje": mensaje
            })

st.divider()




st.subheader("Ejercicio 6: Login Simulado (Session State)", divider="rainbow")

st.write(
    """
*   Crea dos campos: usuario y contraseña (usa `type='password'`).
*   Un botón "Ingresar".
*   Si el usuario es "admin" y la contraseña "1234", guarda en `st.session_state` que el usuario está logueado y muestra un mensaje de éxito.
*   Si ya está logueado, muestra un botón "Cerrar Sesión" que limpie el estado.
    """
)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.success("¡Bienvenido, admin!")
    if st.button("Cerrar Sesión"):
        st.session_state.logged_in = False  
else:
    usuario = st.text_input("Usuario:")
    contraseña = st.text_input("Contraseña:", type="password")
    if st.button("Ingresar"):
        if usuario == "admin" and contraseña == "1234":
            st.session_state.logged_in = True
            st.success("¡Bienvenido, admin!")
        else:
            st.error("Usuario o contraseña incorrectos ")

st.divider()




st.subheader("Ejercicio 7: Lista de Compras (Session State)", divider="rainbow")

st.write(
    """
*   Un `st.text_input` para ingresar un producto.
*   Dos botones: "Agregar" y "Limpiar Lista".
*   Muestra la lista de productos agregados hasta el momento. La lista debe persistir aunque interactúes con otros widgets.
    """
)

if 'compras' not in st.session_state:
    st.session_state.compras = []

nueva_compra = st.text_input("Lista de Compras", key="input_compra")

if st.button("Agregar compra") and nueva_compra:
    st.session_state.compras.append(nueva_compra)
    st.success(f"compra '*{nueva_compra}*' agregada!")


st.write(" Tus Compras:")
for i, compra in enumerate(st.session_state.compras):
    st.write(f"{i + 1}. {compra}")

if st.button("Limpiar lista"):
    st.session_state.compras = []
    st.rerun()


st.divider()


st.subheader("Ejercicio 8: Gráfico Interactivo", divider="rainbow")

st.write(
    """
*   Usa un `st.slider` para seleccionar un número `N` entre 10 y 100.
*   Genera una lista de `N` números aleatorios.
*   Muestra un `st.line_chart` con esos datos.
*   Añade un botón para "Regenerar" los datos (pista: el botón hará rerun, lo que regenerará los aleatorios automáticamente).
    """
)

N = st.slider("Selecciona el número :", min_value=10, max_value=100, value=50)

numeros_aleatorios = [random.randint(0, 100) for i in range(N)]

st.line_chart(numeros_aleatorios)

if st.button("Regenerar datos"):
    st.rerun()


st.divider()