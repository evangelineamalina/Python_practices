print ("hi")
def create_staircase(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
      print (subsets)
    else:
      return False

  #print (subsets)
  return subsets

value = create_staircase([1,2,3,4,5,6,7,8])
print (value)