import requests
import time
import json
from datetime import datetime

#  Configuration บ้าๆ
KUY =  "MTM3NzIxMDQxMjI3MzI0MjE5Mg.GrlVQ-.Ydnbg3lLJLz4uiVwYtvj60ZogVB12XD06wUXaM" 
CHANNEL_IDS = [
    "1213948539273613382",  # ชาแนลที่ 1
    "1164644372873224356",  # ชาแนลที่ 2  
    "1302064245403291740"   # ชาแนลที่ 3
]
MESSAGE = """## ขายเงินเขียว Half City
```
 💵 เงินเขียว : 1M = 300 (พร้อมส่ง)   💰

--------------------------

💥 รับพรีออเดอร์งานไว 
⚡️ เงินสะอาดฟาร์มมือเดียว  ปลอดภัย 100%
💥 กลางได้ สอบถามได้ครับ
```
"""
DELAY_MINUTES = 30  # ดีเลย์ 30 นาที

headers = {
    "Authorization": KUY,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

payload = {
    "content": MESSAGE,
    "tts": False
}

def send_fucking_message(channel_id, attempt_count):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in [200, 201]:
            print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] โพสต์สำเร็จในชาแนล {channel_id} (รอบที่ {attempt_count})")
            return True
        else:
            print(f"❌ [{datetime.now().strftime('%H:%M:%S')}] ล้มเหลวในชาแนล {channel_id}: {response.status_code}")
            return False
    except Exception as e:
        print(f"💥 [{datetime.now().strftime('%H:%M:%S')}] 错误ในชาแนล {channel_id}: {str(e)}")
        return False

#  fucking infinite loop
print("🤖 เริ่มต้นการโพสต์ข้อความแบบไม่รู้จบ...")
print(f"📢 จำนวนชาแนล: {len(CHANNEL_IDS)} ชาแนล")
print("⚠️  กด Ctrl+C เพื่อหยุดการทำงาน")

count = 1
while True:
    try:
        for index, channel_id in enumerate(CHANNEL_IDS, 1):
            print(f"\n📡 รอบที่ {count} - ชาแนลที่ {index}/{len(CHANNEL_IDS)}")
            send_fucking_message(channel_id, count)
            
            if index < len(CHANNEL_IDS):
                print(f"⏳ รอ 5 วินาทีก่อนชาแนลถัดไป...")
                time.sleep(5)  # ดีเลย์สั้นระหว่างชาแนล
        
        print(f"\n⏰ รอ {DELAY_MINUTES} นาที until next cycle...")
        
        #  fucking delay 30 นาทีระหว่างรอบ
        for remaining in range(DELAY_MINUTES * 60, 0, -1):
            mins, secs = divmod(remaining, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            print(f"⏳ เวลาที่เหลือจนถึงรอบถัดไป: {time_format}", end='\r')
            time.sleep(1)
        
        count += 1
        
    except KeyboardInterrupt:
        print("\n🛑 หยุดการทำงานโดยผู้ใช้")
        break
    except Exception as e:
        print(f"\n💀 เกิดข้อผิดพลาด: {str(e)}")
        print("♻️  restarting in 60 seconds...")
        time.sleep(60)

print("👋 จบการทำงานแล้ว ไอ้สัส!")
