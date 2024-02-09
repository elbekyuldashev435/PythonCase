card = int(input("Karta raqamni kiriting: "))
match card:
    case 1:
        print("Gisht")
    case 2:
        print("Olma")
    case 3:
        print("Chillak")
    case 4:
        print("Qarg'a")
    case 11:
        print("Valet")
    case 12:
        print("Dama")
    case 13:
        print("Qirol")
    case 14:
        print("Tuz")
    case _:
        print("Siz faqat [1,2,3,4,11,12,13,14] raqamlaridan foydalana olasiz!!!")