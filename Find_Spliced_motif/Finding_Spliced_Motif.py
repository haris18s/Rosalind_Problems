def parse_fast(filename):

    with open(filename) as f:
        data = f.readlines()
    seqs = []
    current_seq = ''
    for line in data:
        line = line.rstrip()
        if line.startswith(">"):
            if  current_seq:
                seqs.append("".join(current_seq))
            current_seq = ""
        else:
            current_seq +=line

    if current_seq:
        seqs.append("".join(current_seq))
    print(seqs)
    return seqs

def findFirstmatch(s,t):
    t_pointer =0
    match = []
    for i in range(len(s)):
        if s[i] == t[t_pointer]:
            match.append(i+1)
            t_pointer +=1
            if len(t) == t_pointer:
                break

    return first_match
def find_subsequencs(s,t, start =0, t_pointer = 0, current_match = None, results = None):

    if current_match is None:
        current_match = []
    if results is None:
        results = []
    #if the t has atched store the current subsequences
    if t_pointer == len(t):
        #match has found
        results.append(current_match[:])
        return #go back to the previous recursive call

    for i in range(start, len(s)):
        if s[i] == t[t_pointer]:
            current_match.append(i+1)
            #recursively find futher matches
            find_subsequencs(s,t,start =  i+1, t_pointer = t_pointer+1, current_match  = current_match,
                             results = results)
            current_match.pop()


    return results



if __name__ == '__main__':
    seqs = parse_fast("rosalind_sseq.txt")

    s, t = seqs[0], seqs[1]
    #just reurn the first one
    matches = find_subsequencs(s,t)
    first_match = matches[0]
    #use map to convert to strings and join them
    import time
    tic = time.time()
    matches2 = find_subsequencs(s,t)
    first_match2 = matches2[0]

    print(" ".join(map(str, first_match2)))
    toc = time.time()
    print(toc-tic)