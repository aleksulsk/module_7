class WordsFinder:
    file_name = "test_file.txt"
    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        words = []
        str_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as opener:
                for line in opener:
                    line = line.lower()
                    for p in str_punctuation:
                        line = line.replace(p, ' ')
                        if p in line:
                            line = line.replace(p, ' ')
                    split_line = line.split(sep=' ')
                    split_line = list(filter(lambda x: x != '', split_line))
                    words.append(split_line)
        sorted_list = [x for y in words for x in y]
        all_words[self.file_name] = sorted_list
        return all_words

    def find(self, word):
        word_acc = {}

        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower()) + 1  # Позиция с 1
                word_acc[file_name] = position

        return word_acc

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[name] = count

        return result


finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
