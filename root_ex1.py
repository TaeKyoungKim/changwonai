# def root_ex():
#     a = int(input('이차항의 계수는?'))
#     b = int(input('일차항의 계수는?'))
#     c = int(input('상수는?'))

#     x_1= (-b+(b**2-4*a*c)**0.5)/(2*a)
#     x_2= (-b-(b**2-4*a*c)**0.5)/(2*a)
#     return x_1 , x_2


# x1, x2 = root_ex()
# print('해는 {} 또는 {}'.format(x1, x2))


def root_ex_1(a,b,c):
    x_1= (-b+(b**2-4*a*c)**0.5)/(2*a)
    x_2= (-b-(b**2-4*a*c)**0.5)/(2*a)
    return x_1 , x_2

x = int(input('이차항의 계수는fff?'))
y = int(input('일차항의 계수는fffff?'))
z = int(input('상수는?'))
x1, x2 = root_ex_1(x,y,z)

print('해는 {} 또는 {}'.format(x1, x2))