# Dados
ingles = ['A', 'B', 'C', 'D']
frequencia_ingles = [3, 14, 5, 3]

# Gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(ingles, frequencia_ingles, color=['red', 'blue', 'green', 'purple'])
plt.xlabel('Inglês')
plt.ylabel('Frequência')
plt.title('Frequência dos Funcionários por Grau de Inglês')
plt.grid(axis='y')

# Exibir gráfico
plt.show()
