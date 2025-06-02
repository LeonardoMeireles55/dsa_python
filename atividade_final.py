#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATIVIDADE FINAL - ESTRUTURA DE DADOS EM ANALÍTICA
Implementação das 8 partes da atividade
"""

import random

print("=" * 60)
print("ATIVIDADE FINAL - ESTRUTURA DE DADOS EM ANALÍTICA")
print("=" * 60)

# =============================================================================
# PARTE 1 - VETORES E BUSCA SEQUENCIAL
# =============================================================================
print("\n1. VETORES E BUSCA SEQUENCIAL")
print("-" * 40)

# Gerar lista com 10 números aleatórios entre 1 e 100
vetor = random.sample(range(1, 101), 10)
print(f"Vetor gerado: {vetor}")

def busca_sequencial(lista, elemento):
    """Realiza busca sequencial em uma lista"""
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

# Solicitar número para busca
numero_busca = int(input("Digite um número para buscar: "))
posicao = busca_sequencial(vetor, numero_busca)

if posicao != -1:
    print(f"Número {numero_busca} encontrado na posição {posicao}")
else:
    print(f"Número {numero_busca} não encontrado no vetor")

# =============================================================================
# PARTE 2 - FUNÇÕES RECURSIVAS
# =============================================================================
print("\n2. FUNÇÕES RECURSIVAS")
print("-" * 40)

def fatorial(n):
    """Calcula o fatorial de n recursivamente"""
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

def fibonacci(n):
    """Calcula o n-ésimo número de Fibonacci recursivamente"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testes
print(f"Fatorial de 5: {fatorial(5)}")
print(f"6º número de Fibonacci: {fibonacci(6)}")

# =============================================================================
# PARTE 3 - ÁRVORE BINÁRIA SIMPLES
# =============================================================================
print("\n3. ÁRVORE BINÁRIA SIMPLES")
print("-" * 40)

class No:
    """Classe para representar um nó da árvore binária"""
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(raiz, valor):
    """Insere um valor na árvore binária mantendo a ordem"""
    if raiz is None:
        return No(valor)

    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    else:
        raiz.direita = inserir(raiz.direita, valor)

    return raiz

def em_ordem(raiz):
    """Traversa a árvore em ordem (in-order)"""
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.valor, end=" ")
        em_ordem(raiz.direita)

# Inserir valores: 10, 5, 15, 3, 8
arvore = None
valores = [10, 5, 15, 3, 8]
for valor in valores:
    arvore = inserir(arvore, valor)

print(f"Valores inseridos: {valores}")
print("Travessia em ordem: ", end="")
em_ordem(arvore)
print()

# =============================================================================
# PARTE 4 - PILHA E FILA COM LISTAS
# =============================================================================
print("\n4. PILHA E FILA COM LISTAS")
print("-" * 40)

# PILHA (LIFO)
print("PILHA (LIFO):")
pilha = [1, 1, 2, 3, 5]
print(f"Pilha inicial: {pilha}")

pilha.append(8)
pilha.append(13)
print(f"Após adicionar 8 e 13: {pilha}")

pilha.pop()
print(f"Após remover um elemento: {pilha}")

# FILA (FIFO)
print("\nFILA (FIFO):")
fila = [20, 30, 40, 50, 60]
print(f"Fila inicial: {fila}")

fila.append(99)
print(f"Após adicionar 99: {fila}")

for _ in range(3):
    fila.pop(0)
print(f"Após remover 3 elementos: {fila}")

print("\nDiferença: Pilha = último a entrar, primeiro a sair")
print("          Fila = primeiro a entrar, primeiro a sair")

# =============================================================================
# PARTE 5 - LISTAS E MÉTODOS
# =============================================================================
print("\n5. LISTAS E MÉTODOS")
print("-" * 40)

frutas = ['banana', 'maçã', 'kiwi', 'banana', 'pera', 'maçã', 'laranja']
print(f"Lista inicial: {frutas}")

# .count('maçã')
count_maca = frutas.count('maçã')
print(f"Quantidade de 'maçã': {count_maca}")

# .index('banana') e .index('banana', 4)
index_banana = frutas.index('banana')
print(f"Primeira posição de 'banana': {index_banana}")

# Verificar se existe banana após índice 3
try:
    index_banana_4 = frutas.index('banana', 4)
    print(f"Posição de 'banana' a partir do índice 4: {index_banana_4}")
except ValueError:
    print("Não há 'banana' a partir do índice 4")

# .append('uva')
frutas.append('uva')
print(f"Após adicionar 'uva': {frutas}")

# .sort()
frutas.sort()
print(f"Após ordenar: {frutas}")

# .pop()
removido = frutas.pop()
print(f"Após remover último elemento '{removido}': {frutas}")

# =============================================================================
# PARTE 6 - LISTA DUPLAMENTE LIGADA
# =============================================================================
print("\n6. LISTA DUPLAMENTE LIGADA")
print("-" * 40)

