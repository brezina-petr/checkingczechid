import re

# ic/ico verification , input number only - True ok, False not
def verifyIC(ic):
    # testovaci vyhovujici ICO 25596641
    # má požadovaný tvar?
    if not re.search('\d{8}', ic):
        return False

    # kontrolní součet
    a = 0
    for i in range(7):
        a += int(ic[i]) * (8 - i)

    a = a % 11
    if a == 0:
        c = 1
    elif a == 1:
        c = 0
    else:
        c = 11 - a

    return True if int(ic[7]) == c else False

# rc/rodne cislo verification , input number only - True ok, False not
def verifyRC(rc):
    # má požadovaný tvar - 9 nebo 10 cislic?
    if not re.search('\d{9,10}', rc):
        return False
    # z definic rč vyplynuly podminky
    # 00 - 99   pro první dvojčíslí
    # 01 - 12, 21 - 32, 51 - 62 a 71 - 82 pro druhé dvojčíslí
    # 01 - 31 pro třetí dvojčíslí
    # 000 - 9999 pro část za
    # je-li číslo 10.místné (po roce 1954) prvních - 10. je kontrolní číslo.
    # Odpovídá zbytku po dělení 11 prvních (9 čísel). Pro zbytek 10 je kontrolní číslo 0.

    # control number checking
    if len(rc) == 10:
        remainnb = int(rc[:9]) % 11
        if remainnb == 10:
            remainnb = 0
        if remainnb != int(rc[9]):
            return False

    # month checking
    month = rc[2:4]
    if month > "71":
        if month > "82":
            return False
    elif month > "51":
        if month > "62":
            return False
    elif month > "21":
        if month > "32":
            return False
    elif month > "01":
        if month > "12":
            return False
    else:
        return False

    # day checking
    day = rc[4:6]
    if day < "01" or day > "31":
        return False

    remainnumbers = rc[6:]
    if remainnumbers > "000" and remainnumbers < "9999":
        return True
    return False