from random import randrange

nums = []

def checkDup(nums, num):   #함수= 독립된 공간으로 생각

   result = False

   for x in nums:
       if x == num:
           result = True
           break

    return False

#루프를 nums 가 6개가 되는 동안
while len(nums) < 6 :
#1~45사이의 숫자를 뽑는다
    num = randrange(1.46)

    if checkDuplicate(nums, num) == True:
        continue

    nums.append(num)

#뽑은 값이 있다면 다시 뽑는다(중복)



