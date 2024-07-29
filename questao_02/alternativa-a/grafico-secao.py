import matplotlib.pyplot as plt

# Dados
secoes = ['P', 'T', 'V']
frequencia = [7, 6, 12]

# Gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(secoes, frequencia, color=['blue', 'green', 'orange'])
plt.xlabel('Seção')
plt.ylabel('Frequência')
plt.title('Frequência dos Funcionários por Seção')
plt.grid(axis='y')

# Exibir gráfico
plt.show()
