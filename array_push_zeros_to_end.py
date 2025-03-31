def push_zeros_to_end(arra):
    
    j = 0
    n = len(arra)
    temp = [0]*n
    for i in range(n):
        if arra[i] != 0:
            temp[j] = arra[i]
            j += 1
    print (f"thisis temp:{temp}")
    return  temp  



num_array = [1,0,4,0,5,0,0,5,6,7]
new_array = push_zeros_to_end(num_array)
print (f"new array:{new_array}")
