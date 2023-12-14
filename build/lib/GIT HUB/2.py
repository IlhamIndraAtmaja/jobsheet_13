def guess_number():
    print("Konversi berat")
    berat = int(input("Masukan berat = "))
    type = input("K atau L = ")

    if (type == "K"):
        kilo = berat * 0.453592
        print(kilo)
    elif (type == "L"):
        lbs = berat *2.204623
        print(lbs)