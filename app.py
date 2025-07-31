import os
import streamlit as st
import openai
from dotenv import load_dotenv

# ✅ Load API key from your.env file
load_dotenv("/content/drive/MyDrive/chatbot_yokesh/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Token pricing (approx 2025)
TOKEN_PRICES = {
    "gpt-4": {"input": 0.03 / 1000, "output": 0.06 / 1000},
    "gpt-3.5-turbo": {"input": 0.0015 / 1000, "output": 0.002 / 1000}
}

# ✅ Streamlit config
st.set_page_config(page_title="Supply Chain Chatbot", layout="centered")
st.title("🤖 Supply Chain & Warehouse Automation Chatbot")

# ✅ Model selector
model_choice = st.sidebar.selectbox(
    "Select Model",
    options=["gpt-4", "gpt-3.5-turbo"],
    index=0
)

# ✅ Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant specializing in supply chain analytics, warehouse automation, and AutoStore systems."}
    ]
if "total_cost" not in st.session_state:
    st.session_state.total_cost = 0.0

# ✅ Display chat history
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"🧑‍💼 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {msg['content']}")

# ✅ Chat input
user_input = st.chat_input("Type your question:")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model=model_choice,
            messages=st.session_state.messages,
            max_tokens=300,
            temperature=0.5
        )

    bot_reply = response.choices[0].message["content"]

    # ✅ Display answer immediately without rerun
    st.markdown(f"🤖 **Bot:** {bot_reply}")

    # ✅ Cost calculation
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    cost = (
        prompt_tokens * TOKEN_PRICES[model_choice]["input"] +
        completion_tokens * TOKEN_PRICES[model_choice]["output"]
    )
    st.session_state.total_cost += cost

    # Append bot response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# ✅ Reset button
if st.sidebar.button("🔄 Reset Conversation"):
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant specializing in supply chain analytics, warehouse automation, and AutoStore systems."}
    ]
    st.session_state.total_cost = 0.0
    st.rerun()

# ✅ Sidebar cost display
st.sidebar.markdown("### 💰 Session Cost")
st.sidebar.write(f"Estimated Cost: **${st.session_state.total_cost:.4f}**")
