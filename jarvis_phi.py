from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class JarvisPhi:
    def __init__(self, model_name="microsoft/phi-2"):
        print("🧠 Cargando modelo Phi-2...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        ).to(self.device)
        print("✅ Phi-2 listo.")

    def responder(self, texto):
        prompt = f"Eres Jarvis, un asistente matemático. Interpreta y responde con precisión técnica.\nUsuario: {texto}\nJarvis:"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=120, temperature=0.6)
        respuesta = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return respuesta.split("Jarvis:")[-1].strip()
1