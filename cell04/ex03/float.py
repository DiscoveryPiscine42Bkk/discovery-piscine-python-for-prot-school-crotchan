# รับค่าจากผู้ใช้
number = input("Give me a number: ")

# ตรวจสอบว่าเลขที่กรอกเป็นทศนิยมหรือไม่
try:
    # แปลงเป็น float
    float_number = float(number)

    # ตรวจสอบว่าเป็นจำนวนเต็มหรือทศนิยม
    if float_number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("That's not a valid number.")
