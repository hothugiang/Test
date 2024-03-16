def transport_fee_cal(type, weight, distance):
    if type == 'D':
        if 1 <= distance <= 50:
            fee = 10000
        elif 50 < distance <= 500:
            fee = 20000
        elif 500 < distance <= 1000:
            fee = 30000
    elif type == 'P':
        # Tính phụ phí 
        if weight <= 10:
            e = 0
        elif 10 < w <= 50:
            e = 10000
        else: 
            e = 15000
            
        # Tính phí cơ bản dựa trên khoảng cách
        if 1 <= distance <= 50:
            fee = 15000 + e
        elif 50 < distance<= 500:
            fee = 25000 + e
        elif 500 < distance <= 1000:
            fee = 35000 + e

    return fee

t = input("Type (D/P): ")
if not(t in ["D", "P"]):
    print("Invalid type")
    exit()

w = int(input("Weight (kg): "))
if type == 'D':
    if not(0 <= w <= 1):
        print("The weight of the document must be in the range 0 <= w <= 1")
        exit()
elif type == "P":
    if not(0 < w <= 100):
        print("The weight of the package must be in the range 0 < w <= 100")
        exit()

d = int(input("Distance (km): "))
if not(1 <= d <= 1000):
    print("The transport distance must be in the range 1 < w <= 1000")
    exit()

transport_fee = transport_fee_cal(t, w, d)
print(f"Your transport fee is: {transport_fee} VND")