class Node:
    """Classe para nó de lista duplamente ligada"""
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class ListaDuplamenteLigada:
    """Implementação de lista duplamente ligada"""
    def __init__(self):
        self.head = None
        self.tail = None

    def inserir_inicio(self, key, data):
        """Insere elemento no início"""
        novo_node = Node(key, data)
        if not self.head:
            self.head = self.tail = novo_node
        else:
            novo_node.next = self.head
            self.head.prev = novo_node
            self.head = novo_node

    def inserir_fim(self, key, data):
        """Insere elemento no fim"""
        novo_node = Node(key, data)
        if not self.tail:
            self.head = self.tail = novo_node
        else:
            novo_node.prev = self.tail
            self.tail.next = novo_node
            self.tail = novo_node

    def excluir_inicio(self):
        """Remove elemento do início"""
        if not self.head:
            return None

        removido = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        return removido.data

    def excluir_fim(self):
        """Remove elemento do fim"""
        if not self.tail:
            return None

        removido = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removido.data

    def imprimir_frente(self):
        """Imprime lista do início ao fim"""
        atual = self.head
        elementos = []
        while atual:
            elementos.append(f"{atual.key}:{atual.data}")
            atual = atual.next
        print(f"Frente para trás: {' -> '.join(elementos)}")

    def imprimir_tras(self):
        """Imprime lista do fim ao início"""
        atual = self.tail
        elementos = []
        while atual:
            elementos.append(f"{atual.key}:{atual.data}")
            atual = atual.prev
        print(f"Trás para frente: {' -> '.join(elementos)}")

# Simulação de 6 operações
lista_dupla = ListaDuplamenteLigada()

print("Operação 1: Inserir no início (1, 'primeiro')")
lista_dupla.inserir_inicio(1, 'primeiro')
lista_dupla.imprimir_frente()

print("Operação 2: Inserir no fim (2, 'segundo')")
lista_dupla.inserir_fim(2, 'segundo')
lista_dupla.imprimir_frente()

print("Operação 3: Inserir no início (0, 'zero')")
lista_dupla.inserir_inicio(0, 'zero')
lista_dupla.imprimir_frente()

print("Operação 4: Inserir no fim (3, 'terceiro')")
lista_dupla.inserir_fim(3, 'terceiro')
lista_dupla.imprimir_frente()

print("Operação 5: Excluir do início")
removido = lista_dupla.excluir_inicio()
print(f"Removido: {removido}")
lista_dupla.imprimir_frente()

print("Operação 6: Excluir do fim")
removido = lista_dupla.excluir_fim()
print(f"Removido: {removido}")
lista_dupla.imprimir_frente()
lista_dupla.imprimir_tras()

# =============================================================================
# PARTE 7 - HASHING COM ENCADEAMENTO SEPARADO
# =============================================================================
print("\n7. HASHING COM ENCADEAMENTO SEPARADO")
print("-" * 40)

class HashTable:
    """Implementação de tabela hash com encadeamento"""
    def __init__(self, tamanho=7):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, key):
        """Função hash simples"""
        return key % self.tamanho

    def insert(self, key):
        """Insere uma chave na tabela"""
        indice = self._hash(key)
        if key not in self.tabela[indice]:
            self.tabela[indice].append(key)

    def delete(self, key):
        """Remove uma chave da tabela"""
        indice = self._hash(key)
        if key in self.tabela[indice]:
            self.tabela[indice].remove(key)

    def display(self):
        """Exibe a tabela hash"""
        for i, lista in enumerate(self.tabela):
            print(f"Índice {i}: {lista}")

# Inserir [5, 12, 67, 9, 16], excluir 12 e exibir
hash_table = HashTable()
valores = [5, 12, 67, 9, 16]

print(f"Inserindo valores: {valores}")
for valor in valores:
    hash_table.insert(valor)

print("Tabela após inserções:")
hash_table.display()

print("\nExcluindo 12:")
hash_table.delete(12)
hash_table.display()

# =============================================================================
# PARTE 8 - CONDICIONAIS COM LISTAS
# =============================================================================
print("\n8. CONDICIONAIS COM LISTAS")
print("-" * 40)

# Comparação de dois valores
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 > valor2:
    print(f"{valor1} é maior que {valor2}")
elif valor2 > valor1:
    print(f"{valor2} é maior que {valor1}")
else:
    print("Os valores são iguais")

# Cálculo de média e aprovação
print("\nDigite 5 notas (entre 0 e 10):")
notas = []
for i in range(5):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
status = "Aprovado" if media >= 7.0 else "Reprovado"

print(f"\nNotas: {notas}")
print(f"Média: {media:.2f}")
print(f"Status: {status}")

# =============================================================================
# REFLEXÃO FINAL
# =============================================================================
print("\n" + "=" * 60)
print("REFLEXÃO FINAL")
print("=" * 60)

reflexao = """
Durante esta atividade, o maior desafio foi implementar a lista duplamente ligada
mantendo as referências corretas entre os nós. Esses conceitos são fundamentais
para resolver problemas reais como sistemas de cache (usando hash tables),
histórico de navegação (usando pilhas), filas de processamento em sistemas
distribuídos, e estruturas de índices em bancos de dados (usando árvores).
Gostaria de aprofundar mais o estudo de árvores balanceadas (AVL, Red-Black)
pois são cruciais para otimização de consultas. Esses conceitos se conectam
diretamente com decisões de negócios ao permitir análises mais rápidas de
grandes volumes de dados e automação de processos que requerem estruturas
eficientes para tomada de decisões em tempo real.
"""

print(reflexao)
print("\nAtividade concluída com sucesso!")
