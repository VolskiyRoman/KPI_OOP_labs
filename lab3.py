
class Myclass:
    def __init__(self):
        self.dictionary = None
        self.s_words = None
        self.sorted_list = []
        self.s = input("Введіть текст: ")
        vowels_str = "a e i o u y а е є и і ї о у ю я ё э ы A E I O U Y А Е Є И І Ї О У Ю Я Ё Э Ы"
        self.vovels = vowels_str.split(" ")
        punctuation_str = '''. , - : ; ( ) [ ] { } ! ? < >'''
        self.punctuation_list = punctuation_str.split(" ")

    def s_words_gen(self):
        self.s_words = (self.s.split(" "))

    def vovels_check(self):
        self.dictionary = {}
        for i in self.s_words:
            vovel_count = 0
            for j in list(i):
                if j in self.vovels:
                    vovel_count += 1
            update = {i: vovel_count}
            self.dictionary.update(update)

    def get_sorted(self):
        s_dict = sorted(self.dictionary.items(), key=lambda x: x[1])
        sorted_dict = {k: v for k, v in s_dict}

        print("Результат:")
        for i in sorted_dict.keys():
            self.sorted_list.append(i)

    def punctuation(self):
        punc_list = []
        for i in self.sorted_list:
            word = list(i)
            for j in word:
                if j in self.punctuation_list:
                    word.remove(j)
            word = "".join(word)
            punc_list.append(word)
        print(", ".join(punc_list))


obj = Myclass()
obj.s_words_gen()
obj.vovels_check()
obj.get_sorted()
obj.punctuation()


