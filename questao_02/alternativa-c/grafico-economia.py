# Dados
intervalos_economia = ['4.0 - 4.9', '5.0 - 5.9', '6.0 - 6.9', '7.0 - 7.9', '8.0 - 8.9', '9.0 - 9.9']
frequencia_economia = [1, 0, 3, 7, 7, 7]

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(intervalos_economia, frequencia_economia, color='lightcoral')
plt.xlabel('Nota em Economia')
plt.ylabel('Frequência')
plt.title('Frequência dos Funcionários por Nota em Economia')
plt.grid(axis='y')

# Exibir gráfico
plt.show()
