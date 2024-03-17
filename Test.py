def transport_fee_cal(type, weight, distance):
    if type == 'D':
        if 1 <= distance < 500:
            fee = 10000
        elif 500 <= distance <= 1000:
            fee = 25000
    elif type == 'P':
        if 1 <= distance < 500:
            fee = 15000 * weight
        elif 500 <= distance <= 1000:
            fee = 30000 * weight

    return fee

def main():
    t = input("Type (D/P): ")
    if not(t in ["D", "P"]):
        print("Invalid type")
        exit()

    if t == "P":
        w = float(input("Weight (kg): "))
        if not(0 < w <= 10):
            print("The weight must be in the range 0 < w <= 10")
            exit()
    else:
        w = 0

    d = float(input("Distance (km): "))
    if not(1 <= d <= 1000):
        print("The distance must be in the range 1 <= w <= 1000")
        exit()

    transport_fee = transport_fee_cal(t, w, d)
    print(f"Your transport fee is: {transport_fee} VND")

if __name__ == "__main__":
    main()
