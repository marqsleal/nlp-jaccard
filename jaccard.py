from unidecode import unidecode

def jaccard_index(token1: str, token2: str, printIndex=False) -> float:

    # Normalization:
    token1 = unidecode(token1.lower())
    token2 = unidecode(token2.lower())

    # Creating sets spliting by empty space:
    words_token1 = set(token1.split()) 
    words_token2 = set(token2.split())

    if printIndex:
        print(f'\nToken 1: {token1} / Words Token 1: {words_token1}\nToken 2: {token2} / Words Token 2: {words_token2}')
    
    # Intersection:
    intersection = words_token1.intersection(words_token2)

    if printIndex:
        print(f'\nIntersection: {intersection}')

    # Union:
    union = words_token1.union(words_token2)

    index = float(len(intersection)) / len(union)

    if printIndex:
        print(f'\nUnion: {union}')
        print(f'\nJaccard Index: {index:.2f}')
        
    return index