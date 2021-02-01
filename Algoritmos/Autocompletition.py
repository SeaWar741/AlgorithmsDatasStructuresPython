#Class for the nodes
class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}
    
    
    #this is a class for prefixes
    def all_words(self,prefix):
        if self.end:
            yield prefix
        
        for letter,child in self.children.items():
            yield from child.all_words(prefix + letter)
            

#class for the Trie
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    #inserts into the Tire structure
    def insert(self,word):
        curr = self.root
        for letter in word: #iterates and inserts into structured nodes
            node = curr.children.get(letter)
            if not node:
                node = TrieNode()
                curr.children[letter] = node
            curr = node
        curr.end = True
        
        
    #iterates over nodes to get prefixes
    def getWords(self,prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return
        yield from cur.all_words(prefix)



#Solution 
def solution(searchPrefix, listOfwords):
    # Please write your code here.
    wordsData = Trie()
    
    #if the array isnt sorted then two possibilities could be applied
    
    #first (native implementation)
    #listOfwords.sort()
    
    #second (quickSort or any other algorithm)
    #quicksort(listOfwords)
    
    #inserting the list of words into nodes
    #this is o(n) complexity
    for word in listOfwords:
        wordsData.insert(word)
    
    #calling the method to get words from prefix
    #implementing the longest prefix possible could increase performance
    resultsQuery = list(wordsData.getWords(searchPrefix))
    
    #checks if the query gives an empty array or not
    #thus giving noMatches or the matches
    if len(resultsQuery) != 0:
        return resultsQuery
    else:
        return ["noMatches"]



streamers = ["Ninja","Fedmyster","Pokimane","Tfue","Shroud","DrDisrespect","DrLupo","Dakotaz","Fernanflo","Lilypichu","Michaelreeves"]
print(solution("Dr",streamers))
