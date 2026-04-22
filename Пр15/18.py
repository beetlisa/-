from datetime import datetime

deadline = datetime(2026, 4, 10)
if datetime.now() > deadline:
    print("Дедлайн просрочен")
else:
    print("Дедлайн ещё не наступил")