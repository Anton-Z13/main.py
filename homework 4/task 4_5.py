"""Составить список чисел Фибоначчи содержащий 15 элементов."""
e1=1
e2=1
n = 15
print(e1, e2, end=" ")
#for i in range (2,15):
#    e1, e2 = e2, e1+e2
#    print(e2, end=" ")

while n!=0:
    e1, e2 = e2, e1 + e2
    print(e2, end=" ")
    n-=1