import sys
import requests

# 替換為你的 LINE Notify Token
LINE_ACCESS_TOKEN = "XXXXXXXXXXXXXXXXXX"
LINE_API_URL = "https://api.line.me/v2/bot/message/push"
USER_ID = "XXXXXXXXXXXXXXX"  # 替換為你的 User ID

def send_line_message(message):
    """發送訊息到 LINE BOT"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    data = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    response = requests.post(LINE_API_URL, headers=headers, json=data)
    # if response.status_code == 200:
    #    print("訊息已成功發送")
    #else:
    #    print(f"訊息發送失敗: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # 檢查是否有提供命令行參數
    if len(sys.argv) != 2:
        print("請提供一段文字作為參數，例如: python script.py XXXXXXXXXXXXXXXXXXXX")
        sys.exit(1)
    
    # 獲取命令行參數中的 text
    temp_message = sys.argv[1]
    message = f"{temp_message}"
    
    # 發送訊息到 LINE
    send_line_message(message)
