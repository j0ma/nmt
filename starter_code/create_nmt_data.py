from processor import *
import itertools as it
import pickle
import os

flatten = lambda nested: list(it.chain.from_iterable(nested))

OUTPUT_FOLDER = './training_data'

if not os.path.exists(f'{OUTPUT_FOLDER}'):
    os.system(f'mkdir -p {OUTPUT_FOLDER}')

print("Loading data...")
data = load_data('./data/')

# decompose to train/dev/test
print('Decomposing to train/dev/test...')
train_sents, train_trees = data['train']
dev_sents, dev_trees = data['dev']
test_sents, test_trees = data['test']

# linearize trees 
print('Linearizing trees...')
train_lin_trees = [linearize_parse_tree(t) for t in train_trees]
dev_lin_trees = [linearize_parse_tree(t) for t in dev_trees]
test_lin_trees = [linearize_parse_tree(t) for t in test_trees]

# create lines
print('Creating lines of text...')
create_line = lambda tokens: " ".join(tokens)
train_file = "\n".join(create_line(s) for s in train_sents)
dev_file = "\n".join(create_line(s) for s in dev_sents)
test_file = "\n".join(create_line(s) for s in test_sents)

# create vocabs
all_sents = train_sents + dev_sents + test_sents
all_tokens = list(set(flatten(all_sents)))
token_vocab = "\n".join(all_tokens)

all_lin_trees = train_lin_trees + dev_lin_trees + test_lin_trees
all_lintree_tokens = list(set(flatten(all_lin_trees)))
lintree_vocab = "\n".join(all_lintree_tokens)

NAMES = ['train', 'dev', 'test']
TREES = [train_trees, dev_trees, test_trees]
LIN_TREES = [train_lin_trees, dev_lin_trees, test_lin_trees]
FILES = [train_file, dev_file, test_file]

print('Dumping trees')
for name, tree in zip(NAMES, TREES):
    with open(f"{OUTPUT_FOLDER}/tree.{name}", 'wb') as f:
        pickle.dump(tree, f)

print('Dumping linearized trees')
for name, lintree in zip(NAMES, LIN_TREES):
    with open(f"{OUTPUT_FOLDER}/lin_tree.{name}", 'w') as f:
        one_per_line = "\n".join(create_line(t) for t in lintree)
        f.write(one_per_line)

print('Dumping sentence text')
for name, txt in zip(NAMES, FILES):
    with open(f'{OUTPUT_FOLDER}/text.{name}','w') as f:
        f.write(txt)

print('Dumping vocabulary...')
with open(f"{OUTPUT_FOLDER}/vocab", 'w') as f:
    f.write(token_vocab)

with open(f"{OUTPUT_FOLDER}/lin_tree_vocab", 'w') as f:
    f.write(lintree_vocab)
