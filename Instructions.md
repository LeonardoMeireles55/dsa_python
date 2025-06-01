# PROPOSTA DE ATIVIDADE – ESTRUTURA DE DADOS EM ANALÍTICA

## ATIVIDADE FINAL

### Conhecimentos necessários para o desenvolvimento da Atividade:

Para realizar esta atividade, o estudante deverá mobilizar os seguintes conhecimentos desenvolvidos ao longo dos Percursos de Aprendizagem 1, 2, 3 e 4:

- **Manipulação de listas em Python:**
  - Criação de listas.
  - Métodos: `.append()`, `.pop()`, `.count()`, `.index()`, `.sort()` e `.remove()`.
  - Compreensão do funcionamento de estruturas lineares como vetores.

- **Lógica de busca e estruturas de controle:**
  - Implementação de busca sequencial.
  - Utilização de estruturas condicionais (if, else) para controle de fluxo.

- **Funções recursivas:**
  - Construção de funções que chamam a si mesmas (recursão).
  - Aplicações clássicas como cálculo de fatorial e sequência de Fibonacci.

- **Estruturas de dados abstratas (TADs):**
  - Árvores binárias: inserção ordenada e travessia in-order.
  - Pilhas (LIFO) e filas (FIFO): inserção e remoção de elementos com listas.
  - Listas duplamente ligadas: operações de inserção, remoção e navegação bidirecional.

- **Hashing com encadeamento:**
  - Compreensão da lógica de distribuição de dados por função hash.
  - Implementação de tabela hash com tratamento de colisões por listas encadeadas.

- **Entrada de dados e validações:**
  - Leitura de dados com `input()`.
  - Conversão de tipos de dados (int, float) e uso de try-except para segurança opcional.

- **Programação aplicada à análise de dados:**
  - Interpretação e solução de problemas práticos.
  - Capacidade de decompor problemas em partes menores e estruturadas.

Esses conhecimentos combinados proporcionam uma base sólida para a construção de soluções eficientes em programação analítica de negócios, promovendo o raciocínio lógico, a organização de dados e a tomada de decisões orientada por estruturas computacionais eficientes.

### Objetivo da proposta da Atividade:

A presente atividade tem como objetivo consolidar os conhecimentos desenvolvidos ao longo dos quatro Percursos de Aprendizagem da disciplina Estrutura de Dados Analítica, por meio da aplicação prática de estruturas de dados fundamentais em Python.

Espera-se que o estudante seja capaz de:

- Compreender e implementar listas, filas, pilhas, árvores binárias e tabelas hash;
- Utilizar métodos e funções nativas do Python para manipulação de dados em diferentes contextos;
- Aplicar a lógica condicional e a recursividade para resolver problemas computacionais clássicos;
- Reconhecer a importância da escolha adequada da estrutura de dados para a eficiência do algoritmo;
- Desenvolver soluções estruturadas e contextualizadas em situações do cotidiano e da análise de negócios;
- Refletir criticamente sobre os desafios enfrentados, conectando teoria e prática no uso das estruturas abordadas.

Ao final da atividade, o aluno deverá demonstrar domínio técnico e raciocínio lógico ao estruturar algoritmos funcionais, organizados e aplicáveis a diferentes cenários de resolução de problemas com dados.

### Descrição da atividade:

Nesta atividade, os alunos irão desenvolver um projeto prático utilizando a linguagem Python, aplicando conceitos fundamentais das estruturas de dados abordadas nos quatro Percursos de Aprendizagem da disciplina Estrutura de Dados Analítica. A proposta é integrar estruturas como listas, pilhas, filas, árvores binárias, funções recursivas e tabelas hash com encadeamento para resolver problemas estruturados de forma lógica e progressiva.

- A atividade será realizada em equipes de 4 até 6 integrantes, com o objetivo de exercitar a autonomia na construção de soluções computacionais aplicadas à análise de dados. Cada participante deverá desenvolver um conjunto de scripts em Python que simulem situações práticas como buscas em vetores, cálculos recursivos, navegação em árvores, organização de dados em filas e pilhas, manipulação de listas duplamente ligadas e armazenamento eficiente com uso de hash.

