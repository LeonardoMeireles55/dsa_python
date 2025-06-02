# ATIVIDADE FINAL - ESTRUTURA DE DADOS EM ANALÍTICA
## Documentação do Projeto

### Equipe:
- Nome: [Leonardo Nogueira Meireles]
- Matrícula: [Inserir matrículas]

---

## Introdução

Este projeto implementa todas as 8 partes da atividade final da disciplina Estrutura de Dados Analítica, demonstrando o domínio prático de estruturas fundamentais como listas, pilhas, filas, árvores binárias, funções recursivas e tabelas hash.

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
def inserir(raiz, valor): ...

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

## Execução

O programa foi testado e executa todas as partes corretamente:
- Busca sequencial funcional
- Recursão com resultados corretos
- Árvore binária com inserção ordenada
- Pilha e fila com comportamento LIFO/FIFO
- Métodos de lista aplicados corretamente
- Lista duplamente ligada com navegação bidirecional
- Hash table com encadeamento funcionando
- Condicionais com cálculos precisos

## Conclusão

A atividade foi implementada seguindo as melhores práticas de programação:
- **Simplicidade:** Código claro e conciso
- **Organização:** Estrutura modular bem definida
- **Funcionalidade:** Todas as 8 partes implementadas corretamente
- **Tratamento de erros:** Exceções adequadamente tratadas

O projeto demonstra domínio completo dos conceitos de estruturas de dados, desde operações básicas com listas até implementações complexas como árvores binárias e tabelas hash. As estruturas implementadas são fundamentais para desenvolvimento de sistemas eficientes em análise de dados e automação de processos.

## Reflexão Final

Durante esta atividade, o maior desafio foi implementar a lista duplamente ligada mantendo as referências corretas entre os nós. Esses conceitos são fundamentais para resolver problemas reais como sistemas de cache (usando hash tables), histórico de navegação (usando pilhas), filas de processamento em sistemas distribuídos, e estruturas de índices em bancos de dados (usando árvores). Gostaria de aprofundar mais o estudo de árvores balanceadas (AVL, Red-Black) pois são cruciais para otimização de consultas. Esses conceitos se conectam diretamente com decisões de negócios ao permitir análises mais rápidas de grandes volumes de dados e automação de processos que requerem estruturas eficientes para tomada de decisões em tempo real.

---

**Data de entrega:** 02/06/2025
**Arquivos entregues:**
- `atividade_final.py` (código principal com input do usuário)
- `atividade_final_demo.py` (versão demonstração sem input)
- `documentacao.md` (este documento)
