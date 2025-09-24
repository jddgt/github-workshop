product = 0

print("Here's a multiplication calculator:")
print()
while True:
    operand_1 = int(input("Enter an operand: "))
    operand_2 = int(input("Enter another operand: "))
    for o_repeats in range(0, operand_2):
        product += operand_1
    print(f"{operand_1} x {operand_2} = {product}")
    print()
    product = 0
