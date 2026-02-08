import random
from datetime import datetime, timedelta

def gerar_contratos():
    # 1. Configuração da massa de dados
    total_registros = 100
    qtd_especial = 20  # Quantidade com código 5905
    
    # Cria uma lista com 20x '5905' e 80x '5904'
    lista_produtos = ['5905'] * qtd_especial + ['5904'] * (total_registros - qtd_especial)
    
    # Embaralha a lista para não ficarem todos os 5905 no começo
    random.shuffle(lista_produtos)

    print(f"Gerando {total_registros} registros...")

    with open("contratos.txt", "w") as arquivo:
        for i in range(total_registros):
            # --- CAMPO 1: Número do Contrato (12 dígitos) ---
            # Gera um número aleatório e preenche com zeros à esquerda
            num_contrato = str(random.randint(1, 999999999999)).zfill(12)

            # --- CAMPO 2: Código do Produto (4 dígitos) ---
            # Pega um código da nossa lista embaralhada
            cod_produto = lista_produtos[i]

            # --- CAMPO 3: Valor da Parcela (7 dígitos, 2 decimais implícitos) ---
            # Gera valor entre R$ 50,00 e R$ 5.000,00
            valor_float = round(random.uniform(50.00, 5000.00), 2)
            # Remove o ponto e preenche com zeros (Ex: 195.00 vira "0019500")
            valor_str = str(int(valor_float * 100)).zfill(7)

            # --- CAMPO 4: Prazo (3 dígitos) ---
            # Prazo entre 12 e 120 meses
            prazo = str(random.randint(12, 120)).zfill(3)

            # --- CAMPO 5: Data do Contrato (8 dígitos YYYYMMDD) ---
            # Vamos variar a data nos últimos 30 dias ou usar fixa
            data_base = datetime(2026, 2, 8)
            dias_aleatorios = random.randint(0, 30)
            data_final = data_base - timedelta(days=dias_aleatorios)
            data_str = data_final.strftime("%Y%m%d")

            # --- Montagem da Linha ---
            linha = f"{num_contrato}{cod_produto}{valor_str}{prazo}{data_str}\n"
            
            # Escreve no arquivo
            arquivo.write(linha)

    print("Arquivo 'contratos.txt' gerado com sucesso!")

# Executa a função
if __name__ == "__main__":
    gerar_contratos()