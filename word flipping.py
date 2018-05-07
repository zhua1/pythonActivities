# Word/Letter Challenge
import string
##################################################################################################
input_ = "Mother's Day is comming, but I don't know what to get mommy."

word = input_.split()

li = []

for word_ in word:
    # Check if the word contains punctuation
    if any(word in string.punctuation for word in word_):
        # Get rid of the punctuation and flip
        word__ = ''.join([w for w in word_ if w not in string.punctuation])
        flip = []
        for i in range(len(word__)):
            flip.append(word__[len(word__)-i-1])
        li.append(''.join(flip))
        
    else:
        word__ = []
        for i in range(len(word_)):
            word__.append(word_[len(word_)-i-1])
        li.append(''.join(word__))

fin = ' '.join(li)

punc_idx = []
punc_val = []

# Get punctuation index and value
for i in range(len(input_)):
    if(input_[i] in string.punctuation):
        punc_idx.append(i)
        punc_val.append(input_[i])

def insert(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

for i in range(len(punc_idx)):
    fin = insert(fin, punc_val[i], punc_idx[i])

print(fin)