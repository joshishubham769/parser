import nltk
from nltk.tokenize import word_tokenize 
import sys

punctuation={'.',',',':','"',';','!'}

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP |S Conj S
NP -> N | Det NP | Adj NP | Det Adj NP | NP Conj NP | N NP
VP -> V | Adv VP | V Adv | VP NP | VP P NP | VP Conj VP | VP P NP | VP Adv P NP | Det VP | VP NP Adv
"""


grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        print()
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(s):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    s=s.lower()
    s=word_tokenize(s)
    
    for word in s:
    #print(word in punctuation)   
   
        try:
            i=int(word)
            s.remove(word)
        except ValueError:
            if word in punctuation:
                s.remove(word)
            else:
                flag=False
                for char in word:
                    if ord('a')<=ord(char)<=ord('z'):
                        flag=True
                if flag==False:
                    s.remove(word)
                    
    return s
    raise NotImplementedError

def get_np(tree,lst,flag):
    #if there is no NP add to list and return
    #bool t=True
        
    for i in range(len(tree)):
        try:
            if tree[i].label()=='NP':
                get_np(tree[i],lst,True)
            elif tree[i].label()=='VP':
                get_np(tree[i],lst,False)
            else:
                if flag:
                    lst.append(tree[i])
        except:
            continue
            
 
    #else go for all sub_trees
def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    lst=[]
    for i in range(len(tree)):
        if tree[i].label()=='NP':
            get_np(tree[i],lst,True)
        else:
            get_np(tree[i],lst,False)
    
    return lst
        
    raise NotImplementedError


if __name__ == "__main__":
    main()
