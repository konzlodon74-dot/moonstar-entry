import os

LINE = "★☆☆☆☆ Same side for 4.5 billion years, zero atmosphere, ghosts me every new moon. Serious commit issues."

assert 1 <= len(LINE) <= 120, len(LINE)
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
