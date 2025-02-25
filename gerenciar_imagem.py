import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-2.0-flash"   
genai.configure(api_key=CHAVE_API_GOOGLE)

def gerar_imagem_gemini(caminho_imagem):
    arquivo_temporario = genai.upload_file(
        path=caminho_imagem,
        display_name="Imagem Enviada"
    )

    return arquivo_temporario