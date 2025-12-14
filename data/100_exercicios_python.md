# 100 EXERCÍCIOS PYTHON PROGRESSIVOS
## Do Básico ao Avançado - Curso Completo

---

# MÓDULO 0: PRIMEIROS PASSOS (Exercícios 00-09)

## Exercício 00: Organização Inicial

**Exercício: 00**  
Preparando o Ambiente de Trabalho

**Pasta de entrega**: ex00/  
**Arquivos para entregar**: None  
**Funções ou bibliotecas autorizadas**: Nenhuma

- Crie uma pasta chamada `python_exercises` no seu diretório de trabalho.
- Dentro desta pasta, crie subpastas numeradas de `ex00` até `ex99`.
- Use apenas comandos de terminal (mkdir).
- Envie um aquivo ex00.py para passar para o próximo exercício.
- Esta estrutura será usada para todos os exercícios seguintes.

```
A organização é fundamental para acompanhar seu progresso.
```

---

## Exercício 01: Primeiro Output

**Exercício: 01**  
Exibir uma Mensagem Simples

**Pasta de entrega**: ex01/  
**Arquivos para entregar**: message.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um script chamado `message.py`.
- O script deve exibir `Python rocks!` seguido por uma nova linha.

```
?> python3 message.py | cat -e
Python rocks!$
?>
```

---

## Exercício 02: Número da Sorte

**Exercício: 02**  
Exibindo Números

**Pasta de entrega**: ex02/  
**Arquivos para entregar**: lucky.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um script chamado `lucky.py`.
- O script deve exibir seu número da sorte favorito seguido por uma nova linha.

```
?> python3 lucky.py | cat -e
7$
?>
```

---

## Exercício 03: Minha Primeira Variável

**Exercício: 03**  
Armazenando Informação

**Pasta de entrega**: ex03/  
**Arquivos para entregar**: myinfo.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um script chamado `myinfo.py`.
- Defina uma variável `city` com o nome da sua cidade.
- Exiba o conteúdo da variável.

```
?> python3 myinfo.py | cat -e
São Paulo$
?>
```

---

## Exercício 04: Nome e Sobrenome

**Exercício: 04**  
Combinando Variáveis

**Pasta de entrega**: ex04/  
**Arquivos para entregar**: identity.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um script chamado `identity.py`.
- Defina duas variáveis: `first` e `last` com seu nome e sobrenome.
- Combine as duas em uma variável `complete`.
- Exiba a variável `complete`.

```
?> python3 identity.py | cat -e
Ana Silva$
?>
```

---

## Exercício 05: Anos de Vida

**Exercício: 05**  
Operações com Números

**Pasta de entrega**: ex05/  
**Arquivos para entregar**: years.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um script chamado `years.py`.
- Defina uma variável com sua idade.
- Calcule quantos dias você já viveu (aproximadamente, use 365 dias/ano).
- Exiba o resultado.

```
?> python3 years.py | cat -e
9125$
?>
```

---

## Exercício 06: Entrada Interativa

**Exercício: 06**  
Recebendo Dados do Usuário

**Pasta de entrega**: ex06/  
**Arquivos para entregar**: greet.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um script chamado `greet.py`.
- Solicite ao usuário que digite seu apelido.
- Exiba uma saudação personalizada usando o apelido.

```
?> python3 greet.py
Digite seu apelido: Zé
Olá, Zé! Prazer em conhecê-lo!
?>
```

---

## Exercício 07: Verificar Maioridade

**Exercício: 07**  
Primeira Decisão

**Pasta de entrega**: ex07/  
**Arquivos para entregar**: adult.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `adult.py`.
- Torne o programa executável (chmod +x).
- Solicite a idade do usuário.
- Se idade >= 18, exiba `Você é maior de idade`.
- Caso contrário, exiba `Você é menor de idade`.

```
?> ./adult.py
Digite sua idade: 20
Você é maior de idade
?>
```

---

## Exercício 08: Classificar Número

**Exercício: 08**  
Múltiplas Decisões

**Pasta de entrega**: ex08/  
**Arquivos para entregar**: classify.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `classify.py`.
- Torne o programa executável.
- Solicite um número ao usuário.
- Classifique como: `Positivo`, `Negativo` ou `Neutro` (zero).

```
?> ./classify.py
Digite um número: -5
Negativo
?>
```

---

## Exercício 09: Divisível por Três

**Exercício: 09**  
Operador Módulo

**Pasta de entrega**: ex09/  
**Arquivos para entregar**: divthree.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `divthree.py`.
- Torne o programa executável.
- Solicite um número ao usuário.
- Informe se o número é divisível por 3 ou não.

```
?> ./divthree.py
Digite um número: 9
9 é divisível por 3
?>
```

---

# MÓDULO 1: LOOPS E ESTRUTURAS (Exercícios 10-19)

## Exercício 10: Contagem Regressiva

**Exercício: 10**  
Primeiro Loop

**Pasta de entrega**: ex10/  
**Arquivos para entregar**: countdown.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `countdown.py`.
- Torne o programa executável.
- Solicite um número N ao usuário.
- Faça uma contagem regressiva de N até 0.

```
?> ./countdown.py
Digite um número: 5
5
4
3
2
1
0
?>
```

---

## Exercício 11: Sequência de Pares

**Exercício: 11**  
Loop com Condição

**Pasta de entrega**: ex11/  
**Arquivos para entregar**: evenseq.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `evenseq.py`.
- Torne o programa executável.
- Solicite um número N ao usuário.
- Exiba todos os números pares de 0 até N.

```
?> ./evenseq.py
Digite um número: 10
0
2
4
6
8
10
?>
```

---

## Exercício 12: Calculadora de Dois Números

**Exercício: 12**  
Operações Básicas

**Pasta de entrega**: ex12/  
**Arquivos para entregar**: twonums.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `twonums.py`.
- Torne o programa executável.
- Solicite dois números: A e B.
- Exiba: A+B, A-B, A*B, A/B.

