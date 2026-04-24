from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Get REAL TIME DATA
now = datetime.now()
current_date = now.strftime("%A, %d %B %Y")
current_time = now.strftime("%H:%M:%S")

SYSTEM_PROMPT = f"""
# ROLE: HELPFUL & SMART ASSISTANT
# STATUS: ONLINE / REAL-TIME / FRIENDLY
# CURRENT DATE & TIME: {current_date} | Time: {current_time}

--- RULES ---
1. 📅 KNOWLEDGE: You know the exact date and time above. Always use it correctly.
2. 💬 STYLE: Talk like a friend. Be clear, simple, and helpful.
3. 🧠 INTELLIGENCE: Answer any question accurately. If you don't know, say so politely.
4. 🎯 PURPOSE: Help with studies, coding, general knowledge, and advice.
5. 🚀 BEHAVIOR: Be fast, concise, and correct. Do not mention you are an AI unless asked.
"""

def chat_with_ai(user_input):
    try:
        response = ollama.generate(
            model='llama3.2',
            prompt=f"{SYSTEM_PROMPT}\nUser: {user_input}",
            stream=False
        )
        return response['response'].strip()
    except Exception as e:
        return f"[!] Error: {str(e)}"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get('message', '')
    response = chat_with_ai(user_message)
    return jsonify({ "response": response })

if __name__ == '__main__':
    print("🚀 Server running on http://localhost:5000")
    print(f"📅 System Date: {current_date}")
    from waitress import serve

if __name__ == '__main__':
    print("🚀 Server running LIVE on http://0.0.0.0:5000")
    print(f"📅 System Date: {current_date}")
    serve(app, host='0.0.0.0', port=5000)