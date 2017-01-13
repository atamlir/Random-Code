class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tri = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        def recurs(s,i):
            if i>= len(s):
                return 0
            d = {}
            d[s[i]] = recurs(s,i + 1)
            return d
            
        t = self.tri 
        if len(word) == 0: 
            return 
        
        if len(t) == 0: 
            self.tri = recurs(word + '$',0)
        else:
            word = word + '$'
            p = 0 
            d = self.tri
            for i in word:
                if i in d:
                    d = d[i]
                    p += 1
                else: 
                    d[i] = recurs(word, p+1)
                    break
            
        print self.tri
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def research(word,i,d):
            if i >= len(word):
                return True
            if d == 0 :
                return False

            if word[i] == '.':
                x = False
                for j in d:
                    x = x or research(word,i+1,d[j])
                return x
            else:
                return word[i] in d and research(word,i+1,d[word[i]])

        if len(word) == 0: 
            return True
        word = word + '$'

        return research(word,0,self.tri)

x = WordDictionary()
x.addWord("at")
x.addWord("and")
x.addWord("an")
x.addWord("add")
print x.search("a")
print x.search(".at")
x.addWord("bat")
print x.search(".at")
print x.search("an.")
print x.search("a.d.")
print x.search("b.")
print x.search("a.d")
print x.search(".")





