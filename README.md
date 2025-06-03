# ATIVIDADE FINAL - ESTRUTURA DE DADOS EM ANALÍTICA

## Documentação do Projeto

### Equipe:
- Nome: Leonardo Nogueira Meireles
- Matrícula: 2316232

---

## Introdução

Este projeto implementa todas as 8 partes da atividade final da disciplina Estrutura de Dados Analítica, demonstrando o domínio prático de estruturas fundamentais como listas, pilhas, filas, árvores binárias, funções recursivas e tabelas hash.

## Confira
repo contendo estrutura de dados e algoritimos em java:
https://github.com/LeonardoMeireles55/Data-Structures-and-Algorithms-In-JAVA

## Desenvolvimento

### Parte 1 - Vetores e Busca Sequencial
**Implementação:**
- Geração de lista com 10 números aleatórios usando `random.sample()`
- Algoritmo de busca sequencial com complexidade O(n)
- Tratamento de casos onde o elemento não é encontrado

**Resultado:** Demonstra eficiência da busca e diferenças de tempo baseadas na posição do elemento.

### Parte 2 - Funções Recursivas
**Implementação:**
- `fatorial(n)`: Caso base n≤1, recursão n * fatorial(n-1)
- `fibonacci(n)`: Casos base n≤1, recursão fibonacci(n-1) + fibonacci(n-2)

**Resultado:**
- fatorial(5) = 120 ✓
- fibonacci(6) = 8 ✓

### Parte 3 - Árvore Binária Simples
**Implementação:**
- Classe `No` com atributos valor, esquerda, direita
- Função `inserir()` mantendo propriedade de ordem
- Função `em_ordem()` para travessia in-order

**Resultado:** Inserção [10,5,15,3,8] resulta em traversa ordenada [3,5,8,10,15]

### Parte 4 - Pilha e Fila com Listas
**Implementação:**
- **Pilha (LIFO):** `.append()` para inserir, `.pop()` para remover do fim
- **Fila (FIFO):** `.append()` para inserir, `.pop(0)` para remover do início

**Resultado:** Demonstra clara diferença entre LIFO e FIFO

### Parte 5 - Listas e Métodos
**Implementação:** Demonstração prática dos métodos:
- `.count()`: conta ocorrências
- `.index()`: encontra posição (com tratamento de exceção)
- `.append()`: adiciona ao final
- `.sort()`: ordena lista
- `.pop()`: remove último elemento

### Parte 6 - Lista Duplamente Ligada
**Implementação:**
- Classe `Node` com ponteiros prev/next
- Classe `ListaDuplamenteLigada` com head/tail
- Métodos: inserir/excluir início/fim, navegação bidirecional

**Resultado:** 6 operações demonstrando funcionalidade completa

### Parte 7 - Hashing com Encadeamento
**Implementação:**
- Classe `HashTable` com função hash módulo
- Tratamento de colisões usando listas encadeadas
- Métodos insert, delete, display

**Resultado:** Inserção [5,12,67,9,16], exclusão de 12, exibição correta da distribuição

### Parte 8 - Condicionais com Listas
**Implementação:**
- Comparação de dois valores inteiros
- Cálculo de média de 5 notas com decisão Aprovado/Reprovado (≥7.0)

**Resultado:** Lógica condicional funcionando corretamente

## Estrutura do Código

O código foi organizado em seções claras, cada uma correspondendo a uma parte da atividade:

```python
# Imports necessários
import random

# Parte 1 - Vetores e Busca
def busca_sequencial(lista, elemento): ...

# Parte 2 - Recursão
def fatorial(n): ...
def fibonacci(n): ...

# Parte 3 - Árvore Binária
class No: ...
def inserir(no, valor): ...

# Parte 4 - Pilha e Fila
# Implementação com listas Python

# Parte 5 - Métodos de Lista
# Demonstração prática

# Parte 6 - Lista Duplamente Ligada
class Node: ...
class ListaDuplamenteLigada: ...

# Parte 7 - Hash Table
class HashTable: ...

# Parte 8 - Condicionais
# Lógica de decisão
```

## Conclusão

A atividade foi implementada seguindo as melhores práticas de programação:
- **Simplicidade:** Código claro e conciso
- **Funcionalidade:** Todas as 8 partes implementadas corretamente


## Reflexão Final
Estruturas de dados são fundamentais para a organização e manipulação eficiente de dados.
Nesta atividade, exploramos diversas estruturas e técnicas, desde vetores e listas até árvores e tabelas hash.
Cada uma tem suas características, vantagens e desvantagens, dependendo do contexto de uso.
A prática com essas estruturas é essencial para desenvolver habilidades de programação e resolução de problemas.
Exemplos como arvores utilizadas em bancos de dados, tabelas hash em caches e listas ligadas em sistemas operacionais mostram a importância dessas estruturas no mundo real.
---

**Arquivos entregues:**
- `MAIN.py` (código principal com input do usuário)
- `README.md` (este documento)
