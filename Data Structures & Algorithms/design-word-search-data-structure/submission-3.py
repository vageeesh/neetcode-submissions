class Node:
    def __init__(self):
        self.child = {}
        self.is_last = False

class WordDictionary:

    def __init__(self):
        self.r = Node()

    def addWord(self, word: str) -> None:
        t = self.r
        for each in word:
            if each not in t.child:
                # add
                t.child[each] = Node()
        
            # increment[this will cover both if word present or not present]
            t = t.child[each]

        # at end add is_last flag
        t.is_last = True

    def search(self, word: str) -> bool:
        t = self.r

        # since we have "." match that means we have to recursilvely check and backtrack, so iteration will be problem and recurssion is best
        def dfs(st_index, node):

            root_node = node

            for i in range(st_index, len(word)):
                if word[i] == '.':
                    # can be matched to any
                    # here i have to check for all in this level
                    # in a loop i will match with all the childs and continue
                    for each_c in root_node.child:
                        # for each children i have to recursilvely do the DFS
                        if dfs(1+i, root_node.child[each_c]):
                            return True
                    return False
                else:
                    if word[i] not in root_node.child:
                        return False
  
                    root_node = root_node.child[word[i]]


            # for both the cases return the result of last word
            return root_node.is_last

        return dfs(0, t)
        
