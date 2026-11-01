import math

def circle_area(r):
    """计算圆面积"""
    if r < 0:
        return None
    return math.pi * r * r

def is_prime(n):
    """判断是否素数"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def str_reverse(s):
    """字符串反转"""
    return s[::-1]

def factorial(n):
    """求阶乘"""
    if n < 0:
        return None
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def show_menu():
    print("===== 多功能小程序 =====")
    print("1. 计算圆面积")
    print("2. 判断素数")
    print("3. 字符串反转")
    print("4. 计算阶乘")
    print("0. 退出程序")
    print("========================")

def main():
    while True:
        show_menu()
        opt = input("请输入功能序号：")
        if opt == "0":
            print("程序退出")
            break
        elif opt == "1":
            r = float(input("输入半径："))
            area = circle_area(r)
            if area is None:
                print("半径不能为负数！")
            else:
                print(f"圆面积 = {area:.2f}")
        elif opt == "2":
            num = int(input("输入整数："))
            if is_prime(num):
                print(f"{num} 是素数")
            else:
                print(f"{num} 不是素数")
        elif opt == "3":
            s = input("输入字符串：")
            print("反转结果：", str_reverse(s))
        elif opt == "4":
            num = int(input("输入非负整数："))
            fa = factorial(num)
            if fa is None:
                print("不能计算负数阶乘！")
            else:
                print(f"{num}! = {fa}")
        else:
            print("输入选项无效，请重新选择！")
        print("-" * 30)

if __name__ == "__main__":
    main()
