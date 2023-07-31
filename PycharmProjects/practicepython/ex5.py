# import spacy

# Load English tokenizer, tagger,
# parser, NER and word vectors
# nlp1 = spacy.load("en_core_web_sm")

# Process whole documents
b=['Modeling',
 ':',
 'Design',
 ',',
 'build',
 'and',
 'improve',
 'machine',
 'learning',
 'models',
 '.',
 'Work',
 'end',
 'to',
 'end',
 'from',
 'data',
 'collection',
 ',',
 'feature',
 'generation',
 'and',
 'selection',
 ',',
 'algorithm',
 'development',
 ',',
 'forecasting',
 ',',
 'visualization',
 'and',
 'communicating',
 'of',
 'model',
 'results',
 '.',
 'Collaborate',
 'with',
 'engineering',
 'to',
 'productionize',
 'models',
 '.',
 'Drive',
 'experimentation',
 'to',
 'test',
 'impact',
 'of',
 'model',
 'based',
 'optimization']

big_toke=['Design', 'models', 'Work', 'results', 'Collaborate', 'models', 'Drive', 'optimization']
big_toke_index= [2, 9, 11, 34, 36, 41, 43, 51]

d=['Design', 'machine learning', 'forecasting']
aaa=['NOUN', 'PUNCT', 'NOUN', 'PUNCT', 'VERB', 'CCONJ', 'VERB', 'NOUN', 'NOUN', 'NOUN', 'PUNCT', 'SPACE', 'PROPN', 'NOUN', 'PART', 'VERB', 'ADP', 'NOUN', 'NOUN', 'PUNCT', 'NOUN', 'NOUN', 'CCONJ', 'NOUN', 'PUNCT', 'PROPN', 'PROPN', 'PUNCT', 'NOUN', 'PUNCT', 'NOUN', 'CCONJ', 'NOUN', 'ADP', 'NOUN', 'NOUN', 'PUNCT', 'SPACE', 'NOUN', 'ADP', 'NOUN', 'PART', 'VERB', 'NOUN', 'PUNCT', 'SPACE', 'NOUN', 'NOUN', 'PART', 'VERB', 'NOUN', 'ADP', 'NOUN', 'VERB', 'NOUN', 'PUNCT']
for i in aaa:
 if i == 'SPACE':
  aaa.remove(i)

skill=[]
process= []
for i in range(0,len(big_toke_index),2):

    tam = aaa[big_toke_index[i]:big_toke_index[i+1]+1]
    tam1 = b[big_toke_index[i]:big_toke_index[i+1]+1]

    for i in range(len(tam)):
     if d.__contains__(tam1[i]):
       process.append(tam)
       skill.append(tam1)
       break
print(process)
print(skill)
final = []
for i in process:
 for j in range(1,len(i)-1):
  if i[j] =='NOUN' and (i[j+1] =='PUNCT' or skill[process.index(i)][j+1]=='and' ):
   final.append(skill[process.index(i)][j ])
  if (i[j] =='PUNCT' or skill[process.index(i)][j]=='and') and i[j+1] =='NOUN':
   final.append(skill[process.index(i)][j +1])


print(set(final))





