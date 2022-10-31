'''11.1'''
fin = open('Week6_dict_text.txt')
'''not working'''
def create_dict_from_txt():
    dtxt_dict = dict()
    for line in file:
        (key, value) = line.split()
        txt_dict[int(key)] = value
        return dtxt_dict
create_dict_from_txt()

'''working'''
def dict_from_txt():
    txt_dict = dict()
    fin = open('Week6_dict_text.txt')
    for line in fin:
        word = line.strip()
        txt_dict[word] = word
        return txt_dict
list(dict_from_txt())

'''12.1'''

def most_frequent(string):
    d = dict()
    for key in string:
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d

most_frequent('cccctttttvvv')
'''does not sort in reverse of frequency'''


