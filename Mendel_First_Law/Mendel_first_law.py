#!/usr/bin/ python3


"""Script for calculating Rosalind problem of mendel's First law"""



def calculate_prob_mendel(k,m,n):
    """Calculate prob that two randomly slected mating organisms will produce an individual possessing a dominant allels

    Inpit: k,m,n, pos integers for representing k+m+n organisms, k: homo dominant, m hetero, n: homo recessiv

    Output : prob (pos nteger) for 2 randomly selected organisms will produce individual with dominant allele
    """


    total_organisms = k + m + n
    #2 homo dominant alleles
    prob_kk = (k/total_organisms) * (k-1)/ ((total_organisms-1))
    #prob of selecting one homo_domin and one heterzygous allele
    prob_km = (k/total_organisms) * (m/(total_organisms-1)) + (m/total_organisms)* (k/(total_organisms-1))
    #one homozygous dominant and one homo recessive
    prob_kn = (k/total_organisms) *(n/(total_organisms-1)) + (n/ (total_organisms)) * (k/(total_organisms-1))

    # Probability of selecting 2 heterozygous organisms
    prob_mm = (m/total_organisms) * ((m-1)/(total_organisms-1)) *0.75

    #2 individ both recess
    prob_mn = (m/total_organisms) *(n/(total_organisms-1)) *0.5 +  (n/total_organisms) * (m/ (total_organisms-1)) *0.5

    # Total probability of producing an individual with a dominant allele
    totalprob = prob_kk +prob_km + prob_kn +prob_mm + prob_mn

    return totalprob

def main():
    total_prob = calculate_prob_mendel(2,2,2)
    print(f"Probability of producing an individual with a dominant allele: {total_prob:.5f}")

if __name__ == '__main__':
    main()