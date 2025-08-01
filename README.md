🤖 Supply Chain & Warehouse Automation Chatbot
A Streamlit web app powered by OpenAI GPT models that provides domain-specific answers related to Supply Chain, Warehouse Automation, and AutoStore systems.

✅ Domain-Restricted: Only answers questions in the warehouse & automation domain
✅ Supports GPT-4 and GPT-3.5
✅ Works locally and on Streamlit Cloud
✅ Cost Tracking for token usage
✅ Environment-Aware: Uses .env locally or Streamlit Secrets on cloud

---

## 🚀 Features
- Domain-specific conversational AI for Supply Chain and Warehouse Automation  
- Auto-detects environment (Local `.env` or Streamlit Cloud secrets)  
- Works with OpenAI’s **latest v1 API**  
- Context-aware follow-up question handling  
- Streamlit UI with chat history  
- Token usage and cost calculation  

---

## 📂 Project Structure

📁 yokesh_chatbot/
│── app.py # Main Streamlit app
│── requirements.txt # Dependencies for deployment
│── .env # Local API key (ignored in cloud)
│── README.md # Project documentation

---

## ⚙️ Installation

### 🔹 1. Clone Repo
git clone https://github.com/your-username/yokesh_chatbot.git
cd yokesh_chatbot

🔹 2. Install Dependencies
pip install -r requirements.txt

🔹 3. Setup OpenAI API Key
Create a .env file in the project root:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx

For Streamlit Cloud:

Go to Settings → Secrets and add:
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxx"

▶️ Running Locally
streamlit run app.py
The app will start at http://localhost:8501

---
☁️ Deploying on Streamlit Cloud
- Push your repo to GitHub
- Create a new app on Streamlit Cloud
- Set OPENAI_API_KEY in Streamlit Secrets
- Deploy and start chatting

---
📌 Usage Example

🤖 Supply Chain & Warehouse Automation Chatbot

🧑‍💼 You: what is autostore?

🤖 Bot: AutoStore is an advanced automated storage and retrieval system (AS/RS) 
that optimizes warehouse operations. It stacks bins vertically in a grid, 
accessed by robots that move along the top of the grid. This design 
eliminates aisles, providing very high storage density.

🧑‍💼 You: which type of warehouse is this useful?

🤖 Bot: AutoStore is ideal for:
- E-commerce warehouses needing high-speed order fulfillment  
- Retail distribution centers with a large SKU variety  
- Spare parts warehouses in automotive/electronics industries  
- Pharmaceutical and healthcare storage with strict inventory control  
- Food & Beverage warehouses managing high turnover and expiration dates  
- 3PL logistics providers needing flexible, high-density solutions

---
📌 Requirements
- Python 3.8+
- OpenAI API Key
- Streamlit >= 1.35.0
- OpenAI >= 1.0.0

📜 License
MIT License

🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

💡 Acknowledgements
- OpenAI for the GPT models
- Streamlit for the UI framework
