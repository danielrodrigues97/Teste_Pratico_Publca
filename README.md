# Teste_Pratico_Publca
Program de Formação de Talentos Pública Tecnologia

explicação do Código: 


Defini 3 funções, as quais possuem os nomes limpar, consultar e inserir. 

Na função inserir, é a função que detém a interatividade com o usuário. Onde nessa função será requisitado ao usuário para que entre com os valores do Placar, o Mínimo da temporada e o Máximo da temporada.

<div class>
placar = int (input('insira o placar do jogo: '))
minimo = int (input('insira o mínimo da temporada: '))
maximo = int (input('insira o máximo da temporada: '))
</div>

Todavia, o valor que é armazenado na variável Placar, passar por um teste condicional, para verificar se o valor digitado pelo usuário é menor que 1000 (mil), entretanto, se o valor digitado pelo usuário for maior que mil o programa é encerrado. 

<div>
if placar > 1000 or placar < 0:
        print('\n\tPlacar não deve ser maior que 1000 ou menor que 0!',)
        print('\tPlacar pode ser igual a 0!\n')
        sys.exit()
</div>

Após os dados serem inseridos, são realizadas algumas condições, onde se tem comparações dos valores digitados pelo usuário, e se realiza por meio de condições uma verificação para saber se os dados digitados podem ser inseridos. 

<div>
if maximo == minimo and placar == minimo:<br>
        aux= 0 <br>
        auxmin=0<br>
    else:<br>
        for i in range(0,len(reqMax)):<br>
            if  reqMax[i] >= placar:<br>
                aux = 1  <br>
            else:<br>
                aux = 0<br>
            for j in range(0,len(reqMin)): <br>
            if reqMin[j] <= placar: <br>
                auxmin = 1 <br>
            else:<br>
                auxmin = 0 <br> 

<br>
</div>
Após os valores terem passado pelas condições, eles são gravados em um arquivo de texto (tabela_jogo.txt), onde se pode inserir mais dados nesse arquivo de texto, ou apagar todos os dados nesse arquivo por meio da função limpar, ou realizar uma consulta dos dados por meio da função consulta. 
Neste programa a função consulta, retorna os dados que existem no arquivo de texto, é realizado uma varredura no arquivo de texto e os dados são expostos na tela. 

Já a função limpar, apaga todos os dados que existe no arquivo de texto, e também apaga todos os valores que existe nas listas (reqMax e reqMin) e na variável. 
<div>
<br>

<dev>
<p>
def limpar ():<br>
    with open('tabela_jogos.txt', 'w') as arquivo: <br>
        arquivo.close<br>
    global cont <br>
    cont = 0 <br>
    reqMax.clear()<br>
    reqMin.clear()<br>
<p>
</div>
<br>
<p>
Também foi construído um monitor de opções, onde o usuário poderá digitar um número que aparece nas opções, e por meio desse número digitado é feita uma verificação por meio de uma condição, e irá executar a solicitação pedida pelo usuário por meio do número digitado. 
<p>
<br>
<div>
<p>
print('~'*30)<br>
    print('Para Inserir dados do jogo aperte [1]: ')<br>
    print('Para consultar dados dos jogos aperte [2]: ')<br>
    print('para limpar a tabela de jogos aperte [3]')<br>
    print('Para Sair do programa aperte [4]: ')<br>
<p>
</div>    
