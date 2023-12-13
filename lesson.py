x = True
y = 0
z = None


ss = "dsd"


c = 5 if z == 6 else 0



if z == 6:
    c = 5
else:
    c = 0


if y in [3, 0]:
    stroka = "4"
    is_numeric = stroka.isnumeric()

    if is_numeric:
        stroka = int(stroka)
        print(f"Вы ввели число {stroka}")
    else:
        print("Это не число")


    if isinstance(stroka, int):
        stroka -= 2
        print(stroka)



if x is not None:
    if x:
        print('add filter True')
    else:
        print("add filter False")

x = {
    "имя": "Влада",
    "возраст": 25,
}
x = dict(имя="Влада", возраст=25)
x = dict(x).values()

y = set()

