#-*-coding:utf-8-*-
# p = int(input("분자를 입력하시오: "))
# q = int(input("분모를 입력하시오: "))
# print("나눗셈의 몫=", p // q)
# print("나눗셈의 나머지=", p % q)
# ----------------------------------------------
# number = int(input("정수를 입력하시오: "))
# print(number%2)
# ----------------------------------------------
# sec = 1000
# min = sec // 60
# remainder = sec % 60
# print(min, remainder)
# ----------------------------------------------
# import turtle

# n = int(input("몇 각형을 그리시겠어요?(3-6): "))

# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(n):
# 	t.forward(100)
# 	t.left(360/n)
# turtle.mainloop()
# -----------------------------------------------
# americano_price = 2000
# cafelatte_price = 3000
# capucino_price = 3500
# resource_price = 100000

# americanos = int(input("아메리카노 판매 개수: "))
# cafelattes = int(input("카페라테 판매 개수: "))
# capucinos = int(input("카푸치노 판매 개수: "))

# sales = americanos*americano_price
# sales += cafelattes*cafelatte_price
# sales += capucinos*capucino_price

# print("총 매출은 {} 원입니다.".format(sales))

# if sales - resource_price > 0:
# 	print("흑자입니다.")
# else:
# 	print("적자입니다.")
# ------------------------------------------------
# ftemp = int(input("화씨온도: "))
# ctemp = (ftemp - 32) * (5/9)
# print("섭씨온도: ", ctemp)
# ------------------------------------------------
# weight = float(input("몸무게를 kg 단위로 입력하시오: "))
# height = float(input("키를 meter 단위로 입력하시오: "))
# BMI = weight / height ** 2
# print("당신의 BMI= {}".format(BMI))
# ------------------------------------------------
# money = int(input("투입한 돈: "))
# price = int(input("물건 값: "))
# change = money - price
# print("------------------------------------") 
# print("거스름돈: {}".format(change))

# num500 = change // 500
# change = change % 500
# num100 = change // 100 
# change = change % 100
# num50 = change // 50
# change = change % 50
# num10 = change // 10
# print("500원 동전의 개수: {}".format(num500))
# print("100원 동전의 개수: {}".format(num100))
# print("50원 동전의 개수: {}".format(num50))
# print("10원 동전의 개수: {}".format(num10))
# print("------------------------------------")
# -------------------------------------------------
# a = 1000
# r = 0.05
# n = 10
# print(a*(1+r)**n)
# -------------------------------------------------
# x = int(input("x: "))
# y = int(input("y: "))
# print("두수의 합: {}".format(x+y))
# print("두수의 차: {}".format(x-y))
# print("두수의 곱: {}".format(x*y))
# print("두수의 평균: {}".format((x+y)/2))
# print("큰수: {}".format(max(x, y)))
# print("작은수: {}".format(min(x, y)))
# --------------------------------------------------
# import math
# r = int(input("r: "))
# h = int(input("h: "))
# vol = math.pi*(r**2)*h
# print("원기둥의 부피: {0:.2f}".format(vol))
# ----------------------------------------------------
# n = int(input("정수를 입력하시오: "))
# s = n % 10
# n = n // 10
# s += n % 10
# n = n // 10
# s += n % 10
# n = n // 10
# s += n % 10
# print("자리수의 합: {}".format(s))
# ----------------------------------------------------
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
# print("두점 사이의 거리 = {}".format(dist))
# ----------------------------------------------------
# import turtle
# import time
# t = turtle.Turtle()
# t.shape("turtle")
# time.sleep(2)
# t.left(45)
# t.forward(141)
# t.up()
# t.goto(0, 0)
# t.down()
# t.setheading(0)
# t.forward(100)
# t.left(90)
# t.forward(100)
# turtle.mainloop()
# ------------------------------------------------------
# import turtle
# import time
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
# dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

# t = turtle.Turtle()
# t.shape("turtle")
# time.sleep(1)
# t.up()
# t.goto(x1, y1)
# t.down()
# t.goto(x2, y2)
# t.write("점의 길이= {}".format(dist), False,  align="left", font=("Arial", 14, "normal"))
# turtle.mainloop()
# -------------------------------------------------------
# import time
# fseconds = time.time()
# HOUR_FOR_DAY = 24
# SEC_FOR_HOUR = 60*60
# SEC_FOR_DAY = HOUR_FOR_DAY*SEC_FOR_HOUR
# remainsec = fseconds % SEC_FOR_DAY
# hour = int(remainsec // SEC_FOR_HOUR)
# minute = int((remainsec % SEC_FOR_HOUR) // 60)
# seconds = int((remainsec % SEC_FOR_HOUR) % 60)
# print("현재 시간(영국 그리니치 시각): {}시 {}분 {}초".format(hour+9, minute, seconds))
# ---------------------------------------------------------
# weight = int(input("물체의 무게를 입력하시오(킬로그램): "))
# velocity = int(input("물체의 속도를 입력하시오(미터/초): "))
# moving_energy = (1/2)*weight*(velocity**2)
# print("물체는 {} (줄)의 에너지를 가지고 있다.".format(moving_energy))
# ---------------------------------------------------------
# check if user input is int or float
# while True:
# 	x = input("value: ")
# 	try:
# 		x = int(x)
# 		print("integer")
# 	except ValueError:
# 		try:
# 			x = float(x)
# 			print("float")
# 		except ValueError:
# 			print("pure string")
# 			continue
# 		else:
# 			break
# 	else:
# 		break
# ----------------------------------------------------------
# price = 10000
# print("상품의 가격은 %s원입니다." % price)
# ----------------------------------------------------------
# import turtle
# s = turtle.textinput("", "이름을 입력하시오: ")
# t = turtle.Turtle()
# t.shape("turtle")

# t.left(90)
# t.forward(50)
# t.write("안녕하세요? {}씨, 터틀 인사드립니다.".format(s))
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.write("안녕하세요? {}씨, 터틀 인사드립니다.".format(s))
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.write("안녕하세요? {}씨, 터틀 인사드립니다.".format(s))
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.write("안녕하세요? {}씨, 터틀 인사드립니다.".format(s))
# t.forward(50)
# turtle.mainloop()
# --------------------------------------------------
# print("안녕하세요?")
# name = input("이름이 어떻게 되시나요?")
# # print("만나서 반갑습니다. %s씨" % name)
# print("만나서 반갑습니다. {}씨".format(name))
# print("이름의 길이는 다음과 같군요: %s" % len(name))
# age = int(input("나이가 어떻게 되나요?"))
# print("내년이면 {} 이 되시는군요.".format(age+1))
# hobby = input("취미가 무엇인가요?")
# print("네 저도 {} 좋아합니다.".format(hobby))
# --------------------------------------------------
# year = int(input("오늘의 연도를 입력하시오: "))
# month = int(input("오늘의 월을 입력하시오: "))
# day = int(input("오늘의 일을 입력하시요: "))
# print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))
# ---------------------------------------------------
# friends = []
# for i in range(5):
# 	friend = input("친구의 이름을 입력하시오: ")
# 	friends.append(friend)
# print(friends)
# ----------------------------------------------------
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# colors = ['yellow', 'red', 'blue', 'green']
# t.fillcolor(colors[0])
# t.begin_fill()
# t.circle(100)
# t.end_fill()
# t.forward(50)

# t.fillcolor(colors[1])
# t.begin_fill()
# t.circle(100)
# t.end_fill()
# t.forward(50)

# t.fillcolor(colors[2])
# t.begin_fill()
# t.circle(100)
# t.end_fill()
# t.forward(50)

# t.fillcolor(colors[3])
# t.begin_fill()
# t.circle(100)
# t.end_fill()
# t.forward(50)

# turtle.mainloop()
# -----------------------------------------------
# s = input("문자열을 입력하시오: ")
# print(s[0:2]+s[-2:])
# -----------------------------------------------
# s = input("문자열을 입력하시오: ")
# print(s + '하는 중')
# -----------------------------------------------
# symbol = input("기호를 입력하시오: ")
# word = input("중간에 삽입할 문자열을 입력하시오: ")
# print(symbol[0]+word+symbol[1])
# --------------------------------------------------
# list = eval(input("리스트 = "))
# print(list[0]+list[1]+list[2]+list[3])
# --------------------------------------------------
# import turtle

