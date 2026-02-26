from pathlib import Path
from changepulse2.config import load_config

BASE_DIR = Path(__file__).resolve().parent.parent  # folder ChangePulse/
CONFIG_PATH = BASE_DIR / "config.json"

def main() -> None:
    print("ChangePulse2.0 initialized")
    my_url = load_config(str(CONFIG_PATH))
    print(my_url)