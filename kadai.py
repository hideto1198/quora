# N = レジの数 (N >= 1)
# service = 一人の客へのサービス時間
# wait[] = 各レジでの待ち時間
# persons = 一定数の客数
# persons_wait[] = それぞれの待ち時間
from random import randint
from numpy import average

N = 1
service = 3
wait = []
persons = 10
persons_wait = []

# waitの初期化
for n in range(N):
    wait.append(0)

# persons_waitの初期化
for _ in range(persons):
    persons_wait.append(0)

for person in range(1,persons + 1):
    #到着時間
    arrive_time = randint(1, 10) #　1 ~ 10までのランダムの整数を返す => 到着時間は1 ~ 10分の範囲内
    for n in range(N):
        wait[n] -= arrive_time
        if wait[n] < 0:
            wait[n] = 0
    # 並ぶレジの選定
    k = wait.index(min(wait))
    persons_wait[person - 1] = wait[k]
    # 一人の客へのサービス時間が一定だと面白くないため、 1 ~ 5分の範囲内に置き換える
    service = randint(1, 10)
    wait[k] += service
    print(f'arrive_time = {arrive_time}\nservice = {service}\nk = {k}\nwait = {wait}')

print(persons_wait)
print(f'結果　平均待ち時間 = {average(persons_wait)}分')
    