# colors = []
# color = input("색상 #1을 입력하시오: ")
# colors.append(color)
# color = input("색상 #2을 입력하시오: ")
# colors.append(color)
# color = input("색상 #3을 입력하시오: ")
# colors.append(color)

# t = turtle.Turtle()
# t.shape("turtle")

# t.fillcolor(colors[0])
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# t.penup()
# t.forward(100)
# t.pendown()

# t.fillcolor(colors[1])
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# t.penup()
# t.forward(100)
# t.pendown()

# t.fillcolor(colors[2])
# t.begin_fill()
# t.circle(50)
# t.end_fill()

# turtle.mainloop()
# -------------------------------------------------
# import turtle

# coordinates = []
# x1 = int(input('x1: '))
# y1 = int(input('y1: '))
# x2 = int(input('x2: '))
# y2 = int(input('y2: '))
# x3 = int(input('x3: '))
# y3 = int(input('y3: '))

# coordinates.append(x1)
# coordinates.append(y1)
# coordinates.append(x2)
# coordinates.append(y2)
# coordinates.append(x3)
# coordinates.append(y3)

# t = turtle.Turtle()
# t.shape("turtle")

# t.penup()
# t.goto(coordinates[0], coordinates[1])

# t.pendown()
# t.goto(coordinates[2], coordinates[3])
# t.goto(coordinates[4], coordinates[5])

# turtle.mainloop()
# -------------------------------------------------
# import turtle

# s = ''
# t = turtle.Turtle()
# t.shape("turtle")

# n = int(turtle.textinput("", "숫자를 입력하시오: "))

# if n > 0:
# 	t.goto(100, 100)
# 	s = "양수"
# elif n < 0:
# 	t.goto(100, -100)
# 	s = "음수"
# else:
# 	t.goto(100, 0)
# 	s = "0"

# t.write("거북이가 여기로 오면 " + s + "입니다.")
# turtle.mainloop()
# -------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.shapesize(3, 3)

# while True:
# 	order = input("명령을 입력하시오: ")
# 	if order == 'l':
# 		t.left(90)
# 		t.forward(100)
# 	if order == 'r':
# 		t.right(90)
# 		t.forward(100)
# 	if order == 'q':
# 		break
# ----------------------------------------------------------
# year = int(input("연도를 입력하시오: "))

# if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0):
# 	print("{} 년은 윤년입니다.".format(year))
# else:
# 	print("{} 년은 윤년이 아닙니다.".format(year))
# -----------------------------------------------------------
# import random

# print("주사위 던지기 게임을 시작합니다.")
# while True:
# 	q = input()
# 	coin = random.randrange(6)
# 	print("결과는 {} 입니다.".format(coin+1))
# 	if q == 'q':
# 		break
# print("게임이 종료되었습니다.")
# ----------------------------------------------------------
# import turtle
# import random

# screen = turtle.Screen()
# front = "front.gif"
# back = "back.gif"
# screen.addshape(front)
# screen.addshape(back)

# t = turtle.Turtle()

# while True:
# 	q = input()
# 	if q == 'q':
# 		break

# 	coin = random.randrange(2)
# 	if coin == 0:
# 		print("front")
# 		t.shape(front)
# 		t.stamp()
# 	else:
# 		print("back")
# 		t.shape(back)
# 		t.stamp()
# ------------------------------------------------------
# import random

# time = random.randint(1, 24)
# sunny = random.choice([True, False])

# print("좋은 아침입니다. 지금 시각은 {} 시입니다.".format(time))

# if sunny:
# 	print("현재 날씨가 화창합니다.")
# else:
# 	print("현재 날씨가 화창하지 않습니다.")

# if ((time >= 6 and time <= 9) or (time >= 14 and time <= 16)) and sunny:
# 	print("종달새가 노래를 합니다.")
# else:
# 	print("종달새가 노래를 하지 않습니다.")
# ---------------------------------------------------------
# id = 'sylee'
# password = 'rkrrlska'

# i = input("아이디를 입력하시오: ")
# p = input("패스워드를 입력하시오: ")

# if i == id:
# 	if p == password:
# 		print("환영합니다.")
# 	else:
# 		print("잘못된 패스워드입니다.")
# else:
# 	print("아이디를 찾을수 없습니다.")
# --------------------------------------------------------
# import random

# pos = ["왼쪽", "중앙", "오른쪽"]

# pick_usr = input("어디를 수비하시겠어요?(왼쪽, 중앙, 오른쪽)")
# pick_com = random.choice(pos)

# if pick_usr == pick_com:
# 	print("수비에 성공하셨습니다.")
# else:
# 	print("페널티 킥이 성공하였습니다.")
# --------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("", "도형을 입력하시오: ")
# if s == "사각형":
# 	x = int(turtle.textinput("", "가로"))
# 	y = int(turtle.textinput("", "세로"))
# 	t.forward(x)
# 	t.left(90)
# 	t.forward(y)
# 	t.left(90)
# 	t.forward(x)
# 	t.left(90)
# 	t.forward(y)
# elif s == "삼각형":
# 	x = int(turtle.textinput("", "변의 길이"))
# 	t.forward(x)
# 	t.left(120)
# 	t.forward(x)
# 	t.left(120)
# 	t.forward(x)
# elif s == "원":
# 	x = int(turtle.textinput("", "반지름"))
# 	t.circle(x)
# turtle.mainloop()
# --------------------------------------------------------------
# temp = int(input("현재 온도를 입력하시오: "))
# if temp >= 25:
# 	print("반바지를 입으세요")
# else:
# 	print("긴바지를 입으세요")
# ---------------------------------------------------------------
# import random

# f_num = random.randint(1, 100)
# s_num = random.randint(1, 100)

# answer = int(input(str(f_num) + ' - ' + str(s_num) + ' = '))
# if answer == f_num - s_num:
# 	print("맞았습니다.")
# else:
# 	print("오답입니다.")
# ----------------------------------------------------------------
# num = int(input("정수를 입력하시오: "))
# if num % 2 == 0 and num % 3 == 0:
# 	print("2와 3으로 나누어 떨어집니다.")
# else:
# 	print("2와 3으로 나누어 떨어지지 않습니다.")
# ---------------------------------------------------------------
# import random

# win_num = random.randint(10, 99)
# lotto_num = int(input("복권번호를 입력하시오: (두자리 수)"))

# w_f = win_num // 10
# w_b = win_num % 10
# l_f = lotto_num // 10
# l_b = lotto_num % 10

# if win_num == lotto_num:
# 	prize = 100
# elif w_f == l_f or w_f == l_b:
# 	prize = 50
# elif w_b == l_f or w_b == l_b:
# 	prize = 50
# else:
# 	prize = 0

# print("복권 당첨 번호는 {} 였습니다.".format(win_num))
# print("상금은 {} 만원입니다.".format(prize))
# --------------------------------------------------------------
# import turtle

# x1 = int(input("큰 원의 중심좌표 x1: "))
# y1 = int(input("큰 원의 중심좌표 y1: "))
# r1 = int(input("큰 원의 반지름: "))
# x2 = int(input("작은 원의 중심좌표 x2: "))
# y2 = int(input("작은 원의 중심좌표 y2: "))
# r2 = int(input("작은 원의 반지름: "))

# t = turtle.Turtle()
# t.shape("turtle")

# t.penup()
# t.goto(x1, y1)
# t.pendown()
# t.circle(r1)

# t.penup()
# t.goto(x2, y2)
# t.pendown()
# t.circle(r2)

# dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# if dist <= r1 - r2:
# 	t.write("작은 원이 큰원의 내부에 있습니다.")
# else:
# 	t.write("작은 원이 큰원에 포함되지 않습니다.")

# turtle.mainloop()	
# turtle.bye()
# ----------------------------------------------------------------
# for i in range(1, 6, 1):
# 	print(i, end=" ")
# ---------------------------------------------------------
# for i in range(10, 0, -1):
# 	print(i, end= " ")
# ------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# n = int(turtle.textinput("", "몇각형을 원하시나요?"))

