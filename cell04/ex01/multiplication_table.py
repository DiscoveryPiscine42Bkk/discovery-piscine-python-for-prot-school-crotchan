number = int(input("Enter a number\n"))  # รับตัวเลขจากผู้ใช้และแปลงเป็น int

# ใช้ loop เพื่อแสดงตารางการคูณ
for i in range(10):  # ทำซ้ำ 10 ครั้ง (0-9)
    print(f"{i} x {number} = {i * number}")  # แสดงผลลัพธ์การคูณ
