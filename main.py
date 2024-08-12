#Dicionario
usuario = {
    'nome':'Italo Pablo',
    'idade': 27,
    'profissao': 'faz-tudo'
}


#Adicionar uma nova chave
usuario['CPF'] =  input('Informe o CPF do usuario: ')

#Adicionar uma nova chave
usuario['RG'] =  input('Informe o RG do usuario: ')

#Adicionar uma nova chave
usuario['Data de Nascimento'] =  input('Informe a data de nascimento do usuario: ')

#Adicionar uma nova chave
usuario['Sexo'] =  input('Informe o sexo do usuario: ')

#Adicionar uma nova chave
usuario['Signo'] =  input('Informe o Signo do usuario: ')

#Adicionar uma nova chave
usuario['Mãe'] =  input('Informe o nome da Mãe: ')

#Adicionar uma nova chave
usuario['Pai'] =  input('Informe o nome do Pai: ')

#Adicionar uma nova chave
usuario['Email'] =  input('Informe o Email do usuario: ')

#Adicionar uma nova chave
usuario['CEP'] =  input('Informe o CEP do usuario: ')

#Adicionar uma nova chave
usuario['endereço'] =  input('Informe o Endereço do usuario: ')

#Adicionar uma nova chave
usuario['bairro'] =  input('Informe o Bairro do usuario: ')

#Adicionar uma nova chave
usuario['cidade'] =  input('Informe o Estado do usuario: ')

#Adicionar uma nova chave
usuario['telefone'] =  input('Informe o telefone do usuario: ')

#Adicionar uma nova chave
usuario['altura'] =  input('Informe altura do usuario: ')

#Adicionar uma nova chave
usuario['peso'] =  input('Informe o peso do usuario: ')

#Adicionar uma nova chave
usuario['tipo_sanguineo'] =  input('Informe o tipo sanguineo do usuario: ')

#Adicionar uma nova chave
usuario['cor_favorita'] =  input('Informe o a cor favorita do usuario: ')



#Excluindo a chave
del usuario['idade']

# #exibindo valores do dicionário na tela
# print(usuario.get('nome'))
# print(usuario.get('idade'))
# print(usuario.get('profissao'))
# print(usuario.get('email'))

for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')