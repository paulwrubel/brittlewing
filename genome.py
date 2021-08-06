from __future__ import annotations
from hashlib import new
from constants import *
import random


class Genome:
    def __init__(self, raw_g: str):
        self.g = self.__parse_genome_string(raw_g)

    def __parse_genome_string(self, string: str) -> list[int]:
        """
        parse_genome transforms a genome string of form '11111' or 'RrGgBbWwXx' into a coded genome [1, 1, 1, 1, 1]
        """
        genome = []

        # check which format the string is in
        if len(string) == GENE_COUNT:
            # 11111
            for gene_str in string:
                gene_num = int(gene_str)
                if gene_num < 0 or gene_num > 2:
                    raise Exception(
                        "invalid gene short notation: digit out of range 0-2")
                genome.append(gene_num)
        elif len(string) == GENE_COUNT*2:
            # RrGgBbWwXx
            for i, gene in enumerate(self.__pairs(string)):
                # gene in this context would be one of ['Rr', 'Gg', ...]

                # check if the actual characters are right, regardless of case
                if gene.upper()[0] != GENE_NAMES_SHORT[i].upper():
                    raise Exception(
                        "invalid gene long notation: invalid char[{}] in {}".format(0, gene[0]))
                if gene.upper()[1] != GENE_NAMES_SHORT[i].upper():
                    raise Exception(
                        "invalid gene long notation: invalid char[{}] in {}".format(1, gene[1]))

                # check how many chars are upper
                # in this implementation, there is no differentiation between Rr and rR
                upper_count = gene.count(GENE_NAMES_SHORT[i].upper())
                genome.append(upper_count)
        else:
            raise Exception("invalid gene notation: invalid length")

        return genome

    def __pairs(self, genome_string: str) -> str:
        """
        a simple generator to return pairs of chars iteratively from a string
        """
        while len(genome_string) > 0:
            if len(genome_string) == 1:
                gene = genome_string[0]
                genome_string = genome_string[1:]
                yield gene
            else:
                gene = genome_string[0:2]
                genome_string = genome_string[2:]
                yield gene

    def cross(self, b: Genome) -> Genome:
        new_genes = []
        for a_gene, b_gene in zip(self.g, b.g):
            if a_gene == 0:
                if b_gene == 0:
                    new_genes.append(0)
                elif b_gene == 1:
                    new_genes.append(random.choice([0, 1]))
                else:  # b_gene == 2
                    new_genes.append(1)
            elif a_gene == 1:
                if b_gene == 0:
                    new_genes.append(random.choice([0, 1]))
                elif b_gene == 1:
                    new_genes.append(random.choice([0, 1, 1, 2]))
                else:  # b_gene == 2
                    new_genes.append(random.choice([1, 2]))
            else:  # a_gene == 2
                if b_gene == 0:
                    new_genes.append(1)
                elif b_gene == 1:
                    new_genes.append(random.choice([1, 2]))
                else:  # b_gene == 2
                    new_genes.append(2)
        return Genome(''.join(map(str, new_genes)))

    def genes(self) -> list[int]:
        return self.g

    def short(self) -> str:
        short_string = ""
        for gene in self.g:
            short_string += str(gene)
        return short_string

    def long(self) -> str:
        long_string = ""
        for i, gene in enumerate(self.g):
            if gene == 0:
                long_string += GENE_NAMES_SHORT[i].lower() + \
                    GENE_NAMES_SHORT[i].lower()
            if gene == 1:
                long_string += GENE_NAMES_SHORT[i].upper() + \
                    GENE_NAMES_SHORT[i].lower()
            if gene == 2:
                long_string += GENE_NAMES_SHORT[i].upper() + \
                    GENE_NAMES_SHORT[i].upper()
        return long_string
