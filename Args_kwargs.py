def mul(*num):
    wyn = 1
    for n in num:
        wyn *= n
    return wyn


def kw(**war):
    for key, value in war.items():
        print(f'{key},{value}')


print(mul(3, 4, 5, 10))
kw(slowo_1="Python", slowo_2="to", slowo_3="fajny",
   slowo_4="język", slowo_5="!")
