"""
def masala1():
    a = 0
    def count():
        nonlocal a
        a += 1
        return a
    return count

masala = masala1()
print(masala())
print(masala())
print(masala())
print(masala())


def masala2(a):
    def ichki_masala(b):
        return [i for i in b if i > a]
    return ichki_masala

masala_2 = masala2(5)
print(masala_2([2, 4, 7, 1, 9, 10]))



def masala3(a, c):
    def raqam(b):
        if b == '+':
            return f"{a} + {c} = {a + c}"
        elif b == '-':
            return f"{a} - {c} = {a - c}"
        elif b == '*':
            return f"{a} * {c} = {a * c}"
        elif b == '/' or b == ':':
            return f"{a} {b} {c} = {a / c}"
        else:
            return "bunday amal yo'q"
    return raqam

masala_3 = masala3(6, 4)
print(masala_3('+'))
print(masala_3('-'))
print(masala_3('*'))
print(masala_3(':'))
print(masala_3('/'))



def masala4(a):
    def sonlar(b):
        if b == 'juft':
            return [i for i in a if not i % 2]
        elif b == 'toq':
            return [i for i in a if i % 2]
        else:
            return "faqat juft yoki toq so'zlarini kiriting"
    return sonlar

masala_4 = masala4([1, 3, 2, 17, 34, 93, 102])
print(masala_4('juft'))
print(masala_4('toq'))


def masala5(a):
    def polindrom(b):
        if b == 'polindrome':
            return [i for i in a if str(i) == str(i)[::-1]]
        elif b == 'not_polindrome':
            return [i for i in a if str(i) != str(i)[::-1]]
        else:
            return "bunday buyruq yo'q"
    return polindrom

masala_5 = masala5([1, 9, 99, 234, 1221, 23432, 999, 345, 936])
print(masala_5('polindrome'))
print(masala_5('not_polindrome'))


def masala6(a):
    def tub_murakkab(b):
        if b == 'tub':
            tub = []
            for e in a:
                c = 0
                for i in range(2, e):
                    if not e % i:
                        c += 1
                if c == 0:
                    tub.append(e)
            return tub
        elif b != 'murakkab':
            return "bunday buyruq yo'q"
        else:
            murakkab = []
            for e in a:
                c = 0
                for i in range(2, e):
                    if not e % i:
                        c += 1
                if c != 0:
                    murakkab.append(e)
            return murakkab
    return tub_murakkab

masala_6 = masala6([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(masala_6('tub'))
print(masala_6('murakkab'))



def daraja(a):
    def sonlar(x):
        return x ** a
    return sonlar

kvadrat = daraja(2)
kub = daraja(3)

print(kvadrat(7))
print(kub(7))


def til(a):
    def ism(b):
        if a == 'en':
            return f"{b} : Hello World"
        elif a == 'uz':
            return f"{b} : salom dunyo"
        return f"Bu tilni bilmayman. Men faqat uz va en tillarini bilaman"
    return ism

uz = til('uz')
en = til('en')
boshqa = til('boshqa')

print(uz('Feruz'))
print(en('Feruz'))
print(boshqa('Feruz'))
"""

