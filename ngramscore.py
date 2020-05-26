#!/usr/bin/python3


class NGramScore:
    def __init__(self,ngramfile,sep=' '):
        self.ngrams = {}
        f = open(ngramfile)
        content = f.readlines()
        f.close()
        for line in content:
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        for key in self.ngrams.keys():
            self.ngrams[key] = self.ngrams[key]

    def score(self, text):
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text)-self.L+1):
            if text[i:i+self.L] in self.ngrams:
                score += ngrams(text[i:i+self.L])
        return score
       
