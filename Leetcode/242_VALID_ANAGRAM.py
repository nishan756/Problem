def is_anagram(s:str , t:str):
    if len(s) != len(t):
        return False
    item_freq = {}
    for i in s:
        if i not in s:
            item_freq[i] = 1
        else:
            item_freq[i] += 1
    for j in t:
        if j not in item_freq:
            return False
        else:
            item_freq[j] -= 1
    for item in item_freq:
        if item_freq[item] != 0:
            return False
    return True