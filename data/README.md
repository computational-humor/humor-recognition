# Datasets for humor recognition


FUN dataset
========

The dataset of humorous and non-humorous texts for Russian languages. 
License is MIT.

Jokes and funny dialogues were collected from various open online resources and carefully complemented 
with unfunny textswith similar lexical properties.

The  dataset comprises  of  more  than  312,877 short texts.  

Manual annotation of about 2,000 items proved the reliability of corpus 
construction approach. 

Fun dataset is partitioned into train and test parts (80% and 20% respectively)

The dataset is represented by the following data files:

File | Download |Description | Size (Jokes/Non-Jokes) | 
---- | -------- | -----------| -----------
`test` | [JSON](data/FUN-dataset/test.json) | Test part (20%). | 61794 (30897 jokes and 30897 non-humorous texts)|
`train` | [JSON](data/FUN-dataset/train.json)| Train part (80%). | 251416 (125708 jokes and 125708 non-humorous texts)|
`assessed` | [JSON](data/FUN-dataset/assessed.json) | Manually assessed part. | 1877 (899 jokes and 978 non-humorous texts)|


GOLD part
------
Manually assessed 1877 texts from Fun dataset.

The evaluation  was condacted using  an  online  interface, where 1,000 random jokes and 1,000 random non-jokes were assessed 
on a 3-point scale: 
‘not a joke’,  ‘an unfunny joke’ and ‘a joke’.  

More than 100  volunteers  took part in the assessment process resulted in 1,877  examples being labeled by at least three assessors. 


Citing
------

::

    Blinov et al: Large Dataset and Language Model Fun-tuning for Humor Recognition // ACL,
    (2019).


BibTeX::

   @inproceedings{
      year={2019},
      title={Large Dataset and Language Model Fun-tuning for Humor Recognition},
      author={Blinov, Vladislav and Baranova-Bolotova, Valeriia and Braslavski, Pavel},
      language={English},
      booktitle = {ACL},

   }

Loading in python 
------
```python
from data import load_test, load_gold, load_train, load_fun_dataset

gold_part = load_gold() 
fun_dataset = load_fun_dataset() # or call load_test() or load_train() for test or train part

print 'Manually assessed data size: {}'.format(len(gold_part))
print 'Fun dataset size: {}'.format(len(fun_dataset))

```
