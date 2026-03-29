from datetime import date
from pathlib import Path


text = input("jot: ")
jot_path = Path("jot.txt")

jot_contents = jot_path.read_text()
jot_contents += f"{date.today()} {text}\n"
jot_path.write_text(jot_contents)
