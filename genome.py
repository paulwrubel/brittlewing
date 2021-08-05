from constants import *


class Genome:
    def __init__(self, string: str):
        self.genome = self.__parse_genome_string(string)

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

    def genes(self) -> list[int]:
        return self.genome

    def short(self) -> str:
        short_string = ""
        for gene in self.genome:
            short_string += str(gene)
        return short_string

    def long(self) -> str:
        long_string = ""
        for i, gene in enumerate(self.genome):
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
