import os
from dotenv import load_dotenv
from openai import OpenAI # Importante: A classe principal agora é OpenAI

# --- Configuração ---
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da OpenAI.
# A chave da API será lida automaticamente da variável de ambiente OPENAI_API_KEY.
# Certifique-se de que seu arquivo .env está na mesma pasta e tem a chave correta.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Função Principal do Chat ---
def iniciar_chat():
    print("🤖 Chat IA iniciado! Digite 'sair' para encerrar.\n")

    # Lista para manter o histórico da conversa (opcional, mas bom para contexto)
    # Por enquanto, estamos enviando apenas a última pergunta.
    # Se quiser histórico, você adicionaria {"role": "user", "content": pergunta}
    # e {"role": "assistant", "content": mensagem} aqui.
    
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("👋 Encerrando o chat. Até mais!")
            break

        try:
            # Faz a requisição à API usando o novo cliente e sintaxe
            resposta = client.chat.completions.create(
                model="gpt-3.5-turbo", # Modelo que você estava usando
                messages=[{"role": "user", "content": pergunta}]
            )
            
            # Acessa a mensagem da resposta de forma diferente (é um atributo, não mais um item de dicionário)
            mensagem = resposta.choices[0].message.content.strip()
            print("IA:", mensagem)

        except Exception as e:
            # Captura e exibe qualquer erro que ocorra na comunicação com a OpenAI
            print(f"⚠️ Erro ao se comunicar com a OpenAI: {e}")
            print("Verifique sua chave de API, conexão com a internet e status da OpenAI.")

# --- Execução do Script ---
if __name__ == "__main__":
    iniciar_chat()