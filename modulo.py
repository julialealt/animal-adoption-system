#FUNÇÕES PARA A INTERFACE DO PROGRAMA

#Função para ler um número inteiro
def leiaInt(msg):
  while True:
    try:
      #Recebendo um inteiro
      n = int(input(msg))
    #Se o usuário digitar algo diferente de um número inteiro, o programa informa o erro e pede para ele digitar novamente.
    except (ValueError, TypeError):
      print('\n\033[31mERRO: Por favor, digite um número inteiro positivo válido.\033[m \n')
    except (KeyboardInterrupt):
      print('\n\033[31mERRO: O usuário preferiu não digitar\033[m ')
    else:
      if n < 0:
        print('\n\033[31mERRO: Por favor, digite um número inteiro positivo.\033[m \n')
      else:
        return n


def linha (tam=50):
  return '–' * tam


def cabecalho(txt):
  print(linha())
  print(txt.center(50))
  print(linha())


def menu_principal(lista):
  cont = 1
  for item in lista:
    print('{}- \033[34m{}\033[m'.format(cont, item))
    cont += 1
  print(linha())
  opcao = leiaInt('\033[35mDigite uma opção: \033[m')
  return opcao


def menu_alteracao(lista):
  cont = 1
  for item in lista:
    print('\033[36m{}\033[m- {}'.format(cont, item))
    cont += 1
  print(linha())
  opcao = leiaInt('\033[35mDigite o número da categoria a ser alterada: \033[m')
  return opcao


#FUNÇÕES PARA TRATAMENTO DE ERRO
import unicodedata #Importando a biblioteca unicodedata
#A função recebe uma string para remover acentos e cedilha(se houver)
def remover_acento(string):
  #Normalizando a string usando o parâmetro NFD
  string = unicodedata.normalize("NFD", string)
  #Transformando em binário
  string_sem_acento = string.encode("ascii", "ignore")
  #Por fim, decodificando as letras
  string_final = string_sem_acento.decode("utf-8")
  #E retornando a string sem acento
  return string_final

#Função que remove TODOS os espaços que encontra em uma string
def remover_espacos(string):
  #'for' para repetir o comando de substituir um espaço (" ") por um vazio ("") na quantidade de vezes que houver um espaço na string
  for i in range(string.count(" ")):
    string_sem_espacos = string.replace(" ", "")
  #Se, na string, houver ocorrência de espaço em branco, a função retorna a string sem espaços
  if string.count(" ") != 0:
    return string_sem_espacos
  #Se não, ou seja, se a string não possuir nenhuma ocorrência de espaço em branco, a função retorna a mesma string (sem alterações)
  else:
    return string 

#Função que impossibilita que um campo seja preenchido por uma string vazia ou composta inteiramente por espaços.
def verificar_string_vazia(registro, categoria, mensagem):
  while True:
    #a string é preenchida e nela são aplicadas as funções de remoção de acentos e de espaços (além do lower)
    registro[categoria] = input(mensagem)
    if remover_acento(remover_espacos(registro[categoria]).lower()) != '':
      #caso a função seja diferente de '', saímos do loop de repetição e retornamos a mensagem escrita originalmente
      break
    else:
      #caso ela seja vazia, informamos o usuário da necessidade de preenchimento do campo e não saímos do loop, pedindo uma nova inserção
      print('\n\033[31mEsse campo deve ser obrigatoriamente preenchido.\033[m\n')
      
  return registro[categoria]

#Função que verifica se a data está no formato adequado.
#A ideia é, primeiramente, tentar 'splitar' a data no formato recebido usando como parâmetro o '/'. Depois tentar transformar em inteiros os elementos (que no caso seria o dia, mês e ano) que estavam entre a barras . Caso dê algum erro nesse processo, é pedido que o usuário insira a data no formato adequado e a função retorna 'Falso'. Caso não dê nenhum erro naquele processo, verificar se o dia, mês e ano estão dentro do intervalo coerente (0<dia<32, 0<mês<32 e 999<ano<1000). Se for o caso, a função retorna 'Verdade'. Caso contrário, pede-se para o usuário inserir uma data no formato adequado e a função retorna 'Falso'.
def dataVerificar(data): 
  try:
    data_separada = data.split('/')
    dia = int(data_separada[0])
    mes = int(data_separada[1])
    ano = int(data_separada[2])
  except:
    print('\n\033[31mInsira uma data no formato adequado.\033[m\n')
    return False
  else:
    if (dia > 0 and dia < 32) and (mes> 0 and mes <13) and (ano> 999 and ano < 10000):
      return True
    else:
      print('\n\033[31mInsira uma data no formato adequado.\033[m\n')
      return False


#FUNÇÕES RELACIONADAS AOS ARQUIVOS

