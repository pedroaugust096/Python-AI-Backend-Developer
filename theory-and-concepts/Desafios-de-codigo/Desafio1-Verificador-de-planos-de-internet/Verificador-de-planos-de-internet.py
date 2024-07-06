# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_mensal):
    
# TODO: Crie uma Estrutura Condicional para verificar o consumo médio mensal:
  if 0 < consumo_mensal <= 10:
    mensagem = "Plano Essencial Fibra - 50Mbps"
  
  elif 10 < consumo_mensal <= 20:
    mensagem = "Plano Prata Fibra - 100Mbps"
  
  else:
    mensagem = "Plano Premium Fibra - 300Mbps"
    
# TODO: Retorne o plano de internet adequado:
  return mensagem

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Informe seu consumo médio mensal, em GB: "))

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))