- O desenvolvimento da atividade será dividido em oito partes, correspondentes aos quatro percursos de aprendizagem:
  1. **Vetores e Buscas:** Criação de um vetor com números aleatórios e implementação de busca sequencial.
  2. **Funções Recursivas:** Códigos para cálculo de fatorial e sequência de Fibonacci usando recursão.
  3. **Árvore Binária Simples:** Implementação de árvore binária com inserção ordenada e travessia in-order.
  4. **Pilha e Fila:** Simulação de inserção e remoção em pilhas (LIFO) e filas (FIFO) utilizando listas.
  5. **Listas e Métodos:** Aplicação de métodos como `.append()`, `.pop()`, `.count()`, `.index()`, `.sort()` e `.remove()` em uma lista de frutas.
  6. **Lista Duplamente Ligada:** Criação de uma estrutura que permita inserções e exclusões em diferentes posições.
  7. **Tabela Hash com Encadeamento:** Implementação de uma hash table com tratamento de colisões por listas encadeadas.
  8. **Condicionais e Listas:** Aplicação de estruturas condicionais para comparação de valores e cálculo de média com feedback de aprovação.

- Ao final da atividade, os alunos deverão refletir sobre os principais desafios encontrados, relacionando as estruturas de dados aplicadas com problemas reais enfrentados em contextos de negócios, análise de dados e automação de processos computacionais.

## Passo a passo para desenvolvimento da atividade:

- Formar equipes de 4 até 6 integrantes.

### Parte 1 – Vetores e Busca Sequencial

Os alunos deverão criar um vetor de inteiros e aplicar uma lógica de busca:

- Criar um arquivo Python chamado `atividade_final.py`.
- Gerar uma lista com 10 números aleatórios entre 1 e 100 utilizando `random.sample()`.
- Solicitar ao usuário um número inteiro e realizar a busca sequencial no vetor.
- Exibir se o número foi encontrado e sua posição, ou uma mensagem informando que o número não está presente.
- Refletir sobre a diferença de tempo ao buscar um elemento no início, meio ou fim do vetor.

### Parte 2 – Funções Recursivas

Os alunos devem implementar e testar dois algoritmos clássicos recursivos:

- Implementar `fatorial(n)` para retornar o fatorial de n.
- Implementar `fibonacci(n)` para retornar o n-ésimo número da sequência de Fibonacci.
- Testar as funções com `fatorial(5)` e `fibonacci(6)`.
- Exibir os resultados no console e comparar com os valores esperados.

### Parte 3 – Árvore Binária Simples

Os Alunos devem implementar uma estrutura de dados do tipo árvore:

- Criar uma classe `Nó` com os atributos `valor`, `esquerda` e `direita`.
- Escrever uma função `inserir(raiz, valor)` que insira os elementos mantendo a propriedade de ordem da árvore binária de busca.
- Inserir os valores: 10, 5, 15, 3, 8.
- Implementar uma função `em_ordem(raiz)` para imprimir os valores ordenados.
- Mostrar o resultado da travessia no terminal.

### Parte 4 – Pilha e Fila com Listas

Simulação das estruturas de pilha (LIFO) e fila (FIFO):

- **PILHA:** Criar uma lista `[1, 1, 2, 3, 5]`, adicionar dois elementos com `.append()` e remover com `.pop()`.
- **FILA:** Criar uma lista `[20, 30, 40, 50, 60]`, adicionar 99 com `.append()` e remover três elementos com `.pop(0)`.
- Explicar, ao final, a diferença entre pilha (último a entrar, primeiro a sair) e fila (primeiro a entrar, primeiro a sair).

### Parte 5 – Listas e Métodos

Manipulação prática com os métodos de lista:

- Criar uma lista chamada `frutas` com os elementos: `['banana', 'maçã', 'kiwi', 'banana', 'pera', 'maçã', 'laranja']`.
- Aplicar os métodos:
  - `.count('maçã')`
  - `.index('banana')` e `.index('banana', 4)`
  - `.append('uva')`
  - `.sort()`
  - `.pop()`
- Exibir o resultado após cada operação.
- Escrever uma explicação com suas palavras sobre a utilidade de cada método.

### Parte 6 – Lista Duplamente Ligada

Implementar uma estrutura personalizada para inserção e exclusão de elementos:

- Criar a classe `Node` com os atributos `key`, `data`, `prev`, `next`.
- Implementar os métodos:
  - Inserção no início e no fim
  - Exclusão do início e do fim
  - Inserção após uma chave específica
  - Exclusão de um elemento com base em uma chave
  - Impressão da lista do início ao fim e do fim ao início
- Simular ao menos 6 operações e exibir a estrutura da lista a cada passo.

### Parte 7 – Hashing com Encadeamento Separado

Criar uma tabela hash simples com listas para tratar colisões:

