cpf = []
cpf = (input('Digite o seu CPF: '))

cpfArray = list(cpf)

CalculoPrimeiroDigito = (int(cpfArray[0]) * 10) + (int(cpfArray[1]) * 9) + (int(cpfArray[2]) * 8) + (
            int(cpfArray[3]) * 7 +
            (int(cpfArray[4]) * 6) + (int(cpfArray[5]) * 5) + (int(cpfArray[6]) * 4) + (int(cpfArray[7]) * 3) + (
                        int(cpfArray[8]) * 2))

primeiroDigito = (CalculoPrimeiroDigito * 10) % 11

CalculoSegundoDigito = (int(cpfArray[0]) * 11) + (int(cpfArray[1]) * 10) + (int(cpfArray[2]) * 9) + (
            int(cpfArray[3]) * 8 +
            (int(cpfArray[4]) * 7) + (int(cpfArray[5]) * 6) + (int(cpfArray[6]) * 5) + (int(cpfArray[7]) * 4) + (
                        int(cpfArray[8]) * 3) + (primeiroDigito * 2))

segundoDigito = (CalculoSegundoDigito * 10) % 11

verificadorPrimeiroDigito = int(cpfArray[9])
verificadorSegundoDigito = int(cpfArray[10])

if (primeiroDigito == verificadorPrimeiroDigito) and (segundoDigito == verificadorSegundoDigito):
    print('CPF válido')
elif (primeiroDigito == verificadorPrimeiroDigito) and (segundoDigito == 10) or (primeiroDigito == 10) and (
        segundoDigito == verificadorSegundoDigito) or (primeiroDigito == 10) and (segundoDigito == 10):
    print('CPF válido')
else:
    print('CPF inválido')
