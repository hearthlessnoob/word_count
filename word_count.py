#crée en 2023
#crée par Kevin
#tp1/word_count

#fonction + variable
word = input()
def count_word(word):
    #.count compte le nb d'un caractere spécifique dans une variable
    nb_word = word.count(" ")
    return nb_word + 1

print(count_word(word))


