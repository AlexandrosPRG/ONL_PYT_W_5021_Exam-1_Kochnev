import random

def get_random(number=3):
    # zkontrolujeme zda vstup je číslo mezi 1 a 100
    if not isinstance(number, int) or number < 1 or number > 100:
        raise Exception("Invalid Data!")

    result = []  # seznam čísel

    # opakujeme, dokud nemáme požadovaný počet čísel
    while len(result) < number:
        new_number = random.randint(1, 100)  # náhodné číslo od 1 do 100
        if new_number not in result:  # pokud ještě není v seznamu
            result.append(new_number)

    return sorted(result)  # vrácení seznamu

print(get_random(7))
print(get_random())
print(get_random(25))