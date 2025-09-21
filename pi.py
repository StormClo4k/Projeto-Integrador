# Sistema de Controle Financeiro
# Códigos ANSI para colorir a saída do terminal ---
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CINZA = "\033[90m"
RESET = "\033[0m"
NEGRITO = "\033[1m"

# Dicionários que armazenarão as receitas e despesas
entradas = {}
saidas = {}

# --- Cadastro das entradas (receitas) ---
print(f"{AZUL}{NEGRITO}=== Cadastro de Entradas (Receitas) ==={RESET}")
while True:
    categoria = input(
        "Digite a categoria da receita (ou 'fim' para encerrar): ")
    if categoria.lower() == "fim":  # Se o usuário digitar "fim", encerra o loop
        break
    valor = float(input(f"Valor recebido em {categoria}: R$ "))
    # Acumula valores da mesma categoria
    entradas[categoria] = entradas.get(categoria, 0) + valor

# --- Cadastro das saídas (despesas) ---
print(f"\n{AZUL}{NEGRITO}=== Cadastro de Saídas (Despesas) ==={RESET}")
while True:
    categoria = input(
        "Digite a categoria da despesa (ou 'fim' para encerrar): ")
    if categoria.lower() == "fim":
        break
    valor = float(input(f"Valor gasto em {categoria}: R$ "))
    saidas[categoria] = saidas.get(categoria, 0) + valor

# --- Cálculos principais ---
total_entradas = sum(entradas.values())  # Soma todas as receitas
total_saidas = sum(saidas.values())      # Soma todas as despesas
saldo = total_entradas - total_saidas    # Diferença entre receitas e despesas
soma_saida_entrada = total_entradas + \
    total_saidas  # Usado para cálculo percentual

# --- Diagnóstico inicial ---
maior_entrada = max(entradas, key=entradas.get) if entradas else "Nenhuma"
maior_saida = max(saidas, key=saidas.get) if saidas else "Nenhuma"
percentual_saida = (total_saidas / soma_saida_entrada) * \
    100 if soma_saida_entrada > 0 else 0
percentual_entrada = (total_entradas / soma_saida_entrada) * \
    100 if soma_saida_entrada > 0 else 0
if total_entradas > 0:
    # Percentual de lucro/prejuízo sobre receitas
    margem_lucro = (saldo / total_entradas) * 100
else:
    margem_lucro = 0.0

# --- Impressão do recibo financeiro ---
print(f"\n{NEGRITO}{AZUL}=== RECIBO FINANCEIRO ==={RESET}")
print(f"{VERDE}Total de Receitas:{RESET} R$ {total_entradas:.2f} ({percentual_entrada:.2f}%)")
print(f"{VERMELHO}Total de Despesas:{RESET} R$ {total_saidas:.2f} ({percentual_saida:.2f}%)")

# --- Detalhamento das receitas ---
if entradas:
    print(f"\n{NEGRITO}{VERDE}--- Detalhamento das Receitas ---{RESET}")
    for categoria, valor in entradas.items():
        perc = (valor / total_entradas) * 100 if total_entradas > 0 else 0
        print(f"{VERDE}{categoria}:{RESET} R$ {valor:.2f} ({perc:.2f}%)")

# --- Detalhamento das despesas ---
if saidas:
    print(f"\n{NEGRITO}{VERMELHO}--- Detalhamento das Despesas ---{RESET}")
    for categoria, valor in saidas.items():
        perc = (valor / total_saidas) * 100 if total_saidas > 0 else 0
        print(f"{VERMELHO}{categoria}:{RESET} R$ {valor:.2f} ({perc:.2f}%)")

# --- Situação final da empresa ---
if saldo > 0:
    print(f"\n{VERDE}Saldo Final: R$ {saldo:.2f}{RESET}")
    print(f"{NEGRITO}{VERDE}Margem de Lucro: {margem_lucro:+.2f}%{RESET}")
elif saldo < 0:
    print(f"\n{VERMELHO}Saldo Final: R$ {saldo:.2f}{RESET}")
    print(f"{NEGRITO}{VERMELHO}Margem de Lucro: {margem_lucro:+.2f}%{RESET}")
else:
    print(f"\n{AMARELO}Saldo Final: R$ {saldo:.2f}{RESET}")
    print(f"{NEGRITO}{AMARELO}Margem de Lucro: {margem_lucro:+.2f}%{RESET}")

# --- Análise da margem de lucro/prejuízo ---
print(f"\n{NEGRITO}{AZUL}=== ANÁLISE DA MARGEM ==={RESET}")
if margem_lucro >= 25:
    print(f"{VERDE}{NEGRITO}Excelente!{RESET} Sua margem está muito acima da média")
elif margem_lucro >= 10:
    print(f"{VERDE}Ótimo!{RESET} Margem saudável e sustentável")
elif margem_lucro >= 0:
    print(f"{AMARELO}Regular.{RESET} Há espaço para melhorias na rentabilidade")
elif margem_lucro >= -10:
    print(f"{VERMELHO}Atenção!{RESET} Prejuízo moderado - revise suas despesas")
else:
    print(f"{VERMELHO}{NEGRITO}CRÍTICO!{RESET} Prejuízo elevado - ação urgente necessária")

# --- Diagnóstico final ---
print(f"\n{NEGRITO}{AZUL}=== Diagnóstico ==={RESET}")
print(f"Maior fonte de receita: {VERDE}{maior_entrada}{RESET}")
print(f"Maior gasto registrado: {VERMELHO}{maior_saida}{RESET}")

# --- Sugestões de melhorias se houver prejuízo ---
if saldo < 0:
    print(f"\n{NEGRITO}{AMARELO}=== SUGESTÕES PARA MELHORAR ==={RESET}")
    if total_saidas > total_entradas * 1.5:
        print(f"{AMARELO}• Reduza drasticamente suas despesas operacionais")
    print(f"{AMARELO}• Busque novas fontes de receita")
    print(f"{AMARELO}• Renegocie fornecedores e contratos")
    print(f"{AMARELO}• Implemente controle de custos mais rigoroso")

# --- Rodapé ---
print(f"{CINZA}==============================={RESET}")
