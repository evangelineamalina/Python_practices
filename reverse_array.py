def reverse_array(numb):
    #result = numb.reverse()
    result = []

    for i in range(len(numb)-1,-1, -1):
        result.append(numb[i])
      # result.pop()
    return result
      

numbers = [1,3,3,4,5,4,5,7,7,8,8,9]
fresh_list = reverse_array(numbers)

print (f"original list: {numbers}")
print(f"frereversesh list: {fresh_list}")
