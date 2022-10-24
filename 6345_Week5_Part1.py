


fin = open('words.txt')
fin.readline()

'''9.1'''
def TwentyCharacterWords():
    for line in fin:
        words = line.strip()
        if len(words) >= 20:
            print(words)

TwentyCharacterWords()

'''9.2'''
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

has_no_e('library')

'''10.1'''
def nested_sum(lst):
    tot = 0
    for lmnt in lst:
        tot += sum(lmnt)
        return tot

p = [[6], [7], [9]]
print(nested_sum(p))

'''10.2'''
def consum(list):
    result = []
    for i in range(len(list)):
        result.append(sum(list[:i+1]))
    return result

e = [1, 2, 3]
consum(e)
