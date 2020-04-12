import time
import sys
import os
import itertools
import re
import unidecode

# Keep some interesting statistics
NodeCount = 0

# The Trie data structure keeps a set of words, organized with one node for
# each letter. Each node has a branch for each letter that may follow it in the
# set of words.
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

        global NodeCount
        NodeCount += 1

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()

            node = node.children[letter]

        node.word = word

trie = TrieNode()

# The search function returns a list of all words that are less than the given
# maximum distance from the target word
def search( word, maxCost ):

    # build first row
    currentRow = range( len(word) + 1 )

    results = []

    # recursively search each branch of the trie
    for letter in trie.children:
        searchRecursive( trie.children[letter], letter, word, currentRow,
            results, maxCost )

    return results

# This recursive helper is used by the search function above. It assumes that
# the previousRow has been filled in already.
def searchRecursive( node, letter, word, previousRow, results, maxCost ):

    columns = len( word ) + 1
    currentRow = [ previousRow[0] + 1 ]

    # Build one row for the letter, with a column for each letter in the target
    # word, plus one for the empty string at column 0
    for column in range(1,columns):

        deleteCost = previousRow[column] + 1
        insertCost = currentRow[column - 1] + 1

        if unidecode.unidecode(word[column - 1].lower()) != unidecode.unidecode(letter.lower()):
            coûtSubstitution = 1
        else:
            coûtSubstitution = 0

        replaceCost = previousRow[ column - 1 ] + coûtSubstitution

        currentRow.append( min( insertCost, deleteCost, replaceCost ) )

    # if the last entry in the row indicates the optimal cost is less than the
    # maximum cost, and there is a word in this trie node, then add it.
    if currentRow[-1] <= maxCost and node.word != None:
        results.append( (node.word, currentRow[-1] ) )

    # if any entries in the row are less than the maximum cost, then
    # recursively search each branch of the trie
    if min( currentRow ) <= maxCost:
        for letter in node.children:
            searchRecursive( node.children[letter], letter, word, currentRow,
                results, maxCost )

def process_dictionnary():
    dictionary = open("./calibre_clean_author/data/data.txt", "r")
    WordCount = 0

    # read dictionary file into a trie
    for word in dictionary:
        # print(word)
        WordCount += 1
        trie.insert(word.rstrip())
    # print("Read %d words into %d nodes" % (WordCount, NodeCount))

def run_spell_checking(target, max_cost):
    start = time.time()
    results = search(target, max_cost)
    end = time.time()

    # print("Search took %g s" % (end - start))
    return results

'''
Faire un arbre reverse pour les trop long
Faire un arbre avec différents degré de pliage
Faire un arbre avec les noms de famille uniquement
Lire les titres si trop long
'''
def process_author(name):
    regex_comma = re.search(r'(.*),\s*(.*)',name)
    seperator = ' '

    for max_c in range(0,3):
        if regex_comma:
            author_string_test_1 = regex_comma.group(1) + " " + regex_comma.group(2)
            author_string_test_2 = regex_comma.group(2) + " " + regex_comma.group(1)

            results = run_spell_checking(author_string_test_1,max_c)
            # print(results)
            if(results != []):
                return 1;
            results = run_spell_checking(author_string_test_2,max_c)
            # print(results)
            if(results != []):
                return 1;
        else:
            author_split = [x.strip() for x in name.split(' ')]
            len_author_split = len(author_split)

            if len_author_split <= 3:
                perm_list_mask = list(itertools.permutations([i for i in range(1,len_author_split+1)]))
                for pl in perm_list_mask:
                    perm_list = [x for _,x in sorted(zip(pl,author_split))]
                    author_string_test = seperator.join(perm_list)

                    results = run_spell_checking(author_string_test, max_c)
                    # print(results)
                    if(results != []):
                        return 1;
            else :
                # print("trop long !")
                pass

    return 0;


def run():
    i = 1
    well_processed = 0
    file_list = os.listdir("/home/adrien/Bibliothèque_calibre")
    file_list = ["Adrien BLASIAU (de la coco)"]
    len_file_list = len(file_list)

    process_dictionnary()

    for name in file_list:
        percentage = (i/len_file_list)*100
        name = name.strip()
        name = " ".join(name.split())
        name = unidecode.unidecode(name)
        name = re.sub(r'\([^)]*\)', '', name)

        valid = process_author(name)
        well_processed += valid
        if valid == 0:
            print("["+str(i)+" over "+str(len_file_list)+"]"+" / Before : ",name," / percentage_ok: ",well_processed/i," %")
        i+=1
    print(well_processed)
run()

#0.8368352412693812 avec 2
#0.8401680915809303 avec 2 + accent modifié
#0.845317483328501 avec 2 + accent modifié + 5 nombre mots
#0.8553203827196288 avec 2 + accent modifiée + nouvelle db