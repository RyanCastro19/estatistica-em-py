import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados extraídos da tabela
data = {
    "Estado civil": [
        "solteiro", "casado", "casado", "solteiro", "solteiro", "casado", "solteiro", "casado",
        "solteiro", "solteiro", "casado", "solteiro", "solteiro", "solteiro", "casado", "solteiro",
        "solteiro", "ensino fundamental", "ensino médio", "ensino fundamental", "ensino médio", "ensino médio",
        "ensino fundamental", "ensino superior", "ensino médio", "ensino médio", "ensino médio", "ensino fundamental",
        "ensino médio", "ensino médio", "ensino superior", "ensino médio", "ensino superior", "ensino superior", "ensino médio",
        "ensino superior"
    ],
    "Grau de instrução": [
        "ensino fundamental", "ensino fundamental", "ensino fundamental", "ensino fundamental", "ensino fundamental",
        "ensino fundamental", "ensino fundamental", "ensino fundamental", "ensino médio", "ensino fundamental",
        "ensino médio", "ensino fundamental", "ensino médio", "ensino fundamental", "ensino médio", "ensino médio",
        "ensino fundamental", "ensino fundamental", "ensino médio", "ensino fundamental", "ensino médio", "ensino médio",
        "ensino fundamental", "ensino superior", "ensino médio", "ensino médio", "ensino médio", "ensino fundamental",
        "ensino médio", "ensino médio", "ensino superior", "ensino médio", "ensino superior", "ensino superior", "ensino médio",
        "ensino superior"
    ],
    "N° de filhos": [
        2, 1, 1, 0, 1, 0, 1, 2, 1, 0, 2, 1, 1, 3, 3, 0, 2, 2, 1, 1, 0, 0, 0, 2, 3, 3, 1, 1, 2, 2, 3, 0, 3, 3, 2, 2
    ],
    "Salário (x sal. mín.)": [
        4.00, 4.56, 5.20, 5.73, 6.26, 6.72, 6.91, 7.23, 7.54, 7.88, 8.12, 8.15, 8.23, 9.01, 9.35, 9.77, 9.80, 9.80,
        10.00, 10.12, 11.00, 11.09, 11.59, 12.79, 13.65, 13.80, 14.03, 14.77, 15.09, 16.12, 16.23, 17.65, 17.76, 19.22,
        20.00, 23.30
    ],
    "Idade (anos)": [
        26, 32, 30, 22, 28, 43, 31, 40, 33, 25, 23, 44, 37, 29, 38, 24, 39, 39, 32, 43, 33, 42, 36, 26, 40, 29, 27, 29,
        29, 35, 31, 34, 38, 48, 33, 33
    ],
    "Idade (meses)": [
        6, 3, 11, 4, 7, 0, 11, 3, 10, 1, 6, 8, 5, 11, 5, 7, 7, 7, 7, 0, 5, 0, 8, 1, 4, 5, 8, 5, 11, 1, 5, 7, 7, 2, 10, 12
    ],
    "Região de procedência": [
        "interior", "interior", "capital", "outra", "interior", "outra", "capital", "interior", "capital", "interior",
        "interior", "capital", "outra", "outra", "interior", "capital", "interior", "outra", "capital", "capital",
        "interior", "capital", "outra", "capital", "interior", "capital", "interior", "outra", "capital", "outra",
        "interior", "capital", "capital", "capital", "capital", "interior"
    ]
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Calcular as distribuições de frequência
freq_estado_civil = df["Estado civil"].value_counts()
freq_grau_instrucao = df["Grau de instrução"].value_counts()
freq_n_filhos = df["N° de filhos"].value_counts()
freq_salario = df["Salário (x sal. mín.)"].value_counts(bins=10)  # Agrupando os salários em 10 intervalos
freq_idade = df["Idade (anos)"].value_counts(bins=10)  # Agrupando as idades em 10 intervalos
freq_regiao = df["Região de procedência"].value_counts()

# Plotar os gráficos
plt.figure(figsize=(15, 20))

plt.subplot(3, 2, 1)
sns.barplot(x=freq_estado_civil.index, y=freq_estado_civil.values)
plt.title('Distribuição de Frequência - Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Frequência')

plt.subplot(3, 2, 2)
sns.barplot(x=freq_grau_instrucao.index, y=freq_grau_instrucao.values)
plt.title('Distribuição de Frequência - Grau de Instrução')
plt.xlabel('Grau de Instrução')
plt.ylabel('Frequência')

plt.subplot(3, 2, 3)
sns.barplot(x=freq_n_filhos.index, y=freq_n_filhos.values)
plt.title('Distribuição de Frequência - Número de Filhos')
plt.xlabel('Número de Filhos')
plt.ylabel('Frequência')

plt.subplot(3, 2, 4)
sns.barplot(x=freq_salario.index.astype(str), y=freq_salario.values)
plt.title('Distribuição de Frequência - Salário (x sal. mín.)')
plt.xlabel('Salário (Intervalos)')
plt.ylabel('Frequência')

plt.subplot(3, 2, 5)
sns.barplot(x=freq_idade.index.astype(str), y=freq_idade.values)
plt.title('Distribuição de Frequência - Idade (anos)')
plt.xlabel('Idade (Intervalos)')
plt.ylabel('Frequência')

plt.subplot(3, 2, 6)
sns.barplot(x=freq_regiao.index, y=freq_regiao.values)
plt.title('Distribuição de Frequência - Região de Procedência')
plt.xlabel('Região de Procedência')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()
