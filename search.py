def makeInverseIndex(strlist):
    d = {}
    for (words,i) in [(s.split(),i) for i,s in list(enumerate(strlist))]:
        for w in words:
            if w not in d:
                d[w] = {i}
            else:
                d[w].add(i)
    return d


def orSearch(inverseIndex, query):
    # return set of indices of documents containing any words in query
    X = set({})
    for v in query:
        for w in inverseIndex.keys():
            if v == w:
                X = (X|inverseIndex[w])
    return(X)


def andSearch(inverseIndex, query):
    # return set of indices of documents containing all words in query
    if query[0] in inverseIndex.keys():       
        X = inverseIndex[query[0]]
        for s in query:
            if s in inverseIndex.keys():
                X = X&inverseIndex[s]
        return X
    else:
        return set({})
