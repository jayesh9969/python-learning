
from pathlib import Path

BASE_DIR = Path(__file__).parent


folder = BASE_DIR/"test_sandbox"
folder.mkdir(parents=True, exist_ok=True)

file_path = folder/"notes.txt"

file_path.write_text("pathlib is awesome")

print(file_path.name)

print(file_path.suffix)

print(file_path.exists())

print(file_path.read_text())



