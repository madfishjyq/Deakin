class NucleotideSequence:
    '''An abstract class which is inherited by
    DNA and RNA sequences. Do not use!'''
    '''A general nucleotide class. The class is inherited by DNASequence
    and RNASequence classes. Not for general use. Use DNASequence and
    RNASequence instead'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    valid = set('ATGCU')
    def __init__(self, sequence):
        '''Input sequence should be a string,
        in all upper case letters.'''
        assert sequence.isupper() is True
        assert isinstance(sequence,str)
        self.sequence=sequence
        self.base_count={}
        try:
            assert set(sequence).difference(self.valid)==0
        except AssertionError:
            print 'Input should only be ATGC'
    
    def base_count(self, base):
        '''Given a base, returns the number of
        times the base occurs in this sequence.
        
        Returns an integer.
        '''
        assert isinstance(base,str)
        assert base.isupper() is True
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
            return count
    
    def gc_content(self):
        '''Returns the GC ratio in given sequence'''
        '''returns the proportion of residues 
        that are either G or C in the sequence,
        from 0 to 1'''
        '''This calculates the percentage of GC in the
        sequence'''
        
        g = self.base_count('G')
        c = self.base_count('C')
        return float(g+c)/len(self.sequence)
        
    def reverse_complement(self):
        ''''Given a sequence returns a reverse complement of the sequence given'''
        '''Takes a sequence as input, reverses that sequence and then 
        complemenents it (G's become C's, A's become T's, etc), then returns
        the new sequence.'''
        rev_c = ''
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
        return rev_c
        
        
class DNASequence(NucleotideSequence):
    '''Uses the bases GATC.'''
    '''Class appropriate for DNA sequences. Assumes only A,T,C and G are found in the sequence.'''
    pass    
    
class RNASequence(NucleotideSequence):
    '''Uses the bases GAUC.'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}



