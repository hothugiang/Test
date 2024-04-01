def main():
    # Nhập phân loại
    t = input("Type (D/P): ")
    if not(t in ["D", "P"]):
        print("Invalid type")
        return

    # Nhập khối lượng
    w = float(input("Weight (kg): "))
    if not(0 <= w <= 10):
        print("The weight must be in the range 0 ≤ w ≤ 10")
        return
    
    if (t == "D" and w > 1): # Nếu phân loại tài liệu và khối lượng đơn lớn hơn 1kg thì chuyển đơn thành hàng hoá
        t = 'P'
        print("Change type: P")

    # Nhập khoảng cách
    d = float(input("Distance (km): "))
    if not(1 <= d <= 1650):
        print("The distance must be in the range 1 ≤ d ≤ 1650")
        return

    # Tính phí vận chuyển
    fee = 0
    if t == 'D':
        if 1 <= d < 500:
            fee = 10000
        elif 500 <= d <= 1650:
            fee = 25000
    elif t == 'P':
        surcharge = 0 # Phụ phí
        if (w <= 1): surcharge = 10000 * (1 - w)

        if 1 <= d < 500:
            fee = 15000 * w + surcharge
        elif 500 <= d <= 1650:
            fee = 30000 * w + surcharge

    print(round(fee))

if __name__ == "__main__":
    main()
