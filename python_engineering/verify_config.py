from pathlib import Path

BASE_DIR = Path(__file__).parent

read_path = BASE_DIR/"pyproject.toml"

print(read_path.read_text())