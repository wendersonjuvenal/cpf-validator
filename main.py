# by: Wenderson Juvenal

while True:
    cpf = input("CPF (only numbers): ")
    if len(cpf) != 11:
        print("Enter an 11-character CPF! ")
        continue
    break


def dig10():
    count = 10  # counter
    sum = 0
    for i in cpf[:-2]:
        sum += int(i) * count
        count -= 1
    dig10 = (sum * 10) % 11
    dig10 = 0 if (dig10 == 10) else dig10
    return str(dig10)


def dig11():
    count = 11
    sum = 0
    for i in cpf[:-2] + dig10():
        sum += int(i) * count
        count -= 1
    dig11 = (sum * 10) % 11
    dig11 = 0 if dig11 == 10 else dig11
    return str(dig11)


conditions = (cpf[9]==dig10() and cpf[10]==dig11() and len(set(cpf))!=1)
# (len(set(cpf)) != 1) - checks if the string doesn't have all the same values;

print("Valid CPF" if conditions else "Invalid CPF")