# for i in range(n):
# 	t.forward(100)
# 	t.left(360/n)
# ------------------------------------------------------
# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")
# for i in range(50):
# 	t.forward(random.randint(1, 100))
# 	t.setheading(random.randint(0, 360))
# --------------------------------------------------------
# n = int(input("정수를 입력하시오: "))
# s = 1
# for i in range(1, n+1):
# 	s *= i
# print("{}!은 {}".format(n, s))
# -------------------------------------------------------
# response = "아니"
# while response == "아니":
# 	response = input("엄마, 다 됐어?")
# print("먹자")
# --------------------------------------------------------
# password = ""
# while not password == "pythonisfun":
# 	password = input("type password: ")
# print("로그인 성공")
# --------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# cnt = 0
# while cnt < 4:
# 	t.forward(100)
# 	t.right(90)
# 	cnt += 1
# ---------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# for i in range(5):
# 	t.forward(100)
# 	t.right(144)
# ----------------------------------------------------------
# import turtle

# turtle.bgcolor("black")
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)
# t.width(3)

# colors = ["red", "purple", "blue", "green", "yellow", "orange"]
# for i in range(10, 500, 5):
# 	t.color(colors[i%6])
# 	t.forward(i)
# 	t.right(134)

# turtle.mainloop()
# -----------------------------------------------------------
# answer = "yes"
# total = 0
# while answer == "yes":
# 	n = int(input("숫자를 입력하시오: "))
# 	total += n
# 	answer = input("계속?(yes/no): ")
# print("합계는 : {}".format(total))
# ----------------------------------------------------------
# import random

# user = 0
# answer = random.randint(1, 100)
# print("1부터 100 사이의 숫자를 맟추시오 ")

# cnt = 0
# while not user == answer:
# 	cnt += 1								
# 	user = int(input("숫자를 입력하시오: "))
# 	if answer < user:
# 		print("낮음!")
# 	elif answer > user:
# 		print("높음!")

# print("축하합니다. 시도횟수= {}".format(cnt))
# ---------------------------------------------------------
# import random

# operators = ["+", "-"]
# while True:
# 	f_num = random.randint(1, 100)
# 	s_num = random.randint(1, 100)
# 	operator = random.choice(operators)
# 	answer = int(input("{} {} {} = ".format(f_num, operator, s_num)))
# 	if operator == "+":
# 		if answer == f_num + s_num:
# 			print("잘했어요!!")
# 		else:
# 			print("다음번에는 잘할 수 있죠?")
# 	elif operator == "-":
# 		if answer == f_num - s_num:
# 			print("잘했어요!!")
# 		else:
# 			print("다음번에는 잘할 수 있죠?")
# ---------------------------------------------------------
# breads = ["호밀빵", "위트", "화이트"]
# meats = ["미트볼", "소시지", "닭가슴살"]
# vegitables = ["양상추", "토마토", "오이"]
# sources = ["마요네즈", "허니 머스타드", "칠리"]
# for i in breads:
# 	for j in meats:
# 		for x in vegitables:
# 			for y in sources:
# 				print("{} + {} + {} + {}".format(i, j, x, y))
# -----------------------------------------------------------
# while True:
# 	light = input("신호등 색상을 입력하시오 ")
# 	if light == 'blue':
# 		break 
# print("전진!!")
# -----------------------------------------------------------
# import turtle
# import time

# center = turtle.Turtle()
# center.shape("turtle")

# t = turtle.Turtle()
# t.shape("turtle")
# t.color("red")
# t.speed(0)

# angle = 90
# for i in range(12):
# 	t.left(angle)
# 	t.penup()
# 	t.forward(50)
# 	t.pendown()
# 	t.forward(50)
# 	t.penup()
# 	t.forward(20)
# 	t.stamp()
# 	time.sleep(1)
# 	t.home()
# 	angle -= 360 // 12

# turtle.mainloop()
# -----------------------------------------------------------
# import random
# import time 

# while True:
# 	name = input("이름: (종료하려면 엔터키) ")
# 	if name == "":
# 		break

# 	subject = input("무엇에 대하여 알고 싶은가요? ")
# 	print("{}님 \" {} \"에 대하여 질문 주셨군요.".format(name, subject))
# 	print("운명의 주사위를 굴려볼게요...")
# 	answer = random.randint(1, 8)
# 	time.sleep(3)

# 	if answer == 1:
# 		print("네, 확실합니다. ")
# 	elif answer == 2:
# 		print("전망이 좋을거 같은데요.")
# 	elif answer == 3:
# 		print("믿으셔도 됩니다.")
# 	elif answer == 4:
# 		print("글쎄요 아닌거 같군요.")
# 	elif answer == 5:
# 		print("한 점의 의심도 없이 맞습니다.")
# 	elif answer == 6:
# 		print("그럼요, 명백히 올바른 선택을 했습니다.")
# 	elif answer == 7:
# 		print("제 답변은 No 입니다.")
# 	else:
# 		print("나중에 다시 물어보세요.")
# ---------------------------------------------------------------
# for i in range(2, 100, 2):
# 	print(i, end=" ")
# ---------------------------------------------------------------
# year = 0
# balance = 1000

# while balance < 12000:
# 	year = year + 1
# 	interest = balance * 0.07
# 	balance = balance + interest
# print("{} 년이 걸립니다.".format(year))
# -----------------------------------------------------------
# import random

# x = random.randint(1, 9)
# y = random.randint(1, 9)
# guess = 0

# while not guess == x*y:
# 	guess = int(input("{} * {} 는 ".format(x, y)))
# print("맞았습니다.")
# ----------------------------------------------------------
# n = 1
# s = 0
# while not n == 0:
# 	n = int(input("정수를 입력하시오: "))
# 	s += n
# print("합은 {} 입니다.".format(s))
# ----------------------------------------------------------
# import random

# while True:
# 	input()
# 	print("첫번째 주사위= {}".format(random.randint(1, 6)))
# 	print("두번째 주사위= {}".format(random.randint(1, 6)))
# -----------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.color("blue")
# t.speed(0)
# angle = 90

# for i in range(6):
# 	t.left(angle)
# 	t.forward(200)
# 	t.forward(-60)
# 	t.left(60)
# 	t.forward(60)
# 	t.forward(-60)
# 	t.right(120)
# 	t.forward(60)
# 	t.penup()
# 	t.home()
# 	t.pendown()
# 	angle += 360 // 6

# turtle.mainloop()
# -------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.color("red")
# angle  = 0

# for i in range(10):
# 	for j in range(5):
# 		t.left(144)
# 		t.forward(200)
# 	t.home()
# 	angle += 5
# 	t.left(angle)

# turtle.mainloop()
# -------------------------------------------------------
# import random
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(10):
# 	r = random.randint(50, 300)
# 	x = random.randint(-300, 300)
# 	y = random.randint(-300, 300)

# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()
# 	t.circle(r)
# ---------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# leng = 180
# TOTAL = 200
# for i in range(5):
# 	for j in range(4):
# 		t.forward(leng)
# 		if j < 2: 
# 			t.right(90)
# 		else:
# 			t.left(90)
# 		leng = TOTAL - leng

# turtle.mainloop()
# ----------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.color("red", "yellow")
# t.forward(-150)
# init_pos = t.pos()

# t.begin_fill()
# while True:
# 	t.forward(300)
# 	t.right(170)
# 	if abs(t.pos() - init_pos) < 1:
# 		break

# t.end_fill()

# turtle.mainloop()
# ---------------------------------------------------------
# import turtle
# import math

# t = turtle.Turtle()
# t.color("red", "yellow")
# t.shape("turtle")

# for deg in range(360):
# 	rad = 3.14 * deg / 180
# 	print(math.sin(rad))
# 	t.goto(deg, 180*math.sin(rad))

# turtle.mainloop()
# --------------------------------------------------------
# def get_sum(start, end):
# 	sum = 0
# 	for i in range(start, end+1):
# 		sum += i
# 	return sum 

# print(get_sum(1, 10))
# --------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# s = int(turtle.textinput("", "몇각형을 그릴까요?"))
# colors = ["red", "green", "yellow"]

# def square(leng, s):
# 	t.begin_fill()
# 	for i in range(s):
# 		t.forward(leng)
# 		t.left(360/s)
# 	t.end_fill()

# t.penup()
# t.forward(-250)
# t.pendown()
# for i in range(3):
# 	t.color(colors[i])
# 	square(100, s)
# 	t.penup()
# 	t.forward(200)
# 	t.pendown()

# turtle.mainloop()
# --------------------------------------------------------
# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")
# colors = ["yellow", "red", "green", "blue", "purple"]

