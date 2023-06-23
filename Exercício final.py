lista_nomes = []
lista_salarios = []
lista_cpfs = []

def menu():  
    return("""
    --------- Oxente Sistemas --------
1 ................ Cadastrar Funcionário
2 ................ Exibir dados do Funcionário 
3 ................ Remover Funcionário 
4 ................ Exibir todos os funcionários cadastrados
0 ................ Sair""")       


while True:
    print(menu())
    option = int(input('Digite uma opção: '))
    
    if option == 1:
        nome = input('Nome: ')
        salario = input('Salario: ')
        cpf = input('CPF: ')
        
        lista_nomes.append(nome)
        lista_salarios.append(salario)
        lista_cpfs.append(cpf)
        
        print('Usuário adicionado com sucesso')
        
    elif option == 2:
        cpf = input('Digite o cpf: ')
        if cpf in lista_cpfs:
            indice = lista_cpfs.index(cpf)
            print(f'\nNome: {lista_nomes[indice]}')
            print(f'Salário: {lista_salarios[indice]}')
            print(f'CPF: {lista_cpfs[indice]}\n')
        else:
            print('Funcionário não encontrado')

    elif option == 3:
        cpf = input('Digite o cpf: ')
        if cpf in lista_cpfs:
            indice = lista_cpfs.index(cpf)
            lista_cpfs.pop(indice)
            lista_nomes.pop(indice)
            lista_salarios.pop(indice)
            print('Funcionário removido com sucesso.')
        else:
            print('Funcionário não encontrado')
    
    elif option == 4:
        for i in range(len(lista_nomes)):
            print(f'\nNome: {lista_nomes[i]}')
            print(f'Salário: {lista_salarios[i]}')
            print(f'CPF: {lista_cpfs[i]}\n')
    
    elif option == 0:
        print('Programa encerrado!')
        break
    
    else:
        print('Opção não válida')
