num1 = float(input("กรุณาป้อนตัวเลขตัวที่ 1: "))
num2 = float(input("กรุณาป้อนตัวเลขตัวที่ 2: "))

# คำนวณผลคูณ
result = num1 * num2

# ตรวจสอบค่าของผลคูณ
if result < 0:
    print("The result of multiplication is negative.")
elif result > 0:
    print("The result of multiplication is positive.")
else:
    print("The result of multiplication is zero.")

# แสดงผลลัพธ์ของการคูณ
print(f"Multiplication result: {result}")
