
#word list = [[단어, 횟수], [단어, 횟수], [단어, 횟수], [단어, 횟수], [단어, 횟수]... ]
#cur_word : 스페이스나 숫자 등 이 나오기 전까지의 누적 알파벳들.

class dicList():
    def __init__(self,  is_alpha,  check_mis):
        self.word_dict = {}
        self.is_alpha = is_alpha
        self.check_mis = check_mis

    def add_word(self, word):
        if word in self.word_dict:
            self.word_dict[word] += 1
        else:
            self.word_dict[word] = 1

    def print_dic(self):
        for keys, values in self.word_dict.items():
            print(keys + " : " + values)
        

f = open("given_file.txt", 'r')
word_list = dicList(True, False)
while True:
    line_read = f.readlines()
    cur_word = ""
    for i in line_read:
        if i.isalpha():
            cur_word += i.lower()
        else:
            word_list.add_word(cur_word)
            cur_word = ""
    if not line: break
    
given_file.close()

word_list.print_dic()

#result = open("given_name.xlsx", 'w')

#result.close()


