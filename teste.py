# -*- coding:UTF-8 -*- 
import sys
reqMax = []
reqMin = []
cont = 0 


def limpar ():

    with open('tabela_jogos.txt', 'w') as arquivo: 
        arquivo.close
    global cont 
    cont = 0
    reqMax.clear()
    reqMin.clear()

def consulta ():
    print('~'*30)
    linha = open('tabela_jogos.txt','r')
    leitura = linha.read()
    print(leitura)
    
def inserir():
    
    aux = 0
    auxmin = 0
  
    placar = int (input('insira o placar do jogo: '))
    if placar > 1000 or placar < 0:
        print('\n\tPlacar não deve ser maior que 1000 ou menor que 0!',)
        print('\tPlacar pode ser igual a 0!\n')
        sys.exit()
   
    minimo = int (input('insira o mínimo da temporada: '))
    maximo = int (input('insira o máximo da temporada: '))
    reqMax.append(maximo)
    reqMin.append(minimo)
    
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


    with open('tabela_jogos.txt', 'a') as arquivo: 
    
        frases = list()             
        frases.append(f'\rJogo= {str(cont)} |')
        frases.append(f'placar= {str(placar)} |')
        frases.append(f'minimo= {str(minimo)} |')
        frases.append(f'maximo= {str(maximo)} |')
        frases.append(f'Recorde Maximo= {str(aux)} |')
        frases.append(f'Recorde Minimo= {str(auxmin)} |\r')
        frases.append('~'*83)
        arquivo.writelines(frases)
        arquivo.close
        print(reqMax)
    
#print(limpar())     

p = 0
while p != 4:
        
    print('~'*30)
    print('Para Inserir dados do jogo aperte [1]: ')
    print('Para consultar dados dos jogos aperte [2]: ')
    print('para limpar a tabela de jogos aperte [3]')
    print('Para Sair do programa aperte [4]: ')

    p = int(input('Opção: '))
    print('~'*30)
    if p == 1:
        cont+=1
        inserir()
    elif p == 2:
        consulta()
    elif p ==3: 
        limpar()
    elif p == 4:
        print('Opção {}'.format(p), 'Saindo do programa!!!')
    else:
        print('Opção Invalida')
        print('*'*30)


