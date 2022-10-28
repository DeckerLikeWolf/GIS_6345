'''corrected 8.2'''
word = 'banana'
print(word.count('a'))
for letter in word:
    if letter == 'a':
        count = count + 1


'''8.3'''
def is_palindrome(word):
    word = str(word)
    backwards = word[::-1]
    if backwards != word:
        return False
    else: return True

'''Corrected 8.3'''
def is_palindrome1(word):
    return word == word[::-1]

is_palindrome1('elle')