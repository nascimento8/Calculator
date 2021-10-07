print("Digite o valor de X:")
x=input()
print("Digite o valor de Y:")
y=input()

print("Digite a operacao:")
operation=input()

if (operation == "soma"):
    result=int(x)+int(y)
    print("O resultado e = {}".format(result))
elif (operation == "subtracao"):
    result=int(x)-int(y)
    print("O resultado e = {}".format(result))
else:
    print("Operacao '{}' nao reconhecida".format(operation))
