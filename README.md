# Teste_Pratico_Publca
Program de Formação de Talentos Pública Tecnologia

explicação do Código: 


Defini 3 funções, as quais possuem os nomes limpar, consultar e inserir. 

Na função inserir, é a função que detém a interatividade com o usuário. Onde nessa função será requisitado ao usuário para que entre com os valores do Placar, o Mínimo da temporada e o Máximo da temporada.


placar = int (input('insira o placar do jogo: '))
minimo = int (input('insira o mínimo da temporada: '))
maximo = int (input('insira o máximo da temporada: '))


Todavia, o valor que é armazenado na variável Placar, passar por um teste condicional, para verificar se o valor digitado pelo usuário é menor que 1000 (mil), entretanto, se o valor digitado pelo usuário for maior que mil o programa é encerrado. 


if placar > 1000 or placar < 0:
        print('\n\tPlacar não deve ser maior que 1000 ou menor que 0!',)
        print('\tPlacar pode ser igual a 0!\n')
        sys.exit()


Após os dados serem inseridos, são realizadas algumas condições, onde se tem comparações dos valores digitados pelo usuário, e se realiza por meio de condições uma verificação para saber se os dados digitados podem ser inseridos. 

if maximo == minimo and placar == minimo:
        aux= 0 
        auxmin=0
    else:
        for i in range(0,len(reqMax)):
            if  reqMax[i] >= placar:
                aux = 1    
            else:
                aux = 0
            
        for j in range(0,len(reqMin)):
            if reqMin[j] <= placar:
                auxmin = 1
            else:
                auxmin = 0 


Após os valores terem passado pelas condições, eles são gravados em um arquivo de texto (tabela_jogo.txt), onde se pode inserir mais dados nesse arquivo de texto, ou apagar todos os dados nesse arquivo por meio da função limpar, ou realizar uma consulta dos dados por meio da função consulta. 
Neste programa a função consulta, retorna os dados que existem no arquivo de texto, é realizado uma varredura no arquivo de texto e os dados são expostos na tela. 

Já a função limpar, apaga todos os dados que existe no arquivo de texto, e também apaga todos os valores que existe nas listas (reqMax e reqMin) e na variável. 

def limpar ():
    with open('tabela_jogos.txt', 'w') as arquivo: 
        arquivo.close
    global cont 
    cont = 0
    reqMax.clear()
    reqMin.clear()

Também foi construído um monitor de opções, onde o usuário poderá digitar um número que aparece nas opções, e por meio desse número digitado é feita uma verificação por meio de uma condição, e irá executar a solicitação pedida pelo usuário por meio do número digitado. 

print('~'*30)
    print('Para Inserir dados do jogo aperte [1]: ')
    print('Para consultar dados dos jogos aperte [2]: ')
    print('para limpar a tabela de jogos aperte [3]')
    print('Para Sair do programa aperte [4]: ')
    
