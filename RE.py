import spacy
from nltk import Tree
nlp = spacy.load('en')
from nltk.corpus import stopwords
sentence=u"Rahul loves Pizza. He likes to play football. He works in Mohali, His profile is Data Scientist."
text = ' '.join([word for word in sentence.split() if word not in (stopwords.words('english'))])
doc =nlp(text)

def tok_format(tok):
    return "_".join([tok.orth_, tok.tag_])


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(tok_format(node), [to_nltk_tree(child) for child in node.children])
    else:
        return tok_format(node)

a=[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]

from spacy.symbols import nsubj

def find_root_node():
    verbs = []
    for root_verb in doc:
        if root_verb.tag_ == "VBD" or root_verb.tag_ =="VB"or root_verb.tag_ =="VBG"  or root_verb.tag_ =="VBZ" or root_verb.tag_ =="VBP" or root_verb.tag_ =="VBN" or root_verb.tag_=="NN": 
            for subject in root_verb.children:
                if subject.dep == nsubj :
                    verbs.append(root_verb)
            for lft in root_verb.children or root_verb.children.children:
                print([w.text for w in root_verb.lefts  if w.tag_=="NNP"  or w.tag_=="NNPS"or w.tag_=="NNS" or w.tag_=="PRP" or"PRP$"]
                     ,[root_verb],[x.text for x in root_verb.rights if x.tag_=="NNP" or x.tag_=="NN" or x.tag_=="NNPS" or  x.tag_=="NNS"or x.tag_=="PRP"])
                break  

find_root_node()
