a=int(input("숫자를 입력하세요"))
b=int(input("숫자를 입력하세요"))

if a%2==0 and b%2==0:
    print("모두 짝수입니다")
elif a%2==0 or b%2==0:
    print("둘중에 하나는 짝수")
else:
    print("둘다 홀수입니다.")