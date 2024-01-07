compraconfirmada = False 
dados_comrpa = 'Compra no valor de 12 confirmada'


for enviar in range(3):
    if compraconfirmada:
        print(dados_comrpa)
        break 
else:
    print('deu falha')