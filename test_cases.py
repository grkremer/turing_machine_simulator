import sys
from turing_machine import parse_mt_file, simulate

# Caso uma máquina produza um resultado, o esperado_out é a string da fita.
# Caso uma máquina seja de validação (ACEITA ou REJEITA, como as da questão 4), o esperado_out é um booleano.
test_cases = {
    # ------------------ QUESTÕES 1, 2 e 3 (Produzem saída) ------------------
    # 1a.mt corresponde à questão 1(a): f(x) = x^3 + 2x
    "1a.mt": [
        ("", ""),
        ("u", "uuu"),
        ("uu", "uuuuuuuuuuuu"),
        ("uuu", "u" * 33),
        ("uuuu", "u" * 72),
        ("uuuuu", "u" * 135),
        # Adicionando mais alguns (com cuidado pois o 1a.mt na sua maquina talvez seja 4c, mas voce corrigiu que era 1a mesmo)
    ],
    # 1b.mt corresponde à questão 1(b): f(x) = x mod 5
    "1b.mt": [
        ("", ""),                        # 0 mod 5 = 0
        ("u", "u"),                      # 1 mod 5 = 1
        ("uu", "uu"),                    # 2 mod 5 = 2
        ("uuu", "uuu"),                  # 3 mod 5 = 3
        ("uuuu", "uuuu"),                # 4 mod 5 = 4
        ("uuuuu", ""),                   # 5 mod 5 = 0
        ("uuuuuu", "u"),                 # 6 mod 5 = 1
        ("uuuuuuu", "uu"),               # 7 mod 5 = 2
        ("uuuuuuuu", "uuu"),             # 8 mod 5 = 3
        ("uuuuuuuuuu", ""),              # 10 mod 5 = 0
        ("uuuuuuuuuuu", "u"),            # 11 mod 5 = 1
        ("uuuuuuuuuuuuu", "uuu"),        # 13 mod 5 = 3
        ("uuuuuuuuuuuuuu", "uuuu"),      # 14 mod 5 = 4
        ("uuuuuuuuuuuuuuu", ""),         # 15 mod 5 = 0
        ("uuuuuuuuuuuuuuuu", "u"),       # 16 mod 5 = 1
    ],
    # 2.mt corresponde à questão 2(a): m XOR n
    "2.mt": [
        ("u#u", ""),          # 1 XOR 1 = 0 -> vazio
        ("uu#uuu", ""),       # 2 XOR 3 (V e V) -> 0 -> vazio
        ("u#", "u"),          # 1 XOR 0 (V e F) -> 1 -> u
        ("#u", "u"),          # 0 XOR 1 (F e V) -> 1 -> u
        ("#", ""),            # 0 XOR 0 (F e F) -> 0 -> vazio
        ("uuuu#", "u"),       # 4 XOR 0 = 1 -> u
        ("#uuuuu", "u"),      # 0 XOR 5 = 1 -> u
        ("uuuuu#uuuuu", ""),  # 5 XOR 5 = 0 -> vazio
        ("uuuuuuuuuu#uu", ""),# 10 XOR 2 = 0 -> vazio
        ("u#uuuuu", ""),      # 1 XOR 5 (V e V) -> 0
        ("uuu#", "u"),        # 3 XOR 0 (V e F) -> 1
        ("#uuuu", "u"),       # 0 XOR 4 (F e V) -> 1
        ("uuuu#uuuuuuuu", ""),# 4 XOR 8 (V e V) -> 0
        ("u#u", ""),
        ("#uu", "u")
    ],
    # 3.mt corresponde à questão 3(a): f(m,n) = (n,m) se m < n senao (m,n)
    "3.mt": [
        ("uu#uu", "uu#uu"),
        ("#uuu", "uuu#"),
        ("uu#u", "uu#u"),
        ("u#uuuu", "uuuu#u"),
        ("#", "#"),
        ("uuuuu#uuuuu", "uuuuu#uuuuu"), 
        ("uu#uuuuu", "uuuuu#uu"),  
        ("uuuuu#uu", "uuuuu#uu"),  
        ("uuuu#uuuuuu", "uuuuuu#uuuu"), 
        ("uuuuuu#uuuu", "uuuuuu#uuuu"),
        ("u#uuu", "uuu#u"),
        ("uuu#u", "uuu#u"),
        ("#u", "u#"),
        ("u#", "u#"),
        ("uuuuuuuu#uuuuuuuuu", "uuuuuuuuu#uuuuuuuu")
    ],
    
    # ------------------ QUESTÃO 4 (Linguagens de aceitação) ------------------
    # 4a.mt corresponde à questão 4(a): L = {0^m 1^n | m > 0 e n > m}
    "4a.mt": [
        ("011", True),           # ACEITA: m=1, n=2
        ("0111", True),          # ACEITA: m=1, n=3
        ("00111", True),         # ACEITA: m=2, n=3
        ("001111", True),        # ACEITA: m=2, n=4
        ("0001111", True),       # ACEITA: m=3, n=4
        ("00001111111", True),   # ACEITA: m=4, n=7
        ("", False),             # REJEITA: n=0, m=0
        ("0", False),            # REJEITA: m=1, n=0
        ("1", False),            # REJEITA: m=0, n=1
        ("01", False),           # REJEITA: m=1, n=1 (n não é > m)
        ("0011", False),         # REJEITA: m=2, n=2 (n não é > m)
        ("1100", False),         # REJEITA: fora do padrão
        ("00110", False),        # REJEITA: fora do padrão
        ("00011", False),        # REJEITA: m=3, n=2 (n não é > m)
        ("111", False)           # REJEITA: m=0
    ],
    # 4b.mt corresponde à questão 4(b): L = {u^n | n = 2^x, x >= 0}
    "4b.mt": [
        ("u", True),             # ACEITA: n=1 (2^0)
        ("uu", True),            # ACEITA: n=2 (2^1)
        ("uuuu", True),          # ACEITA: n=4 (2^2)
        ("uuuuuuuu", True),      # ACEITA: n=8 (2^3)
        ("uuuuuuuuuuuuuuuu", True),# ACEITA: n=16 (2^4)
        ("", False),             # REJEITA: n=0
        ("uuu", False),          # REJEITA: n=3
        ("uuuuu", False),        # REJEITA: n=5
        ("uuuuuu", False),       # REJEITA: n=6
        ("uuuuuuu", False),      # REJEITA: n=7
        ("uuuuuuuuu", False),    # REJEITA: n=9
        ("uuuuuuuuuu", False),   # REJEITA: n=10
        ("uuuuuuuuuuu", False),  # REJEITA: n=11
        ("uuuuuuuuuuuu", False), # REJEITA: n=12
        ("uuuuuuuuuuuuuuu", False) # REJEITA: n=15
    ],
    # 4c.mt corresponde à questão 4(c): L = {a^n b^n c^n | n >= 0}
    "4c.mt": [
        ("", True),              # ACEITA: n=0
        ("abc", True),           # ACEITA: n=1
        ("aabbcc", True),        # ACEITA: n=2
        ("aaabbbccc", True),     # ACEITA: n=3
        ("aaaabbbbcccc", True),  # ACEITA: n=4
        ("aaaaabbbbbccccc", True),# ACEITA: n=5
        ("a", False),            # REJEITA
        ("ab", False),           # REJEITA
        ("bc", False),           # REJEITA
        ("ac", False),           # REJEITA
        ("aabc", False),         # REJEITA
        ("abbc", False),         # REJEITA
        ("abcc", False),         # REJEITA
        ("bca", False),          # REJEITA
        ("aabbc", False)         # REJEITA
    ],
    # 4d.mt corresponde à questão 4(d): L = {w | w == w^R} (Alfabeto {b, q})
    "4d.mt": [
        ("", True),              # ACEITA: vazio
        ("b", True),             # ACEITA: 1 letra
        ("q", True),             # ACEITA: 1 letra
        ("bb", True),            # ACEITA: par igual
        ("qq", True),            # ACEITA: par igual
        ("bqb", True),           # ACEITA: ímpar palíndromo
        ("qbq", True),           # ACEITA: ímpar palíndromo
        ("bqqb", True),          # ACEITA: par palíndromo
        ("qbbq", True),          # ACEITA: par palíndromo
        ("bbbbb", True),         # ACEITA: tudo b
        ("bq", False),           # REJEITA
        ("qb", False),           # REJEITA
        ("bbq", False),          # REJEITA
        ("bqq", False),          # REJEITA
        ("bqbq", False)          # REJEITA
    ]
}

