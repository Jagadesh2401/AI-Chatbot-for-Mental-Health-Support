from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import pandas as pd
import os

app = Flask(__name__)

# Load DialoGPT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Session dictionary
chat_history_ids = {}

# Ensure log file exists
if not os.path.exists("logs.csv"):
    pd.DataFrame(columns=["session_id", "user_input", "bot_response"]).to_csv("logs.csv", index=False)

def log_session(session_id, user_input, bot_response):
    df = pd.DataFrame([[session_id, user_input, bot_response]], columns=["session_id", "user_input", "bot_response"])
    df.to_csv("logs.csv", mode='a', header=False, index=False)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    session_id = data.get("session_id", "default")

    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    prev_history = chat_history_ids.get(session_id)

    bot_input_ids = torch.cat([prev_history, new_input_ids], dim=-1) if prev_history is not None else new_input_ids

    chat_history_ids[session_id] = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    )

    response = tokenizer.decode(chat_history_ids[session_id][:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    log_session(session_id, user_input, response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
