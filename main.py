#1
def qoshish(a, b):
    return a + b

res = qoshish(4, 5)
print(f"Qo'shish: {res}")


#2
def raqam(a, b):
    c = a * a, b * b
    return c

x = raqam(3, 4)
print(f"Kvadrat: {x}")


#3
def ism(i):
    return len(i)

res = ism("Dilnura")
print(f"Ism uzunligi: {res}")


#4
def k(a, b):
    c = max(a, b)
    return c

res = k(4, 7)
print(f"Eng katta raqam: {res}")


#5
def matn(a):
    return (f"Sizning matningiz: {a}")

res = matn("salom")
print(res)
