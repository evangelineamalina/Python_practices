def secons_largest(numbs):
    n = len(numbs)
    numbs.sort()
    #return numbs[n-2]
    for i in range(n-2, -1, -1):
        if numbs[i] != numbs[n-1]:
           return [numbs[i]]



    

num_arr = [1,3,2,6,9,3,6,9]
second_large = secons_largest(num_arr)
print (f"this is the second large: {second_large}")

