import sys

def parse_mt_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
    
    # Pad lines if necessary
    while len(lines) < 8:
        lines.append('')
        
    input_alphabet = [x.strip() for x in lines[0].split(',') if x.strip()]
    aux_alphabet = [x.strip() for x in lines[1].split(',') if x.strip()]
    left_marker = lines[2].strip()
    blank_symbol = lines[3].strip()
    states = [x.strip() for x in lines[4].split(',') if x.strip()]
    initial_state = lines[5].strip()
    final_states = [x.strip() for x in lines[6].split(',') if x.strip()]
    
    transitions = {}
    
    # transitions are separated by ',,,'
    t_blocks = lines[7].split(',,,')
    for block in t_blocks:
        parts = [p.strip() for p in block.split(',')]
        if len(parts) >= 6:
            # Based on pattern: q0,@,,q1,@,D
            # Note the extra empty item due to empty tape2 symbol ? We ignore indices 2.
            # actually let's just grab the non-empty parts or specific indices
            # Format observed: [current_state, read_symbol, "", next_state, write_symbol, direction]
            curr_state = parts[0]
            read_sym = parts[1]
            
            # Handling possible missing columns if standard 5-tuple was used
            # But observed is 6-tuple with empty 3rd argument
            if parts[2] == '' and len(parts) == 6:
                next_state = parts[3]
                write_sym = parts[4]
                direction = parts[5]
            else:
                # fallback if it's really 5 parts: [q0, @, q1, @, D]
                # we'll just search for direction at the end
                direction = parts[-1]
                write_sym = parts[-2]
                next_state = parts[-3]
                
            transitions[(curr_state, read_sym)] = (next_state, write_sym, direction)
            
    return {
        'left_marker': left_marker,
        'blank_symbol': blank_symbol,
        'initial_state': initial_state,
        'final_states': final_states,
        'transitions': transitions
    }

def simulate(tm, input_string):
    tape = [tm['left_marker']] + list(input_string)
    head = 0
    current_state = tm['initial_state']
    
    while current_state not in tm['final_states']:
        if head < 0:
            # If head goes left of left marker, standard TM crashes or stays? 
            # In these assignments it usually stays or we assume tape is bounded.
            return False, tape
        
        if head >= len(tape):
            tape.append(tm['blank_symbol'])
            
        read_sym = tape[head]
        
        if (current_state, read_sym) in tm['transitions']:
            next_state, write_sym, direction = tm['transitions'][(current_state, read_sym)]
            tape[head] = write_sym
            current_state = next_state
            
            if direction == 'D':
                head += 1
            elif direction == 'E':
                head -= 1
        else:
            # No valid transition = reject
            return False, tape
            
    return True, tape

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python turing_machine.py <arquivo.mt> [fita_entrada]")
        sys.exit(1)
        
    filepath = sys.argv[1]
    input_string = sys.argv[2] if len(sys.argv) > 2 else ""
    
    tm = parse_mt_file(filepath)
    accepted, final_tape = simulate(tm, input_string)
    
    # Limpa fita para impressão
    resultado = "aceitou" if accepted else "rejeitou"
    print(f"{resultado}: {''.join(final_tape)}")
