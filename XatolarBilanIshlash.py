while True:   # cheksiz takrorlanadi
    try:
        yosh = int(input("Yoshingizni kiriting: "))
    except ValueError:
        print("Xato! Iltimos, butun son kiriting.")
    else:
        print(f"Siz {2025 - yosh}-yilda tug‘ilgansiz!")
        break   # to‘g‘ri kiritilganda sikldan chiqadi
