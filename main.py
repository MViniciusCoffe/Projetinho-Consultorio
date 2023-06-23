from classes import *
from functions import *
from os import *


endereço_clinica = Endereço('R. Professor Aluízio Filho 53', 'Várzea do Barro', 'Rio Grande do Meio', '31748-214')
telefone_clinica = Contato('92 2222-2221', 'telefone')
insta_clinica = Contato('@OdontologiaSantoAndre', 'Instagram' )
email_clinica = Contato('SantoAndreOdonto@gmail.com', 'E-mail')
clinica = Clinica(endereço_clinica)
clinica.adicionar_contato_clinica(telefone_clinica)
clinica.adicionar_contato_clinica(insta_clinica)
clinica.adicionar_contato_clinica(email_clinica)


while True:
    (menu_inicial())
    option = int(input('Digite uma opção: '))
    if option == SAIR:      #sair
        print('\033[0;36mPROGRAMA ENCERRADO\033[m')
        break
    
    elif option == AREA_PACIENTE:       #area do paciente
        while True:
            (menu_paciente())
            option = int(input('Digite uma Opção: '))
            
            if option == FAZER_LOGIN:
                cpf_paciente = input('Digite seu CPF: ')
                senha_paciente = input('Digite sua senha: ')
                
                if clinica.fazer_login_paciente(cpf_paciente, senha_paciente, paciente):
                    print('\033[0;36m\nPaciente Logado com sucesso\n\033[m')
                    system('pause')
                    while True:
                        (menu_login_paciente())
                        option = int(input('Digite uma Opção: '))
                        
                        if option == MEUS_DADOS:
                            for paciente in clinica.pacientes_ativos:
                                if paciente.cpf == cpf_paciente:    
                                    print(paciente)
                                    system('Pause')
                        
                        elif option == MUDAR_DADOS:
                            #Repete as informações
                            nome = input('Nome: ')
                            idade = input('Idade: ')
                            telefone = input('Telefone: ')

                            #endereço
                            rua = input('Rua: ')
                            cidade = input('Cidade: ')
                            estado = input('Estado: ')
                            cep = input('CEP: ')

                            #indicação e senha
                            indicacao = input('Indicação: ')
                            senha_nova = input('Senha: ')
                            
                            #classe
                            endereço_novo_paciente = Endereço(rua, cidade, estado, cep )
                            login_novo_paciente = SignUP(cpf_paciente, senha_nova)
                            novo_paciente = Paciente(nome, cpf_paciente, idade, endereço_novo_paciente, telefone, indicacao, login_novo_paciente)

                            clinica.editar_paciente(novo_paciente, cpf_paciente)

                            print('\n\033[0;36mPaciente Alterado com sucesso\n\033[m')
                            system('pause')
                            break
                        
                        elif option == APAGAR_CONTA:
                            clinica.desativar_paciente(cpf_paciente, paciente)
                            print('\n\033[0;36mUsuário Removido\n\033[m')
                            system('pause')
                            break
                        
                        elif option == SAIR:
                            break
                else:
                    print('\n\033[0;31mLogin ou senha incorretos\n\033[m')
                    system('pause')

            
            elif option == CADASTRAR_PACIENTE:       #cadastrar paciente
                #informações básicas
                nome = input('Nome: ')
                cpf = input('CPF: ')
                idade = input('Idade: ')
                telefone = input('Telefone: ')

                #endereço do paciente
                rua = input('Rua: ')
                cidade = input('Cidade: ')
                estado = input('Estado: ')
                cep = input('CEP: ')

                #indicação e senha
                indicacao = input('Recebeu alguma indicacao da nossa clínica?: ')
                senha = input('Senha: ')
                
                #início da classe do paciente
                endereço_paciente = Endereço(rua, cidade, estado, cep)
                signup_paciente = SignUP(cpf, senha)
                paciente = Paciente(nome, cpf, idade, endereço_paciente, telefone, indicacao, signup_paciente)

                try:
                    verif = clinica.adicionar_paciente(paciente, cpf)
                    print('\033[0;36m\nPaciente cadastrado com sucesso\n\033[m')
                    system('Pause')
                except(PacienteRepetidoException):
                    print('\033[0;31m\nEste CPF já está cadastrado\n\033[m')
                    system('pause')
                
            elif option == SAIR:
                break
            
            else:
                print('\033[0;31m\nVALOR INVÁLIDO')
                print('Tente Novamente\n\033[m')
                system('Pause')

    elif option == AREA_FUNCIONARIO:
        while True:
            (menu_funcionario())
            option = int(input('Digite uma opção: '))
            
            if option == FAZER_LOGIN:       #Opções de login
                cpf_funcionario = input('Digite seu CPF: ')
                senha_funcionario = input('Digite sua Senha: ')
                
                if clinica.fazer_login_funcionario(cpf_funcionario, senha_funcionario, funcionario):
                    print('\n\033[36mBem Vindo\n\033[m')
                    system('Pause')
                    while True:
                        (menu_login_funcionario())
                        option = int(input('Digite uma opção: '))

                        if option == MEUS_DADOS:
                            for funcionario in clinica.funcionarios_ativos:
                                if funcionario.cpf == cpf_funcionario:
                                    print(funcionario)
                            system('Pause')
                        
                        elif option == MUDAR_DADOS:
                            #informações básicas
                            nome = input('Nome: ')
                            idade = input('Idade: ')
                            telefone = input('Telefone: ')

                            #endereço funcionário
                            rua = input('Rua: ')
                            cidade = input('Cidade: ')
                            estado = input('Estado: ')
                            cep = input('CEP: ')

                            #designação de trabalho
                            funcao = input('Digite sua função: ')
                            salario = input('Digite o salario recebido: ')

                            senha_nova = input('Digite sua senha: ')
                            #Classes

                            endereço_novo_funcionario = Endereço(rua, cidade, estado, cep)
                            cadastro_novo_funcionario = SignUP(cpf_funcionario, senha_nova)
                            novo_funcionario = Funcionario(nome, cpf_funcionario, idade, endereço_novo_funcionario, telefone, funcao, salario, cadastro_novo_funcionario)
                            
                            clinica.editar_funcionario(novo_funcionario, cpf_funcionario)
                            
                            print('\n\033[0;36mFuncionário Alterado com sucesso\n\033[m')
                            system('pause')
                            break

                        elif option == APAGAR_CONTA:
                            clinica.desativar_funcionario(cpf_funcionario, funcionario)
                            print('\n\033[36mUsuário Removido\n\033[m')
                            system('Pause')
                            break
                        
                        elif option == USUARIOS_DELETADOS:
                            for pessoas in clinica.pessoas_removidas:
                                print(pessoas)
                                system('pause')

                        elif option == SAIR:
                            break
                        
                        else:
                            print('\033[31m\nValor Inválido!!\n\033[m')
                else:
                    print('\033[31m\nLogin ou Senha inválidos\n\033[m')
                    system('pause')

            elif option == CADASTRAR_FUNCIONARIO:       
                #informações básicas
                nome = input('Nome: ')
                cpf = input('CPF: ')
                idade = input('Idade: ')
                telefone = input('Telefone: ')

                #endereço funcionário
                rua = input('Rua: ')
                cidade = input('Cidade: ')
                estado = input('Estado: ')
                cep = input('CEP: ')

                #designação de trabalho
                funcao = input('Digite sua função: ')
                salario = input('Digite o salario recebido: ')

                senha = input('Digite sua senha: ')
                #Classes

                endereço_funcionario = Endereço(rua, cidade, estado, cep)
                cadastro_funcionario = SignUP(cpf, senha)
                funcionario = Funcionario(nome, cpf, idade, endereço_funcionario, telefone, funcao, salario, cadastro_funcionario)

                try:
                    verif = clinica.adicionar_funcionario(funcionario, cpf)
                    print('\033[0;36m\nFuncionário cadastrado com sucesso\n\033[m')
                    system('Pause')
                except(FuncionarioRepetidoException):
                    print('\n\033[31mFuncionario já cadastrado\n\033[m')
                    system('pause')
            
            elif option == SAIR:
                break

            else:
                print('\033[0;31m\nVALOR INVÁLIDO')
                print('Tente Novamente\n\033[m')
                system('Pause')
    
    else:
        print('\033[0;31m\nVALOR INVÁLIDO')
        print('Tente Novamente\n\033[m')
        system('Pause')