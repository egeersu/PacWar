import random
import os

#[(gene1,score1), (gene2,score2) ...]
def read_genes(file):
    f = open(file, "r")
    lst = []
    for l in f:
        lst.append(string_to_gene(l))
    return lst

def write_gene(gene, score, file):
    f = open(file, "w")
    f.write(gene, score)

def write_genes(genes, file):
    f = open(file, "w")
    for t in genes:
        f.write(gene_to_string(t[0], t[1]))

def initialize_champions(size):
    f = open("champions.txt", "r+")
    if len(f.read()) == 0:
        print("EMPTY AS FUCK")
        for i in range(size):
            gene = random_gene()
            f.write(gene_to_string(gene, 0.00))
    else:
        print("OH SHIT IT'S FULL")


def initialize_champions2(size):
    #if file does not exist create new
    f = open("champions.txt", "")
    print("length: ", len(f.read()))
    if len(f.read()) == 0:
        print("EMPTY AS FUCK")
        for i in range(size):
            gene = random_gene()
            f.write(gene_to_string(gene, 0.00))
    else:
        print("OH SHIT IT'S FULL")

def read_champions():
    return read_genes("champions.txt")

def gene_to_string(gene, score):
    #  [1,3,2], 17 -> "1 3 2 17"
    return ''.join(str(g) + " " for g in gene) + str(score) + "\n"

def string_to_gene(s):
    #  "1 3 2 17" -> ( [1,3,2], 17)
    s = s.split()
    gene = list(map(int, s[0:len(s)-1]))
    score = float(s[len(s)-1])
    return (gene, score)

def random_gene():
    gene = []
    for i in range(50):
        gene.append(random.choice([0,1,2,3]))
    return gene


initialize_champions(10)
print(read_champions())
