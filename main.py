# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
            # Process opening bracket, write your code here
            

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1
            # Process closing bracket, write your code here

    if opening_brackets_stack:
        top = opening_brackets_stack[0]
        return top.position + 1
    else:
        return "Success"


def main():
    xd = input()
    if xd[0] == "I":
        text = input()
        mismatch = find_mismatch(text)
        if isinstance(mismatch, int):
            print(mismatch)
        else:
            print("Success")
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
