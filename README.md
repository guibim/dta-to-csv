# Conversor de Arquivos `.dta` para `.csv`

Este projeto fornece um script simples em Python para converter arquivos no formato
Stata (`.dta`) para o formato `.csv`, amplamente usado em análises estatísticas,
planilhas e softwares diversos.

O script funciona automaticamente usando a **pasta Downloads do Windows** como
local padrão de entrada e saída.

---
## Requisitos

Instale o Python e as bibliotecas necessárias:

pip install pandas pyreadstat

## Como usar

1. Coloque seu arquivo `.dta` na pasta **Downloads** do Windows.

2. Edite o script e substitua:
   ```python
   entrada_nome = "xxxxx.dta"
   saida_nome = "xxxxx.csv"

Execute o script:

python converter.py

O arquivo .csv será gerado automaticamente na pasta Downloads.