```
?> ./twonums.py
Número A: 20
Número B: 4
Soma: 24
Subtração: 16
Multiplicação: 80
Divisão: 5.0
?>
```

---

## Exercício 13: Potenciação

**Exercício: 13**  
Cálculo de Potência

**Pasta de entrega**: ex13/  
**Arquivos para entregar**: power.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `power.py`.
- Torne o programa executável.
- Solicite base e expoente.
- Calcule e exiba o resultado da potenciação.

```
?> ./power.py
Base: 2
Expoente: 8
Resultado: 256
?>
```

---

## Exercício 14: Inverter Texto

**Exercício: 14**  
Manipulação de String

**Pasta de entrega**: ex14/  
**Arquivos para entregar**: invert.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `invert.py`.
- Torne o programa executável.
- Solicite uma palavra ao usuário.
- Exiba a palavra invertida.

```
?> ./invert.py
Digite uma palavra: Python
nohtyP
?>
```

---

## Exercício 15: Capitalizar

**Exercício: 15**  
Transformação de Texto

**Pasta de entrega**: ex15/  
**Arquivos para entregar**: caps.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `caps.py`.
- Torne o programa executável.
- Solicite uma frase ao usuário.
- Exiba a frase com todas as letras maiúsculas.

```
?> ./caps.py
Digite uma frase: olá mundo
OLÁ MUNDO
?>
```

---

## Exercício 16: Contar Caracteres

**Exercício: 16**  
Tamanho de String

**Pasta de entrega**: ex16/  
**Arquivos para entregar**: charcount.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `charcount.py`.
- Torne o programa executável.
- Solicite uma string ao usuário.
- Exiba quantos caracteres a string possui.

```
?> ./charcount.py
Digite um texto: Programação
Total de caracteres: 11
?>
```

---

## Exercício 17: Multiplicar String

**Exercício: 17**  
Repetição de Padrão

**Pasta de entrega**: ex17/  
**Arquivos para entregar**: multiply_str.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `multiply_str.py`.
- Torne o programa executável.
- Solicite um símbolo e um número.
- Exiba o símbolo repetido N vezes.

```
?> ./multiply_str.py
Digite um símbolo: *
Quantas vezes: 5
*****
?>
```

---

## Exercício 18: Criar Sequência

**Exercício: 18**  
Primeira Lista

**Pasta de entrega**: ex18/  
**Arquivos para entregar**: sequence.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `sequence.py`.
- Torne o programa executável.
- Crie uma lista com os números de 10 a 20.
- Exiba a lista.

```
?> ./sequence.py
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
?>
```

---

## Exercício 19: Primeiro e Último

**Exercício: 19**  
Acessar Elementos

**Pasta de entrega**: ex19/  
**Arquivos para entregar**: edges.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `edges.py`.
- Torne o programa executável.
- Crie uma lista de cores: ["vermelho", "azul", "verde", "amarelo", "roxo"].
- Exiba a primeira e a última cor.

```
?> ./edges.py
Primeira: vermelho
Última: roxo
?>
```

---

# MÓDULO 2: LISTAS E ITERAÇÃO (Exercícios 20-29)

## Exercício 20: Percorrer Lista

**Exercício: 20**  
Loop For com Lista

**Pasta de entrega**: ex20/  
**Arquivos para entregar**: traverse.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `traverse.py`.
- Torne o programa executável.
- Crie uma lista com 6 animais diferentes.
- Use for para exibir cada animal em uma linha.

```
?> ./traverse.py
Cachorro
Gato
Coelho
Pássaro
Peixe
Hamster
?>
```

---

## Exercício 21: Soma Total

**Exercício: 21**  
Acumulador

**Pasta de entrega**: ex21/  
**Arquivos para entregar**: totalsum.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `totalsum.py`.
- Torne o programa executável.
- Crie uma lista: [5, 12, 8, 3, 15].
- Calcule a soma de todos os elementos.
- Exiba o resultado.

```
?> ./totalsum.py
Soma total: 43
?>
```

---

## Exercício 22: Construir Lista

**Exercício: 22**  
Método append()

**Pasta de entrega**: ex22/  
**Arquivos para entregar**: buildlist.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `buildlist.py`.
- Torne o programa executável.
- Inicie com lista vazia.
- Solicite 5 nomes ao usuário e adicione à lista.
- Exiba a lista completa.

```
?> ./buildlist.py
Nome 1: Ana
Nome 2: Bruno
Nome 3: Carlos
Nome 4: Diana
Nome 5: Eduardo
['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
?>
```

---

## Exercício 23: Cubos

**Exercício: 23**  
List Comprehension

**Pasta de entrega**: ex23/  
**Arquivos para entregar**: cubes.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `cubes.py`.
- Torne o programa executável.
- Use list comprehension para criar lista dos cubos de 1 a 5.
- Exiba a lista.

```
?> ./cubes.py
[1, 8, 27, 64, 125]
?>
```

---

## Exercício 24: Apenas Ímpares

**Exercício: 24**  
Filtro com Comprehension

**Pasta de entrega**: ex24/  
**Arquivos para entregar**: odds.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `odds.py`.
- Torne o programa executável.
- Crie lista com números de 1 a 30.
- Use list comprehension para filtrar apenas ímpares.
- Exiba a lista filtrada.

```
?> ./odds.py
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
?>
```

---

## Exercício 25: Inverter Ordem

**Exercício: 25**  
Método reverse()

**Pasta de entrega**: ex25/  
**Arquivos para entregar**: flip.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `flip.py`.
- Torne o programa executável.
- Crie lista: [10, 20, 30, 40, 50].
- Inverta a ordem e exiba.

```
?> ./flip.py
Original: [10, 20, 30, 40, 50]
Invertida: [50, 40, 30, 20, 10]
?>
```

---

