
p= int(input("Введите p "))
q= int(input("Введите q "))
n=p*q
f=(p-1)*(q-1)
lst=[]
for i in range (2,100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)
for x in lst:
    if f % x !=0:
        e=x
        print("e=",e)
        break
for o in range(2,100):
    if o *e %f==1 :
        d=o
        print("d=",d)

p=int(input("Введите сообщение "))
s=(p**e)%n
a = (s**d)%n
print ("Зашифрованное сообщение ",s)
print ("Расшифрованное сообщение ",a)
j=int(input())
