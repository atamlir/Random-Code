import re
import itertools

class Vector(object):
        
	@staticmethod
	def multi(a,b):
		return [a[i] * b[i] for i in xrange(len(a))]

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def convert_word_to_abbriv(word,fixed_letters):

        	binary_rep = list(fixed_letters[2:])
        	for i in xrange(len(fixed_letters)-2):
        		if fixed_letters[i+2] == '1':
        			binary_rep[i] = word[i]
        	return re.sub('0+',lambda x: str(len(x.group())),''.join(binary_rep))

            
        if word == '':
        	return ['']

        abbriv_words = []
        v_len = '#0{0}b'.format(len(word)+2)
        for i in xrange(1<<len(word)):
        	j = format(i,v_len)
        	abbr_word = convert_word_to_abbriv(word,j)
        	abbriv_words.append(abbr_word)
        return abbriv_words

sol = Solution()
sol.generateAbbreviations('word')


print Vector.multi([1,1],[2,3])
"""
sol 1
class Solution(object):
    def generateAbbreviations(self, word):

        def convert_word_to_abbriv(word,fixed_letters):
            binary_rep = ['0'] * len(word)
            for i in fixed_letters:
                binary_rep[i] = word[i]
            return re.sub('0+',lambda x: str(len(x.group())),''.join(binary_rep))

            
                
        abbriv_words = [word,str(len(word))]
        for i in xrange(1,len(word)):
            for j in itertools.combinations(range(len(word)),i):
                abbr_word = convert_word_to_abbriv(word,j)
                abbriv_words.append(abbr_word)
        print abbriv_words
        return abbriv_words

"""

"""
sol 2

import re
import itertools

class Solution(object):
    def generateAbbreviations(self, word):
        def convert_word_to_abbriv(word,fixed_letters):

        	binary_rep = list(fixed_letters[2:])
        	for i in xrange(len(fixed_letters)-2):
        		if fixed_letters[i+2] == '1':
        			binary_rep[i] = word[i]
        	return re.sub('0+',lambda x: str(len(x.group())),''.join(binary_rep))

            
        if word == '':
        	return ['']

        abbriv_words = []
        v_len = '#0{0}b'.format(len(word)+2)
        for i in xrange(1<<len(word)):
        	j = format(i,v_len)
        	abbr_word = convert_word_to_abbriv(word,j)
        	abbriv_words.append(abbr_word)
        return abbriv_words
"""
