# Peter's Problem 2022 No.16

def is_valid(num):
    condition1 = False
    condition2 = False
    condition3 = False
    condition4 = False
    condition5 = False

    if num % 3 == 1:
        condition1 = True
    if num % 4 == 2:
        condition2 = True
    if num % 5 == 3:
        condition3 = True
    if num % 6 == 4:
        condition4 = True
    if num % 7 == 0:
        condition5 = True
    
    if condition1 and condition2 and condition3 and condition4 and condition5:
        return True
    else:
        return False

for num_of_students in range(1, 10000):
    if is_valid(num_of_students):
        print(f"Answer: {num_of_students}")
        break
