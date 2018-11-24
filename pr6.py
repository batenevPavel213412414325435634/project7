def yen(rub):
    return rub / 9.5


def eur(rub):
    return rub / 75


def pou(rub):
    return rub / 84.5


def fr(rub):
    return rub / 66


def pes(rub):
    return rub / 3.2


def hry(rub):
    return rub / 2.4


def dol(rub):
    return rub / 65.5


def jen(rub):
    return rub / 0.6


def din(rub):
    return rub / 22.7


def bel(rub):
    return rub / 31.2


def output(n, label):
    if n > 0:
        print(n, label)


def main():
    rub = int(input('Введите сумму денег, которую хотите перевести: '))

    doll = round((dol(rub)), 2)
    yuan = round((yen(rub)), 2)
    euro = round((eur(rub)), 2)
    frank = round((fr(rub)), 2)
    peso = round((pes(rub)), 2)
    dinar = round((din(rub)), 2)
    pound = round((pou(rub)), 2)
    jena = round((jen(rub)), 2)
    hryvn = round((hry(rub)), 2)
    belor = round((bel(rub)), 2)

    output(doll, "$" " " "(доллар)")
    output(yuan, "¥" " " "(юань)")
    output(dinar, " " "(динар)")
    output(euro, "€" " " "(евро)")
    output(frank, "₣" " " "(франк)")
    output(peso, "$" " " "(песо)")
    output(pound, "£" " " "(фунт стерлингов)")
    output(jena, "¥" " " "(йена)")
    output(hryvn, "₴" " " "(Украинская гривна)")
    output(belor, "Br" " " "(Белорусский рубль)")


main()
