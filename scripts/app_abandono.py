# Script para analizar abandono de clientes
# Prueba escritura desde VSC

df['segmento_valor'] = pd.qcut(df['valor'], 3, labels=['bajo', 'medio', 'alto']) 