product = 0

print("[Multiplication Calculator]")
print()
while True:
    operand_1 = int(input("Enter an operand: "))
    operand_2 = int(input("Enter another operand: "))
    if operand_1 == 0 or operand_2 == 0:
        print("Why should you calculate this? The answer is always zero!")
        print()
    else:
        for o_repeats in range(0, operand_2):
            product += operand_1
        print(f"{operand_1} x {operand_2} = {product}")
        print()
        product = 0
