import os
import streamlit as st
import openai
from dotenv import load_dotenv
import json

# ✅ Load API key from your .env file
load_dotenv("/content/drive/MyDrive/chatbot_yokesh/.env")
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Token pricing
TOKEN_PRICES = {
    "gpt-4": {"input": 0.03 / 1000, "output": 0.06 / 1000},
    "gpt-3.5-turbo": {"input": 0.0015 / 1000, "output": 0.002 / 1000}
}

# ✅ Streamlit setup
st.set_page_config(page_title="Supply Chain Chatbot", layout="centered")
st.title("🤖 Supply Chain & Warehouse Automation Chatbot")

# ✅ Model selector
model_choice = st.sidebar.selectbox("Select Model", ["gpt-4", "gpt-3.5-turbo"])

# ✅ Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant that ONLY answers questions about Supply Chain, Warehouse Automation, and AutoStore systems. If the user asks anything outside this domain, politely refuse."}
    ]
if "total_cost" not in st.session_state:
    st.session_state.total_cost = 0.0
if "last_user_input" not in st.session_state:
    st.session_state.last_user_input = None

# ✅ Show chat history
for msg in st.session_state.messages[1:]:
    if msg["role"] == "user":
        st.markdown(f"🧑‍💼 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:**\n\n{msg['content']}")

# ✅ Domain check with context awareness
def is_domain_question(user_input, messages):
    domain_keywords = ["warehouse", "autostore", "inventory", "automation", "supply chain", "fulfillment", "logistics"]
    if any(word in user_input.lower() for word in domain_keywords):
        return True
    # allow follow-up if last user question was in domain
    for msg in reversed(messages):
        if msg["role"] == "user":
            if any(word in msg["content"].lower() for word in domain_keywords):
                return True
            break
    return False

# ✅ Chat input
user_input = st.chat_input("Type your question:")

if user_input and user_input != st.session_state.last_user_input:
    st.session_state.last_user_input = user_input

    # ✅ Display question immediately
    st.markdown(f"🧑‍💼 **You:** {user_input}")
    st.session_state.messages.append({"role": "user", "content": user_input})

    if not is_domain_question(user_input, st.session_state.messages):
        bot_reply = "⚠️ This chatbot only answers questions related to Supply Chain, Warehouse Automation, and AutoStore systems."
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.markdown(f"🤖 **Bot:**\n\n{bot_reply}")
    else:
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model=model_choice,
                messages=st.session_state.messages,
                max_tokens=300,
                temperature=0.5
            )
        bot_reply = response.choices[0].message["content"].strip()
        bot_reply = bot_reply.replace("\n\n", "\n")  # ✅ Clean formatting

        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.markdown(f"🤖 **Bot:**\n\n{bot_reply}")

        # ✅ Calculate cost
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        cost = (
            prompt_tokens * TOKEN_PRICES[model_choice]["input"] +
            completion_tokens * TOKEN_PRICES[model_choice]["output"]
        )
        st.session_state.total_cost += cost

# ✅ Reset button
if st.sidebar.button("🔄 Reset Conversation"):
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant that ONLY answers questions about Supply Chain, Warehouse Automation, and AutoStore systems."}
    ]
    st.session_state.total_cost = 0.0
    st.session_state.last_user_input = None
    st.rerun()

# ✅ Sidebar cost display
st.sidebar.markdown("### 💰 Session Cost")
st.sidebar.write(f"Estimated Cost: **${st.session_state.total_cost:.4f}**")

# ✅ Debug conversation
with st.sidebar.expander("🔍 Debug - Conversation Log"):
    st.text_area("Model Input", value=json.dumps(st.session_state.messages, indent=2), height=300)
