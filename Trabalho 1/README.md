# Desenhos Eulerianos
### 1. Introdução
&nbsp;&nbsp;&nbsp;&nbsp;Bento, como um bom estudante, estava assistindo as aulas de Cálculo 3 do
professor Possani para tentar entender alguma coisa sobre integrais. Vendo as
aulas, percebeu que seria necessário aprender a desenhar diferentes regiões de
integração e ficou levemente preocupado, já que não tinha habilidade nenhuma para
isso.

&nbsp;&nbsp;&nbsp;&nbsp;Motivado pela vontade de se livrar logo da disciplina, resolveu aprender a
desenhar e começou com as formas mais simples, como retângulos e triângulos.
Em determinado momento, ao combinar as formas chegou ao desenho abaixo:

![alt-text](Trabalho 1/img1.png)

&nbsp;&nbsp;&nbsp;&nbsp;Curiosamente, Bento percebeu que para este desenho, iniciando em um
determinado ponto, não precisou tirar o lápis do papel ou retroceder os traços, e
traçando cada linha uma única vez retornou ao ponto inicial. Empolgado com sua
observação ele foi logo contar para você.
Você como um bom computeiro, entendido de grafos, prontamente contou
que a maneira que ele traçou o desenho pode ser entendida como um circuito
euleriano no grafo euleriano abaixo:

![alt-text](Trabalho 1/img2.png)

Como você é um bom amigo resolveu, juntamente com Bento (que de tão
empolgado esqueceu totalmente de Cálculo 3!), criar um programa que verifica para
diferentes desenhos se é possível traçá-los da mesma forma que foi feito
anteriormente e qual a trajetória a ser seguida para obtê-los, ou seja, dado um grafo
conexo verifica se ele é euleriano, e se for apresenta o circuito euleriano no grafo.

### 2. Entrada

&nbsp;&nbsp;&nbsp;&nbsp;A entrada para seu programa é um grafo conexo, que representa o desenho.


&nbsp;&nbsp;&nbsp;&nbsp;Seu programa deverá ler da entrada padrão:
* Uma string, que é o nome de um arquivo contendo as seguintes informações,
separadas por linha:
* Dois inteiros: v e a, que representam respectivamente a quantidade de
vértices e arestas do grafo.
* a linhas que informam dois inteiros, que representam os vértices
extremos ligados por uma aresta


&nbsp;&nbsp;&nbsp;&nbsp;Observação: os vértices são necessariamente rotulados como inteiros de 0 a
(v -1), como no exemplo, em que v = 5.
&nbsp;&nbsp;&nbsp;&nbsp;Ou seja, se temos, por exemplo, um arquivo que representa o grafo mostrado
anteriormente, ele será dessa forma:

        5 7
        0 1
        0 3
        1 2
        1 3
        1 4
        2 3
        3 4

### 3. Saída
A saída esperada do seu programa é:

* A string “Sim” caso seja possível traçar o desenho da forma descrita (ou seja,
o grafo possui circuito euleriano); ou
* A string “Não” caso não seja possível traçar o desenho da forma descrita.
* Caso tenha impresso “Sim”, na linha seguinte vem a sequência de vértices
(inteiros) que corresponde ao circuito euleriano, separados por um espaço
em branco.

### 4. Orientações para a confecção do código
Ao buscar por um circuito euleriano, inicie sempre pelo vértice
representado pelo valor 0, e ao procurar pelo caminho no grafo, ao escolher uma
aresta a incluir no caminho entre várias opções possíveis, escolha sempre a
aresta que leva ao vértice de menor valor. 

Por exemplo, no grafo acima, o
circuito seria indicado por 0 1 2 3 1 4 3 0

Na entrada, será fornecido o nome do arquivo

### 5. Exemplos de entrada e saída
__Entrada:__

        exemplo.in
__Saida:__

        Sim
        0 1 2 3 1 4 3 0

__Arquivo Exemplo.in__

        5 7
        0 1
        0 3
        1 2
        1 3
        1 4
        2 3
        3 4

__Entrada:__

        2.in

__Saída:__

        Sim
        0 1 2 0 5 2 3 4 5 6 0

__Arquivo 2.in__

        7 10
        0 1
        0 2
        0 5
        0 6
        1 2
        2 3
        2 5
        3 4
        4 5
        5 6