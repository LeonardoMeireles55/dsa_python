#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ATIVIDADE FINAL - ESTRUTURA DE DADOS EM ANALÍTICA (VERSÃO COLORIDA)
"""

import random

# =============================================================================
# CLASSE PARA CORES NO TERMINAL (ANSI ESCAPE CODES)
# =============================================================================
class Cores:
    """Códigos ANSI para colorir texto no terminal"""
    # Cores do texto
    PRETO = '\033[30m'
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'
    BRANCO = '\033[37m'

    # Cores brilhantes
    VERMELHO_BRILHANTE = '\033[91m'
    VERDE_BRILHANTE = '\033[92m'
    AMARELO_BRILHANTE = '\033[93m'
    AZUL_BRILHANTE = '\033[94m'
    MAGENTA_BRILHANTE = '\033[95m'
    CIANO_BRILHANTE = '\033[96m'

    # Estilos
    NEGRITO = '\033[1m'
    SUBLINHADO = '\033[4m'
    PISCANDO = '\033[5m'

    # Reset (volta ao normal)
    RESET = '\033[0m'

    @staticmethod
    def colorir(texto, cor):
        """Aplica cor ao texto e reseta no final"""
        return f"{cor}{texto}{Cores.RESET}"

    @staticmethod
    def sucesso(texto):
        """Texto de sucesso (verde)"""
        return Cores.colorir(texto, Cores.VERDE_BRILHANTE)

    @staticmethod
    def erro(texto):
        """Texto de erro (vermelho)"""
        return Cores.colorir(texto, Cores.VERMELHO_BRILHANTE)

    @staticmethod
    def aviso(texto):
        """Texto de aviso (amarelo)"""
        return Cores.colorir(texto, Cores.AMARELO_BRILHANTE)

    @staticmethod
    def info(texto):
        """Texto informativo (azul)"""
        return Cores.colorir(texto, Cores.AZUL_BRILHANTE)

    @staticmethod
    def titulo(texto):
        """Título destacado (ciano + negrito)"""
        return Cores.colorir(texto, Cores.CIANO_BRILHANTE + Cores.NEGRITO)

print(Cores.titulo("=" * 60))
print(Cores.titulo("ATIVIDADE FINAL - ESTRUTURA DE DADOS"))
print(Cores.titulo("=" * 60))

# =============================================================================
# PARTE 1 - VETORES E BUSCA SEQUENCIAL
# =============================================================================
print("\n" + Cores.colorir("1. VETORES E BUSCA SEQUENCIAL", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

# Gerar lista com 10 números aleatórios entre 1 e 100
vetor = random.sample(range(1, 101), 10)
print(f"Vetor gerado: {Cores.colorir(str(vetor), Cores.CIANO)}")

def busca_sequencial(lista, elemento):
    """Realiza busca sequencial em uma lista"""
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

# Solicitar número para busca
numero_busca = int(input(Cores.colorir("Digite um número para buscar: ", Cores.AMARELO)))
posicao = busca_sequencial(vetor, numero_busca)

if posicao != -1:
    print(Cores.sucesso(f"✅ Número {numero_busca} encontrado na posição {posicao}"))
else:
    print(Cores.erro(f"❌ Número {numero_busca} não encontrado no vetor"))

# =============================================================================
# PARTE 2 - FUNÇÕES RECURSIVAS
# =============================================================================
print("\n" + Cores.colorir("2. FUNÇÕES RECURSIVAS", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

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

num_fatorial = int(input(Cores.colorir("Digite um número para calcular o fatorial: ", Cores.AMARELO)))
resultado_fatorial = fatorial(num_fatorial)
print(Cores.info(f"🧮 Fatorial de {num_fatorial}: {Cores.colorir(str(resultado_fatorial), Cores.VERDE_BRILHANTE)}"))

num_fibonacci = int(input(Cores.colorir("Digite um número para calcular o Fibonacci: ", Cores.AMARELO)))
resultado_fibonacci = fibonacci(num_fibonacci)
print(Cores.info(f"🔢 Fibonacci de {num_fibonacci}: {Cores.colorir(str(resultado_fibonacci), Cores.VERDE_BRILHANTE)}"))

# =============================================================================
# PARTE 3 - ÁRVORE BINÁRIA SIMPLES
# =============================================================================
print("\n" + Cores.colorir("3. ÁRVORE BINÁRIA SIMPLES", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

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
        print(Cores.colorir(str(raiz.valor), Cores.VERDE_BRILHANTE), end=" ")
        em_ordem(raiz.direita)

print(Cores.colorir("Digite os números para inserir na árvore (separados por vírgula):", Cores.AMARELO))
nums_arvore = input(Cores.colorir("Números: ", Cores.CIANO)).split(',')

nums_arvore = [int(num.strip()) for num in nums_arvore if num.strip().isdigit()]

arvore = None
valores = nums_arvore
for valor in valores:
    arvore = inserir(arvore, valor)

print(f"Valores inseridos: {Cores.colorir(str(valores), Cores.CIANO)}")
print(Cores.colorir("🌳 Travessia em ordem: ", Cores.MAGENTA_BRILHANTE), end="")
em_ordem(arvore)
print()

# =============================================================================
# PARTE 4 - PILHA E FILA COM LISTAS
# =============================================================================
print("\n" + Cores.colorir("4. PILHA E FILA COM LISTAS", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

# PILHA (LIFO)
print(Cores.colorir("📚 PILHA (LIFO):", Cores.MAGENTA_BRILHANTE))
print(Cores.colorir("Digite os valores iniciais da pilha (separados por vírgula):", Cores.AMARELO))
valores_pilha = input(Cores.colorir("Valores: ", Cores.CIANO)).split(',')
pilha = [int(val.strip()) for val in valores_pilha if val.strip().isdigit()]
print(f"Pilha inicial: {Cores.colorir(str(pilha), Cores.CIANO)}")

print(Cores.colorir("Digite dois números para adicionar à pilha:", Cores.AMARELO))
num1 = int(input(Cores.colorir("Primeiro número: ", Cores.CIANO)))
num2 = int(input(Cores.colorir("Segundo número: ", Cores.CIANO)))

pilha.append(num1)
pilha.append(num2)
print(f"Após adicionar {num1} e {num2}: {Cores.colorir(str(pilha), Cores.VERDE)}")

removido = pilha.pop()
print(f"Após remover {Cores.colorir(str(removido), Cores.VERMELHO)}: {Cores.colorir(str(pilha), Cores.VERDE)}")

# FILA (FIFO)
print("\n" + Cores.colorir("🎯 FILA (FIFO):", Cores.MAGENTA_BRILHANTE))
print(Cores.colorir("Digite os valores iniciais da fila (separados por vírgula):", Cores.AMARELO))
valores_fila = input(Cores.colorir("Valores: ", Cores.CIANO)).split(',')
fila = [int(val.strip()) for val in valores_fila if val.strip().isdigit()]
print(f"Fila inicial: {Cores.colorir(str(fila), Cores.CIANO)}")

elemento_fila = int(input(Cores.colorir("Digite um número para adicionar à fila: ", Cores.CIANO)))
fila.append(elemento_fila)
print(f"Após adicionar {elemento_fila}: {Cores.colorir(str(fila), Cores.VERDE)}")

num_remover = int(input(Cores.colorir("Quantos elementos deseja remover da fila? ", Cores.CIANO)))
elementos_removidos = []
for _ in range(min(num_remover, len(fila))):
    elementos_removidos.append(fila.pop(0))
print(f"Removidos: {Cores.colorir(str(elementos_removidos), Cores.VERMELHO)} -> Fila: {Cores.colorir(str(fila), Cores.VERDE)}")

print("\n" + Cores.info("💡 Diferença: Pilha = último a entrar, primeiro a sair"))
print(Cores.info("              Fila = primeiro a entrar, primeiro a sair"))

# =============================================================================
# PARTE 5 - LISTAS E MÉTODOS
# =============================================================================
print("\n" + Cores.colorir("5. LISTAS E MÉTODOS", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

print(Cores.colorir("Digite as frutas para a lista (separadas por vírgula):", Cores.AMARELO))
entrada_frutas = input(Cores.colorir("Frutas: ", Cores.CIANO)).split(',')
frutas = [fruta.strip() for fruta in entrada_frutas if fruta.strip()]
print(f"Lista inicial: {Cores.colorir(str(frutas), Cores.CIANO)}")

# .count()
fruta_contar = input(Cores.colorir("Digite uma fruta para contar quantas vezes aparece: ", Cores.AMARELO))
count_fruta = frutas.count(fruta_contar)
print(f"🔢 Quantidade de '{fruta_contar}': {Cores.colorir(str(count_fruta), Cores.VERDE_BRILHANTE)}")

# .index()
fruta_buscar = input(Cores.colorir("Digite uma fruta para encontrar sua primeira posição: ", Cores.AMARELO))
try:
    index_fruta = frutas.index(fruta_buscar)
    print(Cores.sucesso(f"📍 Primeira posição de '{fruta_buscar}': {index_fruta}"))

    # Buscar a partir de um índice específico
    indice_inicio = int(input(Cores.colorir(f"Digite um índice para buscar '{fruta_buscar}' a partir dele: ", Cores.AMARELO)))
    try:
        index_fruta_pos = frutas.index(fruta_buscar, indice_inicio)
        print(Cores.sucesso(f"📍 Posição de '{fruta_buscar}' a partir do índice {indice_inicio}: {index_fruta_pos}"))
    except ValueError:
        print(Cores.aviso(f"⚠️  Não há '{fruta_buscar}' a partir do índice {indice_inicio}"))
except ValueError:
    print(Cores.erro(f"❌ '{fruta_buscar}' não encontrada na lista"))

# .append()
nova_fruta = input(Cores.colorir("Digite uma fruta para adicionar à lista: ", Cores.AMARELO))
frutas.append(nova_fruta)
print(f"Após adicionar '{nova_fruta}': {Cores.colorir(str(frutas), Cores.VERDE)}")

# .sort()
frutas.sort()
print(f"📊 Após ordenar: {Cores.colorir(str(frutas), Cores.VERDE)}")

# .pop()
removido = frutas.pop()
print(f"Após remover último elemento '{Cores.colorir(removido, Cores.VERMELHO)}': {Cores.colorir(str(frutas), Cores.VERDE)}")

# =============================================================================
# PARTE 6 - LISTA DUPLAMENTE LIGADA
# =============================================================================
print("\n" + Cores.colorir("6. LISTA DUPLAMENTE LIGADA", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

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
        print(f"➡️  Frente para trás: {Cores.colorir(' -> '.join(elementos), Cores.CIANO)}")

    def imprimir_tras(self):
        """Imprime lista do fim ao início"""
        atual = self.tail
        elementos = []
        while atual:
            elementos.append(f"{atual.key}:{atual.data}")
            atual = atual.prev
        print(f"⬅️  Trás para frente: {Cores.colorir(' -> '.join(elementos), Cores.MAGENTA)}")

# Operações interativas com lista duplamente ligada
lista_dupla = ListaDuplamenteLigada()

print(Cores.colorir("🔗 Vamos realizar 6 operações na lista duplamente ligada:", Cores.MAGENTA_BRILHANTE))
for i in range(6):
    print(f"\n{Cores.colorir(f'Operação {i+1}:', Cores.AMARELO_BRILHANTE)}")
    print(Cores.colorir("1", Cores.VERDE) + " - Inserir no início")
    print(Cores.colorir("2", Cores.VERDE) + " - Inserir no fim")
    print(Cores.colorir("3", Cores.VERMELHO) + " - Excluir do início")
    print(Cores.colorir("4", Cores.VERMELHO) + " - Excluir do fim")

    opcao = int(input(Cores.colorir("Escolha uma operação (1-4): ", Cores.CIANO)))

    if opcao == 1:
        key = int(input(Cores.colorir("Digite a chave: ", Cores.AMARELO)))
        data = input(Cores.colorir("Digite o dado: ", Cores.AMARELO))
        lista_dupla.inserir_inicio(key, data)
        print(Cores.sucesso(f"✅ Inserido no início: {key}:{data}"))
    elif opcao == 2:
        key = int(input(Cores.colorir("Digite a chave: ", Cores.AMARELO)))
        data = input(Cores.colorir("Digite o dado: ", Cores.AMARELO))
        lista_dupla.inserir_fim(key, data)
        print(Cores.sucesso(f"✅ Inserido no fim: {key}:{data}"))
    elif opcao == 3:
        removido = lista_dupla.excluir_inicio()
        if removido:
            print(Cores.erro(f"❌ Removido do início: {removido}"))
        else:
            print(Cores.aviso("⚠️  Lista vazia, nada para remover"))
    elif opcao == 4:
        removido = lista_dupla.excluir_fim()
        if removido:
            print(Cores.erro(f"❌ Removido do fim: {removido}"))
        else:
            print(Cores.aviso("⚠️  Lista vazia, nada para remover"))

    lista_dupla.imprimir_frente()

print("\n" + Cores.titulo("📋 Estado final da lista:"))
lista_dupla.imprimir_frente()
lista_dupla.imprimir_tras()

# =============================================================================
# PARTE 7 - HASHING COM ENCADEAMENTO SEPARADO
# =============================================================================
print("\n" + Cores.colorir("7. HASHING COM ENCADEAMENTO SEPARADO", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

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
            cor = Cores.VERDE if lista else Cores.CINZA if hasattr(Cores, 'CINZA') else Cores.BRANCO
            print(f"📦 Índice {Cores.colorir(str(i), Cores.AMARELO)}: {Cores.colorir(str(lista), cor)}")

# Operações com tabela hash
tamanho_tabela = int(input(Cores.colorir("Digite o tamanho da tabela hash (recomendado: 7): ", Cores.AMARELO)))
hash_table = HashTable(tamanho_tabela)

print(Cores.colorir("Digite os valores (inteiros) para inserir na tabela hash (separados por vírgula):", Cores.AMARELO))
entrada_valores = input(Cores.colorir("Valores: ", Cores.CIANO)).split(',')
valores = [int(val.strip()) for val in entrada_valores if val.strip().isdigit()]

print(f"🔧 Inserindo valores: {Cores.colorir(str(valores), Cores.CIANO)}")
for valor in valores:
    hash_table.insert(valor)

print(Cores.titulo("\n📊 Tabela após inserções:"))
hash_table.display()

valor_excluir = int(input(Cores.colorir("\nDigite um valor para excluir da tabela: ", Cores.AMARELO)))
print(f"🗑️  Excluindo {Cores.colorir(str(valor_excluir), Cores.VERMELHO)}:")
hash_table.delete(valor_excluir)
hash_table.display()

# =============================================================================
# PARTE 8 - CONDICIONAIS COM LISTAS
# =============================================================================
print("\n" + Cores.colorir("8. CONDICIONAIS COM LISTAS", Cores.AZUL_BRILHANTE + Cores.NEGRITO))
print(Cores.colorir("-" * 40, Cores.AZUL))

# Comparação de dois valores
valor1 = int(input(Cores.colorir("Digite o primeiro valor: ", Cores.AMARELO)))
valor2 = int(input(Cores.colorir("Digite o segundo valor: ", Cores.AMARELO)))

if valor1 > valor2:
    print(Cores.sucesso(f"🏆 {valor1} é maior que {valor2}"))
elif valor2 > valor1:
    print(Cores.sucesso(f"🏆 {valor2} é maior que {valor1}"))
else:
    print(Cores.info(f"⚖️  Os valores são iguais ({valor1} = {valor2})"))

# Cálculo de média e aprovação
print(Cores.colorir("\n📝 Digite 5 notas (entre 0 e 10):", Cores.MAGENTA_BRILHANTE))
notas = []
for i in range(5):
    nota = float(input(Cores.colorir(f"Nota {i+1}: ", Cores.CIANO)))
    notas.append(nota)

media = sum(notas) / len(notas)
status = "Aprovado" if media >= 7.0 else "Reprovado"

print(f"\n📊 Notas: {Cores.colorir(str(notas), Cores.AZUL)}")
print(f"📈 Média: {Cores.colorir(f'{media:.2f}', Cores.AZUL)}")
status_color = Cores.VERDE_BRILHANTE if status == "Aprovado" else Cores.VERMELHO_BRILHANTE
emoji = "🎉" if status == "Aprovado" else "😔"
print(f"📋 Status: {Cores.colorir(f'{emoji} {status}', status_color)}")

# =============================================================================
# REFLEXÃO FINAL
# =============================================================================
print("\n" + Cores.titulo("=" * 60))
print(Cores.titulo("🤔 REFLEXÃO FINAL"))
print(Cores.titulo("=" * 60))

reflexao = """
Estruturas de dados são fundamentais para a organização e manipulação eficiente de dados.
Nesta atividade, exploramos diversas estruturas e técnicas, desde vetores e listas até árvores e tabelas hash.
Cada uma tem suas características, vantagens e desvantagens, dependendo do contexto de uso.
A prática com essas estruturas é essencial para desenvolver habilidades de programação e resolução de problemas.
Exemplos como arvores utilizadas em bancos de dados, tabelas hash em caches e listas ligadas em sistemas operacionais mostram a importância dessas estruturas no mundo real.
"""

print(Cores.colorir(reflexao, Cores.AZUL))
print("\n" + Cores.sucesso("🎉 Atividade concluída com sucesso!"))
print(Cores.titulo("=" * 60))
