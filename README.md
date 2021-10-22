
# Introdução

Resolução do Problema da Mochila (knapsack problem) por meio de um algoritmo genético.

## Problema da Mochila

O Problema da mochila é consta que existem 20 livro que precisam ser levado em uma mochila, que possui a capacidade igual a de 5 quilos. Cada livro possui sua pesagem também em quilos. A solução do problema consta em levar o maximo de livros possíveis dentro da mochila sem que ela rasgue.

## Algoritmo

O Algoritmo foi inicialmente em todo um arquivo com as funções basicas dos operadores genéticos, além de outras funções de demonstrações. Os testes de resultados serão impressos no terminal por meio da função basica <code>print</code>.

Todas a funções necessárias podem ser encontradas dentro da função <code>main()</code>

# Desenvolvimento 

O algoritmo possui um conjunto com todas as pesagens do livro em array <code>peso = []</code> que pode ser encontrado como uma global no topo do código. Esse array serve para construir um critério de avaliação chamado **função de avaliação** que calcula a soma de pesos dentro da mochila e analisa se ela deve ou não rasgar.

## Cromossomos

Cada cromossomo, que se trata uma solução, é composto por 20 genes, sendo cada um dos genes representando a existencia ou não do livro presente na mochila. Portanto a função de avaliação deve somar cada um desses genes com seus respectivos livros na mochila e gerar, caso ela não rasgue, sua função de aptidão.

## Função Aptidão

A função de aptidão nesse caso é dada pela quantidade de livros presente em cada cromossomo (solução). Para isso a função recebe o cromossomo, que é um vetor de 0 e 1 de tamanho 20, e vai multiplicando cada vetor por 10 e somando todos eles. Por fim temos o valor de aptidão ou valor fitness e isso que irá definir se o individuo deve ou não se manter na população de cromossomos

Um vez com a aptidão atribuida a cada um dos individuos da população, precisamos definir a porcentagem de aptidão de cada um deles em comparação com a aptidão total dos individuos. Isso é necessário para a etapa de seleção que precede a etapa de cruzamento.

## Método da Roleta

Para selecionarmos os melhores individuos que iram gerar descendentes para compor a nova geração da população usamos da Amostragem Estocástica. Ela garante que todos os individuos da geração anterior tem chances de se manterem para a próxima geração, contudo os individuos mais adaptados possuem mais probabilidade de sobreviver. 

Nisso usamos o método da roleta, que semelhante aos casinos, utiliza da sorte e o acaso para escolhermos os individuos selecionados. Graças a proporção tirada na etapa anterior, temos o quantos porcentos a aptidão de um individuo infere no resto do grupo e portanto essa porcentagem definirá a probabilidade dele ser sorteado durante a etapa de seleção.

A solução arranjada para isso foi criar uma tabela, com 100 entrada, na qual um número sorteado deve escolher uma dessas entradas e definir o individuo. A tabela é composta por numero que representa os individuos repetindo-os de acordo com sua probabilidade de seleção. Uma vez que o numero aleatorio cair numa entrada que possuir o numero que representa um individuo, este deve ser escolhido para o cruzamento. O processo se repete, garantindo que o mesmo individuo não pode ser escolhido duas vezes, e ambos individuos gera dois filhos.

## Mutação e Substituição

Após serem gerados os filhos são mutados e a população é substituida. Durante a mutação, alguns filhos são escolhidos aleatoriamente, baseado na taxa de mutação e tem exatamente um gene alterado de 0 para 1 ou de 1 para 0. Após isso a população de filhos e somada a população de pais. 

Quanto ao metodo de substituição utilizado consiste na eliminação dos cromossomos com menos fitness possível, sendo eles filhos ou pais da geração anterior. O intuito é que a proxima geração possua apenas os melhores individuos de maneira exatamente arbitrária. Não existe aleatoriedade no método de substituição.

## Gerações

Por fim, o método de cruzamento, mutação e substituição constituem o que podemos chamar de uma geração de individuos. A função geração portanto engloba todas essas funções em uma só e garante que o roteiro se repita pelo numero de gerações exigidas (valor introduzido na função principal por meio de uma variavel) ou até que se cumpra o critério de parada.

## Critério de Parada

Nesse caso o critério de parada é simples e não muito exigente. Como no exemplo dado não havia nenhum critério elaborado o mesmo foi definido baseado no conjunto de experiencias adquirido por meio dos testes durante a elaboração do algoritmo. Como geralmente o valor fitness resultante da segunda geração era entre 80-100, foi definido um critério de parada (a fim de resumir o tempo e custo de produção) a existencia de qualquer cromossomo com mais de 100 de fitness