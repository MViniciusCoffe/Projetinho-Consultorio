class Endereço:
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep


class Contato:
    def __init__(self, contato, tipo):
        self.contato = contato
        self.tipo = tipo


class Pessoa:
    def __init__(self, nome, cpf, idade, endereço, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.endereço = endereço
        self.telefone = telefone
        self.ativo = True

    def __str__(self):
        return (f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\n' 
                f'Endereço:\n'
                f'  Rua: {self.endereço.rua}\n'
                f'  Cidade: {self.endereço.cidade}\n'
                f'  Estado: {self.endereço.estado}\n'
                f'  CEP: {self.endereço.cep}\n'
                f'telefone: {self.telefone}\n'
                f'Senha: {self.signup.senha}\n')


class Paciente(Pessoa):
    def __init__(self, Nome, cpf, idade, Endereço, telefone, indicacao, signup):
        super().__init__(Nome, cpf, idade, Endereço, telefone)
        self.indicacao = indicacao
        self.signup = signup

    def __str__(self):
        return (f'{super().__str__()}'
        f'indicação: {self.indicacao}\n')


class Funcionario(Pessoa):
    def __init__(self, Nome, cpf, idade, endereço, telefone, função, salario, signup):
        super().__init__(Nome, cpf, idade, endereço, telefone)
        self.função = função
        self.salario = salario
        self.signup = signup

    def __str__(self):
        return (f'{super().__str__()}'
        f'Função: {self.função}\n'
        f'Salário: {self.salario}\n')
        

class SignUP:
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha


class Clinica:
    def __init__(self, endereço):
        self.dono = 'Doutor Tiago de Medeiros Almeida'
        self.nomeClinica = 'Clinica Odontológica Santo André'
        self.cnpj = '49.520.643/0001-55'
        self.endereço = endereço
        self.contatos_clinica = []
        self.funcionarios_ativos = []
        self.pacientes_ativos = []
        self.pessoas_removidas = []

    def adicionar_contato_clinica(self, contato):
        self.contatos_clinica.append(contato)

    #ÁREA PACIENTES
    def adicionar_paciente(self, paciente, cpf):
        if self.isCpfPacienteRepetido(cpf):
            raise PacienteRepetidoException
        self.pacientes_ativos.append(paciente)
        return True

    def desativar_paciente(self, cpf, pessoa):
        for paciente in self.pacientes_ativos:
            if paciente.cpf == cpf:
                indice = self.pacientes_ativos.index(paciente)
                self.pessoas_removidas.append(pessoa)
                self.pacientes_ativos[indice].ativo = False
                self.pacientes_ativos.remove(paciente)

    def editar_paciente(self, novo_paciente, cpf):
        for paciente in self.pacientes_ativos:
            if paciente.cpf == cpf:
                indice = self.pacientes_ativos.index(paciente)
                self.pacientes_ativos[indice] = novo_paciente

    def fazer_login_paciente(self, cpf, senha, pessoa):
        if self.isPessoaAtivo(pessoa):
            for paciente in self.pacientes_ativos:
                if paciente.signup.cpf == cpf and paciente.signup.senha == senha:
                    return paciente
        return False

    #ÁREA FUNCIONÁRIO
    def adicionar_funcionario(self, funcionario, cpf):
        if self.isCpfFuncionarioRepetido(cpf):
            raise FuncionarioRepetidoException
        self.funcionarios_ativos.append(funcionario)

    def desativar_funcionario(self, cpf, pessoa):   
        for funcionario in self.funcionarios_ativos:
            if funcionario.cpf == cpf:
                indice = self.funcionarios_ativos.index(funcionario)
                self.pessoas_removidas.append(pessoa)
                self.funcionarios_ativos[indice].ativo = False
                self.funcionarios_ativos.remove(funcionario)

    def editar_funcionario(self, novo_funcionario, cpf):
        for funcionario in self.funcionarios_ativos:
            if funcionario.cpf == cpf:
                indice = self.funcionarios_ativos.index(funcionario)
                self.funcionarios_ativos[indice] = novo_funcionario

    def fazer_login_funcionario(self, cpf, senha, pessoa):
        if self.isPessoaAtivo(pessoa):
            for funcionario in self.funcionarios_ativos:
                if funcionario.signup.cpf == cpf and funcionario.signup.senha == senha:
                    return funcionario
        return False

    #VERIFICADORES
    def isPessoaAtivo(self, pessoa):
        if pessoa.ativo is True:
            return True
        return False

    def isCpfPacienteRepetido(self, cpf):
        for paciente in self.pacientes_ativos:
            if paciente.cpf == cpf:
                return True
            return False

    def isCpfFuncionarioRepetido(self, cpf):
        for funcionario in self.funcionarios_ativos:
            if funcionario.cpf == cpf:
                return True
        return False


class PacienteRepetidoException(Exception):
    pass


class FuncionarioRepetidoException(Exception):
    pass