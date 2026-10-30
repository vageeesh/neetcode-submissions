class Trie:
    def __init__(self):
        self.childrens = {}
        self.is_last_word=False

class PrefixTree:

    def __init__(self):
        # each workd is a node
        self.root = Trie()

    def insert(self, word: str) -> None:
        # each work is a node, so check each if exists else create new node
        tmp_root = self.root
        for each_w in word:
            if each_w in tmp_root.childrens:
                # if presen then update the root and keep checking its childrens
                tmp_root = tmp_root.childrens[each_w]
            else:
                # inser new word and make the value as node again
                # so in we can insert child of child
                tmp_root.childrens[each_w] = Trie()
                tmp_root = tmp_root.childrens[each_w]


        # at the end set as last word for th last word in node
        # this is useful later for searching
        tmp_root.is_last_word = True


    def search(self, word: str) -> bool:
        tmp_root = self.root
        for each_w in word:
            if each_w in tmp_root.childrens:
                tmp_root = tmp_root.childrens[each_w]
            else:
                return False

        # if above completed without return, then word exists
        # now we have to check if word in Tries ends, if yes then only its full word not sub-word, so check and return
        if tmp_root.is_last_word:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        tmp_root = self.root
        for each_w in prefix:
            if each_w in tmp_root.childrens:
                tmp_root = tmp_root.childrens[each_w]
            else:
                return False

        # no need to check endswith because its check with match only not full-word
        return True
        
        