# def n_polygon(n, length):
# 	for i in range(n):
# 		t.forward(length)
# 		t.left(360/n)

# for i in range(10):
# 	t.left(20)	
# 	t.color(random.choice(colors))
# 	t.begin_fill()
# 	n_polygon(6, 100)
# 	t.end_fill()
	
# turtle.mainloop()
# -------------------------------------------------------
# # global variable
# def calculate_area(radius):
# 	global area 
# 	area = 3.14 * radius**2
# 	return 

# area = 0
# r = float(input("원의 반지름: "))
# calculate_area(r)
# print(area)
# -------------------------------------------------------
# # default argument
# def greet(name, msg="반가워^^"):
# 	print("안녕", name + ', ' + msg)

# greet("영희")
# --------------------------------------------------------
# # keyword argument
# def calc(x, y, z):
# 	return x*y+z

# print(calc(y=20, x=10, z=30))
# --------------------------------------------------------
# import turtle
# import random

# colors = ["yellow", "red", "green", "blue", "purple"]

# def square():
# 	leng = random.randint(10, 100)
# 	for i in range(4):
# 		t.forward(leng)
# 		t.left(90)

# def circle():
# 	radius = random.randint(10, 100)
# 	t.color(random.choice(colors))
# 	t.circle(radius)

# def drawit(x, y):
# 	t.color(random.choice(colors))
# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()

# 	t.begin_fill()
# 	# square()
# 	circle()
# 	t.end_fill()

# s = turtle.Screen()
# s.onscreenclick(drawit)
# t = turtle.Turtle()
# t.shape("turtle")
# turtle.mainloop()
# ----------------------------------------------------------
# import turtle

# def drawit(x, y):
# 	t.goto(x, y)

# t = turtle.Turtle()
# t.shape("turtle")
# t.width(3)

# s = turtle.Screen()
# s.onscreenclick(drawit)
# s.onkey(t.penup, "Up")
# s.onkey(t.pendown, "Down")
# s.listen()

# turtle.mainloop()
# --------------------------------------------------
## draw fractal
# import turtle
# import random

# # GAP = 20
# # RATE = 0.7
# GAP = random.randint(10, 30)
# RATE = random.uniform(0.6, 0.8)

# def fractal(leng, deg):
# 	t.left(deg)
# 	# stop for iteration
# 	if leng < 10:
# 		return
# 	t.forward(leng)
	
# 	fractal(leng*RATE, GAP)
# 	fractal(leng*RATE, -2*GAP)
# 	# get back to previous position 
# 	t.left(GAP)
# 	t.backward(leng)

# t = turtle.Turtle()
# t.color("green")
# t.speed(0)
# t.penup()
# t.goto(0, -350)
# t.pendown()
# fractal(200, 90)
# turtle.mainloop()
# ---------------------------------------------------------
# import turtle

# def tree(length):
# 	if length > 5:
# 		t.forward(length)
# 		t.right(20)
# 		tree(length-15)
# 		t.left(40)
# 		tree(length -15)
# 		t.right(20)
# 		t.backward(length)

# t = turtle.Turtle()
# t.left(90)

# t.color("green")
# t.speed(1)
# tree(90)
# -----------------------------------------------------------
# import turtle

# def draw_chart(data):
# 	for num in data:
# 		t.begin_fill()
# 		t.left(90)
# 		t.forward(num)
# 		t.write(num, align="left")
# 		t.right(90)
# 		t.forward(30)
# 		t.right(90)
# 		t.forward(num)
# 		t.left(90)
# 		t.end_fill()

# data = [120, 56, 309, 220, 156, 23, 98]
# t = turtle.Turtle()
# t.color("blue", "red")
# t.width(3)
# draw_chart(data)
# turtle.mainloop()
# ----------------------------------------------------------
# import turtle

# def draw_maze(x, y):
# 	for i in range(2):
# 		t.penup()
# 		if i==1:
# 			# shift(move) the line
# 			t.goto(x+100, y+100)
# 		else:
# 			t.goto(x, y)
# 		t.pendown()
# 		t.forward(300)
# 		t.right(90)
# 		t.forward(300)
# 		t.left(90)
# 		t.forward(300)

# def turn_left():
# 	t.left(10)

# def turn_right():
# 	t.right(10)

# def move():
# 	t.forward(10)

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)

# draw_maze(-300, 200)

# screen = turtle.Screen()
# screen.onkey(turn_left, "Up")
# screen.onkey(turn_right, "Down")
# screen.onkey(move, "Right")
# screen.listen()

# t.penup()
# t.goto(-300, 250)
# t.pendown()
# t.speed(3)
# t.width(3)
# t.color("red")
# turtle.mainloop()
# --------------------------------------------------------
# import turtle
# import random

# def draw_circle(x, y, r):
# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()
# 	t.begin_fill()
# 	t.circle(r)
# 	t.end_fill()

# def draw_line(x, y, deg):
# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()
# 	t.left(deg)
# 	t.forward(40)
# 	t.left(-deg)

# def draw_snowman(x, y):
# 	draw_circle(x, y, 30)
# 	draw_circle(x, y-20, 20)
# 	draw_circle(x, y-80, 40)
# 	draw_line(x-20, y, 130)
# 	draw_line(x+20, y, 50)

# s = turtle.Screen()
# s.bgcolor("skyblue")
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("black", "white")

# for i in range(5):
# 	x = random.randint(-300, 300)
# 	y = random.randint(-300, 300)
# 	draw_snowman(x, y)

# turtle.mainloop()
# ------------------------------------------------------------
# import turtle

# def hexagon():
# 	for i in range(6):
# 		# rotate to the left 
# 		# for single hexa
# 		t.forward(50)
# 		t.left(360/6)

# def draw_hexa():
# 	for i in range(6):
# 		hexagon()
# 		# rotate to the right
# 		# for all hexas
# 		t.forward(50)
# 		t.right(60)

# t = turtle.Turtle()
# t.shape("turtle")
# draw_hexa()
# turtle.mainloop()
# --------------------------------------------------------
# import turtle

# x_leng = 300
# y_leng = 600

# def f(x):
# 	return x**2+1

# t = turtle.Turtle()
# t.speed(0)
# t.penup()
# t.goto(-x_leng/2, -y_leng/2)
# t.pendown()
# t.forward(x_leng)
# t.write("X", font=("Arial", 30, "normal"), align="right")
# t.backward(x_leng)
# t.left(90)
# t.forward(y_leng)
# t.write("Y", font=("Arial", 30, "normal"), align="right")
# t.backward(y_leng)
# t.right(90)
# t.shape("turtle")

# for x in range(230):
# 	# print("{},{}".format(x, f(x)))
# 	t.goto(-x_leng/2+x, -y_leng/2+0.01*f(x))

# turtle.mainloop()
# -------------------------------------------------------------
# import turtle

# num_line = 12

# def draw_line():
# 	t.forward(100)
# 	t.backward(100)

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)

# for i in range(num_line):
# 	draw_line()
# 	t.right(360/num_line)

# turtle.mainloop()
# --------------------------------------------------------------
# def happyBirthday(name):
# 	for i in range(4):
# 		if i == 2:
# 			print("Happy Birthday, dear {}".format(name))
# 		else:
# 			print("Happy Birthday to you!")
		
# happyBirthday("이성용")
# ---------------------------------------------------------------
# def make_problem():
# 	x = int(input("첫번째 정수: "))
# 	y = int(input("두번째 정수: "))
# 	print("정수 {} + {} 의 합은?".format(x, y))

# make_problem()
# --------------------------------------------------------------
# PI = 3.14

# def circleArea(radius):
# 	return PI*radius**2

# def circleCircumference(radius):
# 	return 2*PI*radius

# print("반지름이 5인 원의 면적: {}".format(circleArea(5)))
# print("반지름이 5인 원의 둘레: {}".format(circleCircumference(5)))
# --------------------------------------------------------------
# def add(a, b):
# 	return a+b

# print("({} + {}) = {}".format(20, 10, add(20, 10)))
# ---------------------------------------------------------------
# import turtle
# import random

# screen = turtle.Screen()
# screen.addshape("rabbit.gif")
# screen.addshape("turtle.gif")

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t1.shape("rabbit.gif")
# t1.color("yellow")
# t1.shapesize(3)
# t1.pensize(3)

