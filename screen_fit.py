class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        NumberOfCycles = 0
        NextWordRunner = 0
        PrevNextWordRunner = 0
        Buffer = []
        ListOfRows = []
        for i in range(rows):
            print i,(NextWordRunner - PrevNextWordRunner)/len(sentence), len(Buffer), Buffer

            Buffer = [NextWordRunner % len(sentence), NextWordRunner % len(sentence)]
            PrevNextWordRunner = NextWordRunner
            BufferSize = 0
            while BufferSize + len(Buffer) + len(sentence[NextWordRunner % len(sentence)]) <= cols:
                    
                Buffer[1] = NextWordRunner % len(sentence)
                NextWordRunner += 1
                BufferSize = sum([len(sentence[x]) for x in range(Buffer[0],Buffer[1]+1)])
                print Buffer
            """      
                    if sum(Buffer) + 1 <= cols: 
                        Buffer = Buffer + ['-']
                else:
                    Buffer += (cols - sum(Buffer)) * ['-']
            """
            
            for B in xrange(len(ListOfRows)):
                if Buffer == ListOfRows[B][0]:
                    #print B,Buffer
                    return (ListOfRows[B][2] + (rows - B) * (PrevNextWordRunner - ListOfRows[B][2]) /(i - B)) / len(sentence)
                
            ListOfRows.append([Buffer,i, PrevNextWordRunner])
            
        return NextWordRunner/len(sentence)


sentence, rows, cols = ["a", "bcd", "e"] , 3, 6
x = Solution()
x.wordsTyping(sentence,rows,cols)