from czechid import verifyIC, verifyRC

def testRC(rodnecislo):
    result = verifyRC(rodnecislo)
    ret = "valid " if result else "unvalid"
    print(f'RČ {rodnecislo} is {ret}')

def testICO(ico):
    result = verifyIC(ico)
    ret = "valid " if result else "unvalid"
    print(f'IČ/IČO {ico} is {ret}')

def testingexamples():
    rc = ["8810214897", "8810214896", "881021/4896", "8860210018", "421023689", "0509141985", "1262052528"]
    for x in rc:
        testRC(x)

    ico = ["25596641", "25596642", "a2559664"]
    for x in ico:
        testICO(x)


if __name__ == '__main__':
    testingexamples()