## Exercício 26: Organizar

**Exercício: 26**  
Método sort()

**Pasta de entrega**: ex26/  
**Arquivos para entregar**: organize.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `organize.py`.
- Torne o programa executável.
- Crie lista: [45, 12, 67, 23, 89, 34].
- Ordene em ordem crescente e exiba.

```
?> ./organize.py
Desordenada: [45, 12, 67, 23, 89, 34]
Ordenada: [12, 23, 34, 45, 67, 89]
?>
```

---

## Exercício 27: Frequência

**Exercício: 27**  
Método count()

**Pasta de entrega**: ex27/  
**Arquivos para entregar**: frequency.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `frequency.py`.
- Torne o programa executável.
- Crie lista: [1, 2, 3, 2, 4, 2, 5, 2].
- Conte quantas vezes o número 2 aparece.

```
?> ./frequency.py
O número 2 aparece 4 vezes
?>
```

---

## Exercício 28: Elementos Únicos

**Exercício: 28**  
Usando Set

**Pasta de entrega**: ex28/  
**Arquivos para entregar**: uniques.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `uniques.py`.
- Torne o programa executável.
- Crie lista: [1, 1, 2, 3, 3, 4, 5, 5, 5].
- Remova duplicatas usando set().
- Exiba o conjunto resultante.

```
?> ./uniques.py
Original: [1, 1, 2, 3, 3, 4, 5, 5, 5]
Únicos: {1, 2, 3, 4, 5}
?>
```

---

## Exercício 29: Combinar Listas

**Exercício: 29**  
Concatenação

**Pasta de entrega**: ex29/  
**Arquivos para entregar**: combine.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `combine.py`.
- Torne o programa executável.
- Crie duas listas: [1, 2, 3] e [4, 5, 6].
- Combine-as em uma única lista.
- Exiba o resultado.

```
?> ./combine.py
Lista 1: [1, 2, 3]
Lista 2: [4, 5, 6]
Combinada: [1, 2, 3, 4, 5, 6]
?>
```

---

# MÓDULO 3: DICIONÁRIOS E STRINGS (Exercícios 30-39)

## Exercício 30: Agenda

**Exercício: 30**  
Primeiro Dicionário

**Pasta de entrega**: ex30/  
**Arquivos para entregar**: agenda.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `agenda.py`.
- Torne o programa executável.
- Crie um dicionário com 3 contatos: nome → telefone.
- Exiba o dicionário.

```
?> ./agenda.py
{'João': '11-1234-5678', 'Maria': '11-8765-4321', 'Pedro': '11-5555-9999'}
?>
```

---

## Exercício 31: Buscar Telefone

**Exercício: 31**  
Acesso por Chave

**Pasta de entrega**: ex31/  
**Arquivos para entregar**: findphone.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `findphone.py`.
- Torne o programa executável.
- Crie dicionário: {"Ana": "99999-1111", "Bruno": "88888-2222"}.
- Solicite um nome e exiba o telefone correspondente.

```
?> ./findphone.py
Digite o nome: Ana
Telefone: 99999-1111
?>
```

---

## Exercício 32: Adicionar Contato

**Exercício: 32**  
Modificar Dicionário

**Pasta de entrega**: ex32/  
**Arquivos para entregar**: addcontact.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `addcontact.py`.
- Torne o programa executável.
- Inicie com dicionário vazio.
- Solicite nome e telefone 3 vezes.
- Adicione ao dicionário e exiba.

```
?> ./addcontact.py
Nome: Carlos
Telefone: 77777-3333
Nome: Diana
Telefone: 66666-4444
Nome: Eduardo
Telefone: 55555-5555
{'Carlos': '77777-3333', 'Diana': '66666-4444', 'Eduardo': '55555-5555'}
?>
```

---

## Exercício 33: Listar Dados

**Exercício: 33**  
Iterar Dicionário

**Pasta de entrega**: ex33/  
**Arquivos para entregar**: listdata.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `listdata.py`.
- Torne o programa executável.
- Crie dicionário: {"produto": "Notebook", "preço": 3500, "estoque": 15}.
- Use loop para exibir cada chave e valor.

```
?> ./listdata.py
produto: Notebook
preço: 3500
estoque: 15
?>
```

---

## Exercício 34: Separar Frase

**Exercício: 34**  
String Split

**Pasta de entrega**: ex34/  
**Arquivos para entregar**: splitphrase.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `splitphrase.py`.
- Torne o programa executável.
- Defina frase: "Aprender Python é divertido".
- Separe em palavras e exiba a lista.

```
?> ./splitphrase.py
['Aprender', 'Python', 'é', 'divertido']
?>
```

---

## Exercício 35: Unir Palavras

**Exercício: 35**  
String Join

**Pasta de entrega**: ex35/  
**Arquivos para entregar**: joinwords.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `joinwords.py`.
- Torne o programa executável.
- Crie lista: ["Python", "é", "incrível"].
- Una com espaços e exiba a frase.

```
?> ./joinwords.py
Python é incrível
?>
```

---

## Exercício 36: Trocar Palavra

**Exercício: 36**  
String Replace

**Pasta de entrega**: ex36/  
**Arquivos para entregar**: swap.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `swap.py`.
- Torne o programa executável.
- Defina frase: "Eu gosto de JavaScript".
- Substitua "JavaScript" por "Python".
- Exiba a nova frase.

```
?> ./swap.py
Original: Eu gosto de JavaScript
Modificada: Eu gosto de Python
?>
```

---

## Exercício 37: Contar Letras A

**Exercício: 37**  
Análise de String

**Pasta de entrega**: ex37/  
**Arquivos para entregar**: countera.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `countera.py`.
- Torne o programa executável.
- Solicite uma frase ao usuário.
- Conte quantas letras 'a' (maiúsculas e minúsculas) existem.

```
?> ./countera.py
Digite uma frase: A casa amarela
A frase tem 5 letras 'a'
?>
```

