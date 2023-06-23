from classes import *

#CONSTANTES
#----------------------#

SAIR = 0
AREA_PACIENTE = 1
AREA_FUNCIONARIO = 2
SOBRE = 3

#----------------------#

CADASTRAR_PACIENTE = CADASTRAR_FUNCIONARIO = 2

#----------------------#

MEUS_DADOS = 1
MUDAR_DADOS = 2
APAGAR_CONTA = 3
USUARIOS_DELETADOS = 4

#----------------------#

FAZER_LOGIN = 1

#----------------------#

#menus 
def menu_inicial():
    print("""
\033[1;36m================================================
>>         \033[1;32mCONSULTÓRIO DO DR. OJUARA\033[m          \033[1;36m<<
================================================\033[m
\033[31m================================================
>>   1.  Área paciente                        <<
>>   2.  Área funcionário                     <<
>>   0.  Sair                                 <<
================================================\033[m""")
    return ''

def menu_paciente():
    print("""
\033[1;36m================================================
>>         \033[1;32mCONSULTÓRIO DO DR. OJUARA\033[m          \033[1;36m<<
================================================\033[m
\033[31m================================================
>>   1.  Fazer Login                          <<
>>   2.  Cadastrar Paciente                   <<
>>   0.  Sair                                 <<
================================================\033[m""")
    return ''

def menu_login_paciente():
    print("""
\033[1;36m================================================
>>         \033[1;32mCONSULTÓRIO DO DR. OJUARA\033[m          \033[1;36m<<
================================================\033[m
\033[31m================================================
>>   1.  Exibir meus dados                    <<
>>   2.  Modificar dados                      <<
>>   3.  Excluir conta                        <<             
>>   0.  Sair                                 <<
================================================\033[m""")
    return ''
    
def menu_funcionario():
    print("""
\033[1;36m================================================
>>         \033[1;32mCONSULTÓRIO DO DR. OJUARA\033[m          \033[1;36m<<
================================================\033[m
\033[31m================================================
>>   1.  Fazer Login                          <<
>>   2.  Cadastrar funcionario                <<
>>   0.  Sair                                 <<
================================================\033[m""")
    return ''


def menu_login_funcionario():
    print("""
\033[1;36m================================================
>>         \033[1;32mCONSULTÓRIO DO DR. OJUARA\033[m          \033[1;36m<<
================================================\033[m
\033[31m================================================
>>   1.  Exibir meus dados                    <<
>>   2.  Modificar dados                      <<
>>   3.  Excluir conta                        <<
>>   4.  Ver usuários deletados               <<                
>>   0.  Sair                                 <<
================================================\033[m""")
    return ''






















"""
if area paciente
    if cadastrar paciente
        crud paciente
    elif fazer login
        user
        pasw
        if true then
            exibir meus dados
            editar conta
            adicionar contatos
            editar contatos
        if false then
            return False
    else:
        return false
if area fucionario
    if fazer login
        user
        pasw
        if true then
            exibir meus dados
            editar conta
            adicionar contatos
            editar contatos
        if false
            return false
if area dentista
    if fazer login
        user
        pasw

"""