#Função que checa a existencia de um arquivo
def arquivoExiste(nome):
  #checamos se o arquivo existe, em caso contrário retornamos 'False'
  try:
    #rt = leitura de arquivo texto
    a = open(nome,'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True

#Função que cria um novo arquivo
def criarArquivo(nome):
  #tentamos abrir um novo arquivo, em caso contrário sinalizamos erro
  try:
    #wt+ = escrever um novo arquivo texto
    a = open(nome, 'wt+')
    a.close()

  except:
    print('Houve um ERRO na criação do arquivo')
  
  else:
    print(f'Arquivo {nome} criado com sucesso!')

#Função para adicionar uma string de um registro de um animal em um arquivo
def adicionar_registro(arquivo, string):
  #Primeiramente, abrimos o arquivo no modo leitura
  a = open(arquivo, 'rt')
  #A função .readlines() transforma cada linha de um arquivo em um elemento de uma lista. Criamos a variável 'lista_linhas' para guardar a lista das linhas do arquivo
  lista_linhas = a.readlines()
  #Adicionamos a string desejada na lista de linhas do arquivo
  lista_linhas.append(string)
  #Transformamos a lista de linhas em uma string já com o novo elemento/linha
  nova_string = "".join(lista_linhas)
  #Fechando o arquivo para depois abrí-lo novamente no modo de escrita
  a.close()
  #Abrindo o arquivo no modo 'wt+', o qual irá apagar todo o conteúdo existente no arquivo texto e irá possibilitar a escrita de uma nova string
  a = open(arquivo, 'wt+')
  #Escrevendo no arquivo texto a nova string (a string da lista de linhas)
  a.write(f'{nova_string}\n')
  #Fechando o arquivo
  a.close()


#FUNÇÕES RELACIONADAS AO CADASTRO/REGISTRO DE ANIMAIS

#Função que verifica se o nome inserido pelo usuário está presente em determinado arquivo e, em caso positivo, também retorna sua posição no arquivo (nome usado como método de detecção do animal a ser excluído ou alterado)
def checar_nome (nome, arq):
  #variável que checa a presença do nome procurado é inicializada (como False, uma vez que ele ainda não foi identificado)
  presenca_nome = False
  #inicialização do contador que, caso o nome seja encontrado, devolverá em sua posição 
  cont = 0
  try:
    a = open(arq, 'rt')
  except:
    print('Erro ao ler arquivo!')
  else:
    #se não houver erro na leitura, lê cada linha do arquivo (estrutura for)
    for linha in a:
      #eval transforma a string dentro do arq em registro
      registro = eval(linha)
      #verificação da igualdade entre o nome inserido na busca do animal e o valor dentro da key ['nome'] do registro
      if remover_acento(remover_espacos(registro['nome'])).lower() == remover_espacos(nome).lower():
        #caso o nome (desconsiderando os espaços, para evitar possíveis repetições por adição deles no início ou no fim) seja encontrado, a variável presenca_nome torna-se verdadeira e a função para de procurá-lo.
        presenca_nome = True
        break
      #para cada linha que o nome não é encontrado, o contador é incrementado (ou seja, só para quando o nome for identificado ou quando todo o arquivo foi percorrido)
      cont += 1
    #criação de uma lista que possibilite e retorno de duas variáveis ([0] = presenca_nome e [1] = contador) pela função
    lista = [presenca_nome, cont]
    #fechamento do arquivo
    a.close()
    #a função deve retornar a lista criada
    return lista

#Função cadastrar (retorna um registro)
def cadastrar(arq1, arq2):
  #abertura vazia do registro
  cadastro = {}
  #adição dos elementos requisitados em um novo cadastro
  #abertura de loop que possibilite a repetição do texto até que uma resposta válida seja digitada
  while True:
    #uso da função que já pede o texto a ser visto pelo usuário e trata a resposta, caso ela seja vazia ou inteiramente composta por espaços
    cadastro['nome'] = verificar_string_vazia(cadastro, 'nome', 'Nome do animal: ')
    nome = cadastro['nome']
    #checamos, com a função checar_nome, a presença do nome nos arquivos de cadastrados e de não cadastrados e pedimos a lista (presenca_nome, cont)
    lista_arq1 = checar_nome(nome, arq1)
    lista_arq2 = checar_nome(nome, arq2)
    #caso o presenca_nome retorne True em qualquer uma das listas (indicando que o nome já foi cadastrado), o usuário é informado e o loop segue intacto, pedindo uma nova entrada
    if lista_arq1[0] == True or lista_arq2[0] == True:
      print('\n\033[31mNome já cadastrado, insira um novo.\033[m\n')
    #caso o nome digitado seja inédito, saímos do loop e seguimos para a próxima categoria
    else:
      break

  #uso da função leiaInt para verificação da idade inserida, que precisa ser um inteiro positivo
  cadastro['idade'] = leiaInt('Idade (em meses): ')

  #para o porte só são permitido 4 tipos de entradas (pequeno, grande, médio e medio)
  while True:
    cadastro['porte'] = remover_acento(remover_espacos(input('Porte (pequeno, médio ou grande): ')))
    if cadastro['porte'].lower() == 'pequeno' or cadastro['porte'].lower() == 'medio' or cadastro['porte'].lower() == 'grande':
      break
    else:
      print('\n\033[31mInsira um porte adequado.\033[m\n')

  #uso da função verificar_string_vazia para as categorias 'raça' e 'lar temporário', impedindo que o animal seja cadastrado sem a inserção de alguma informação nesses campos
  cadastro['raca'] = verificar_string_vazia(cadastro, 'raca', 'Raça (caso não houver será ‘sem raça definida’ - SRD): ')

  cadastro['lar_temp'] = verificar_string_vazia(cadastro, 'lar_temp', 'Lar temporário (onde o animal está ou esteve antes de ser adotado): ')

  #no campo do responsável deve ser possível ter uma entrada vazia (característica que definirá um animal como 'não adotado')
  cadastro['responsavel'] = input('Nome do responsável pela adoção: ')

  #tratamento do recebimento da data
  while True: #criando um loop while True
    cadastro['data'] = input('Data de adoção (DD/MM/AAAA): ') #recebendo a data do usuário

    #caso o campo do responsável esteja vazio, significa que o animal não foi adotado e, portanto, a data deve estar vazia
    if remover_espacos(cadastro['responsavel']) == '' and cadastro['data'] != '': 
      print('\n\033[31mA data deve estar vazia.\033[m\n')
    #caso contrário, 
    else:
      #tratando pro caso do usuário escrever somente vários espaços. nesse caso, o campo do responsável deve ser considerado vazio
      if remover_espacos(cadastro['responsavel']) == '' and cadastro['data'] == '':
        cadastro['responsavel'] = ''
        break
      #caso a data passe no testes anteriores e a verificação da função que analisa o formato da data retorne verdadeira, pode parar o loop.
      elif dataVerificar(cadastro['data']) == True:
        break

  #retorna o registro preenchido
  return cadastro

#Função que exclui um registro inteiro
def excluir_registro(arquivo, linha):
  #abertura do arquivo
  a = open(arquivo, 'rt')
  #readlines retorna o todo o conteúdo do arquivo em uma lista de strings, cada item da lista representa uma linha do arquivo (será a lista a ser deletada)
  lista_del = a.readlines()
  #deletar, da lista, o item referente à posição da linha do arquivo a ser indicada
  del lista_del [linha]
  #transformação da lista com o elemento já deletado em uma string a partir da função join, possibilitando que ela seja novamente inserida em um arquivo de texto
  nova_string = "".join(lista_del)
  a.close()
  #arquivo é fechado para que possa ser novamente aberto no formato de escrita (wt+ apaga toda a informação existente anteriormente, deixando o arquivo 'vazio')
  a = open(arquivo, 'wt+')
  #escrever a nova string no arquivo anteriormente aberto, substituindo a string antiga pela nova (com o registro do animal deletado)
  a.write(f'{nova_string}')
  a.close()

#Função de busca do registro a ser removido (e sua efetuação)
def remover_registro (arq1, arq2):
  #pedir o nome do animal a ser removido
  nome_a_remover = input("Digite o nome do animal cujo registro será removido: ")
  if nome_a_remover.upper() != 'PARAR':
    #uso da função que checa se o nome inserido pelo usuário está no arq1, retornando a lista (presenca_nome, cont)
    lista_arq1 = checar_nome (nome_a_remover, arq1)
    #caso presenca_nome seja True (indicando que o nome foi encontrado), a função de exclusão do registro deve ser utilizada 
    if lista_arq1 [0] == True: #presença_nome
      #devemos informar a posição da linha a ser excluída a partir do contador feito na função checar_nome e retornado pelo segundo elemento da lista 
      excluir_registro (arq1, lista_arq1[1])
      print('\n\033[33mRegistro removido com sucesso! \033[m\n')
    #caso o nome não tenha sido identificado no primeiro arquivo, repetimos o processo para o segundo
    else:
      lista_arq2 = checar_nome (nome_a_remover, arq2)
      if lista_arq2 [0] == True: #presença_nome
        excluir_registro (arq2, lista_arq2[1])
        print('\n\033[33mRegistro removido com sucesso! \033[m\n')
      #caso o nome também não seja encontrado no segundo arquivo, o usuário deve ser informado e repetimos a função; pedindo a inserção de um novo nome até que um existente na lista de adotados ou na de não adotados seja inserido ou até que uma resposta específica que a finaliza ("PARAR") seja escrita pelo usuário
      else:
        print('\n\033[31mAnimal não identificado! Tente novamente.\nCaso deseje ser redirecionado ao menu, digite PARAR. \033[m\n')
        remover_registro (arq1, arq2)

#Função de alteração do registro
def mudar_registro (resposta, nome, arq, cont, arq1, arq2):
  try:
    #tentativa de abertura do aquivo de texto para leitura
    a = open(arq, 'rt')
  except:
    print('Erro ao ler arquivo!')
  else:
    #se não houver erro na leitura, lê cada linha do arquivo (pela estrutura for)
    for linha in a:
      #eval transforma a string dentro do arq em registro
      registro = eval(linha)
      #verificação da igualdade entre o nome inserido na busca do animal e o valor dentro da key ['nome'] do registro
      if remover_acento(remover_espacos((registro['nome']))).lower() == nome.lower():
        #em caso positivo, a resposta selecionada pelo usuário direciona qual nova informação será pedida e a coloca no lugar do que já estava armazenado anteriormente
        
        #tratamentos de entradas similares aos realizados durante o cadastro
        
        if resposta == 1:
          while True:
            #verifica se a string é vazia, composta de espaços (a partir da função verificar_string_vazia) ou se o nome inserido já foi cadastrado anteriormente
            registro['nome'] = verificar_string_vazia(registro, 'nome', 'Digite um novo nome: ')
            nome = registro['nome']
            lista_arq1 = checar_nome(nome, arq1)
            lista_arq2 = checar_nome(nome, arq2)
            if lista_arq1[0] == True or lista_arq2[0] == True:
              print('\n\033[31mNome já cadastrado, insira um novo.\033[m\n')
            else:
              break

        elif resposta == 2:
          #checa se a idade inserida está no formato int
          registro['idade'] = leiaInt('Digite uma nova idade (em meses): ')
          
        elif resposta == 3:
          while True:
            #aceita apenas as mesmas 4 respostas que o cadastro
            registro['porte'] = remover_acento(remover_espacos(input('Digite um novo porte (pequeno, médio ou grande): ')))
            if registro['porte'].lower() == 'pequeno' or registro['porte'].lower() == 'medio' or registro['porte'].lower() == 'grande':
              break
            else:
              print('\n\033[31mInsira um porte adequado.\033[m\n')
          
        elif resposta == 4:
          #verifica se a string inserida não é vazia
          registro['raca'] = verificar_string_vazia(registro, 'raca', 'Digite uma nova raça: ')

        elif resposta == 5:
          #verifica se a string inserida não é vazia
          registro['lar_temp'] = verificar_string_vazia(registro, 'lar_temp', 'Digite um novo lar temporário: ')

        #para as respostas == 6 ou 7, é necessário que o 'nome do responsável' e que a 'data de adoção' não sejam vazias, uma vez que a alteração de um animal não adotado para adotado (caracterizada pelo preenchimento dessas categorias) só pode ser efetuada a partir da entrevista.

        elif resposta == 6 and registro['responsavel'] != '':
          registro['responsavel'] = verificar_string_vazia(registro, 'responsavel', 'Digite um novo nome para o responsável: ')

        elif resposta == 7 and registro['responsavel'] != '':
          #tratamento de entrada da data (também usado na função cadastrar())
          while True:
            registro['data'] = input('Nova data de adoção (DD/MM/AAAA): ')
            #aplicação da função de tratamento de datas
            if dataVerificar(registro['data']) == True:
              break

        else:
          #caso nenhuma das opções válidas sejam selecionadas, não imprimimos a mensagem de 'registro alterado'.
          print('\n\033[31mOpção inválida! Tente novamente.\033[m')
          break
          
        print('\n\033[33mRegistro alterado com sucesso! \033[m\n')
        break
      
    #o registro, agora devidamente atualizado, deve ser novamente convertindo em string para que possa ser novamente inserido no arquivo
    str_registro = str(registro)
    a.close()
    #excluir a linha refrente às informações de cadastro anteriores do arquivo
    excluir_registro(arq, cont)
    #adicionar a nova linha de cadastro ao arquivo
    adicionar_registro(arq, str_registro)

#Função que busca o registro a ser alterado (e sua efetuação)
def alterar_registro (arq1, arq2):
  #pedir o nome do animal a ter seu cadastro alterado
  nome_a_alterar = input("Digite o nome do animal cujo registro será alterado: ")
  if nome_a_alterar.upper() != 'PARAR':
    #uso da função que checa se o nome inserido pelo usuário está no arq1, retornando a lista (presenca_nome, cont)
    lista_arq1 = checar_nome (nome_a_alterar, arq1)
    #caso presenca_nome seja True (indicando que o nome foi encontrado), a função de alteração do registro deve ser utilizada 
    if lista_arq1 [0] == True: #presença_nome
      print("\nIndique qual das categorias a seguir deve ser alterada.\n")
      #menu das categorias que devem ser alteradas (pedindo uma resposta numérica), ignorando a de 'nome do responsável' e 'data de adoção', impedindo que um animal não adotar 
      resposta = menu_alteracao(['Nome do animal', 'Idade', 'Porte', 'Raça', 'Lar Temporário'])
      #função que solicita a escolha da categoria (resposta), o nome a ser alterado, o arquivo e o contador que informa a linha na qual o nome foi encontrado
      mudar_registro (resposta, nome_a_alterar, arq1, lista_arq1[1], arq1, arq2)
    else:
      #caso o nome não tenha sido identificado no primeiro arquivo, repetimos o processo para o segundo
      lista_arq2 = checar_nome (nome_a_alterar, arq2)
      if lista_arq2 [0] == True: #presença_nome
        print("\nIndique qual das categorias a seguir deve ser alterada.\n")
        #menu das categorias que devem ser alteradas (pedindo uma resposta numérica)
        resposta = menu_alteracao(['Nome do animal', 'Idade', 'Porte', 'Raça', 'Lar Temporário', 'Nome do responsável', 'Data da adoção'])
        mudar_registro (resposta, nome_a_alterar, arq2, lista_arq2[1], arq1, arq2)
      else:
        #caso o nome também não seja encontrado no segundo arquivo, o usuário deve ser informado e repetimos a função; pedindo a inserção de um novo nome até que um existente na lista de adotados ou na de não adotados seja inserido ou até que uma resposta específica que a finaliza ("PARAR") seja escrita pelo usuário
        print('\n\033[31mAnimal não identificado! Tente novamente.\nCaso deseje ser redirecionado ao menu, digite PARAR. \033[m\n')
        alterar_registro (arq1, arq2)



#FUNÇÕES RELACIONADAS À CONSULTA DE ANIMAIS ADOTADOS E DE NÃO ADOTADOS
#A ideia da função é bem parecida com a implementação da função '.sort(), a única diferença é o critério para a substituição.
def dataSort(lista): #definindo função
  lista_sortada = [] #definindo a lista que terá as datas em ordem decrescente
  while lista != []: #enquanto a lista de todas as datas não estiver vazia
    maior_elemento_agora = lista[0] #maior data até agora
    
    maior_elemento_agora_separado = maior_elemento_agora.split('/') #lista com a maior data até agora separada em dia, mês e ano
    
    dia_maior_elemento_agora = int(maior_elemento_agora_separado[0]) #dia da maior data até agora

    mes_maior_elemento_agora = int(maior_elemento_agora_separado[1]) #mês da maior data até agora

    ano_maior_elemento_agora = int(maior_elemento_agora_separado[2]) #ano da maior data até agora
    

    for elemento in lista: #para elemento na lista de datas
      elemento_separado = elemento.split('/') #lista com a data separadas em dia, mês e ano

      dia_elemento = int(elemento_separado[0]) #dia 

      mes_elemento = int(elemento_separado[1]) #mês

      ano_elemento = int(elemento_separado[2]) #ano

      #condições
      if ano_elemento > ano_maior_elemento_agora or ano_elemento == ano_maior_elemento_agora and mes_elemento > mes_maior_elemento_agora or ano_elemento == ano_maior_elemento_agora and mes_elemento == mes_maior_elemento_agora and dia_elemento > dia_maior_elemento_agora:
        maior_elemento_agora = elemento #substituindo 
    lista_sortada.append(maior_elemento_agora) #adicionando na lista
    lista.remove(maior_elemento_agora) #removendo o maior elemento (data) da lista

  return lista_sortada #retornando a lista com as datas ordenadas em forma decrescente

#Função que lê o arquivo dos animais não adotados
def lerArquivo1(nome): #definindo a função
  try:
    a = open(nome, 'rt') #tentando abrir o arquivo

  except: 
    print('Erro ao ler o arquivo') #caso dê erro, printar essa mensagem
  
  else: #caso contrário,
    cabecalho('\033[95m         ANIMAIS NÃO ADOTADOS\033[m') #mostrando cabeçalho

    lista_linhas = [] #definindo lista com todas as linhas do arquivo
    for i in a: #para cada linha no arquivo
      registro = eval(i) #eval é um dict() que funciona, ou seja, é uma função que transforma uma string em um dicionário
      lista_linhas.append(registro) #anexando na lista
    
    

    lista_idades = [] #definindo a lista que terá as idades dos animais
    for i in range(len(lista_linhas)): #para i no alcance da lista
      idade = lista_linhas[i]['idade'] #definindo variavel idade
      lista_idades.append(idade) #anexando na lista com as idades

    lista_idades.sort(reverse=True) #usando o sort reverse para deixar na ordem decrescente

  
    for i in lista_idades: #para i na lista com as idades
      for j in range(len(lista_linhas)): #para j no alcance da lista com todas as linhas
        if lista_linhas[j]['idade'] == i: #se a idade for igual a i, pode printar o cadastro do animal
          print('Nome: ', lista_linhas[j]['nome'])
          print('Idade: ', lista_linhas[j]['idade'], 'meses')
          print('Porte: ', lista_linhas[j]['porte'])
          print('Raça: ', lista_linhas[j]['raca'])
          print('Lar temporário: ', lista_linhas[j]['lar_temp'])
          print(linha())
          
          lista_linhas.remove(lista_linhas[j]) #removendo da lista principal
          break 


  finally: #finalmente,
    a.close() #fechando o arquivo

#Função que lê o arquivo dos animais adotados
def lerArquivo2(nome): #definindo a função
  try: 
    a = open(nome, 'rt') #tentando abrir o arquivo

  except:
    print('Erro ao ler o arquivo') #printar essa mensagem caso dê erro

  else: #caso contrário,
    cabecalho('\033[95m         ANIMAIS ADOTADOS\033[m') #mostrando o cabeçalho

    lista_linhas = [] #definindo lista que irá conter todas as linhas do arquivo
    for i in a: #para cada linha no arquivo
      registro = eval(i) #definindo registro
      lista_linhas.append(registro) #adicionando registro


    lista_datas = [] #definindo lista com as datas
    for i in range(len(lista_linhas)): #para i no alcance do tamanho da lista com todas as linhas
      data = lista_linhas[i]['data'] #definindo data
      lista_datas.append(data) #anexando na lista


    lista_datas_sortadas = dataSort(lista_datas) #usando a função de ordenar as datas
    
    for i in lista_datas_sortadas: #para cada elemento na lista de datas ordenadas
      for j in range(len(lista_linhas)): #para j no alcance do tamanho da lista com todas as linhas
        if lista_linhas[j]['data'] == i: #se o campo 'data' daquele registro for igual a i
          #pode printar o registro
          print('Nome: ', lista_linhas[j]['nome'])
          print('Idade: ', lista_linhas[j]['idade'], 'meses')
          print('Porte: ', lista_linhas[j]['porte'])
          print('Raça: ', lista_linhas[j]['raca'])
          print('Lar temporário: ', lista_linhas[j]['lar_temp'])
          print('Responsável pela adoção: ', lista_linhas[j]['responsavel'])
          print('Data de adoção: ', lista_linhas[j]['data'])
          print(linha())

          lista_linhas.remove(lista_linhas[j])
          break

  finally: #finalmente,
    a.close() #fechando o arquivo



#FUNÇÕES RELACIONADAS À ENTREVISTA DOS CANDIDATOS PARA ADOÇÃO

#Função para receber as respostas das perguntas feitas na entrevista de adoção
def perguntas():
  #Lista com as 3 perguntas da entrevista
  lista_perguntas = ['Você possui condições financeiras para adotar um novo animal? ', 
    'Avaliando sua rotina, você possui tempo livre para se dedicar ao seu novo pet? ', 
    'Pense agora no espaço que você possui em casa. Qual o porte máximo que o animal deverá ter para viver confortavelmente com você? ']
  #Criando lista para armazenar as respostas do candidato
  lista_respostas = []

  #Estrutura de repetição 'for' para percorrer cada posição/elemento da lista de perguntas
  for i in range(3):
    #Se i = 0, informamos ao usuário qual tipo de resposta esperamos para a 1ª e 2ª pergunta
    if i == 0:
      print(linha())
      print('Responda com "Sim" ou "Não".')
    #Se i = 2, informamos ao usuário qual tipo de resposta esperamos para a 3ª pergunta)
    if i == 2:
      print('\nResponda com "Pequeno", "Médio" ou "Grande".')
    
    #Recebendo as respostas do usuário e já colocando todos os caracteres em minúsculo para o tratamento de erro
    resposta = input(f'\033[34m{i+1}-\033[m {lista_perguntas[i]}').lower()
    #A cada resposta digitada pelo usuário, a adicionamos na lista de respostas
    lista_respostas.append(resposta)
  
  #Por fim, a função retorna a lista com as respostas das 3 perguntas
  return lista_respostas


#Função que procura, no arquivo de animais não adotados, animais que atendem a condição do porte indicado na entrevista e adiciona-os em uma lista
def verifica_porte(arq_animais_nao_adotados, porte1, porte2='-', porte3='-'):
  try:
    #Primeiro tentamos abrir o arquivo de animais não adotados
    a = open(arq_animais_nao_adotados, 'rt')
  except:
    #Se houver algum erro na abertura do arquivo, informamos ao usuário
    print('Erro ao ler arquivo!')
  #Se não:
  else:
    #Inicializamos uma lista para armazenar os animais disponíveis que atendem a condição do porte desejado
    lista_animais_disponíveis = []

    #Estrutura de repetição 'for' para percorrer cada linha do arquivo de animais não adotados
    for linha in a:
      #Como cada linha do arquivo de animais é uma string mas no formato de registro/dicionário, quando usamos a função eval nessa string, ela a interpreta como registro. E, assim, podemos manipular essa variável de retorno como um registro.
      registro = eval(linha)
      #Criamos uma variável 'registro_porte' para receber o campo 'porte' do registro de cada animal sem acento (tratando o caso de porte médio). Assim, percorremos cada registro dos animais e pegamos o porte de cada um deles.
      registro_porte = remover_acento(registro['porte'].lower())
      #Se o porte do animal que estamos analisando no momento for igual a algum dos portes desejados, transformamos o registro em string e a adicionamos na lista de animais disponíveis
      if registro_porte == porte1 or registro_porte == porte2 or registro_porte == porte3:
        str_registro = str(registro)
        lista_animais_disponíveis.append(str_registro)

    #Por fim, retornamos a lista de animais disponíveis com a string do registro de cada animal que atende a condição do porte desejado
    return lista_animais_disponíveis


#Função que recebe como parâmetro a lista de animais não adotados de acordo com o porte que o candidato escolheu na entrevista e coloca em outra lista esses animais em ordem decrescente de idade (do animal mais velho ao mais novo)
def colocar_em_ordem(lista):
  #Inicializando uma lista para armazenar os registros dos animais
  lista_registros = []
  #Estrutura de repetição 'for' para percorrer a lista que a função recebeu como parâmetro
  for elemento in lista:
    #Para cada elemento da lista, utilizamos a função eval para interpretar a string contida na lista como um registro
    registro = eval(elemento)
    lista_registros.append(registro) #e adicionamos na lista de registros

  #Inicializando uma outra lista, agora para armazenar as idades dos animais na ordem decrescente
  lista_idades = []
  for i in range(len(lista_registros)):
    #Pegando a idade do campo 'idade' do registro de cada animal e adicionando na lista de idades
    idade = int(lista_registros[i]['idade'])
    lista_idades.append(idade)

  #Utilizando a função sort reverse para colocar as idades em ordem decrescente
  lista_idades.sort(reverse=True)

  #Inicializando outra lista, agora para armazenar as strings dos registros dos animais em ordem decrescente de idade
  lista_final = []
  for idade in lista_idades: #Percorrendo a lista de idades
    #Para cada idade da lista de idades, procuramos na lista de registros qual animal possui a idade que estamos analisando no momento
    for i in range(len(lista_registros)):
      if int(lista_registros[i]['idade']) == idade:
        #Quando encontrarmos, printamos cada campo do registro do animal; adicionamos a string do registro desse animal na lista final; a removemos da lista de registros (para garantir que não vamos adicionar o registro do mesmo animal mais de uma vez) e damos um break nesse segundo 'for' já que já encontramos o animal com a idade que estávamos analisando naquele momento
        print('Nome: ', lista_registros[i]['nome'])
        print('Idade: ', lista_registros[i]['idade'], 'meses')
        print('Porte: ', lista_registros[i]['porte'])
        print('Raça: ', lista_registros[i]['raca'])
        print('Lar temporário: ', lista_registros[i]['lar_temp'])
        print(linha())

        lista_final.append(str(lista_registros[i]))
        lista_registros.remove(lista_registros[i])
        break

  #Por fim, retornamos a lista final com os animais disponíveis em determinado(s) porte(s) em ordem decrescente de idade
  return lista_final


#Função para escolher um animal para a adoção
def escolher_animal(arq_animais_nao_adotados, arq_animais_adotados, nome, lista):
  #loop para continuar pedindo para o usuário digitar o nome do animal se o nome digitado for de um animal que não está presente na lista de animais disponíveis
  while True: 
    #Recebendo o nome do animal que se deseja adotar
    nome_animal = input('Digite o nome do animal que você deseja adotar: ')
    #Criando uma variável animal_encontrado para sabermos se encontramos o animal com o nome que o usuário digitou ou não (por enquanto o valor dela é Falso)
    animal_encontrado = False

    for item in lista: #Percorrendo a lista de animais disponíveis
      registro = eval(item) #Usando a função eval para retornar na variável registro o registro de cada animal da lista
      #Comparando o nome de cada animal da lista com o nome que o usuário digitou
      if remover_acento(remover_espacos(registro['nome'].lower())) == remover_acento(remover_espacos(nome_animal.lower())):
        #Se encontrarmos um animal com aquele nome, então animal_encontrado fica Verdadeiro e damos um break para parar de percorrer a lista
        animal_encontrado = True
        break

    #Se animal_encontrado for Falso, significa que não encontramos o nome do animal digitado na lista de animais disponíveis, e então informamos ao usuário e pedimos para digitar novamente
    if animal_encontrado == False:
      print('\n\033[31mAnimal não identificado! Digite um nome válido.\033[m')
    #Se não, ou seja, se animal_encontrado for Verdadeiro, saimos do loop while True
    else:
      break

  while True:
    #Recebendo a data de adoção para adicionar no registro do animal adotado
    data = input('Digite a data da adoção (DD/MM/AAAA): ')
    if dataVerificar(data) == True: #tratamento de erro da data com a função dataVerificar()
      break

  #Inicializando um contador que servirá para contar qual linha do arquivo está o animal que se deseja adotar
  cont = 0
  try:
    a = open(arq_animais_nao_adotados, 'rt')
  except:
    print('Erro ao ler arquivo!')
  else:
    for linha in a: #Percorrendo cada linha do arquivo
      #Para cada linha do arquivo, transformamos a string contida naquela linha em um registro (para manipular como um registro)
      registro = eval(linha)
      #E então podemos pegar somente o campo 'nome' do registro para encontrar o animal desejado. Se encontrarmos, adicionamos ao registro do animal, o nome do responsável (a pessoa que vai adotar) e a data de adoção
      if remover_acento(remover_espacos(registro['nome'].lower())) == remover_acento(remover_espacos(nome_animal.lower())):
        registro['responsavel'] = nome
        registro['data'] = data
        #Break para encerrar o 'for' e, consequentemente, o contador
        break
      #A cada linha do arquivo "lida", incrementamos 1 no contador referente ao número da linha lido no momento
      cont += 1
    
    a.close() #Fechando o arquivo

    #Transformamos o registro do animal que será adotado (o que encontramos no 'for') em string
    str_registro = str(registro)
    #Utilizamos a função excluir_registro() para excluir o registro do animal adotado do arquivo de animais não adotados, a partir do número da linha (contador) do arquivo que se encontra o registro do animal
    excluir_registro(arq_animais_nao_adotados, cont)
    #Utilizamos a função adicionar_registro() para adicionar o registro atualizado do animal adotado no arquivo de animais adotados
    adicionar_registro(arq_animais_adotados, str_registro)
    #Imprimimos a mensagem de que o animal foi adotado com sucesso!
    print('\n\033[32mParabéns! Animal adotado!\033[m')


#Função para adicionar o cadastro do possível candidato à adoção ao arquivo de candidatos
def cadastrar_candidato(nome_arq, nome, pergunta1, pergunta2, pergunta3='-', apto='', justificativa='-'):
  try:
    #Abrindo o arquivo no modo append (escrever novas informações sem apagar o que já está escrito nele)
    a = open(nome_arq, 'at')
  except:
    print('Ocorreu um erro ao tentar abrir o arquivo.')
  else:
    #Se não, então criamos um registro e adicionamos o valor de cada campo com base nas respostas dadas na entrevista de adoção
    cadastro = {}
    cadastro['nome'] = nome           #nome do possível candidato à adoção
    cadastro['pergunta1'] = pergunta1 #resposta do candidato para a primeira pergunta
    cadastro['pergunta2'] = pergunta2 #resposta do candidato para a segunda pergunta
    cadastro['pergunta3'] = pergunta3 #resposta do candidato para a terceira pergunta
    cadastro['apto'] = apto           #se o candidato está apto ou não apto a adotar
    cadastro['justificativa'] = justificativa #e, se não estiver apto, deve-se incluir a justificativa do porquê
    #Transformando o cadastro do candidato em string
    str_cadastro = str(cadastro)
    #Adicionando a string do candidato no arquivo de candidatos
    a.write('{}\n'.format(str_cadastro))
    #Informamos ao usuário que o cadastro foi feito com sucesso
    print('Novo cadastro de {} adicionado!\n'.format(nome))
    a.close() #Fechando o arquivo


#Função da entrevista, onde há o uso de outras funções para a adoção
def entrevista(arq_animais_adotados, arq_animais_nao_adotados, arquivo_candidatos):
  print('\033[94mOlá! Você já deu o primeiro passo para a adoção de um animal, contribuindo para que mais um '
    'amiguinho encontre seu lar!\nAgora, antes de passar para o segundo passo, você precisará responder algumas perguntas '
    'para sabermos as condições de vida\nque o animal terá e para encontrarmos o animal ideal para você!\033[m')

  #Recebendo o nome do possível candidato à adoção
  while True:
    #Recebendo o nome do possível candidato à adoção
   nome = input('\nDigite o nome do candidato: ')
   if remover_espacos(nome) != '':
     break
   else:
     print('\n\033[31mEste campo deve ser obrigatoriamente preenchido.\033[m')
  

  #Loop while True para verificação de respostas inválidas
  while True:
    #Utilizamos a função perguntas() para receber a lista de respostas do candidato
    lista_respostas = perguntas()
    #Utilizamos a função remover_acento() para remover o acento (se houver) das respostas digitadas
    lista_respostas0 = remover_acento(lista_respostas[0])
    lista_respostas1 = remover_acento(lista_respostas[1])
    lista_respostas2 = remover_acento(lista_respostas[2])

    #Se todas as respostas das perguntas forem válidas, encerramos o while com um break 
    if (lista_respostas0 == 'sim' or lista_respostas0 == 'nao') and (lista_respostas1 == 'sim' or lista_respostas1 == 'nao') and (lista_respostas2 == 'pequeno' or lista_respostas2 == 'medio' or lista_respostas2 == 'grande'):
      break
    
    #Caso contrário, informamos ao usuário que a resposta digitada é inválida e continuamos a pedir para ele digitar
    print('\n\033[31mResposta inválida! Tente novamente.\033[m')


  #Se a resposta da primeira ou da segunda pergunta for diferente de 'sim', então significa que o candidato não poderá adotar um animal, pois não atende aos critérios das perguntas
  if lista_respostas0 != 'sim' or lista_respostas1 != 'sim':
    #Então, informamos isso ao usuário
    print('\n\033[31mInfelizmente o candidato não atendeu aos critérios das perguntas e não está apto a adotar.\033[m')
    apto = 'Não'
    justificativa = 'O candidato não atendeu aos critérios das perguntas'

  #Caso contrário, ou seja, se a resposta da primeira *e* da segunda pergunta for 'sim', então significa que o candidato está apto a adotar e continuamos o processo de adoção
  else:
    #Se a resposta da terceira pergunta for 'pequeno', então utilizamos a função verifica_porte() para gerar a lista dos animais disponíveis apenas de pequeno porte
    if lista_respostas[2] == 'pequeno':
      lista_animais_disponíveis = verifica_porte(arq_animais_nao_adotados, 'pequeno')

    #Se não, se a resposta da terceira pergunta for 'médio/medio', a função verifica_porte() irá retornar a lista dos animais disponíveis apenas de pequeno e médio porte
    elif lista_respostas[2] == 'médio' or lista_respostas[2] == 'medio':
      lista_animais_disponíveis = verifica_porte(arq_animais_nao_adotados, 'pequeno', 'medio')

    #E, em último caso, se a resposta for 'grande', a função verifica_porte() irá retornar a lista dos animais disponíveis de pequeno, médio e grande porte (ou seja, todos os animais disponíveis)
    elif lista_respostas[2] == 'grande':
      lista_animais_disponíveis = verifica_porte(arq_animais_nao_adotados, 'pequeno', 'medio', 'grande')

    #Se a lista_animais_disponiveis for de tamanho zero, significa que não existem animais disponíveis nas condições de porte dadas
    if len(lista_animais_disponíveis) == 0:
      #Então, informamos ao usuário que não existem animais disponíveis para adoção
      print("\n\033[31mDesculpe, não há animais disponíveis para adoção no momento.\033[m")
      apto = 'Não'
      justificativa = 'Não existem animais disponíveis no momento'
    
    #Caso contrário, ou seja, se o tamanho da lista_animais_disponiveis for diferente de zero, então imprimimos as informações dos animais disponíveis para que o candidato possa escolher qual deseja adotar
    else:
      cabecalho('\033[95m         ANIMAIS NÃO ADOTADOS\033[m')
      #A função colocar_em_ordem() irá retornar a lista de animais disponíveis em ordem decrescente de idade (do animal mais velho para o mais novo)
      lista_animais_disponiveis_em_ordem = colocar_em_ordem(lista_animais_disponíveis)
      #Utilizamos a função escolher_animal() para que o candidato possa escolher qual animal ele deseja adotar, e para excluirmos o registro do animal escolhido do arquivo de animais não adotados e adicioná-lo ao arquivo de animais adotados
      escolher_animal(arq_animais_nao_adotados, arq_animais_adotados, nome, lista_animais_disponiveis_em_ordem)
      apto = 'Sim'
      justificativa = '-'
    
  #Por fim, fazemos o cadastro do candidato para armazenar no arquivo de candidatos com as informações referentes ao nome do candidato, resposta da primeira, segunda e terceira pergunta da entrevista, se ele está apto ou não a fazer a adoção e, se não estiver apto, a justificativa.
  cadastrar_candidato(arquivo_candidatos, nome, lista_respostas[0], lista_respostas[1], lista_respostas[2], apto, justificativa)
