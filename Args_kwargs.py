def mul(*num):
    wyn = 1
    for n in num:
        wyn *= n
    return wyn

def kw(**war):
    for w in war:
        print(w)

print(mul(3,4,5,10))
print("Python","to","fajny","język","!")
