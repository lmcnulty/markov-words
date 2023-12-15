# markov-words.py

Generates imaginary but plausible-sounding words:

```bash
$ markov-words.py --count 20 --no-apostrophes
pipe
taffy
Eisembinactions
ferabblier
circuitly
espee
Erid
elay
Meling
apped
sloosts
boisoms
stuteria
gulping
posthance
savoils
mooning
action
Tarth
resgives
```

## Dictionaries and Languages

This works for any language where words 
are composed of more than a few characters:

```bash
$ markov-words.py --count 5 --dictionary-file /usr/share/dict/french
pilués
évassent
ouassentâmes
émentasses
diapées
```

```bash
$ wget https://github.com/danakt/russian-words/raw/master/russian.txt
$ markov-words.py --count 5 --dictionary-file russian.txt --encoding 'windows-1251'
безводилануласт
ком
полного
больной
потрическую
```

```bash
$ ./markov-words.py --count 5 --dictionary-file /usr/share/dict/spanish
desoxismo
ñapote
enemadriciar
moteo
cumuleja
```

```bash
$ markov-words.py --count 5 --dictionary-file /usr/share/dict/swedish --encoding 'latin1'
ser
framträngd
förholmars
upptäcknekännes
barna
```

```bash
$ markov-words.py --count 5 --dictionary-file /usr/share/dict/italian
andogliato
trasassico
renevarla
simormassero
ete
```

## Randomness

The probability that a letter will occur in a word
depends on the frequency with which it follows after the $n$ previous letters
in dictionary words.
As $n$ increases, the results go from 
"completely random" to 
"somewhat interesting" to 
"exactly copying the dictionary".

```bash
$ markov-words.py -n 0 --count 5 --no-apostrophes
dteoaiunsoaseer
i
tiinrtfa
pcosunuenicrrsn
io
```

```bash
$ markov-words.py -n 1 --count 5 --no-apostrophes
bletin
Cakeahiacyordix
qunatinenomatho
Cogrtern
sswefaty
```

```bash
$ markov-words.py -n 2 --count 5 --no-apostrophes
stawers
lizes
stelchotogithro
supper
horgerliacizes
```

```bash
$ markov-words.py -n 3 --count 5 --no-apostrophes
chua
Quation
alodhoolybug
mists
Dnient
```

```bash
$ markov-words.py -n 4 --count 5 --no-apostrophes
aments
pronolines
garness
unmodify
germainley
```

```bash
$ markov-words.py -n 5 --count 5 --no-apostrophes
lightlier
panning
Sui
succumbs
outbalance
```

## Help

```
usage: markdov-words [-h] [-d DICTIONARY_FILE] [--no-apostrophes]
                     [--no-capitals] [--encoding ENCODING] [-c COUNT]
                     [-e END_BIAS] [-n N] [-l MAX_LENGTH]

options:
  -h, --help            show this help message and exit
  -d DICTIONARY_FILE, --dictionary-file DICTIONARY_FILE
                        Path to dictionary file -- A dictionary file is just
                        one containing a list of words separated by line-
                        breaks. On Unix systems these can usually be found in
                        /usr/share/dict/.
  --no-apostrophes      Exclude words with apostrophes from the dictionary
  --no-capitals         Exclude words starting with A-Z capital letters
  --encoding ENCODING   Number of words to print
  -c COUNT, --count COUNT
                        Number of words to print
  -e END_BIAS, --end-bias END_BIAS
                        Multiplier for the probability that a word will end at
                        a given point -- Note that sometime the probability is
                        zero, so setting this very high does not guarantee
                        that words will not be abnormally long.
  -n N, --n N           The number of previous letters to take into accountin
                        selecting the next one -- For high values of n, the
                        results are likely to exactly reproduce words in the
                        dictionary, whereas for lower values, they are likely
                        to sound implausible.
  -l MAX_LENGTH, --max-length MAX_LENGTH
                        Maximum length of a word, which if reached will simply
                        terminate the word, even if the ending is not a
                        probable one.
```

