str = input()

# Please write your code here.
def solution(s):
    stack = []

    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if not stack:
                return "No"
            stack.pop()

    if stack:
        return "No"

    return "Yes"

print(solution(str))