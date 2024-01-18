print("Tere! Olen sinu uus sõber - Python!\n")  
nimi = str(input("Mis sinu nimi on?\n"))
print(nimi, ", oi kui ilus nimi!" )

try:
    vastus = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
except:
    ValueError

try:
    if vastus == 1:
        try:
            pikkus =  float(input("Mis on teie pikkus? "))
            print(pikkus)
        except:
            ValueError

        try:
            mass = int(input("Mis on teie mass? "))
            print(mass)
        except:
            ValueError

        if pikkus > 0 and mass > 0:
            indeks = mass / (0.01*pikkus)**2

            print(nimi, "! Sinu keha indeks on: ", round(indeks, 1))
         
            if 40 > indeks > 35:
                print("Tugev rasvumine")

            elif 35 > indeks > 30:
                print("Rasvumine")

            elif 30 > indeks > 25:
                print("Ülekaal")

            elif 25 > indeks > 19:
                print("Normaalkaal")

            elif 19 > indeks > 16:
                print("Alakaal")

            elif indeks < 16:
                print("Tervisele ohtlik alakaal")

            else:
                print("Tervisele ohtlik rasvumine")
        else:
            print("Numbrid peavad olema nullist suuremad")

    else:
        print("Kahju! See on väga kasulik info!")
        print("")
except:
    ValueError


print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
