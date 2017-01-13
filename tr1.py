class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        def r_insert(word,i):
            if len(word) <= i:
                return 0
            
            d = {}
            d[word[i]] = r_insert(word,i+1)
            
            return d
            
        if len(word) == 0:
            return 
        
        d = self.root.d
        word = word + '$'
        
        for i in xrange(len(word)):
            if word[i] in d:
                d = d[word[i]]
            else:
                d[word[i]] = r_insert(word,i+1)
                break

        print self.root.d
        return
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        def r_search(word,i,d):
            if len(word) <= i:
                return True
            
            if d == 0:
                return False
                
            return (word[i] in d) and r_search(word,i+1,d[word[i]])
            
        tri = self.root.d
        if len(word) == 0: 
            return True
            
        if len(tri) == 0:
            return False
        
        return r_search(word + '$',0,tri)
            
    def words_start_with(self,prefix):


        def words(d):
            if d == 0:
                return [""]

            ls = []
            for i in d: 
                if i == '$':
                    ls.extend([ ""])
                else:
                    ls.extend([i + x for x in words(d[i])])

            print(ls)
            return ls

        tri = self.root.d
        
        if len(tri) == 0:
            return None

        for i in xrange(len(prefix)):
            if tri != 0 and prefix[i] in tri:
                tri = tri[prefix[i]]
            else:
                return None
        ls = []

        ls.extend([prefix +  x for x in words(tri)]) 

        return ls


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tri = self.root.d
        
        
        if len(prefix) == 0: 
            return True
            
        if len(tri) == 0:
            return False
         
        p = 0
        
        for i in xrange(len(prefix)):
            if tri != 0 and prefix[i] in tri:
                tri = tri[prefix[i]]
            else:
                return False
       
        return True

x = Trie()
x.insert("no")
x.insert("nop")
x.insert('n')
print x.startsWith('nopno')
print x.search("alex")
x.insert('alex')
print x.search("ale")
print x.startsWith('ale')
print x.words_start_with('no')
