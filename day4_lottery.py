# 로또 '함수'
# if __name__ == '__main__':
# 입력과 출력을 분리

import random

def makeNums():
    balls = [i for i in range(1,46)]
    random.shuffle(balls)
    return balls[0:6]

#def display():
#    # 화면 출력용도의 함수
#    # 함수안의 로직은 절차지향
#    money = int(input("금액을 입력하세요"))

def input_display():
    money = int(input("금액을 입력하세요"))
    if money % 1000 != 0:
        print("다시입력")
        return input_display()        # 재귀함수 : 값이 자기자신을 다시 호출하는것

    else:
        return money / 1000


def main():
    count  = input_display()
    for x in range(int(count)):
        nums = makeNums()
        print(sorted(nums))
    print("----------------------------------------------------------------")


if __name__ == '__main__':
    main()