---

## Exercício 38: Espelhar

**Exercício: 38**  
Inverter String

**Pasta de entrega**: ex38/  
**Arquivos para entregar**: mirror.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `mirror.py`.
- Torne o programa executável.
- Solicite uma palavra ao usuário.
- Exiba a palavra original e sua versão invertida lado a lado.

```
?> ./mirror.py
Digite uma palavra: código
código → ogídóc
?>
```

---

## Exercício 39: É Palíndromo?

**Exercício: 39**  
Verificação de Palíndromo

**Pasta de entrega**: ex39/  
**Arquivos para entregar**: checkpalin.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `checkpalin.py`.
- Torne o programa executável.
- Solicite uma palavra ao usuário.
- Verifique se é palíndromo (ignora maiúsculas/minúsculas).

```
?> ./checkpalin.py
Digite uma palavra: radar
SIM - É palíndromo!
?>
```

---

# MÓDULO 4: FUNÇÕES (Exercícios 40-49)

## Exercício 40: Primeira Função

**Exercício: 40**  
Definindo Função

**Pasta de entrega**: ex40/  
**Arquivos para entregar**: intro_func.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `intro_func.py`.
- Torne o programa executável.
- Defina função `bemvindo()` que exibe "Bem-vindo ao Python!".
- Chame a função 2 vezes.

```
?> ./intro_func.py
Bem-vindo ao Python!
Bem-vindo ao Python!
?>
```

---

## Exercício 41: Função Personalizada

**Exercício: 41**  
Parâmetros

**Pasta de entrega**: ex41/  
**Arquivos para entregar**: custom_greet.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `custom_greet.py`.
- Torne o programa executável.
- Defina função `cumprimentar(pessoa)` que exibe saudação.
- Teste com diferentes nomes.

```
?> ./custom_greet.py
Olá, Carlos! Como vai?
Olá, Diana! Como vai?
?>
```

---

## Exercício 42: Função com Return

**Exercício: 42**  
Retornando Valores

**Pasta de entrega**: ex42/  
**Arquivos para entregar**: add_func.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `add_func.py`.
- Torne o programa executável.
- Defina função `adicionar(x, y)` que retorna a soma.
- Teste e exiba resultados.

```
?> ./add_func.py
5 + 3 = 8
10 + 15 = 25
?>
```

---

## Exercício 43: Multiplicador

**Exercício: 43**  
Função Matemática

**Pasta de entrega**: ex43/  
**Arquivos para entregar**: mult_func.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `mult_func.py`.
- Torne o programa executável.
- Defina função `multiplicar(a, b)` que retorna o produto.
- Teste com vários pares de números.

```
?> ./mult_func.py
4 × 5 = 20
7 × 8 = 56
?>
```

---

## Exercício 44: Elevar ao Quadrado

**Exercício: 44**  
Cálculo de Potência

**Pasta de entrega**: ex44/  
**Arquivos para entregar**: square.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `square.py`.
- Torne o programa executável.
- Defina função `quadrado(num)` que retorna num².
- Teste com números de 1 a 5.

```
?> ./square.py
1² = 1
2² = 4
3² = 9
4² = 16
5² = 25
?>
```

---

## Exercício 45: Teste Paridade

**Exercício: 45**  
Função Booleana

**Pasta de entrega**: ex45/  
**Arquivos para entregar**: test_even.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `test_even.py`.
- Torne o programa executável.
- Defina função `e_par(n)` que retorna True/False.
- Teste com números diferentes.

```
?> ./test_even.py
8 é par? True
13 é par? False
?>
```

---

## Exercício 46: Fatorial Recursivo

**Exercício: 46**  
Recursão

**Pasta de entrega**: ex46/  
**Arquivos para entregar**: fact.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `fact.py`.
- Torne o programa executável.
- Defina função recursiva `fatorial(n)`.
- Teste com valores: 0, 4, 6.

```
?> ./fact.py
0! = 1
4! = 24
6! = 720
?>
```

---

## Exercício 47: Máximo da Lista

**Exercício: 47**  
Processar Lista

**Pasta de entrega**: ex47/  
**Arquivos para entregar**: find_max.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `find_max.py`.
- Torne o programa executável.
- Defina função `encontrar_maior(numeros)`.
- Teste com lista: [15, 42, 8, 23, 16].

```
?> ./find_max.py
Maior número: 42
?>
```

---

## Exercício 48: Primeira Letra Maiúscula

**Exercício: 48**  
Processar String

**Pasta de entrega**: ex48/  
**Arquivos para entregar**: cap_first.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `cap_first.py`.
- Torne o programa executável.
- Defina função `primeira_maiuscula(texto)`.
- Teste com várias palavras.

```
?> ./cap_first.py
python → Python
mundo → Mundo
?>
```

---

## Exercício 49: Saudação Padrão

**Exercício: 49**  
Parâmetro Default

**Pasta de entrega**: ex49/  
**Arquivos para entregar**: default_hello.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `default_hello.py`.
- Torne o programa executável.
- Defina função `oi(nome="amigo")` com valor padrão.
- Teste com e sem argumento.

```
?> ./default_hello.py
Oi, amigo!
Oi, Lucas!
?>
```

---

# MÓDULO 5: PROGRAMAÇÃO ORIENTADA A OBJETOS (Exercícios 50-59)

## Exercício 50: Classe Pessoa

**Exercício: 50**  
Primeira Classe

**Pasta de entrega**: ex50/  
**Arquivos para entregar**: person.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `person.py`.
- Torne o programa executável.
- Defina classe `Pessoa` com atributos `nome` e `idade`.
- Crie instâncias e exiba.

```
?> ./person.py
Nome: João, Idade: 28
Nome: Maria, Idade: 32
?>
```

---

## Exercício 51: Classe com Método

**Exercício: 51**  
Métodos

