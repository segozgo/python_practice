#https://google.com

sentence1 ='https://google.com'
sentence2 = sentence1.replace('https://', '')
sentence3 = sentence2.index('.')

password_word1 = sentence2[:sentence3]
password_word2 = password_word1[:3]
password_word_nof_len = len(password_word1)
password_nof_e = password_word1.count('e')

print(password_word2 + str(password_word_nof_len) + str(password_nof_e) + '!')
print(str(f'{password_word2}{password_word_nof_len}{password_nof_e}') + '!')