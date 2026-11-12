# clasificadordeperrosygatosuwu
Proyecto de programación, "Clasificador de perros y gatos".
# Resumen
Se realizo una dinamica desarrollando una aplicacion "identificador de perros y gatos" basado en el modelo tensorflow y keras. Este modelo se desarrollo utilizando el modelo de programacion python. 
Se utilizo streamlit como interfaz para crear una web interactiva
# Introducción: ¿Para qué se realizó este proyecto?
Este proyecto se realizó con el fin de desarrollar y utilizar las herramientas y conocimientos adquiridos hasta el momento en nuestra clase de programación, las cuales son la ejecución de python, streamlit y google colab. Al igual que dar a conocer la manera en que se utiliza TensorFlow para poder identificar y clasificar imágenes de perros y gatos para que un usuario suba una foto y obtenga una predicción en una app utilizando el interfaz de streamlit
# Objetivos
Objetivo general: Clasificar imágenes en cuestión de segundos utilizando el modelo TensorFlow y organizar colecciones de fotos para la utilidad del usuario
1. Programar un codigo de algoritmos que evaluen imagenes, basandose en Tensorflow para que el usuario interactue a traves de una interfaz (Streamlit)
2. Se crearan botones interactivos como los siguientes: "sube una imagen" y "aceptar"
3. Para concluir, se le dará al usuario el resultado de la imagen que proporciono, ya sea un perro o un gato
# Solución y evidencia
Entrenamiento: https://colab.research.google.com/drive/1wP6_jbbEAFuLkdyrLJKqP3pc0tTvABhR
El dataset utilizado fue adquirido de: https://huggingface.co/datasets/microsoft/cats_vs_dogs?library=datasets

Entrenamiento:
Se instalaron las terminales y biblioteca necesarias

<img width="1030" height="287" alt="image" src="https://github.com/user-attachments/assets/fb1aad7b-e97e-47bc-9149-37e9653e8686" />

Se dividieron las imágenes de la biblioteca entre 80% de entrenamiento y 20% de prueba

<img width="1287" height="240" alt="WhatsApp Image 2026-11-09 at 11 15 29 AM" src="https://github.com/user-attachments/assets/ae453ccf-8d1c-43d7-a6a0-f6281a6a4b14" />

Después se coloco una columna que recorta las imagenes a 64

<img width="693" height="177" alt="WhatsApp Image 2026-11-09 at 2 32 39 PM" src="https://github.com/user-attachments/assets/d06ec8df-18d9-4637-9397-2da4c386b974" />

Posteriormente se establecieron las capas con ese nuevo tamaño y con los colores que se tomarian para el entrenamiento (3: azul, amarillo, magenta)

<img width="1259" height="235" alt="WhatsApp Image 2026-11-09 at 2 32 54 PM" src="https://github.com/user-attachments/assets/43e20ad8-c8fe-4a3c-bade-705ca0d079d5" />

Se utilizó el optimizador "adam"

<img width="562" height="70" alt="WhatsApp Image 2026-11-09 at 2 33 14 PM" src="https://github.com/user-attachments/assets/524a254a-3f8e-4cf0-a2ae-cc3a4cf31374" />

Se especificaron las etapas de validacion hasta tener un exactitud alta

<img width="886" height="466" alt="WhatsApp Image 2026-11-09 at 2 33 25 PM" src="https://github.com/user-attachments/assets/70f335ff-e7df-4543-8830-8b628e6dfaf9" />

Se dio el comando de importar a drive los archivos, en especifico el archivo con el modelo entrenado

<img width="933" height="133" alt="WhatsApp Image 2026-11-09 at 2 33 47 PM" src="https://github.com/user-attachments/assets/2b72d253-b75e-435e-86c1-2fd07fba401e" />

Posteriormente se creo una carpeta para streamlit en que estuviera el archivo del modelo 

<img width="788" height="261" alt="WhatsApp Image 2026-11-09 at 2 58 30 PM (1)" src="https://github.com/user-attachments/assets/68c7f6c4-de14-405e-8c34-69c0bc7a70ed" />

