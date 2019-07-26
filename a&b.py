import random

def A(ans_real, check):
    a = 0
    for i in range(4):
        if ans_real[i] == int(check[i]):
            a += 1
    return a

def B(ans_real, check):
    b = 0
    for i in range(0, 4):
        for j in range(1, 4):
            if ans_real[i] == int(check[i - j]):
                b += 1
    return b

def wrong(ans_real):
    for i in range(4):
        for j in range(i):
            if ans_real[i] == ans_real[j]:
                return False
    return True

a = 0
value = [i for i in range(0, 10)]
ans_real = []

for i in range(4):
    ans_real.append(random.choice(value))
    value.remove(ans_real[i])
print(ans_real)

while a != 4:
    while 1:
        ans_user = input("Enter 4 numbers:")
        if len(ans_user) == 4 and wrong(ans_user):
            break
        print('Format Error')
    check = list(ans_user)
    a = A(ans_real, check)
    b = B(ans_real, check)
    print(a, 'A', b, 'B')

print('Answer Correct')