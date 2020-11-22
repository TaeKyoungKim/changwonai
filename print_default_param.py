def print_star( l,n = 3 , m=3): # 매개변수 n은 디폴트 값 1을 가짐
    for _ in range(n):
        print('************************')
        print(m)
# print_star() # 인자가 없더라도 에러 없이 수행됨
print_star(5)