**Pasta de entrega**: ex51/  
**Arquivos para entregar**: dog.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `dog.py`.
- Torne o programa executável.
- Defina classe `Cachorro` com método `latir()`.
- Crie instância e chame o método.

```
?> ./dog.py
Au au au!
?>
```

---

## Exercício 52: Construtor

**Exercício: 52**  
Método __init__

**Pasta de entrega**: ex52/  
**Arquivos para entregar**: vehicle.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `vehicle.py`.
- Torne o programa executável.
- Defina classe `Veiculo` com construtor (marca, modelo, ano).
- Crie instâncias diferentes.

```
?> ./vehicle.py
Veículo: Ford Mustang 2020
Veículo: Tesla Model 3 2023
?>
```

---

## Exercício 53: Calculadora Classe

**Exercício: 53**  
Métodos com Parâmetros

**Pasta de entrega**: ex53/  
**Arquivos para entregar**: calc_class.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `calc_class.py`.
- Torne o programa executável.
- Defina classe `Calc` com método `dividir(a, b)`.
- Teste a divisão.

```
?> ./calc_class.py
20 ÷ 4 = 5.0
?>
```

---

## Exercício 54: Classe Triângulo

**Exercício: 54**  
Cálculos

**Pasta de entrega**: ex54/  
**Arquivos para entregar**: triangle.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `triangle.py`.
- Torne o programa executável.
- Defina classe `Triangulo` com base e altura.
- Implemente método para calcular área.

```
?> ./triangle.py
Base: 10, Altura: 5
Área: 25.0
?>
```

---

## Exercício 55: Cronômetro

**Exercício: 55**  
Atributos Mutáveis

**Pasta de entrega**: ex55/  
**Arquivos para entregar**: timer.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `timer.py`.
- Torne o programa executável.
- Defina classe `Cronometro` que inicia em 0.
- Métodos: `tick()` (incrementa), `reset()` (zera).

```
?> ./timer.py
Tempo: 0
Tempo: 1
Tempo: 2
Tempo: 0
?>
```

---

## Exercício 56: Classe Carteira

**Exercício: 56**  
Simulação Financeira

**Pasta de entrega**: ex56/  
**Arquivos para entregar**: wallet.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `wallet.py`.
- Torne o programa executável.
- Defina classe `Carteira` com saldo inicial.
- Métodos: `adicionar()`, `retirar()`, `saldo()`.

```
?> ./wallet.py
Saldo: R$ 50
Saldo após adicionar: R$ 100
Saldo após retirar: R$ 70
?>
```

---

## Exercício 57: Herança Animal

**Exercício: 57**  
Classe Filha

**Pasta de entrega**: ex57/  
**Arquivos para entregar**: animals.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `animals.py`.
- Torne o programa executável.
- Classe base `Animal` com método `emitir_som()`.
- Classes filhas: `Leao`, `Passaro` sobrescrevem o método.

```
?> ./animals.py
Rugido!
Piu piu!
?>
```

---

## Exercício 58: Áreas Diferentes

**Exercício: 58**  
Polimorfismo

**Pasta de entrega**: ex58/  
**Arquivos para entregar**: shapes.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `shapes.py`.
- Torne o programa executável.
- Classes: `Circulo`, `Retangulo` com método `calcular_area()`.
- Demonstre polimorfismo.

```
?> ./shapes.py
Área do círculo: 50.24
Área do retângulo: 40
?>
```

---

## Exercício 59: Representação Objeto

**Exercício: 59**  
Método __str__

**Pasta de entrega**: ex59/  
**Arquivos para entregar**: product.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `product.py`.
- Torne o programa executável.
- Defina classe `Produto` com `__str__()`.
- Exiba objetos de forma legível.

```
?> ./product.py
Produto: Notebook (R$ 2500)
?>
```

---

# MÓDULO 6: CONCEITOS AVANÇADOS (Exercícios 60-69)

## Exercício 60: Filtro Complexo

**Exercício: 60**  
Comprehension Avançada

**Pasta de entrega**: ex60/  
**Arquivos para entregar**: complex_filter.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `complex_filter.py`.
- Torne o programa executável.
- Lista de 1 a 100.
- Filtre números divisíveis por 7 E terminados em 3.

```
?> ./complex_filter.py
[63]
?>
```

---

## Exercício 61: Lambda Quadrado

**Exercício: 61**  
Funções Lambda

**Pasta de entrega**: ex61/  
**Arquivos para entregar**: lam_square.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `lam_square.py`.
- Torne o programa executável.
- Use lambda para elevar ao quadrado números de uma lista.

```
?> ./lam_square.py
[4, 16, 36, 64, 100]
?>
```

---

## Exercício 62: Map Maiúsculas

**Exercício: 62**  
Função Map

**Pasta de entrega**: ex62/  
**Arquivos para entregar**: map_upper.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `map_upper.py`.
- Torne o programa executável.
- Use `map()` para converter lista de palavras em maiúsculas.

```
?> ./map_upper.py
['PYTHON', 'RUBY', 'JAVASCRIPT']
?>
```

---

## Exercício 63: Filter Maiores

**Exercício: 63**  
Função Filter

**Pasta de entrega**: ex63/  
**Arquivos para entregar**: filter_big.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `filter_big.py`.
- Torne o programa executável.
- Use `filter()` para números maiores que 50.

```
?> ./filter_big.py
[60, 75, 90, 100]
?>
```

---

## Exercício 64: Reduce Produto

**Exercício: 64**  
Função Reduce

**Pasta de entrega**: ex64/  
**Arquivos para entregar**: reduce_prod.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `reduce_prod.py`.
- Torne o programa executável.
- Use `reduce()` para multiplicar lista: [2, 3, 4].

```
?> ./reduce_prod.py
Produto: 24
?>
```

---

## Exercício 65: Tratar Erro

**Exercício: 65**  
Try Except

