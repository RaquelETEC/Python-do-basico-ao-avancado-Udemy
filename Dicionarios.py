#Utiliza index no formato de keys e values 
#aceita string , integer , float , boolean...

aluno  = {'nome': 'Ana',
          'idade': 16,
          'not_final':'A',
          'aprovacao': True}

#ATUALIZAR SOMENTE 1 CAMPO
aluno['nome'] = 'Jose'

#Atualizar mais de um
aluno.update({'nome': 'raquel',
             'idade': 16,
             'not_final':'B',
             'aprovacao': True})

#retorna erro quando nao tem a chave
#print(aluno['endereco'])

#se nao tiver ele nao gera o erro, mas sim informa a mensagem
print(aluno.get('endereco','chave nao existente'))

#removendo
del aluno['idade']

print(aluno)
print()

#-------------looping dentro dos dicionarios --------------#

aluno  = {'nome': 'Ana',
          'idade': 16,
          'not_final':'A',
          'aprovacao': True}

for x in aluno:
    print(f'{x} : {aluno[x]}')

print ()

for keys, values in aluno.items():
    print(keys, values)

print()
#-------Adicionando mais valores --------------------#

aluno2  = {'nome': 'Ana',
          'idade': 16,
          'not_final':'A',
          'aprovacao': True, 
          'materias':['fisica', 'matematica', 'ingles']}
print(aluno2) 
print()

print(aluno2.items())
print(aluno2.keys())
print(aluno2.values())