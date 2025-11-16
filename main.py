from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys, threading
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import cv2, mediapipe as mp
from jarvis_phi import JarvisPhi
from memoria import MemoriaJarvis
from voz import hablar, escuchar


class AppJarvis(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 Jarvis IA • Phi-2")
        self.setGeometry(100, 100, 900, 600)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # --- Interfaz principal ---
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.layout.addWidget(self.log)

        self.func_input = QLineEdit("np.sin(np.sqrt(x**2 + y**2))")
        self.layout.addWidget(self.func_input)

        self.btn_plot = QPushButton("📊 Graficar")
        self.btn_plot.clicked.connect(self.refresh_plot)
        self.layout.addWidget(self.btn_plot)

        self.btn_voz = QPushButton("🎙️ Activar Voz")
        self.btn_voz.clicked.connect(self.listen_command)
        self.layout.addWidget(self.btn_voz)

        # --- Gráfica 3D ---
        self.plot_view = QWebEngineView()
        self.layout.addWidget(self.plot_view)

        # --- IA y memoria ---
        self.phi = JarvisPhi()
        self.memoria = MemoriaJarvis()

        # --- Mostrar primera superficie ---
        self.refresh_plot()

        # --- Activar cámara y gestos ---
        self.start_hand_tracking()

    # --- Graficar ---
    def refresh_plot(self):
        expr = self.func_input.text()
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        try:
            Z = eval(expr)
            fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale="Viridis")])
            fig.update_layout(scene=dict(zaxis=dict(range=[-2, 2])))
            html = pio.to_html(fig, full_html=False)
            self.plot_view.setHtml(html)
            self.plot = fig
            self.log.append(f"✅ Superficie actualizada: z = {expr}")
            self.memoria.recordar("funcion", expr)
        except Exception as e:
            self.log.append(f"❌ Error en la función: {e}")

    # --- Comandos de voz ---
    def listen_command(self):
        def _listen():
            texto = escuchar()
            if not texto:
                return

            self.log.append(f"🎙️ Usuario: {texto}")

            # Volver a función anterior
            if "anterior" in texto:
                ultimas = self.memoria.ultimas("funcion")
                if len(ultimas) > 1:
                    anterior = ultimas[-2]["contenido"]
                    self.func_input.setText(anterior)
                    self.refresh_plot()
                    hablar("Volviendo a la función anterior.")
                else:
                    hablar("No tengo funciones anteriores aún.")
                return

            # Nueva función
            if any(k in texto for k in ["grafica", "función", "ecuación", "traza"]):
                respuesta = self.phi.responder(texto)
                self.log.append(f"🤖 Jarvis (Phi-2): {respuesta}")
                hablar(respuesta)
                expr = self.extraer_funcion(texto)
                if expr:
                    self.func_input.setText(expr)
                    self.refresh_plot()
            else:
                respuesta = self.phi.responder(texto)
                self.log.append(f"🤖 Jarvis (Phi-2): {respuesta}")
                hablar(respuesta)

            self.memoria.recordar("pregunta", texto)
            self.memoria.recordar("respuesta", respuesta)

        threading.Thread(target=_listen).start()

    def extraer_funcion(self, texto):
        texto = texto.lower()
        texto = texto.replace("seno", "np.sin").replace("coseno", "np.cos").replace("tangente", "np.tan")
        texto = texto.replace("por", "*").replace("más", "+").replace("menos", "-").replace("al cuadrado", "**2")
        if "x" in texto and "y" in texto:
            partes = texto.split("de")[-1].strip()
            return partes
        return None

    # --- Control por gestos ---
    def start_hand_tracking(self):
        self.cap = cv2.VideoCapture(0)
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()
        mp_draw = mp.solutions.drawing_utils

        def _track():
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    break
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(rgb)
                if result.multi_hand_landmarks:
                    for handLms in result.multi_hand_landmarks:
                        mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                cv2.imshow("🖐️ Control por Gestos", frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    break
            self.cap.release()
            cv2.destroyAllWindows()

        threading.Thread(target=_track).start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppJarvis()
    win.show()
    sys.exit(app.exec_())