**Pasta de entrega**: ex65/  
**Arquivos para entregar**: safe_div.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `safe_div.py`.
- Torne o programa executável.
- Solicite dois números e divida.
- Trate divisão por zero com try/except.

```
?> ./safe_div.py
Número 1: 10
Número 2: 0
ERRO: Não é possível dividir por zero!
?>
```

---

## Exercício 66: Ler Arquivo de Texto

**Exercício: 66**  
Manipulação de Arquivo

**Pasta de entrega**: ex66/  
**Arquivos para entregar**: read_txt.py, data.txt  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `read_txt.py`.
- Torne o programa executável.
- Crie arquivo `data.txt` com 3 linhas de texto.
- Leia e exiba o conteúdo.

```
?> ./read_txt.py
Linha 1 do arquivo
Linha 2 do arquivo
Linha 3 do arquivo
?>
```

---

## Exercício 67: Criar Arquivo

**Exercício: 67**  
Escrever Arquivo

**Pasta de entrega**: ex67/  
**Arquivos para entregar**: create_file.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `create_file.py`.
- Torne o programa executável.
- Solicite 3 linhas de texto ao usuário.
- Salve em arquivo `output.txt`.

```
?> ./create_file.py
Linha 1: Primeira linha
Linha 2: Segunda linha
Linha 3: Terceira linha
Arquivo criado com sucesso!
?>
```

---

## Exercício 68: Trabalhar com JSON

**Exercício: 68**  
Formato JSON

**Pasta de entrega**: ex68/  
**Arquivos para entregar**: json_work.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `json_work.py`.
- Torne o programa executável.
- Crie dicionário com dados de pessoa.
- Salve em arquivo JSON e leia de volta.

```
?> ./json_work.py
Dados salvos em JSON
Dados lidos: {'nome': 'Ana', 'idade': 28, 'cidade': 'Rio'}
?>
```

---

## Exercício 69: Decorator Simples

**Exercício: 69**  
Decoradores

**Pasta de entrega**: ex69/  
**Arquivos para entregar**: simple_dec.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `simple_dec.py`.
- Torne o programa executável.
- Crie decorator que exibe "Executando..." antes da função.
- Aplique em uma função de teste.

```
?> ./simple_dec.py
Executando...
Função concluída!
?>
```

---

# MÓDULO 7: PROJETOS PRÁTICOS (Exercícios 70-79)

## Exercício 70: Adivinhe o Número

**Exercício: 70**  
Jogo Interativo

**Pasta de entrega**: ex70/  
**Arquivos para entregar**: guess_game.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `guess_game.py`.
- Torne o programa executável.
- Computador escolhe número aleatório 1-50.
- Usuário tenta adivinhar com dicas.

```
?> ./guess_game.py
Adivinhe (1-50): 25
Muito baixo!
Adivinhe (1-50): 40
Muito alto!
Adivinhe (1-50): 33
Correto! Você acertou!
?>
```

---

## Exercício 71: Cálculo IMC

**Exercício: 71**  
Saúde

**Pasta de entrega**: ex71/  
**Arquivos para entregar**: bmi.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `bmi.py`.
- Torne o programa executável.
- Solicite peso (kg) e altura (m).
- Calcule IMC e classifique o resultado.

```
?> ./bmi.py
Peso (kg): 70
Altura (m): 1.75
IMC: 22.86
Classificação: Peso normal
?>
```

---

## Exercício 72: Gerar Senhas

**Exercício: 72**  
Segurança

**Pasta de entrega**: ex72/  
**Arquivos para entregar**: passgen.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `passgen.py`.
- Torne o programa executável.
- Gere senha aleatória (letras, números, símbolos).
- Tamanho definido pelo usuário.

```
?> ./passgen.py
Tamanho: 10
Senha: aK9@mP3#xL
?>
```

---

## Exercício 73: Lista de Tarefas

**Exercício: 73**  
Gerenciador

**Pasta de entrega**: ex73/  
**Arquivos para entregar**: tasks.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `tasks.py`.
- Torne o programa executável.
- Menu: 1-Adicionar, 2-Listar, 3-Remover, 4-Sair.
- Use lista para armazenar tarefas.

```
?> ./tasks.py
[1] Adicionar [2] Listar [3] Remover [4] Sair
Escolha: 1
Tarefa: Estudar Python
Adicionada!
?>
```

---

## Exercício 74: Converter Temperatura

**Exercício: 74**  
Conversões

**Pasta de entrega**: ex74/  
**Arquivos para entregar**: temp_conv.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `temp_conv.py`.
- Torne o programa executável.
- Menu para converter: C→F, F→C, C→K.

```
?> ./temp_conv.py
[1] C→F [2] F→C [3] C→K
Escolha: 1
Temperatura: 30
30°C = 86°F
?>
```

---

## Exercício 75: Cadastro Simples

**Exercício: 75**  
Sistema CRUD

**Pasta de entrega**: ex75/  
**Arquivos para entregar**: register.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `register.py`.
- Torne o programa executável.
- Cadastre pessoas: nome, email, telefone.
- Opções: adicionar, listar, buscar.

```
?> ./register.py
[1] Adicionar [2] Listar [3] Buscar
Escolha: 1
Nome: João
Email: joao@email.com
Telefone: 99999-0000
Cadastrado!
?>
```

---

## Exercício 76: Análise de Texto

**Exercício: 76**  
Processamento

**Pasta de entrega**: ex76/  
**Arquivos para entregar**: text_analysis.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `text_analysis.py`.
- Torne o programa executável.
- Solicite texto e exiba:
  - Número de palavras
  - Palavra mais frequente
  - Número de caracteres

```
?> ./text_analysis.py
Digite o texto: Python Python é legal Python é bom
Palavras: 6
Mais frequente: Python (3x)
Caracteres: 31
?>
```

---

## Exercício 77: Pedra Papel Tesoura

**Exercício: 77**  
Jogo Clássico

