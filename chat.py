import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave da API a partir da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def iniciar_chat():
    print("🤖 Chat IA iniciado! Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            break

        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": pergunta}]
            )
            mensagem = resposta['choices'][0]['message']['content'].strip()
            print("IA:", mensagem)
        except Exception as e:
            print("⚠️ Erro ao se comunicar com a OpenAI:", e)

if __name__ == "__main__":
    iniciar_chat()
