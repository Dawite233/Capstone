class solution_words:
    def solve(self, words):
        d = "".join(word[0].upper() + word[1:].lower() for word in words )
        return d[0].lower() + d[1:]

od = solution_words()
print('This is a program that turns a sentence into camel case')
words = input(" Plase write one sentence! ")
print(od.solve(words.title()))