**Pasta de entrega**: ex77/  
**Arquivos para entregar**: rps.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `rps.py`.
- Torne o programa executável.
- Jogue pedra-papel-tesoura contra o computador.

```
?> ./rps.py
[1] Pedra [2] Papel [3] Tesoura
Sua escolha: 1
Computador escolheu: Tesoura
Você venceu!
?>
```

---

## Exercício 78: Juros Compostos

**Exercício: 78**  
Financeiro

**Pasta de entrega**: ex78/  
**Arquivos para entregar**: compound.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `compound.py`.
- Torne o programa executável.
- Calcule montante final com juros compostos.
- Fórmula: M = C × (1 + i)^t

```
?> ./compound.py
Capital: 1000
Taxa (% ao mês): 2
Meses: 12
Montante final: R$ 1268.24
?>
```

---

## Exercício 79: Validar Email

**Exercício: 79**  
Validação

**Pasta de entrega**: ex79/  
**Arquivos para entregar**: validate_email.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `validate_email.py`.
- Torne o programa executável.
- Valide formato de email (deve conter @ e .).

```
?> ./validate_email.py
Email: teste@exemplo.com
Email válido!
?> ./validate_email.py
Email: invalido.email
Email inválido!
?>
```

---

# MÓDULO 8: TÓPICOS ESPECIALIZADOS (Exercícios 80-89)

## Exercício 80: Requisição Web

**Exercício: 80**  
API Requests

**Pasta de entrega**: ex80/  
**Arquivos para entregar**: web_request.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `web_request.py`.
- Torne o programa executável.
- Faça requisição HTTP GET para uma API pública.
- Exiba o status code.

```
?> ./web_request.py
Status: 200
Requisição bem-sucedida!
?>
```

---

## Exercício 81: Consultar CEP

**Exercício: 81**  
API Externa

**Pasta de entrega**: ex81/  
**Arquivos para entregar**: cep_api.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `cep_api.py`.
- Torne o programa executável.
- Consulte API ViaCEP.
- Exiba endereço completo.

```
?> ./cep_api.py
CEP: 01310-100
Rua: Avenida Paulista
Bairro: Bela Vista
Cidade: São Paulo - SP
?>
```

---

## Exercício 82: Gráfico de Barras

**Exercício: 82**  
Matplotlib

**Pasta de entrega**: ex82/  
**Arquivos para entregar**: bar_chart.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `bar_chart.py`.
- Torne o programa executável.
- Crie gráfico de barras com vendas mensais.
- Salve como imagem.

```
?> ./bar_chart.py
Gráfico salvo: vendas.png
?>
```

---

## Exercício 83: Banco de Dados

**Exercício: 83**  
SQLite

**Pasta de entrega**: ex83/  
**Arquivos para entregar**: db_simple.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `db_simple.py`.
- Torne o programa executável.
- Crie banco SQLite.
- Tabela: produtos (id, nome, preço).
- Insira 3 produtos e liste.

```
?> ./db_simple.py
Produtos cadastrados:
1 - Notebook - R$ 2500
2 - Mouse - R$ 50
3 - Teclado - R$ 150
?>
```

---

## Exercício 84: Validar com Regex

**Exercício: 84**  
Expressões Regulares

**Pasta de entrega**: ex84/  
**Arquivos para entregar**: regex_phone.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `regex_phone.py`.
- Torne o programa executável.
- Valide telefone brasileiro: (XX) XXXXX-XXXX.

```
?> ./regex_phone.py
Telefone: (11) 98765-4321
Telefone válido!
?>
```

---

## Exercício 85: Multithreading

**Exercício: 85**  
Threads

**Pasta de entrega**: ex85/  
**Arquivos para entregar**: multi_thread.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `multi_thread.py`.
- Torne o programa executável.
- Crie 3 threads que contam de 1 a 5.
- Exiba qual thread está executando.

```
?> ./multi_thread.py
Thread-1: 1
Thread-2: 1
Thread-3: 1
Thread-1: 2
...
?>
```

---

## Exercício 86: Enviar Notificação

**Exercício: 86**  
Email SMTP

**Pasta de entrega**: ex86/  
**Arquivos para entregar**: send_mail.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `send_mail.py`.
- Torne o programa executável.
- Configure SMTP (Gmail/Outlook).
- Envie email de teste.

```
?> ./send_mail.py
Para: destinatario@exemplo.com
Assunto: Teste Python
Corpo: Olá do Python!
Email enviado!
?>
```

---

## Exercício 87: Compactar Arquivos

**Exercício: 87**  
ZIP

**Pasta de entrega**: ex87/  
**Arquivos para entregar**: zipper.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `zipper.py`.
- Torne o programa executável.
- Solicite nomes de arquivos.
- Compacte todos em um ZIP.

```
?> ./zipper.py
Arquivos: file1.txt, file2.txt, file3.txt
ZIP criado: arquivos.zip
?>
```

---

## Exercício 88: Gerar QR Code

**Exercício: 88**  
QR Code

**Pasta de entrega**: ex88/  
**Arquivos para entregar**: qr_gen.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `qr_gen.py`.
- Torne o programa executável.
- Gere QR Code de uma URL ou texto.

```
?> ./qr_gen.py
Digite o texto: https://python.org
QR Code salvo: qrcode.png
?>
```

---

## Exercício 89: Criar PDF

**Exercício: 89**  
PDF

**Pasta de entrega**: ex89/  
**Arquivos para entregar**: pdf_create.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `pdf_create.py`.
- Torne o programa executável.
- Crie PDF com título e parágrafo de texto.

```
?> ./pdf_create.py
Título: Relatório Python
Texto: Este é um relatório gerado automaticamente.
PDF criado: relatorio.pdf
?>
```

---

# MÓDULO 9: DESAFIOS FINAIS (Exercícios 90-99)

## Exercício 90: Sistema Login

**Exercício: 90**  
Autenticação

