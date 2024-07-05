

with open('anna_julia.txt', 'r', encoding='utf-8') as file:
    choradeira_anna = 0
    for linha in file.readlines():
        if 'Anna' in linha:
            choradeira_anna += 1

    print(choradeira_anna)