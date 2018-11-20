#  [1,3,2], 17 -> "1 3 2 17"
def gene_to_string(gene, score):
    return ''.join(str(g) + " " for g in gene) + str(score) + "\n"

#  "1 3 2 17\n" -> ( [1,3,2], 17)
def string_to_gene(s):
    s = s.split()
    gene = list(map(int, s[0:len(s)-1]))
    score = int(s[len(s)-1])
    return (gene, score)

def write_genes(genes, file):
    f = open(genes, file)
    for t in genes:
        f.write(gene_to_string(t[0], t[1]))


gene1 = [([1,3,2], 10), ([0,1,2], 12), ([3,2,1], 28)]

s = gene_to_string(gene1, 17)
print(s)
g = string_to_gene(s)
print(g)
