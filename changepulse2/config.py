import json

def load_config(path: str) -> dict:
    """
    Load config from JSON file.
    Expected format:
    {
      "url": "https://example.com"
    }
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
            if not raw.strip():
                return {}
            parsed = json.loads(raw)
            return parsed if isinstance(parsed, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError, OSError, UnicodeError):
        return {}