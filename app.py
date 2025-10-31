import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

st.set_page_config(
    page_title="Chatbot CAG com Gemini",
    layout="wide",
    page_icon="🤖"
)

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

model = None
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
    except Exception as e:
        st.error(f"⚠️ Erro ao configurar Gemini: {str(e)}")
        model = None
else:
    st.warning("⚠️ **GOOGLE_API_KEY não encontrada!**")
    st.info("Para usar o chatbot, adicione sua chave API no arquivo `.env`:")
    st.code("GOOGLE_API_KEY=sua_chave_aqui", language="bash")
    st.markdown("---")

st.title("🤖 Chatbot CAG by Liv_IA")
st.caption("💬 Chat com Context-Aware Generation - Mantém o contexto da conversa")

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.markdown("## ℹ️ Sobre CAG")
    st.markdown("""
    **Context-Aware Generation (CAG)** usa o histórico da conversa 
    para manter contexto entre mensagens.
    
    O modelo recebe todas as mensagens anteriores como contexto,
    permitindo conversas mais naturais e contextuais.
    """)

def ask_gemini(prompt, history):
    if model is None:
        return "❌ Erro: Modelo não inicializado. Verifique se a GOOGLE_API_KEY está configurada.", ""
    
    try:
        conversation_context = ""
        for user, bot in history:
            conversation_context += f"Usuário: {user}\nAssistente: {bot}\n"
        
        if conversation_context:
            final_prompt = f"""Você é um assistente útil e amigável. Responda de forma clara e objetiva, mantendo o contexto da conversa.

### Histórico da conversa:
{conversation_context}

### Nova mensagem:
Usuário: {prompt}
"""
        else:
            final_prompt = f"""Você é um assistente útil e amigável. Responda de forma clara e objetiva.

### Mensagem:
{prompt}
"""
        
        response = model.generate_content(final_prompt)
        return response.text, final_prompt
    except Exception as e:
        return f"❌ Erro ao gerar resposta: {str(e)}", ""

chat_container = st.container()

with chat_container:
    if st.session_state.history:
        for user_msg, bot_msg in st.session_state.history:
            with st.chat_message("user"):
                st.write(user_msg)
            
            with st.chat_message("assistant"):
                st.write(bot_msg)

user_input = st.chat_input("Digite sua mensagem aqui...")

if user_input:
    if model is None:
        st.error("❌ Não é possível enviar mensagens: GOOGLE_API_KEY não está configurada.")
    else:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.chat_message("assistant"):
            with st.spinner("💭 Pensando..."):
                bot_response, _ = ask_gemini(user_input, st.session_state.history)
                st.write(bot_response)
        
        st.session_state.history.append((user_input, bot_response))
        
        st.rerun()