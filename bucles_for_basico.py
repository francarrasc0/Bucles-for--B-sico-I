#1.-Básico
for num in range(0, 151):
    print(num)

print("---")

#2.- Múltiplos de 5
for num in range (5, 1001, 5):
    print(num)

print("---")

#3.- Contar, a la manera del Dojo
for num in range (0,101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else: 
        print(num)

print("---")

#4.- Whoa. Es un gran idiota
sum=0
for num in range (0,500_000):
    if not num % 2 == 0:
        sum = sum + num
print(sum)

print("---")

#5.- Cuenta regresiva de a 4
for num in range (2018, 0, -4):
    print(num)

print("---")

#6.- Contador flexible
lowNum=2
highNum=9
mult=3
for num in range (lowNum, highNum+1):
    if num % mult==0:
        print(num)