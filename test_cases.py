import sys
from turing_machine import parse_mt_file, simulate

# Caso uma máquina produza um resultado, o esperado_out é a string da fita.
# Caso uma máquina seja de validação (ACEITA ou REJEITA, como as da questão 4), o esperado_out é um booleano.
test_cases = \
{'1a.mt': [('', ''),
           ('u', 'uuu'),
           ('uu', 'uuuuuuuuuuuu'),
           ('uuu', 'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),
           ('uuuu', 'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),
           ('uuuuu',
            'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),
           ('uuuuuu',
            'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),
           ('uuuuuuu',
            'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),
           ('uuuuuuuu',
            'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'),
           ('uuuuuuuuu',
            'uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')],
 '1b.mt': [('', ''),
           ('u', 'u'),
           ('uu', 'uu'),
           ('uuu', 'uuu'),
           ('uuuu', 'uuuu'),
           ('uuuuu', ''),
           ('uuuuuu', 'u'),
           ('uuuuuuu', 'uu'),
           ('uuuuuuuu', 'uuu'),
           ('uuuuuuuuu', 'uuuu'),
           ('uuuuuuuuuu', ''),
           ('uuuuuuuuuuu', 'u'),
           ('uuuuuuuuuuuu', 'uu'),
           ('uuuuuuuuuuuuu', 'uuu'),
           ('uuuuuuuuuuuuuu', 'uuuu'),
           ('uuuuuuuuuuuuuuu', ''),
           ('uuuuuuuuuuuuuuuu', 'u'),
           ('uuuuuuuuuuuuuuuuu', 'uu'),
           ('uuuuuuuuuuuuuuuuuu', 'uuu'),
           ('uuuuuuuuuuuuuuuuuuu', 'uuuu')],
 '2.mt': [('#', ''),
          ('#u', 'u'),
          ('u#', 'u'),
          ('u#u', ''),
          ('#uuuuu', 'u'),
          ('uuuuu#', 'u'),
          ('uu#uuu', ''),
          ('uuuu#uuuu', ''),
          ('#uuuuuuuuuu', 'u'),
          ('uuuuuuuuuu#', 'u'),
          ('uuuuuuu#uuuuuuuu', ''),
          ('uuuuuuuuuuuu#uuuuuuuuuuuu', ''),
          ('#uu', 'u'),
          ('uu#', 'u'),
          ('uuu#uuu', ''),
          ('u#uuuuu', ''),
          ('uu#u', ''),
          ('#uuuuuuu', 'u'),
          ('uuuuuuu#', 'u'),
          ('uuuuuuuu#uuuuuuuu', '')],
 '3.mt': [('#', '#'),
          ('#u', 'u#'),
          ('u#', 'u#'),
          ('u#u', 'u#u'),
          ('uu#uuu', 'uuu#uu'),
          ('uuu#uu', 'uuu#uu'),
          ('uuuu#uuuu', 'uuuu#uuuu'),
          ('#uuuuu', 'uuuuu#'),
          ('uuuuu#', 'uuuuu#'),
          ('u#uuuuu', 'uuuuu#u'),
          ('uuuuu#u', 'uuuuu#u'),
          ('uuu#uuuuuuu', 'uuuuuuu#uuu'),
          ('uuuuuuu#uuu', 'uuuuuuu#uuu'),
          ('uuuuuuuu#uuuuuuuu', 'uuuuuuuu#uuuuuuuu'),
          ('uu#uuuuuuuu', 'uuuuuuuu#uu'),
          ('uuuuuuuu#uu', 'uuuuuuuu#uu'),
          ('uuuuuuuuuu#uuuuuuuuuuuu', 'uuuuuuuuuuuu#uuuuuuuuuu'),
          ('uuuuuuuuuuuu#uuuuuuuuuu', 'uuuuuuuuuuuu#uuuuuuuuuu'),
          ('#uuuuuuuuuu', 'uuuuuuuuuu#'),
          ('uuuuuuuuuu#', 'uuuuuuuuuu#')],
 '4a.mt': [('011', True),
           ('0111', True),
           ('00111', True),
           ('001111', True),
           ('0001111', True),
           ('00011111', True),
           ('000011111', True),
           ('0000111111', True),
           ('00000111111', True),
           ('000001111111', True),
           ('', False),
           ('0', False),
           ('1', False),
           ('01', False),
           ('0011', False),
           ('001', False),
           ('00011', False),
           ('10', False),
           ('010', False),
           ('1100', False)],
 '4b.mt': [('u', True),
           ('uu', True),
           ('uuuu', True),
           ('uuuuuuuu', True),
           ('uuuuuuuuuuuuuuuu', True),
           ('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', True),
           ('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', True),
           ('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',
            True),
           ('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',
            True),
           ('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu',
            True),
           ('', False),
           ('uuu', False),
           ('uuuuu', False),
           ('uuuuuu', False),
           ('uuuuuuu', False),
           ('uuuuuuuuu', False),
           ('uuuuuuuuuu', False),
           ('uuuuuuuuuuu', False),
           ('uuuuuuuuuuuu', False),
           ('uuuuuuuuuuuuu', False)],
 '4c.mt': [('', True),
           ('abc', True),
           ('aabbcc', True),
           ('aaabbbccc', True),
           ('aaaabbbbcccc', True),
           ('aaaaabbbbbccccc', True),
           ('aaaaaabbbbbbcccccc', True),
           ('aaaaaaabbbbbbbccccccc', True),
           ('aaaaaaaabbbbbbbbcccccccc', True),
           ('aaaaaaaaabbbbbbbbbccccccccc', True),
           ('a', False),
           ('b', False),
           ('c', False),
           ('ab', False),
           ('bc', False),
           ('ac', False),
           ('aabc', False),
           ('abbc', False),
           ('abcc', False),
           ('bca', False)],
 '4d.mt': [('', True),
           ('b', True),
           ('q', True),
           ('bb', True),
           ('qq', True),
           ('bqb', True),
           ('qbq', True),
           ('bqqb', True),
           ('qbbq', True),
           ('bbbbb', True),
           ('bq', False),
           ('qb', False),
           ('bbq', False),
           ('bqq', False),
           ('bqbq', False),
           ('qbqb', False),
           ('bqqbq', False),
           ('qbb', False),
           ('qqb', False),
           ('bqbqq', False)]}

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