def trim_tape(tape_array, blank_symbol='-'):
    result = "".join(tape_array)
    result = result.replace("@", "").replace(blank_symbol, "")
    return result

def main():
    total_tests = 0
    total_passed = 0
    
    for machine, cases in test_cases.items():
        print(f"=== Testando a máquina {machine} ===")
        machine_tests = len(cases)
        machine_passed = 0
        
        try:
            tm = parse_mt_file(machine)
            blank_symbol = tm['blank_symbol']
            
            # Checa se é questão 4 (apenas linguagem de aceitação)
            is_language_recognition = machine.startswith("4")
            
            for (case_in, expected_out) in cases:
                accepted, tape = simulate(tm, case_in)
                raw_tape = "".join(tape)
                
                res_acc = "ACEITA" if accepted else "REJEITA"
                
                if is_language_recognition: 
                    # Na questão 4, expected_out é True (ACEITA) ou False (REJEITA)
                    passou = "OK" if accepted == expected_out else "FALHOU"
                    # formata saida esperada pra facilitar o print
                    exp_str = "ACEITA" if expected_out else "REJEITA"
                    
                    print(f"Entrada: '{case_in:15}' | Res: {res_acc:7} | Fita Crua: '{raw_tape}' | Esperado: '{exp_str:7}' | {passou}")
                    
                    if passou == "OK":
                        machine_passed += 1
                        
                else:
                    # Nas questões 1, 2 e 3 o foco é a fita limpa
                    trimmed_tape = trim_tape(tape, blank_symbol)
                    passou = "OK" if trimmed_tape == expected_out else "FALHOU"
                    
                    print(f"Entrada: '{case_in:15}' | Res: {res_acc:7} | Fita Crua: '{raw_tape}' | Esperado: '{expected_out}' | {passou}")
                    
                    if passou == "OK":
                        machine_passed += 1
                
            percent_machine = (machine_passed / machine_tests) * 100
            print(f"-> Acertos {machine}: {machine_passed}/{machine_tests} ({percent_machine:.1f}%)\n")
            
            total_tests += machine_tests
            total_passed += machine_passed
            
        except FileNotFoundError:
            # Se a máquina não foi criada ainda, apenas avise e adicione no total de testes mas com 0 passed
            print(f"Arquivo {machine} não encontrado (Ainda não desenvolvida).\n")
            total_tests += machine_tests

    percent_total = (total_passed / total_tests) * 100 if total_tests > 0 else 0
    print(f"========================================")
    print(f"-> TOTAL DE ACERTOS: {total_passed}/{total_tests} ({percent_total:.1f}%)")
    print(f"========================================")

if __name__ == '__main__':
    main()
