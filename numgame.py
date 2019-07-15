#数字猜谜游戏
import random
number = random.randint(0,100)
guess = -1
count = 5
print("数字猜谜游戏!\n数字在0~100之间，只有5次机会哦\n")
while guess != number & 0 < count <= 5:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜，你猜对了！么么哒")
        exit()
    elif guess < number:
        print("猜的数字小了哦...")
        count = count -1
        print("剩余次数为:",count)
    elif guess > number:
        print("猜的数字大了哦...")
        count = count -1
        print("剩余次数为:",count)
print("次数用完了哦，下次再来吧！")
