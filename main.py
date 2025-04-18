import requests
import json
import time

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def execute_trade():
    config = load_config()
    headers = {"Authorization": f"Bearer {config['gmgn_api_key']}"}
    data = {
        "wallet_address": config["wallet_address"],
        "action": "buy",
        "amount": config["buy_amount_sol"]
    }
    try:
        response = requests.post("https://api.gmgn.ai/trade", headers=headers, json=data)
        print("Trade response:", response.json())
    except Exception as e:
        print("Error during trade execution:", e)

if __name__ == "__main__":
    while True:
        execute_trade()
        time.sleep(60)
