num=35
for i in range(0,3):
    age=int(input("请输入你要猜的数字:"))
    if age==num:
        print("good")
        break
    print("猜错了")
