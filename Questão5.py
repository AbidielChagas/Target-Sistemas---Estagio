# Função para inverter a string
def inverter_string(s):
    invertida = ""
    # Itera sobre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

# Solicitar ao usuário para inserir uma string
entrada = input("Informe uma string: ")

# Chamar a função e exibir a string invertida
resultado = inverter_string(entrada)
print(f"String invertida: {resultado}")
