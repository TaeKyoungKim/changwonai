n = int(input('합계를 구할 수를 입력하세요 : '))
s = 0
i = 1
while i <= n:
    s = s + i
    i += 1
# print('1부터 {} 까지의 합은 {}'.format(n,s))
print('1부터 %d 까지의 합은 %s' %(n ,s))
