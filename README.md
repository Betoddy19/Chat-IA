# 🤖 Chat IA com OpenAI

Este projeto é um chatbot simples feito em Python utilizando a API da OpenAI (`gpt-3.5-turbo`).

## 🚀 Funcionalidades

- Envia perguntas para a IA
- Recebe respostas em tempo real
- Suporte a múltiplas interações

## 🛠 Como usar

```bash
# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Crie um arquivo .env com sua chave da OpenAI
echo OPENAI_API_KEY=sk-... > .env

# Execute
python chat.py
