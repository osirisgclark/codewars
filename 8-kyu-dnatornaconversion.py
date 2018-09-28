#8 kyu DNA to RNA Conversion
def DNAtoRNA(dna):
	import re
	return dna.translate(dna.maketrans('T', 'U'))
        #return dna.replace('T', 'U')

print(DNAtoRNA("GCAT"), "GCAU")
