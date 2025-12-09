import os
import pandas as pd

# Caminho da pasta Downloads no Windows
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Preencha o nome dos arquivos
entrada_nome = "xxxxx.dta"
saida_nome = "xxxxx.csv"

# Caminhos completos
caminho_entrada = os.path.join(downloads, entrada_nome)
caminho_saida = os.path.join(downloads, saida_nome)

print(f"Lendo arquivo: {caminho_entrada}")

# Ler arquivo .dta
df = pd.read_stata(caminho_entrada)

# Converter para CSV
df.to_csv(caminho_saida, index=False)

print("✔ Conversão concluída!")
print(f"CSV criado em: {caminho_saida}")
