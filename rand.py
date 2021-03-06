import math

# 1단계: 데이터 정리
movie_sample = [
    (45,5,'M'),(40,10,'M'),(30,20,'M'), (25,24,'M'),
    (1,40,'A'), (10,30,'A'), (20,25,'A'),(15,30,'A')
]

# 2단계: 거리를 계산해주는 함수 만들기
def calcDistance(point1,point2):
    result = math.sqrt(math.pow(point2[0]-point1[0],2) # ,2 = 제곱
                       + math.pow(point2[1]-point1[1],2))
    return result

    # math.sqrt()  루트
    # math. pow() 제곱

count_kiss = int(input("키스씬의 숫자를 입력하세요"))
count_action = int(input("액션씬의 숫자를 입력하세요"))

#  3단계: 계산값을 기준으로 정렬

target = (count_kiss, count_action)
movie_sample.sort(key=lambda x : calcDistance(x,target))
print(movie_sample[0:3])

AA = 0
MM = 0

for x in range(3):
    if movie_sample[x][2] == 'A' :
        AA += 1
    else:
        MM += 1

#  4단계: 3개만 뽑아서 a가 많은지 m 이 많은지

if AA > MM:
    print('target은 액션')
else:
    print("target은 멜로")