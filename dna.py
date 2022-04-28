

seq = 'GATTATCA'



# find numer of kmers in dna sequence
def count_kmers(seq, k):
    kmer_count = {}
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1
    return kmer_count



