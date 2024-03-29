# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return list((dct[x] for x in keylist))

def list2dict(L, keylist): return { k:v for (k,v) in list(zip((keylist),(L))) }

def listrange2dict(L): return { k:v for (k,v) in zip(list(range(len(L))), L) }