- Criar uma classe `HashTable` com tamanho fixo.
- Implementar:
  - `insert(key)`
  - `delete(key)`
  - `display()`
- Inserir os itens `[5, 12, 67, 9, 16]`, excluir 12 e exibir a tabela resultante.

### Parte 8 – Condicionais com Listas

Exercício prático com estruturas de decisão e listas:

- Solicitar dois valores inteiros do usuário e verificar qual é maior, exibindo no console.
- Solicitar cinco notas (entre 0 e 10), calcular a média e informar se o aluno foi "Aprovado" ou "Reprovado" com base na média ≥ 7.0.
- Exibir mensagens formatadas com base nas decisões.

### Parte Final – Reflexão Escrita

Ao final do notebook/script, os alunos devem escrever uma pequena reflexão (mínimo de 5 linhas) respondendo:

- O que foi mais desafiador?
- Como esses conceitos podem ser usados em problemas reais?
- Que estrutura você gostaria de aprofundar mais?
- Como isso se conecta com decisões de negócios ou sistemas automatizados?

## Orientações para envio da atividade:

- **Formato de entrega:** O arquivo final da atividade deve ser enviado em formato PDF contendo toda a documentação do projeto.
- **Código-fonte:** Além do documento em PDF, deve ser enviado o arquivo do código Python (.py), contendo toda a implementação do projeto.
- **Identificação da equipe:** O PDF deve conter na capa os seguintes dados de cada integrante da equipe:
  - Nome completo
  - Número de matrícula
  - Turma
- **Forma de envio:** O envio deve ser realizado por todos os membros da equipe na plataforma de submissão, para fins de correção.
- **Quantidade de arquivos:** Cada equipe deverá submeter dois arquivos:
  - Documento PDF com a descrição e explicação do código.
  - Arquivo Python (projeto.py) com a implementação do projeto.
- **Estrutura do PDF:** O documento deve conter:
  - Introdução explicando o objetivo do projeto.
  - Desenvolvimento detalhando cada parte da implementação.
  - Conclusão com uma reflexão sobre o aprendizado da equipe.
  - Trechos de código explicativos, quando necessário.
- **Disponibilização de arquivo base:** Caso necessário, será disponibilizado um modelo de estrutura para auxiliar os alunos na organização do projeto.

## Critérios a serem avaliados:

A atividade será avaliada com base nos seguintes critérios:

### 1. Manipulação de Vetores, Listas e Métodos (Percursos 1 e 2) – 1,0 ponto

✔ Criação de listas e aplicação de métodos (`.append`, `.pop`, `.count`, `.sort`, etc.) de forma adequada – (0,5 pt)

✔ Implementação correta da busca sequencial e exibição estruturada dos dados – (0,5 pt)

### 2. Funções Recursivas e Aplicações Matemáticas (Percurso 1) – 0,5 ponto

✔ Implementação correta das funções `fatorial()` e `fibonacci()` – (0,25 pt)

✔ Testes realizados e resultados apresentados corretamente – (0,25 pt)

### 3. Estruturas de Dados Abstratas – Árvore Binária, Pilha e Fila (Percursos 2 e 3) – 1,0 ponto

✔ Implementação da árvore binária com inserção ordenada e travessia in-order – (0,5 pt)

✔ Simulação correta de pilha (LIFO) e fila (FIFO) utilizando listas – (0,5 pt)

### 4. Lista Duplamente Ligada e Hashing com Encadeamento (Percurso 3 e 4) – 1,0 ponto

✔ Operações de inserção, exclusão e navegação em lista duplamente ligada implementadas corretamente – (0,5 pt)

✔ Implementação funcional de tabela hash com encadeamento e manipulação de dados – (0,5 pt)

### 5. Condicionais, Média e Decisões com Listas (Percurso 4) – 0,5 ponto

✔ Código de comparação entre dois números e cálculo de média com decisão Aprovado/Reprovado funcionando corretamente – (0,5 pt)

### 6. Reflexão Final, Organização e Documentação – 1,0 ponto

✔ Reflexão escrita final completa e coerente (mínimo de 5 linhas) – (0,5 pt)

✔ Clareza, organização e indentação correta no código Python / Notebook – (0,25 pt)

✔ Documento PDF bem estruturado e explicativo (quando aplicável) – (0,25 pt)

---

**Atenção:** A nota final será atribuída com base na correta aplicação dos conceitos, na organização do trabalho e na clareza das explicações no documento PDF.

**Total de pontuação:** 5,0 pts.

**Prazo para envio da atividade:** 02/06/2025