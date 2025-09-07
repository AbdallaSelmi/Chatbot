# Chatbot 🤖

A simple rule-based chatbot built in Python.  
It recognizes user input patterns defined in a JSON file and can respond with small talk, tell the current time, or solve math expressions.

---

## ✨ Features
- Greet and say goodbye  
- Respond to thanks  
- Provide a help menu  
- Return the current time ⏰  
- Solve math expressions ➗  
- Fallback response for unrecognized input  

---

## 📂 Project Structure

CHATBOT/
│
├── bot/
│ ├── actions.py # Dynamic actions (time, calculator)
│ └── ... (more to come in Phase 1)
│
├── data/
│ └── intents.json # Patterns and responses
│
├── main.py # Entry point (will run the bot)
├── README.md
└── .gitignore

## 🛠️ Technologies
- Python 3  
- JSON (data storage)  
- Git/GitHub  

---

## 📌 Roadmap
- Phase 1: Basic intents, time, calculator ✅  
- Phase 2: Add fuzzy matching for typos, more actions (weather, jokes, etc.), web/GUI interface  
- Phase 3: Explore ML/NLP intent classification  

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/AbdallaSelmi/Chatbot.git
   cd Chatbot
   python main.py

