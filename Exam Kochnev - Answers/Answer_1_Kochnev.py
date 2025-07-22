def check_character(text, character):
    count = 0  # počet znaku

    # projdeme každý znak v textu
    for char in text:
        if char == character:  # porovnáme znak s hledaným znakem
            count += 1  # pokud se shoduje, zvýšuje se počet

    return count  # vrácení výsledku

print(check_character('Order of the Phoenix', 'o'))
print(check_character('New Testament', 'o'))
print(check_character('Day of Defeat', 'o'))