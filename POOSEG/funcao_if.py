# homem -> maior de 18 anos, nome não pode começar com a letra A B C (ok)
# mulher -> maior de 17 anos, nome não pode começar com L M N (ok)

def pode_entrar(nome, idade, sexo):
    if sexo.lower() == 'masculino':
        if idade >= 18 and nome[0].upper() not in ['A', 'B', 'C']:
            return True
        else:
            return False
    elif sexo.lower() == 'feminino':
        if idade >= 17 and nome[0].upper() not in ['L', 'M', 'N']:
            return True
        else:
            return False
    else:
        return False

print(pode_entrar("Kevem",18,"masculino"))