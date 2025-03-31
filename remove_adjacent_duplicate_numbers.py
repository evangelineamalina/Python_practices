def remove_adjacent_duplicate(numb):
    result = [numb[0]]

    for i in range(1, len(numb)):
        if numb[i] != numb[i-1]:
            result.append(numb[i])
        else:
            result.pop()
    return result
      

numbers = [1,3,3,4,5,4,5,7,7,8,8,9]
fresh_list = remove_adjacent_duplicate(numbers)

print (f"original list: {numbers}")
print(f"fresh list: {fresh_list}")
