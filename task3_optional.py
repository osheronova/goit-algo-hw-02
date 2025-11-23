def check_brackets(expression: str) -> bool:
    """Return True if brackets are balanced."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    # Process each character
    for ch in expression:
        # Push opening brackets
        if ch in "([{":
            stack.append(ch)
        # Check closing brackets
        elif ch in ")]}":
            # Wrong type or empty stack
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    # Stack must be empty if balanced
    return len(stack) == 0


def main():
    expr = input("Enter expression: ")
    if check_brackets(expr):
        print(f"{expr}: Balanced")
    else:
        print(f"{expr}: Not balanced")


if __name__ == "__main__":
    main()
