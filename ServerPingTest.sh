#!/bin/bash

# 要PING的IP
IPS=("X.X.X.X" "X.X.X.X")
LOG_FILE="~/ServerPing/ping_check.log"

# 初始化訊息變數
OUTPUT=""

# 檢查每個 IP 的連通性
for ip in "${IPS[@]}"; do
    ping -c 2 "$ip" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        # 如果 ping 不通，記錄並通知
        ERROR_MSG="⚠️ 警告: 無法連接到 $ip"
        OUTPUT+="$(date): $ERROR_MSG\n"
        python3 SendMessageLine.py "$ERROR_MSG"
    else
        SUCCESS_MSG="$ip 正常連通"
        OUTPUT+="$(date): $SUCCESS_MSG\n"
	#python3 SendMessageLine.py "$SUCCESS_MSG"
    fi
done

# 將累積的訊息寫入 LOG_FILE（覆蓋寫入）
echo -e "$OUTPUT" > "$LOG_FILE"
