import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# --- Configuração ---
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da OpenAI UMA VEZ para evitar múltiplas inicializações
# Usamos st.cache_resource para garantir que o cliente seja criado apenas uma vez
# e reutilizado nas sessões do Streamlit, o que é eficiente para objetos grandes.
@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = get_openai_client()

# --- Título da Aplicação ---
st.title("🤖 Meu Chat-IA")

# --- Inicialização do Histórico da Conversa ---
# Usamos st.session_state para armazenar o histórico do chat
# Isso garante que o histórico persista entre as interações do usuário
if "messages" not in st.session_state:
    st.session_state.messages = [] # Lista de dicionários: [{"role": "user", "content": "Olá"}, {"role": "assistant", "content": "Oi!"}]

# --- Exibir Mensagens Anteriores ---
# Itera sobre o histórico e exibe as mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Campo de Entrada do Usuário ---
# Este é o campo onde o usuário digita a pergunta
if prompt := st.chat_input("Pergunte algo à IA..."):
    # Adiciona a pergunta do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a pergunta do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Lógica de Resposta da IA ---
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # Placeholder para a resposta ser atualizada em tempo real
        full_response = ""
        
        try:
            # Chama a API da OpenAI com o histórico completo para contexto
            # Convertemos o histórico para o formato que a API espera
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True, # Habilita o streaming para respostas mais rápidas
            )
            
            # Processa a resposta em streaming
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌") # Adiciona cursor piscando
            
            message_placeholder.markdown(full_response) # Exibe a resposta final

            # Adiciona a resposta da IA ao histórico
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"⚠️ Erro ao se comunicar com a OpenAI: {e}")
            st.warning("Verifique sua chave de API, conexão com a internet e se há créditos na sua conta OpenAI.")