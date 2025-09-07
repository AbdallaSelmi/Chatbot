# action.py holds functions that make the
# bot do things dynamically, such as:
# pulling real time from computer clock
# and running calculations dynamically

from datetime import datetime


def action_time_now(_: str) -> str:
    # unable to nest single quotes in fstring
    return f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


def action_calc(expr: str) -> str:
    try:
        result = eval(expr, {'__builtins__': {}}, {})
        return f'= {result}'
    except Exception:
        return 'I could not compute that. Try something like 12*(5+2).'
