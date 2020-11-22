st = 'Programming'
# 자음만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue # 모음일 경우 건너띈다
    print(ch)
print('The end')