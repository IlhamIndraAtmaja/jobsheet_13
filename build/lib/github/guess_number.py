def guess_number():
    secret_number = 9
    guess_count = 0
    guess_limit = 3

    print("Tebaklah nomor rahasia")
    while(guess_count < guess_limit):
        user =int(input("Masukan nomor = "))
        if user == secret_number:
             print("Anda benar")
             break
        else:
            print("salah")
            guess_count =+1
    else:
        print("kesempatan habis")