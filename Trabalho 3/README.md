### 1. Introdução
&nbsp;&nbsp;&nbsp;&nbsp;Você, diferente do estereótipo padrão de programador, possui inúmeras
habilidades sociais e consegue interagir, tanto presencialmente quanto online, com
as diversas pessoas da universidade.

&nbsp;&nbsp;&nbsp;&nbsp;E assim como a maioria, você com certeza
tem o seu grupo de amigos mais próximos, aqueles com quem você geralmente faz
trabalhos, conversa mais, se seguem mutuamente no twitter e coloca no close
friends do instagram.

&nbsp;&nbsp;&nbsp;&nbsp;Pensando neste assunto, você decide que gostaria de identificar todos os
subgrupos de amigos próximos que existem dentro de um grupo de pessoas que
interagem online. Para isso, utilizando seus conhecimentos de computação, você
modela o problema de diversas formas, e numa delas representa o grupo como um
grafo direcionado, no qual cada vértice representa uma pessoa e cada aresta (A, B)
indica que a pessoa A segue a B online. Um exemplo dessa modelagem pode ser
visto a seguir, para um grupo de 8 pessoas que se seguem online:

![alt-text]()


        8 11
        0 1
        0 2
        0 4
        1 6
        2 5
        2 6
        3 7
        5 6
        6 2
        6 4
        7 6

### 3. Saída

&nbsp;&nbsp;&nbsp;&nbsp;A saída esperada do seu programa é:
* A quantidade n (inteiro) de componentes fortemente conexos do grafo.
* Em cada uma das n linhas a seguir, a sequência de vértices (inteiros) que
compõem aquele determinado componente conexo.

### 4. Orientações para a confecção do código
&nbsp;&nbsp;&nbsp;&nbsp;Para que a saída do seu programa esteja correta, é preciso que a sequência
de vértices de um componente conexo esteja ordenada, iniciando no vértice de
menor valor, e que a sequência de componentes também esteja ordenada segundo
o mesmo critério. Por exemplo, no grafo acima a saída seria:

Saída:

        6
        0
        1
        2 5 6
        3
        4
        7

&nbsp;&nbsp;&nbsp;&nbsp;A saída mostra que, naquele grupo de 8 pessoas que interagem online,
existem 6 sub-grupos de amigos mais próximos, os subgrupos individuais das
pessoas: 0, 1, 3, 4, 7 e o sub-grupo formado por 2, 5, 6.

### 5. Exemplos de entrada e saída

__Entrada:__

        7 9
        0 3
        1 2
        1 3
        1 5
        2 6
        3 1
        4 2
        5 3
        6 4

__Saída:__

        3
        0
        1 3 5
        2 4 6 


__Entrada:__

        8 7
        0 3
        1 3
        2 0
        3 7
        5 1
        6 4
        7 6

__Saída:__

        8
        0
        1
        2
        3
        4
        5
        6
        7