# t2.shape("turtle.gif")
# t2.color("blue")
# t2.shapesize(3)
# t2.pensize(3)

# t1.speed(0)
# t2.speed(0)

# t1.penup()
# t1.goto(-400, 0)
# t1.pendown()

# t2.penup()
# t2.goto(-400, -100)
# t2.pendown()

# t1.speed(1)
# t2.speed(1)

# input()
# for i in range(100):
# 	if t1.pos()[0] < 400 and t2.pos()[0] < 400:
# 		t1.forward(random.randint(1, 50))
# 		t2.forward(random.randint(1, 50))

# turtle.mainloop()
# ---------------------------------------------------------------
# import turtle

# def draw_shape(radius, color):
# 	t.left(270)
# 	t.width(1)
# 	t.color("black", color)
# 	t.begin_fill()
# 	t.circle(radius/2.0, -180)
# 	t.circle(radius, 180)
# 	t.left(180)
# 	t.circle(-radius/2.0, -180)
# 	t.end_fill()

# t = turtle.Turtle()
# t.speed(1)
# draw_shape(200, "red")
# t.right(90)
# draw_shape(200, "blue")

# turtle.mainloop()
# ----------------------------------------------------------
# fun game 
# import turtle
# import random
# import math
# import time

# def turnleft():
# 	player.left(30)

# def turnright():
# 	player.right(30)

# def play():
# 	player.forward(2)

# def moveCommets(c):
# 	c.forward(2)
# 	c.left(random.randint(-30, 30))
# 	if c.xcor() > 400:
# 		c.setx(400)
# 	if c.xcor() < -400:
# 		c.setx(-400)
# 	if c.ycor() > 400:
# 		c.sety(400)
# 	if c.ycor() < -400:
# 		c.sety(-400)

# def isCollision(t1, t2):
# 	x_diff = t1.xcor() - t2.xcor()
# 	y_diff = t1.ycor() - t2.ycor()
# 	distance = math.sqrt(x_diff**2+y_diff**2)
# 	if distance < 15:
# 		return True
# 	else:
# 		return False

# wn = turtle.Screen()

# score = 0
# commet_num = 3

# player = turtle.Turtle()
# player.color("blue")
# player.shape("turtle")
# player.shapesize(1)
# player.penup()
# player.speed(0)

# score_pen = turtle.Turtle()
# score_pen.speed(0)
# score_pen.color("Black")
# score_pen.penup()
# score_pen.setposition(-400, 350)
# scorestring = "Score: %s" %score
# score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
# score_pen.hideturtle()

# screen = player.getscreen()
# s = turtle.Screen()
# s.onkey(turnleft, "Left")
# s.onkey(turnright, "Right")
# s.listen()

# commets = []
# for i in range(commet_num):
# 	t = turtle.Turtle()
# 	commets.append(t)

# for commet in commets:
# 	commet.shape("circle")
# 	commet.color("red")
# 	commet.penup()
# 	commet.speed(0)
# 	commet.goto(random.randint(-300, 300), random.randint(-300, 300))
# 	commet.col = False

# # Speed Up the Game
# wn.tracer(0)
# while True:
# 	wn.update()
# 	if not score == commet_num * 10:
# 		play()
# 	for commet in commets:
# 		moveCommets(commet)

# 		if isCollision(player, commet):
# 			commet.hideturtle()
# 			commet.col = True
# 			break

# 	score = 0
# 	for commet in commets:
# 		if commet.col:
# 			score += 10

# 	score_pen.clear()
# 	scorestring = "Score: %s" %score
# 	score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

# 	if score == commet_num * 10:
# 		commets[0].goto(0, 0)
# 		commets[0].write("Game Over", False, align="center", font=("Arial", 50, "normal"))

# 	time.sleep(0.01)
# --------------------------------------------------------------
# import turtle
# import math

# def turnleft():
# 	player.left(5)

# def turnright():
# 	player.right(5)

# def fire():
# 	print(vel)
# 	x = 0
# 	y = 0
	
# 	angle = player.heading()
# 	vx = vel*math.cos(angle*3.14/180.0)
# 	vy = vel*math.sin(angle*3.14/180.0)

# 	while player.ycor() >= 0:
# 		x = x + vx
# 		y = y + vy
# 		vy = vy - 10
# 		player.goto(x, y)


# player = turtle.Turtle()
# player.shape("turtle")
# player.width(3)

# vel = int(turtle.textinput("", "초기속도를 입력하시오"))
# screen = turtle.Screen()
# screen.onkey(turnleft, "Left")
# screen.onkey(turnright, "Right")
# screen.onkey(fire, "space")
# screen.listen()

# turtle.mainloop()
# -----------------------------------------------------------
# decryption and encryption
# plain_text = "I can find my dream !!"

# def encrypt(text):
# 	enc_text = ""
# 	for c in text:
# 		x = ord(c)
# 		x = x+1
# 		cc = chr(x)
# 		enc_text += cc
# 	return enc_text

# def decryption(text):
# 	dec_text = ""
# 	for c in text:
# 		x = ord(c)
# 		x = x - 1
# 		cc = chr(x)
# 		dec_text += cc
# 	return dec_text

# encrypted_text = encrypt(plain_text)
# decrypted_text = decryption(encrypted_text)
# print("encription text: [  {}  ]".format(encrypted_text))
# print("encription text: [  {}  ]".format(decrypted_text))
# -------------------------------------------------------------
# import turtle
# from random import randint

# def draw_circle(turtle, color, x, y, radius):
# 	turtle.penup()
# 	turtle.fillcolor(color)
# 	turtle.goto(x, y)
# 	turtle.pendown()
# 	turtle.begin_fill()
# 	turtle.circle(radius)
# 	turtle.end_fill()

# def draw_rectangle(turtle, color, x, y, width, height):
# 	turtle.penup()
# 	turtle.fillcolor(color)
# 	turtle.goto(x, y)
# 	turtle.pendown()
# 	turtle.begin_fill()
# 	for i in range(2):
# 		turtle.forward(width)
# 		turtle.left(90)
# 		turtle.forward(height)
# 		turtle.left(90)
# 	turtle.end_fill()

# def draw_trepezoid(turtle, color, x, y, width, height):
# 	turtle.penup()
# 	turtle.fillcolor(color)
# 	turtle.goto(x, y)
# 	turtle.pendown()
# 	turtle.begin_fill()
# 	turtle.forward(width)
# 	turtle.right(60)
# 	turtle.forward(height)
# 	turtle.right(120)
# 	turtle.forward(width+20)
# 	turtle.right(120)
# 	turtle.forward(height)
# 	turtle.right(60)
# 	turtle.end_fill()

# def draw_star(turtle, color, x, y, size):
# 	turtle.penup()
# 	turtle.fillcolor(color)
# 	turtle.goto(x, y)
# 	turtle.pendown()
# 	turtle.begin_fill()
# 	for i in range(5):
# 		turtle.forward(size)
# 		turtle.right(144)
# 	turtle.end_fill()

# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(0)

# x = 0
# y = 0
# width = 240

# draw_rectangle(t, "brown", x-20, y-50, 30, 50)

# height = 20
# for i in range(10):
# 	width = width - 20
# 	x = - width/2
# 	draw_trepezoid(t, "green", x, y, width, height)
# 	draw_circle(t, "red", x+randint(0, width), y+randint(0, height), 10)
# 	y = y + 20

# draw_star(t, "yellow", 4, y, 100)
# t.penup()
# t.color("red")
# t.goto(-200, 250)
# t.write("Merry Christmas", font=("Arial", 24, "italic"))
# t.goto(-200, 220)
# t.write("Happy New Year!", font=("Arial", 24, "italic"))
# turtle.mainloop()
# -----------------------------------------------------------------
# heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
# heroes.sort()
# for hero in heroes:
# 	print(hero)

# numbers = [9, 6, 7, 1, 8, 4, 5, 3, 2]
# numbers.sort()
# numbers.reverse()
# print(numbers)
# print(sorted(numbers, reverse=True))
# -----------------------------------------------------------------
# import random

# quotes = []
# quotes.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.")
# quotes.append("분노는 바보들의 가슴속에서만 살아간다.")
# quotes.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
# quotes.append("사람은 사랑할 때 누구나 시인이 된다.")
# quotes.append("시작이 반이다.")

