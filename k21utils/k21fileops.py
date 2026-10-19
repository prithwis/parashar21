from datetime import datetime
from zoneinfo import ZoneInfo

def saveAnswer(tg_id, model, answer):
    timestamp = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%y%m%d_%H%M%S")
    filepath = f"/content/K21_{tg_id}_{model}_{timestamp}.md"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(answer)

    print(f"Saved: {filepath}")
    return filepath