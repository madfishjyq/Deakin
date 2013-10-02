def base_count(sequence,base):
    if base in  sequence:
        return sequence.count(base)
    else: return 0

print base_count("GATCTAGTGATGCAC","A")

def gc_content(sequence):
    return (base_count(sequence,'G')+base_count(sequence,'C'))/float(len(sequence))

print gc_content("GATCTAGTGATGCAC")
