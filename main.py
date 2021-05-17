a = float(input())
if a > 100:
    print("Fora de intervalo")
else:
    if a > 75:
        print("Intervalo (75,100]")
    else:
        if a > 50:
            print("Intervalo (50,75]")
        else:
            if a > 25:
                print("Intervalo (25,50]")
            else:
                if a >= 0:
                    print("Intervalo [0,25]")
                else:
                    print("Fora de intervalo")