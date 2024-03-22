def main():
    t = input("Type (D/P): ")
    if not(t in ["D", "P"]):
        print("Invalid type")
        return

    if t == "P":
        w = float(input("Weight (kg): "))
        if not(0 < w <= 10):
            print("The weight must be in the range 0 < w <= 10")
            return
    else:
        w = 0

    d = float(input("Distance (km): "))
    if not(1 <= d <= 1000):
        print("The distance must be in the range 1 <= d <= 1000")
        return

    fee = 0
    if t == 'D':
        if 1 <= d < 500:
            fee = 10000
        elif 500 <= d <= 1000:
            fee = 25000
    elif t == 'P':
        if 1 <= d < 500:
            fee = 15000 * w
        elif 500 <= d <= 1000:
            fee = 30000 * w

    print(fee)

if __name__ == "__main__":
    main()