# dailyQuote = random.choice(quotes)
# print("#######################")
# print("#  오늘의 속담 #")
# print("#######################")
# print("")
# print(dailyQuote)
# -------------------------------------------------------------------
# import random

# problems = []
# problems.append("3+127")
# problems.append("24+47")
# problems.append("674+42")
# problems.append("19+72")
# problems.append("76+353")



# dailyProblem = random.choice(problems)
# print("#######################")
# print("#  오늘의 산수 문제 #")
# print("#######################")
# print("")
# print("{} = ?".format(dailyProblem))
# answer = int(input("답을 입력하세요. "))
# if answer == eval(dailyProblem):
# 	print("정답입니다.")
# else:
# 	print("틀렸습니다.")
# ------------------------------------------------------------
# import turtle

# def draw_olympic_symbol():
# 	for x, y, c in pos:
# 		t.penup()
# 		t.goto(x, y)
# 		t.pendown()
# 		t.color(c)
# 		t.begin_fill()
# 		t.circle(30)
# 		t.end_fill()

# pos = [
# 			[0, 0, "blue"],
# 			[-120, 0, "purple"],
# 			[60, 60, "red"],
# 			[-60, 60, "yellow"],
# 			[-180, 60, "green"]
# 		]

# t = turtle.Turtle()
# t.shape("turtle")
# draw_olympic_symbol()
# turtle.mainloop()
# --------------------------------------------------------
# phone_book = {}
# phone_book["홍길동"] = "010-1234-5678"
# phone_book["강감찬"] = "010-1234-5677"
# phone_book["이순신"] = "010-1234-5679"
# phone_book.clear()
# for key, value in phone_book.items():
# 	print(key + " : " + phone_book[key])
# for key in sorted(phone_book.keys()):
# 	print(key + " : " + phone_book[key])
# print(dir(phone_book))
# --------------------------------------------------------
# def show_stocks(itmes):
# 	print("")
# 	print("--------------------")
# 	print("  재고 수량   ")
# 	print("--------------------")
# 	for item in sorted(items.keys()):
# 		print("{} - {}".format(item, items[item]))
# 	print("--------------------")

# def inc_stocks(items, item, num):
# 	if item in items:
# 		items[item] += num
# 		print("{} 의 재고가 {} 만큼 증가하였습니다.".format(item, num))
# 		show_stocks(items)
# 	else:
# 		print("입력하신 물건은 판매하지 않습니다.")

# def dec_stocks(items, item, num):
# 	if item in items:
# 		items[item] -= num
# 		print("{} 의 재고가 {} 만큼 감소하였습니다.".format(item, num))
# 		show_stocks(items)
# 	else:
# 		print("입력하신 물건은 판매하지 않습니다.")


# items = {"커피음료":7, "펜":3, "종이컵":2, "우유":1, "콜라":4, "책":5}


# print("############################################################")
# print("###                 편의점 재고관리 프로그램             ###")
# print("############################################################")

# while True:
# 	print("\n\n")
# 	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# 	print("       프로그램 메뉴       ")
# 	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# 	print(" 1. 재고 리스트")
# 	print(" 2. 재고량 증가")
# 	print(" 3. 재고량 감소")
# 	print(" 4. 프로그램 종료")
# 	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# 	sel = int(input("\n원하시는 프로그램 메뉴를 선택하여 주세요. : "))

# 	if sel == 1:
# 		show_stocks(items)
# 	elif sel == 2:
# 		item = input("물건의 이름을 입력하시오: ")
# 		num = int(input("증가할 재고 수량을 입력하시오: "))
# 		inc_stocks(items, item, num)
# 	elif sel == 3:
# 		item = input("물건의 이름을 입력하시오: ")
# 		num = int(input("감소할 재고 수량을 입력하시오: "))
# 		dec_stocks(items, item, num)
# 	elif sel == 4:
# 		break
# -------------------------------------------------------------
# eng_dict = {}

# eng_dict['one'] = '하나'
# eng_dict['two'] = '둘'
# eng_dict['three'] = '셋'

# word = input("단어를 입력하시오: ")
# if word in eng_dict:
# 	print(eng_dict[word])
# else:
# 	print("사전에 그런 단어는 없습니다.")
# -----------------------------------------------------------
# import smtplib
# from email.mime.text import MIMEText

# me = "sssssqew@gmail.com"
# you = ["sssssqew@gmail.com", "sssssqew@naver.com"]
# contents = "두근두근 파이썬 책에서 보냈습니다."

# for to in you:
# 	msg = MIMEText(contents, _charset='euc-kr')
# 	msg['Subject'] = "두근두근 파이썬"
# 	msg['From'] = me
# 	msg['To'] = to

# 	server = smtplib.SMTP('smtp.gmail.com', 587)
# 	server.ehlo()
# 	server.starttls()
# 	server.ehlo()

# 	server.login(me, "7618353ab")
# 	server.sendmail(me, to, msg.as_string())
# 	server.quit()
# print("이메일 보내기를 완료하였습니다.")
# ---------------------------------------------------------------
# nums = []
# for i in range(5):
# 	n = int(input("정수를 입력하시오: "))
# 	nums.append(n)
# mean = sum(nums)/len(nums)
# print("평균 : {}".format(mean))
# ----------------------------------------------------------------
# import random

# dice_counts = [0, 0, 0, 0, 0, 0]

# for i in range(1000):
# 	result = random.randint(1, 6)
# 	dice_counts[result-1] += 1

# for idx, freq in enumerate(dice_counts):
# 	print("주사위가 {}인 경우는 {}".format(idx+1, freq))
# -----------------------------------------------------------------
# phone_book = {}
# mode = 1

# def switch_mode(name):
# 	global mode
# 	if name == "":
# 		mode = 1- mode 

# while True:
# 	if mode:
# 		name = input("(입력모드)이름을 입력하시오: ")
# 		switch_mode(name)
# 		if mode: 
# 			phone_number = input("전화번호를 입력하시오: ")
# 			phone_book[name] = phone_number
# 	else:
# 		name = input("(검색모드)이름을 입력하시오: ")
# 		switch_mode(name)
# 		if not mode:
# 			if name in phone_book:
# 				print("'{}'씨의 전화번호는 {}입니다.".format(name, phone_book[name]))
# 			else:
# 				print("전화번호부에 그런 이름은 존재하지 않습니다.")
# ----------------------------------------------------------------
# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")

# colors = ['red', "blue", "green", "yellow", "purple", "orange"]

# def draw_square(x, y, c):
# 	t.color(c)
# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()
# 	t.begin_fill()
# 	for i in range(4):
# 		t.forward(100)
# 		t.left(90)
# 	t.end_fill()

# for color in colors:
# 	x = random.randint(-300, 300)
# 	y = random.randint(-300, 300)
# 	draw_square(x, y, color)

# turtle.mainloop()
# --------------------------------------------------
# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")

# colors = ['red', "blue", "green", "yellow", "purple", "orange"]

# def draw_square(x, y, c, leng, sides):
# 	t.color(c)
# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()
# 	t.begin_fill()
# 	for i in range(sides):
# 		t.forward(leng)
# 		t.left(360/sides)
# 	t.end_fill()

# for color in colors:
# 	x = random.randint(-300, 300)
# 	y = random.randint(-300, 300)
# 	leng = random.randint(50, 300)
# 	sides = random.randint(3, 8)
# 	draw_square(x, y, color, leng, sides)

# turtle.mainloop()
# -----------------------------------------------------------
# import turtle
# import random

# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.Screen()
# s.bgcolor("black")

# colors = ['red', "blue", "green", "yellow", "purple", "orange"]

# def draw_star(x, y, c, leng):
# 	t.color(c)
# 	t.penup()
# 	t.goto(x, y)
# 	t.pendown()
# 	t.begin_fill()
# 	for i in range(5):
# 		t.forward(leng)
# 		t.left(144)
# 	t.end_fill()

# for color in colors:
# 	x = random.randint(-300, 300)
# 	y = random.randint(-300, 300)
# 	leng = random.randint(50, 300)
# 	draw_star(x, y, color, leng)

# turtle.mainloop()
# -------------------------------------------------------
# domains = {
# 	"kr": "대한민국", 
# 	"sk": "슬로바키아"	,
# 	"no": "노르웨이",
# 	"us": "미국",
# 	"jp": "일본",
# 	"hu": "헝가리",
# 	"de": "독일"
# }

