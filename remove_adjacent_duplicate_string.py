def remove_adjacent_duplicate(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)




string_with_duplicates = "adcckvvzakkdeed"
string_without_duplicates = remove_adjacent_duplicate(string_with_duplicates)
print (f"original:{string_with_duplicates}")
print (f"final:{string_without_duplicates}")

