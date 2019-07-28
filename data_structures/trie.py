# https://github.com/nepsilon/Python-Trie
# https://www.youtube.com/watch?v=zIjfhVPRZCg


class Node():
    def __init__(self, value):
        self.childs = list()
        self.value = value
        self.terminal = False


class Trie():
    def __init__(self):
        self.root = Node('.')
        self.curr = self.root

    def __insert_letter(self, head, l):
        for c in head.childs:
            if c.value == l:
                return c
        else:
            n = Node(l)
            head.childs.append(n)
            return n

    def insert(self, word):
        self.curr = self.root
        for l in word:
            self.curr = self.__insert_letter(self.curr, l)
        self.curr.terminal = True

    def dump(self, i=0):
        print(self.curr.value)
        if self.curr.terminal:
            print
            print(" "*i)
        for c in self.curr.childs:
            self.curr = c
            self.dump(i+2)
        self.curr = self.root

    def has_word(self, w):
        self.curr = self.root
        for l in w:
            for x in self.curr.childs:
                if x.value == l:
                    self.curr = x
                    break
            else:
                return False

        if self.curr.terminal:
            return True
        else:
            return False

    def has_prefix(self, w):
        self.curr = self.root
        for l in w:
            for x in self.curr.childs:
                if x.value == l:
                    self.curr = x
                    break
            else:
                return False
        return True


'''
>>> from trie import Trie
>>> foo = Trie()
>>> foo.insert('bahamas')
>>> foo.insert('banana')
>>> foo.has_prefix('ba')
True
>>> foo.has_prefix('bahamas')
True
>>> foo.has_prefix('bai')
False
>>> foo.has_word('banana')
True
>>> foo.has_word('ba')
False
>>> foo.has_word('BANANA')
False
>>> foo.dump()
. b a h a m a s
      n a n a
'''
