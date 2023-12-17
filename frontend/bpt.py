pms={
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259 ,
    "F": 147.06841 ,
    "G": 57.02146 ,
    "H": 137.05891 ,
    "I": 113.08406,
    "K": 128.09496 ,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858 ,
    "R": 156.10111 ,
    "S": 87.03203 ,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931 ,
    "Y": 163.06333,
}




def find_mut(seq1,seq2):
        list_mut=[]
        count = 0
        len_sq= 0
        if len(seq1) < len(seq2):
            len_sq=len(seq1)
        elif len(seq1) > len(seq2):
            len_sq=len(seq2)
        elif len(seq1) == len(seq2):
            len_sq= len(seq1)
        for i in range(len_sq):
            if seq1[i].lower() != seq2[i].lower():
                count+=1
                t_mut=(i,seq1[i],seq2[i])
                list_mut.append(t_mut)
        return list_mut


def calculate_pms(seq):
        pmass=0
        for key,value in pms.items():
            for p in seq.upper():
                if key == p:
                    pmass += value

        return pmass
