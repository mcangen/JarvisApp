# 📘 README – JarvisApp Multivariable
🧠 JarvisApp Multivariable

JarvisApp es una aplicación interactiva diseñada para el aprendizaje de Cálculo Vectorial, integrando:

Visualización avanzada de superficies en R³

Control por voz

Control por gestos con cámara

Asistente inteligente basado en Phi-2

Interfaz gráfica completa con PyQt5

Memoria de funciones y estados previos

El objetivo es combinar IA, visión por computadora y cálculo multivariable en un entorno educativo moderno.

# 🚀 Características principales
## ✔️ 1. Graficación 3D interactiva

Renderizado con Plotly dentro de PyQt5.

Superficies del tipo z = f(x, y).

Rotación, zoom y actualización en tiempo real.

## ✔️ 2. Asistente inteligente (Phi-2)

Explica conceptos de cálculo multivariable.

Interpreta funciones dictadas por el usuario.

Responde preguntas matemáticas.

Conversación contextualizada.

## ✔️ 3. Control por voz

Activación por botón.

Reconoce comandos:
"grafica seno de x por y",
"volver a la función anterior",
"compara con la función 2", etc.

## ✔️ 4. Control por gestos

Basado en MediaPipe Hands.

Detección de mano en tiempo real usando la cámara.

Interacción natural con la gráfica.

## ✔️ 5. Memoria interna

Guarda las funciones usadas.

Permite retroceder a versiones anteriores.

Permite comparaciones gráficas.

# 🖥️ Requisitos del sistema

✓ Windows 10 / 11
✓ Python 3.10 (OBLIGATORIO)
✓ Cámara web (para gestos)
✓ Micrófono (para voz)

⚠️ Python 3.11 o 3.12 NO funcionan debido a incompatibilidades con PyAudio, MediaPipe y PyTorch.

# 📦 Instalación
## 1️⃣ Instalar Python 3.10

Descargar:
📥 https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

Marcar Add to PATH.

## 2️⃣ Crear el entorno virtual

En la carpeta del proyecto:

python -m venv venv


Activar el entorno:

venv\Scripts\activate

## 3️⃣ Actualizar pip
python -m pip install --upgrade pip

## 4️⃣ Instalar PyAudio (OBLIGATORIO PARA VOZ)
pip install pipwin
pipwin install pyaudio

## 5️⃣ Instalar PyTorch (CPU) compatible con Python 3.10
pip install torch==2.1.0+cpu torchvision==0.16.0+cpu torchaudio==2.1.0+cpu -f https://download.pytorch.org/whl/cpu

## 6️⃣ Instalar dependencias principales
pip install pyqt5 pyqtwebengine plotly numpy==1.26 mediapipe==0.10.14 opencv-python pyttsx3 SpeechRecognition transformers==4.37


# 🔥 Importante:

numpy==1.26 es necesario porque MediaPipe NO funciona con numpy 2.x

mediapipe==0.10.14 es estable con Python 3.10

transformers==4.37 soporta Phi-2 correctamente

# 📁 Estructura del proyecto
-JarvisApp/
- main.py              # Interfaz, gráficos, cámara, voz, integración IA
- jarvis_phi.py        # Asistente inteligente Phi-2
- memoria.py           # Sistema de memoria del asistente
- voz.py               # TTS y reconocimiento de voz
-  README.md

# ▶️ Cómo ejecutar la aplicación

## Activar el entorno:

venv\Scripts\activate


## Ejecutar el programa:

python main.py

# 🎮 Cómo usar JarvisApp
## 🟦 1. Graficación

Escribe una función en el recuadro, ej.:

np.sin(np.sqrt(x**2 + y**2))


Presiona 📊 Graficar

## 🎙️ 2. Comandos por voz

Presiona 🎙️ Activar Voz, luego di:

“Grafica seno de x por y”

“Comparar con la función dos”

“Volver a la anterior”

“¿Qué es una superficie de nivel?”

“Explica derivadas parciales”

## ✋ 3. Control por gestos

Con la cámara encendida:

Mueve tu mano para ver la detección (MediaPipe Hands)

Control del gráfico (rotación/zoom) depende de movimientos naturales

# 📚 Contenido matemático cubierto

Funciones de varias variables

Superficies en R³

Derivadas parciales

Gradiente

Niveles y curvas

Campos vectoriales

Curvas paramétricas

Divergencia y rotacional (conceptual)

Visualización tridimensional

# 🧩 Conclusión

JarvisApp Multivariable demuestra que es posible integrar:

IA moderna (Phi-2)

Reconocimiento de voz

Visión por computadora

Visualización 3D

Cálculo vectorial

en un solo entorno interactivo para enseñar y aprender de manera intuitiva, dinámica y futurista.

Este proyecto ofrece una visión de cómo será la educación potenciada por IA en los próximos años.
