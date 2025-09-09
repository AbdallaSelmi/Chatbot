# Natural language understanding (NLU) file
from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

# a determined access path for the intents.json file
INTENTS_PATH = Path(__file__).resolve().parents[1] / 'data' / 'intents.json'

# giving the bot access to his intents after a file path was determined


def _load_intents() -> Dict[str, Dict[str, List[str]]]:
    with INTENTS_PATH.open('r', encoding='utf-8') as f:
        return json.load(f)


INTENTS = _load_intents()


def normalize(text: str) -> str:  # cleaning up the input for the bot
    return ''.join(text.strip().lower().split())


# regex fun to detect the pattern for calc instances
def detect_intent(user_text: str) -> Tuple[str, str]:
    text = normalize(user_text)

    for name, spec in INTENTS.items():
        for pat in spec.get("patterns", []):
            if any(c in pat for c in r'.^$*+?()[]\|'):
                if re.fullmatch(pat, text):
                    return name, user_text
# step 1 done
