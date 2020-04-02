
nums = [10,20,30,40,50,60,70,80,90]

score = 65

nums.sort(key=lambda num: abs(score - num))  # abs(연산)= 절대값
                                            #  num -> x값, 자동으로 선언됨

print(nums)