from modulo import *
from time import sleep

print('\n\033[95mBem-vindo ao Lar Mundo Pet!\033[m')

#definindo o nome do arquivo 
arq1 = 'arq_animais_nao_adotados.txt' 

#verificando se o arquivo (arq1) não existe ainda através da função arquivoExiste()
if not arquivoExiste(arq1):
  #caso não exista, cria-se o arquivo com a função criarArquivo()
  criarArquivo(arq1)

#o mesmo processo é feito com os outros 2 arquivos txt
arq2 = 'arq_animais_adotados.txt'

if not arquivoExiste(arq2):
  criarArquivo(arq2)

arq3 = 'arq_candidatos.txt'

if not arquivoExiste(arq3):
  criarArquivo(arq3)


while True:
  cabecalho('MENU PRINCIPAL')
  resposta = menu_principal(['Cadastrar novo animal', 'Alterar registro do animal', 'Remover registro do animal', 'Consultar animais não adotados', 'Consultar animais adotados', 'Entrevista para nova adoção', 'Sair'])

  if resposta == 1:

  #CADASTRO DE NOVOS ANIMAIS
    #Uso da função cadastrar e transformação do registro retornado em string, para que ele possa ser armazenado em um arquivo txt. 
    cabecalho('CADASTRO DE NOVOS ANIMAIS')
    print("\n\033[94mPara um animal que ainda não foi adotado os campos de “nome do responsável pela adoção” e “data de adoção” devem ficar vazios.\033[m\n")
    cadastro = cadastrar(arq1, arq2)
    str_cadastro = str(cadastro)

    #Se a entrada para as categorias 'responsável pela adoção' e 'data da adoção' forem vazias, o animal deve ser colocado na lista de animais não adotados (arq1)
    if cadastro['responsavel'] == '' and cadastro['data'] == '':
      #abre o arq txt de não adotados e adiciona o novo cadastro 
      a = open(arq1, 'at')
      a.write(f'{str_cadastro}\n')
      a.close()
      print('\n\033[33mCadastro realizado com sucesso! \033[m')
        
    #Se as entradas não forem vazias, o animal deve ir para a lista de adotados (arq2)
    else:
      a = open(arq2, 'at')
      a.write(f'{str_cadastro}\n')
      a.close()
      print('\n\033[33mCadastro realizado com sucesso! \033[m')
    
    sleep(6)
  
  #ALTERAÇÃO DO REGISTRO DE UM ANIMAL
  elif resposta == 2:
    #uso da função da lib de alteração do registro
    cabecalho('ALTERAÇÃO DE REGISTRO')
    alterar_registro(arq1,arq2)
    sleep(6)

  #REMOÇÃO DO REGISTRO DE UM ANIMAL
  elif resposta == 3:
    #uso da função da lib de remoção do registro
    cabecalho('REMOÇÃO DE REGISTRO')
    remover_registro (arq1, arq2)
    sleep(6)

  #CONSULTA DO ARQ1 (NÃO ADOTADOS)
  elif resposta == 4:
    lerArquivo1(arq1)
    sleep(6)

  #CONSULTA DO ARQ2 (ADOTADOS)
  elif resposta == 5:
    lerArquivo2(arq2)
    sleep(6)
  
  #ENTREVISTA PARA ADOÇÃO
  elif resposta == 6:
    cabecalho('ENTREVISTA PARA ADOÇÃO')
    entrevista(arq2, arq1, arq3)
    sleep(6)
  
  #Se a resposta digitada for 7, então damos um break no while e encerramos o programa
  elif resposta == 7:
    cabecalho('Encerrando o programa... Até logo!')
    break

  #Se a resposta digitada não estiver entre 1 e 7, avisamos o usuário que a resposta é inválida e repetimos a aparição do menu
  else:
    print('\n\033[31mOpção inválida! Tente novamente.\033[m')
