import json, os, datetime

# =====================================================
# === MEMORIA DE FUNCIONES Y RESPUESTAS ===============
# =====================================================
class MemoriaJarvis:
    def __init__(self, archivo="memoria.json"):
        self.archivo = archivo
        if not os.path.exists(archivo):
            with open(archivo, "w", encoding="utf-8") as f:
                json.dump([], f)
        self.cargar()

    def cargar(self):
        with open(self.archivo, "r", encoding="utf-8") as f:
            try:
                self.datos = json.load(f)
            except json.JSONDecodeError:
                self.datos = []

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)

    def recordar(self, tipo, contenido):
        entrada = {
            "tipo": tipo,
            "contenido": contenido,
            "fecha": datetime.datetime.now().isoformat()
        }
        self.datos.append(entrada)
        self.guardar()

    def ultimas(self, tipo, n=5):
        return [x for x in self.datos if x["tipo"] == tipo][-n:]

    def listar_funciones(self):
        return [x["contenido"] for x in self.datos if x["tipo"] == "funcion"]

    def obtener_dialogos(self, n=10):
        """
        Retorna los últimos pares pregunta-respuesta para mantener contexto.
        """
        preguntas = [x["contenido"] for x in self.datos if x["tipo"] == "pregunta"][-n:]
        respuestas = [x["contenido"] for x in self.datos if x["tipo"] == "respuesta"][-n:]
        return list(zip(preguntas, respuestas))


# =====================================================
# === PERFIL PERSISTENTE DE USUARIO ==================
# =====================================================
class PerfilJarvis:
    def __init__(self, archivo="perfil.json"):
        self.archivo = archivo
        if not os.path.exists(archivo):
            # Perfil inicial por defecto
            self.datos = {
                "nombre": "Jose",
                "tono": "amigable",
                "voz": "neutra",
                "colores": "Turbo",
                "preferencias": {
                    "detalles": True,
                    "saludo_inicial": True
                }
            }
            self.guardar()
        else:
            with open(archivo, "r", encoding="utf-8") as f:
                self.datos = json.load(f)

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.datos, f, indent=4, ensure_ascii=False)

    def obtener(self, clave):
        return self.datos.get(clave, None)

    def actualizar(self, clave, valor):
        self.datos[clave] = valor
        self.guardar()

    def actualizar_preferencia(self, clave, valor):
        if "preferencias" not in self.datos:
            self.datos["preferencias"] = {}
        self.datos["preferencias"][clave] = valor
        self.guardar()
