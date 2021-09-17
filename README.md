# codes
いろんな関数をメモする用
//時計
ima=datetime.datetime.now()
print(ima)

//ランダム選択（じゃんけん）
import random
data = ['goo','choki','pa']
data_choice = random.choice(data)
print(data_choice)

//今まで何日生きたか計算したいよね
import datetime
today = datetime.date.today()
birthday = datetime.date(西暦,月,日)
life = today - birthday
print(life.days)
