"""
Simulated AI with random function dispatcher
Every execution randomly selects one function to run.
Available features: math calculation, text reverse, random quote, dice roll, timestamp report, case converter.
No external dependencies.
"""
import random
import time
from datetime import datetime


def math_demo() -> str:
    """Random arithmetic calculation"""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    op = random.choice(["+", "-", "*"])
    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    else:
        res = a * b
    return f"[Math Task] {a} {op} {b} = {res}"


def text_reverse_demo() -> str:
    """Reverse random sample text"""
    sample_texts = [
        "Artificial intelligence simulation",
        "Local random function executor",
        "Standalone python ai module",
        "No large language model required"
    ]
    text = random.choice(sample_texts)
    reversed_text = text[::-1]
    return f"[Text Reverse] Original: {text}\nReversed: {reversed_text}"


def random_quote_demo() -> str:
    """Output random wisdom quote"""
    quotes = [
        "Progress comes from continuous trial.",
        "Keep things simple whenever you can.",
        "Small steps create big changes over time.",
        "Logic builds reliable systems."
    ]
    return f"[Quote Output] {random.choice(quotes)}"


def dice_roll_demo() -> str:
    """Simulate multi‑sided dice roll"""
    sides = random.choice([4, 6, 8, 12, 20])
    roll_result = random.randint(1, sides)
    return f"[Dice Roll] D{sides} → result: {roll_result}"


def timestamp_report_demo() -> str:
    """Return formatted current time info"""
    now = datetime.now()
    return f"[Time Report] Current runtime timestamp: {now.strftime('%Y‑%m‑%d %H:%M:%S')}"


def case_convert_demo() -> str:
    """Random upper/lower text conversion"""
    source = "Sample input string for ai processing"
    mode = random.choice(["upper", "lower", "title"])
    if mode == "upper":
        output = source.upper()
    elif mode == "lower":
        output = source.lower()
    else:
        output = source.title()
    return f"[Case Convert] Mode:{mode} → {output}"


# Register all available functions here
FUNCTION_POOL = [
    math_demo,
    text_reverse_demo,
    random_quote_demo,
    dice_roll_demo,
    timestamp_report_demo,
    case_convert_demo
]


class RandomAIEngine:
    def __init__(self):
        self.function_pool = FUNCTION_POOL

    def run_random_task(self) -> str:
        """Randomly select one function and execute it"""
        selected_func = random.choice(self.function_pool)
        return selected_func()

    def run_multiple_tasks(self, count: int = 3) -> list[str]:
        """Run several distinct random tasks"""
        selected = random.sample(self.function_pool, k=min(count, len(self.function_pool)))
        return [func() for func in selected]


def main():
    ai_engine = RandomAIEngine()
    print("=== Random‑Function AI Engine ===")
    print("Single random task output:")
    print(ai_engine.run_random_task())

    print("\nMultiple random tasks:")
    results = ai_engine.run_multiple_tasks(4)
    for idx, res in enumerate(results, 1):
        print(f"\nTask {idx}")
        print(res)


if __name__ == "__main__":
    main()

