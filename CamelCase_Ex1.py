class words:
   def solution(self, words):
      D = "".join(word[0].upper() + word[1:].lower() for word in words)
      return D[0].lower() + D[1:]
ob = words()
words = ["Hello", "MCTC", "Python", "Programming", "Students"]
print(ob.solution(words))