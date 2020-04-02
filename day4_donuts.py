# 단위기능 = 도형의 넓이
import math

def getCircleArea(radius):
    return math.pow(radius,2) * math.pi
  ##         제곱(raius 의 n승)  * 원주율


def getDonutsArea(r1, r2):
                                                  # 함수 -> 반환 return
                                                  # print 하려면 또 다른함수가 필요
    area1 = getCircleArea(r1)
    area2 = getCircleArea(r2)

    return abs(area1 - area2)

if __name__ == '__main__':

    result = getDonutsArea(5,10)
    print (result)