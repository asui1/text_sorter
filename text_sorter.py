
#word list = [[단어, 횟수], [단어, 횟수], [단어, 횟수], [단어, 횟수], [단어, 횟수]... ]
#cur_word : 스페이스나 숫자 등 이 나오기 전까지의 누적 알파벳들.
given_file = open("given_file.txt", 'r')

while True:
    line_read = given_file.read_line()
    if not line: break
    
given_file.close()

result = open("given_name.xlsx", 'w')

result.close()


