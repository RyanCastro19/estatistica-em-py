import numpy as np

# Dados
intervalos_adm = ['6.0 - 6.9', '7.0 - 7.9', '8.0 - 8.9', '9.0 - 9.9', '10.0-10.9']
frequencia_adm = [3, 2, 11, 5, 4]

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(intervalos_adm, frequencia_adm, color='skyblue')
plt.xlabel('Nota em Administração')
plt.ylabel('Frequência')
plt.title('Frequência dos Funcionários por Nota em Administração')
plt.grid(axis='y')

# Exibir gráfico
plt.show()
