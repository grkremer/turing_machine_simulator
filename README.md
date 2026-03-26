# Simulador de Máquina de Turing

Este repositório contém um simulador e scripts de teste automatizado para programas em Máquinas de Turing, escritos em Python.

## Máquinas de Turing Originais

Os arquivos de extensão `.mt` usados neste simulador são gerados utilizando o seguinte **Simulador de Máquina de Turing** (utilizado pela disciplina):

🔗 [http://www.inf.ufrgs.br/~rma/simuladores/turing.html](http://www.inf.ufrgs.br/~rma/simuladores/turing.html)

## ⚠️ Instrução Importante de Uso

Note que os arquivos `.mt` implementados não estão versionados no repositório (foram ignorados no `.gitignore` por motivos de plágio acadêmico e para não serem copiados por colegas).

Para que o simulador ou os testes funcionem, **você deve colocar os seus próprios arquivos `.mt` (ex: `1a.mt`, `1b.mt`, `2.mt`, etc.) na raiz deste diretório**.

## Como executar o Simulador (`turing_machine.py`)

Você pode simular o comportamento passo-a-passo de uma de suas máquinas de Turing a partir de uma palavra da sua escolha fornecendo o nome do arquivo `.mt` e a entrada (string).

```cmd
python turing_machine.py <arquivo.mt> [fita_entrada]

# Exemplo
python turing_machine.py 1a.mt uu
```

A saída irá demonstrar se a máquina ACEITOU ou REJEITOU a cadeia e imprimirá o estado final da fita.

## Como executar e configurar os Testes (`test_cases.py`)

O script de testes gerado e já incluído (`test_cases.py`) foi estruturado especificamente com exemplos e validações do trabalho e problemas da disciplina referente ao semestre **2026/1**.

Para rodar todos os testes contra as suas máquinas, execute:

```cmd
python test_cases.py
```

Isso mostrará quais testes as máquinas passaram, informando as fitas em formato final de simulação e fornecendo o percentual de acerto total da lista!

### Como gerar seus próprios casos de teste

Caso você queira adicionar mais testes ou utilizar esse projeto para testar exercícios futuros, basta editar o código do `test_cases.py`. Funciona através de um dicionário (`test_cases`) onde a **chave** é o nome do seu arquivo `.mt` e os **valores** definem as premissas dependendo do exercício:

- **Se a máquina processa uma string com limite matemático ou operações:** Insira no formato de tupla `("Entrada da Fita", "Saída Esperada após execução")`.
- **Se a máquina testa aceitação/rejeição de linguagem (sem alterar o valor da fita):** O segundo argumento da tupla deve ser um booleano: `("Cadeia testada", True)` ou `False`.

Sinta-se livre para usar o sistema implementado e adicionar ou remover casos de teste!