Despues se abrio esa carpeta en Visual code

<img width="972" height="540" alt="WhatsApp Image 2026-11-09 at 3 01 59 PM" src="https://github.com/user-attachments/assets/28337638-cbd8-4f95-b780-9d1541cc52e4" />

Se creo el código para Streamlit junto con las dependencias en el entorno virtual con Pythom

<img width="852" height="536" alt="WhatsApp Image 2026-11-09 at 2 54 46 PM" src="https://github.com/user-attachments/assets/eec9c942-0d63-473a-aa0f-7cf32901e1e2" />
<img width="853" height="520" alt="WhatsApp Image 2026-11-09 at 2 55 26 PM" src="https://github.com/user-attachments/assets/e0ce8e29-028c-46ab-94fe-fd45addec9b6" />

Nos dimos cuenta que la version actual no permite la instalacion de Tensorflow por lo que se instalo la version de Python 3.12.10

<img width="721" height="452" alt="WhatsApp Image 2026-11-09 at 2 56 22 PM" src="https://github.com/user-attachments/assets/33b094d2-98e7-4870-bdaa-510e3c11f7ee" />


Una vez instalado streamlit, tensorflow y pillow se subio el codigo al repositorio junto con los requeriments.

<img width="948" height="350" alt="WhatsApp Image 2026-11-11 at 11 21 14 PM" src="https://github.com/user-attachments/assets/ad545c2c-a9b0-408d-b092-dfaaeb2a2b0c" />


Realizamos la pagina en streamlit

<img width="1366" height="625" alt="WhatsApp Image 2026-11-11 at 11 23 52 PM" src="https://github.com/user-attachments/assets/658bc0eb-7882-4d50-b8fe-24fea6185edd" />

<img width="1366" height="438" alt="WhatsApp Image 2026-11-11 at 11 24 55 PM" src="https://github.com/user-attachments/assets/d6c87ab3-dde2-4d59-b371-8a3fc278a279" />

Verificamos que funcionara la pagina ya como tal

<img width="1366" height="676" alt="WhatsApp Image 2026-11-11 at 11 39 27 PM (1)" src="https://github.com/user-attachments/assets/a1df350f-ab32-404a-ac9f-0d080f9e7624" />

<img width="1365" height="672" alt="WhatsApp Image 2026-11-11 at 11 26 03 PM (1)" src="https://github.com/user-attachments/assets/bf2fa8a1-c39f-4696-85c5-4a6ba971f7c5" />

# Conclusiones generales:
Finalmente consideramos que la creación de este clasificador puso a prueba nuestros conocimiento sobre lo aprendido en clase así como la capacidad de resolver las dudas por nuestra cuenta, ya que el problema que se nos presento sobre que teníamos que usar una versión de Python que admitiera tensorflow era algo que no esperábamos, pero pudimos resolver gracias a la practica que hemos tenido en clase. Sobre el programa al final comprendimos mejor el funcionamiento de el entrenamiento de modelos de reconocimiento asi como sus partes.

# Conclusiones particulares:
El código genero varios errores a la hora de precisar si es perro o gato, debido a que las imágenes de la biblioteca que se utilizó son imágenes muy claras en las cuales se puede distinguir entre un perro o gato, pero si se sube una imagen volteada de un perro o un gato con los ojos cerrados el modelo no predice con precisión si es uno u otro.

Asimismo concluimos que al programa le es mas fácil distinguir perros, pensamos que es porque tienen razgos más marcados o porque el modelo tomo mas imagenes de perros para entrenarse.

El conocer más herramientas como tensorflow nos ayudo a entender como cada una puede llegar a tener particularidades las cuales hay que conocer con anterioridad para evitar tiempo muerto intentando resolver un problema que se pudo evitar.

# Reproducibilidad.
Se puede utilizar mediante la pagina de Streamlit:
https://clarificadordeperrosygatosuwu-ww2pfnlpqbyootncqovqjd.streamlit.app/
