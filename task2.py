from collections import deque


def is_palindrome(text: str) -> bool:
    # Keep only alphanumeric characters in lowercase
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())   
    # Load characters into deque
    d = deque(cleaned)

    # Compare characters from both ends
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


def main():
    s = input("Enter a string: ")
    if is_palindrome(s):
        print("Palindrome")
    else:
        print("Not a palindrome")


if __name__ == "__main__":
    main()