# for k, v in domains.items():
# 	print(k, ": ", v)
# ---------------------------------------------------------
# import random

# problems = {
# 	'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
# 	'변수': '데이터를 저장하는 메모리 공간',
# 	'함수': '작업을 수행하는 문장들의 집합에 이름을 붙인것',
# 	'리스트': '서로 관련이 없는 항목들의 모임'
# }

# while True:
# 	print("다음은 어떤 단어에 대한 설명일까요?")
# 	print("-----------------------------------------")
# 	result = random.choice(list(problems.values()))
# 	print(result)
# 	print("")
# 	for idx, key in enumerate(problems.keys()):
# 		print("({}) {}\t".format(idx, key))
# 	print("")
# 	answer = input()
# 	if problems[answer] == result:
# 		print("정답입니다 !")
# 	else:
# 		print("아쉽지만 오답입니다 T.T")
# 	print("\n\n")
# ----------------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# size = int(input("집의 크기를 얼마로 할까요? "))

# t.forward(size)
# t.right(90)
# t.forward(size)
# t.right(90)
# t.forward(size)
# t.right(90)
# t.forward(size)
# t.right(90)

# t.forward(size)
# t.left(120)
# t.forward(size)
# t.left(120)
# t.forward(size)
# t.left(120)

# turtle.mainloop()
# --------------------------------------------------
# stadium = input("경기장은 어디입니까? ")
# winner = input("이긴팀은 어디입니까? ")
# loser = input("진팀은 어디입니까? ")
# vip = input("우수선수는 누구입니까? ")
# score = input("스코어는 몇대몇입니까? ")

# print("")
# print("================================")
# print("오늘 {}에서 야구 경기가 열렸습니다.".format(stadium))
# print("{}과 {}가 치열한 공방전을 펼쳤습니다.".format(winner, loser))
# print("{}이 맹활약을 하였습니다.".format(vip))
# print("결국 {}이 {}를 {}로 이겼습니다.".format(winner, loser, score))
# print("================================")
# ---------------------------------------------------
# street = "서울시 종로구"
# type = "아파트"
# number_of_rooms = 3
# price = 10**8

# print("#######################")
# print("# #")
# print("# 부동산 매물 광고 #")
# print("# #")
# print("#######################")
# print("")
# print("{}에 위치한 아주 좋은 {}가 매물로 나왔습니다.".format(street, type))
# print("이 {}는 {}개의 방을 가지고 있으며 가격은 {}입니다.".format(type, number_of_rooms, price))
# ---------------------------------------------------
# from datetime import datetime

# name = input("이름을 입력하시오: ")
# age = int(input("나이를 입력하시오: "))
# current_year = datetime.today().year
# print("{}씨는 {}년에 100살이시네요!".format(name, current_year+(100-age)))
# ---------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# radius = 50
# for i in range(3):
# 	t.circle(radius)
# 	t.penup()
# 	t.forward(100)
# 	t.pendown()
# 	radius += 20

# turtle.mainloop()
# ---------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")

# side = 100
# for i in range(3):
# 	t.forward(side)
# 	t.left(120)
# ---------------------------------------------------
# import turtle

# t = turtle.Turtle()
# t.shape("turtle")
# t.shapesize(2)

# size = 50
# num = 6
# for i in range(num):
# 	t.right(360/num)
# 	for j in range(num):
# 		t.forward(size)
# 		t.right(360/num)

# turtle.mainloop()
# ----------------------------------------------------
# from tkinter import *

# window = Tk()
# button = Button(window, text="클릭!")
# button.pack()
# # handle event from user
# window.mainloop()
# ----------------------------------------------------
# from tkinter import *

# window = Tk()

# l1 = Label(window, text="화씨")
# l2 = Label(window, text="섭씨")
# l1.pack()
# l2.pack()

# e1 = Entry(window)
# e2 = Entry(window)
# e1.pack()
# e2.pack()

# b1 = Button(window, text="화씨->섭씨")
# b2 = Button(window, text="섭씨->화씨")
# b1.pack()
# b2.pack()

# window.mainloop()
# -----------------------------------------------------
# from tkinter import *

# def process():
# 	temp = float(e1.get())
# 	mytemp = (temp-32)*5/9
# 	e2.insert(0, str(mytemp))

# window = Tk()

# l1 = Label(window, text="화씨", font="helvetica 16 italic")
# l2 = Label(window, text="섭씨", font="helvetica 16 italic")
# l1.grid(row=0, column=0)
# l2.grid(row=1, column=0)

# e1 = Entry(window, bg="black", fg="yellow")
# e2 = Entry(window, bg="black", fg="yellow")
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

# b1 = Button(window, text="화씨->섭씨", command=process)
# b2 = Button(window, text="섭씨->화씨")
# b1.grid(row=2, column=0)
# b2.grid(row=2, column=1)

# window.mainloop()
# ------------------------------------------------
# from tkinter import *

# def process():
# 	print("안녕하세요?")

# window = Tk()
# button = Button(window, text="클릭", command=process)
# button.pack()
# window.mainloop()
# -------------------------------------------------
# from tkinter import *

# def change_img():
# 	path = inputBox.get()
# 	img = PhotoImage(file=path)
# 	imageLabel.configure(image=img)
# 	imageLabel.image = img


# window = Tk()

# photo = PhotoImage(file="turtle.gif")
# imageLabel = Label(window, image=photo)
# imageLabel.pack()

# inputBox = Entry(window)
# inputBox.pack()

# button = Button(window, text="Submit", command=change_img)
# button.pack()

# window.mainloop()
# -------------------------------------------------------
# from tkinter import *
# from PIL import Image, ImageTk
# import os

# width = 590
# height = 850

# def change_img():
# 	path = inputBox.get()
# 	if os.path.isfile(path):
# 		img = Image.open(path).resize((width, height))
# 		photo = ImageTk.PhotoImage(img)
# 		imgLabel.configure(image=photo)
# 		imgLabel.image = photo
# 	else:
# 		print("찾으시는 파일이 없습니다.")


# # img = Image.open('supergirl.jpg')
# # img.show()

# window = Tk()
# window.geometry("600x900")

# img = Image.open('supergirl.jpg').resize((width, height))
# photo = ImageTk.PhotoImage(img)
# imgLabel = Label(window, image=photo)
# imgLabel.pack()

# inputBox = Entry(window)
# inputBox.pack()

# button = Button(window, text="Change Img", command=change_img)
# button.pack()

# window.mainloop()
# ----------------------------------------------------------
# 이미지 보여주기 (다른 버전)
# from tkinter import *
# from PIL import Image, ImageTk
# import os

# width = 590
# height = 850
# ext = ['jpg', 'png']
# pos = 0

# def change_img():
# 	path = inputBox.get()
# 	if os.path.isfile(path):
# 		img = Image.open(path).resize((width, height))
# 		photo = ImageTk.PhotoImage(img)
# 		imgLabel.configure(image=photo)
# 		imgLabel.image = photo
# 	else:
# 		print("찾으시는 파일이 없습니다.")

# def ch_img(pos):
# 	img = Image.open(imgs[pos]).resize((width, height))
# 	photo = ImageTk.PhotoImage(img)
# 	imgLabel.configure(image=photo)
# 	imgLabel.image = photo

# def prev_img():
# 	global pos
# 	pos = (pos - 1) % len(imgs)
# 	ch_img(pos)

# def next_img():
# 	global pos
# 	pos = (pos + 1) % len(imgs)
# 	ch_img(pos)


# window = Tk()
# window.geometry("600x930")

# img = Image.open('supergirl.jpg').resize((width, height))
# photo = ImageTk.PhotoImage(img)
# imgLabel = Label(window, image=photo)
# imgLabel.grid(row=0, column=0)

# inputBox = Entry(window)
# inputBox.grid(row=1, column=0)

# button1 = Button(window, text="Prev Img", command=prev_img)
# button1.grid(row=2, column=0)

# button2 = Button(window, text="Next Img", command=next_img)
# button2.grid(row=3, column=0)

# cur_dir = os.getcwd()