**Pasta de entrega**: ex90/  
**Arquivos para entregar**: login_system.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `login_system.py`.
- Torne o programa executável.
- Cadastro com senha (use hash).
- Login verificando credenciais.

```
?> ./login_system.py
[1] Cadastrar [2] Login
Escolha: 1
Usuário: admin
Senha: ****
Cadastrado com sucesso!
?>
```

---

## Exercício 91: Bot Respondedor

**Exercício: 91**  
Chatbot

**Pasta de entrega**: ex91/  
**Arquivos para entregar**: bot.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `bot.py`.
- Torne o programa executável.
- Bot responde perguntas predefinidas.
- Use dicionário para respostas.

```
?> ./bot.py
Você: Oi
Bot: Olá! Tudo bem?
Você: Qual seu nome?
Bot: Meu nome é PyBot!
?>
```

---

## Exercício 92: Análise Sentimento

**Exercício: 92**  
NLP Básico

**Pasta de entrega**: ex92/  
**Arquivos para entregar**: sentiment.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `sentiment.py`.
- Torne o programa executável.
- Analise texto: positivo, negativo ou neutro.
- Use lista de palavras-chave.

```
?> ./sentiment.py
Texto: Eu amo programar em Python!
Sentimento: Positivo ✓
?>
```

---

## Exercício 93: Enquete

**Exercício: 93**  
Sistema de Votação

**Pasta de entrega**: ex93/  
**Arquivos para entregar**: poll.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `poll.py`.
- Torne o programa executável.
- 3 opções de voto.
- Exiba resultados percentuais.

```
?> ./poll.py
Opções: [A] Python [B] Java [C] C++
Seu voto: A
Voto registrado!
Resultados:
Python: 60%
Java: 30%
C++: 10%
?>
```

---

## Exercício 94: Jogo da Velha

**Exercício: 94**  
Tic-Tac-Toe

**Pasta de entrega**: ex94/  
**Arquivos para entregar**: tictactoe.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `tictactoe.py`.
- Torne o programa executável.
- Jogo da velha para 2 jogadores.
- Detecte vitória e empate.

```
?> ./tictactoe.py
 X | O | X
-----------
 O | X | O
-----------
 X | O | X
Empate!
?>
```

---

## Exercício 95: Cotação Moedas

**Exercício: 95**  
API Câmbio

**Pasta de entrega**: ex95/  
**Arquivos para entregar**: exchange.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `exchange.py`.
- Torne o programa executável.
- Consulte API de câmbio.
- Converta USD → BRL.

```
?> ./exchange.py
Valor em USD: 100
100 USD = 490.50 BRL
Taxa: 4.905
?>
```

---

## Exercício 96: Gerador HTML

**Exercício: 96**  
Automação

**Pasta de entrega**: ex96/  
**Arquivos para entregar**: html_gen.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `html_gen.py`.
- Torne o programa executável.
- Gere página HTML com título e conteúdo.

```
?> ./html_gen.py
Título: Minha Página
Conteúdo: Olá, mundo!
HTML gerado: pagina.html
?>
```

---

## Exercício 97: Backup Automático

**Exercício: 97**  
Automação Backup

**Pasta de entrega**: ex97/  
**Arquivos para entregar**: auto_backup.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `auto_backup.py`.
- Torne o programa executável.
- Copie arquivos de uma pasta para backup.
- Adicione timestamp no nome.

```
?> ./auto_backup.py
Pasta origem: /documentos
Backup criado: backup_20251214_110000.zip
?>
```

---

## Exercício 98: Monitor Sistema

**Exercício: 98**  
Informações Sistema

**Pasta de entrega**: ex98/  
**Arquivos para entregar**: sys_monitor.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `sys_monitor.py`.
- Torne o programa executável.
- Exiba: CPU, RAM, Disco.
- Use biblioteca psutil.

```
?> ./sys_monitor.py
CPU: 35%
RAM: 52% (4.2 GB / 8 GB)
Disco: 68% (340 GB / 500 GB)
?>
```

---

## Exercício 99: Projeto Integrado Final

**Exercício: 99**  
Sistema Completo

**Pasta de entrega**: ex99/  
**Arquivos para entregar**: integrated_system.py  
**Funções ou bibliotecas autorizadas**: Todas

- Crie um programa chamado `integrated_system.py`.
- Torne o programa executável.
- Sistema que integre 5+ conceitos:
  - Classes (POO)
  - Banco de Dados
  - Arquivos
  - API externa
  - Interface de menu

```
?> ./integrated_system.py
=== SISTEMA INTEGRADO ===
[1] Gerenciar Usuários (DB)
[2] Consultar API
[3] Gerar Relatório (PDF)
[4] Backup de Dados
[5] Sair
Escolha: 
?>
```

---

# CONCLUSÃO

## 🎉 Parabéns! Você completou 100 Exercícios Python!

### 📊 Resumo da Jornada:

| Módulo | Exercícios | Tópicos |
|--------|-----------|---------|
| 0 | 00-09 | Primeiros Passos |
| 1 | 10-19 | Loops e Estruturas |
| 2 | 20-29 | Listas e Iteração |
| 3 | 30-39 | Dicionários e Strings |
| 4 | 40-49 | Funções |
| 5 | 50-59 | POO |
| 6 | 60-69 | Conceitos Avançados |
| 7 | 70-79 | Projetos Práticos |
| 8 | 80-89 | Tópicos Especializados |
| 9 | 90-99 | Desafios Finais |

### ✅ Você dominou:

- Fundamentos Python
- Estruturas de Dados
- Funções e Métodos
- Programação Orientada a Objetos
- Manipulação de Arquivos
- APIs e Web
- Banco de Dados
- Bibliotecas Avançadas

**Continue praticando e construindo projetos incríveis! 🚀**

---

**Versão 1.0 | Dezembro 2025 | 100 Exercícios Python Progressivos**