# imgs = []
# for file in os.listdir(cur_dir):
# 	for e in ext:
# 		if os.path.splitext(file)[1][1:] == e:
# 			imgs.append(file)
# 			# print(file)
# 			break
# # print(imgs)

# window.mainloop()
# -----------------------------------------------------
# mp3 player

from tkinter import *
from PIL import Image, ImageTk
from mutagen.id3 import ID3, USLT, TRCK, TIT2, TPE1, TALB, TDRC, TCON, TENC, COMM, APIC, error
from mutagen import File
import vlc
import os
import random
import timeit
import time
import threading
import tooltips


class Song:
	'''
	get song info.
	'''

	def __init__(self, song_name):
		self.song_name = song_name

	def get_metadata(self):
		global art_name
		global info

		mp3 = File(self.song_name)
		art_name = os.path.splitext(self.song_name)[0] + ".jpg"

		meta = {}
		duration = mp3.info.length
		pTimeMin = str(int(duration // 60))
		pTimeSec = str(int(duration % 60))

		if int(pTimeMin) < 10:
			pTimeMin = "0" + pTimeMin

		if int(pTimeSec) < 10:
			pTimeSec = "0" + pTimeSec

		meta["재생시간"] = str(" : ".join([pTimeMin, pTimeSec]))
		meta["가사"] = str(mp3.tags.getall("USLT")[0])

		for key in mp3.tags:
			if key == "APIC:Cover" or key == "APIC:":
				artwork = mp3.tags[key].data
				if not os.path.isfile(art_name):
					with open(art_name, 'wb') as img:
					   img.write(artwork)
				else:
					print("앨범 아트가 이미 존재합니다.")
			if key == "TALB":
				meta["앨범"] = str(mp3.tags[key])					

			if key == "TIT2":
				meta["타이틀"] = str(mp3.tags[key])
				
			if key == "TPE1":
				meta["가수"] = str(mp3.tags[key])	

			if key == "TCON":
				meta["장르"] = str(mp3.tags[key])
			
			if key == "TDRC":
				date = str(mp3.tags[key])
				date = ".".join([date[:4] , date[4:6], date[6:8]])
				meta["발매일"] = date

		# concatenate song info 
		info = ""
		for key in sorted(meta.keys()):
			info += " : ".join([key, meta[key]])
			info += "\n------------------------------\n"

		return duration, len(meta["가사"])

class Play:
	'''
	control music playing
	'''

	def __init__(self):
		pass

	def get_songs_list(self):
		cur_dir = os.getcwd()

		print("---------------- [track] ----------------")
		for file in os.listdir(cur_dir):
			for e in ext:
				if os.path.splitext(file)[1][1:] == e:
					songs_track.append(file)
					print(file)
					break		
		print("-----------------------------------------")

	def load_track(self):  
		self.line = 2
		song = Song(songs_track[pos])	
		self.duration, self.len_letters = song.get_metadata()
		self.p = vlc.MediaPlayer(song.song_name)

	def playing(self):
		time_per_letter = self.duration / self.len_letters
		# print("playing...")
	
		if self.p.is_playing():
			self.line += 0.1
			# print(str(self.line))
			# print("재생시간 : {}".format(self.duration))
			# print("글자수 : {}".format(self.len_letters))
			# print("글자당 시간간격 : {}".format(time_per_letter))
			song_info.see(str(round(self.line, 1)))
		threading.Timer(time_per_letter+0.115, self.playing).start()

	def play_music(self):
		self.p.play()
		p_btn.configure(text="Pause", command=self.pause_music)
		self.playing()

	def pause_music(self):
		self.p.pause()
		p_btn.configure(text="Play", command=self.play_music)
	
	def ch_img(self):
		global img_copy

		img_path = os.path.splitext(songs_track[pos])[0] + ".jpg"
		img = Image.open(img_path).resize((width, height))
		photo = ImageTk.PhotoImage(img)
		img_copy = img.copy()

		album_cover.configure(image=photo)
		album_cover.image = photo

	def prev_song(self):
		global pos
		play_list.selection_clear(pos)

		pos = (pos - 1) % len(songs_track)
		# print(songs_track[pos])
		self.p.stop()
		self.load_track()
		self.ch_img()
		p_btn.configure(text="Play", command=self.play_music)
		song_info.delete('1.0', END)
		song_info.insert("1.0", info)
		song_info.tag_add("center", "1.0", "end")
		
		# enable focus
		play_list.selection_set(pos)
		play_list.activate(pos)
		play_list.focus()

	def next_song(self):
		global pos
		# disable focus
		play_list.selection_clear(pos)

		pos = (pos + 1) % len(songs_track)
		# print(songs_track[pos])
		self.p.stop()
		self.load_track()
		self.ch_img()
		p_btn.configure(text="Play", command=self.play_music)
		song_info.delete('1.0', END)
		song_info.insert("1.0", info)
		song_info.tag_add("center", "1.0", "end")
		
		# enable focus
		play_list.selection_set(pos)
		play_list.activate(pos)
		play_list.focus()


def resize(e):
	img = img_copy.resize((e.width, e.width))
	photo = ImageTk.PhotoImage(img)
	album_cover.configure(image=photo)
	album_cover.image = photo

def show_list(e):
	song_info.pack_forget()
	play_list.configure(state="normal")
	
	# Clear the listbox
	play_list.delete(0, "end")
	for song in songs_track:
		play_list.insert("end", song)

	print("double clicked !!")

def show_lyrics(e):
	play_list.selection_clear(pos)
	song_info.pack()
	play_list.configure(state="disabled")

def check_selection(e):
	global pos
	play_list.selection_clear(pos)

	sel_song = play_list.get('active')
	if sel_song in songs_track:
		pos = songs_track.index(sel_song)

	play.p.stop()
	play.load_track()
	play.ch_img()
	p_btn.configure(text="Play", command=play.play_music)
	song_info.delete('1.0', END)
	song_info.insert("1.0", info)
	song_info.tag_add("center", "1.0", "end")
	print(sel_song)



	
# set album size
width = 500
height = 500

# initialize to get track
songs_track = []
ext = ['mp3']
art_name = "" 
info = ""

# create playing control instance
play = Play()
play.get_songs_list()

pos = random.randint(0, len(songs_track)-1)
play.load_track()


# create GUI to control songs
window = Tk()
window.title("Sylee Music Player")
window.geometry("500x800")
# window.resizable(0, 0) # do not resize
window.minsize(300,700) 
window.maxsize(700,900)

# add album cover to label
img = Image.open(art_name).resize((width, height))
photo = ImageTk.PhotoImage(img)
img_copy = img.copy()

album_cover = Label(window, image=photo)
album_cover.pack(fill=BOTH, expand=True)
album_cover.bind('<Configure>', resize)

# control buttons
btn_frame = Frame()
btn_frame.pack(fill="none", expand=True)

prev_btn = Button(btn_frame, text="Prev", fg="ivory2", bg="#383a39", font="Verdana 10 bold", command=play.prev_song)
prev_btn.pack(side=LEFT, padx=5, pady=5)

p_btn = Button(btn_frame, text="Play", fg="mint cream", bg="#383a39", font="Verdana 10 bold", command=play.play_music)
p_btn.pack(side=LEFT, padx=5, pady=5)

next_btn = Button(btn_frame, text="Next", fg="ivory2", bg="#383a39", font="Verdana 10 bold", command=play.next_song)
next_btn.pack(side=LEFT, padx=5, pady=5)

# display info.
song_info = Text(window, wrap=None, bg="black", fg="#383a39", font=("Helvetica", 12, "bold"), borderwidth=0, highlightthickness=0, pady=15)
song_info.tag_configure("center", justify='center')
song_info.insert("1.0", info)
song_info.tag_add("center", "1.0", "end")
song_info.pack()
song_info.bind('<Double-Button-1>', show_list)

play_list = Listbox(window, bg="black", fg="#383a39", font=("Helvetica", 12, "bold"), borderwidth=0, highlightthickness=0
										, justify=CENTER, state="disabled")
play_list.pack(fill=BOTH, expand=True)
play_list.bind('<Double-Button-1>', check_selection)
# play_list.bind("<Enter>", show_lyrics)
# play_list.bind("<Leave>", show_list)


window.update()
tip = tooltips.ListboxToolTip(song_info, ["* Double click *", "Show songs list"])


# process events
window.mainloop()
# -----------------------------------------------------




















































































