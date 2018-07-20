# TokenizerTaggerUtilityApp
An NLP (Natural Language Processing) Application, which is a simple GUI app for tagging and tokenizing text, written in Python

<p align="center">
  <img src="imagesForUtilApp/Screen Shot 2018-07-20 at 12.52.07 AM.png" alt="img1" height=50% width=50%></img>
</p>

## Installation:
1. Install Python (if you have not done so: click <a href="http://www.greenteapress.com/thinkpython/swampy/install.html">here</a> for instructions)
2. Install Tkinter, which is used for Python GUI. The above link from #1 also contains instructions for the installation.
3. For the installation of NLTK (Natural Language Toolkit) and Stanford NER Tagger (Named Entity Recognition), click on this <a href=https://blog.sicara.com/train-ner-model-with-nltk-stanford-tagger-english-french-german-6d90573a9486>link</a>.

## Tokenization
This is the process of breaking down a text into (either word or sentence) tokens, depending on the option that you select. This app can also display the number of tokens the text has.

<p align="center">
  <img src="imagesForUtilApp/Screen Shot 2018-07-20 at 12.53.00 AM.png" alt="img2" height=50% width=50%></img>
</p>

This image above shows the tokenized text (in words), with the token count.

<p align="center">
  <img src="imagesForUtilApp/Screen Shot 2018-07-20 at 12.53.17 AM.png" alt="img2" height=50% width=50%></img>
</p>

This image above shows the tokenized text (in sentences).

## Tagging
Part of the blackboxing process of tagging is word tokenization, and for each token - it shall be tagged with a specific __tag__:
- Stanford NER - Stanford's Named Entity Recognition (__named entities__ can be thought of "brands"), can recognize and tag each token as '0' (i.e. not a named entity), 'PERSON' (name of a person), 'LOCATION' (name of a location), 'ORGANIZATION' (name of an organization), etc. It might not be perfect to detect every single named entity (or a false positive wherein it detects a named entity but is not), but most of the time it gets it right.
- NLTK POS - Part of the Natural Language Toolkit is Part-of-Speech tagging. While Stanford's NER algorithm specializes with named entities among nouns, NLTK's POS focuses on tagging each tokenized word (see <a href="http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html">here</a> for the complete list of tags).

<p align="center">
  <img src="imagesForUtilApp/Screen Shot 2018-07-20 at 12.54.02 AM.png" alt="img2" height=50% width=50%></img>
</p>

Above shows an image screenshot for tagging using Stanford's NER algorithm.

<p align="center">
  <img src="imagesForUtilApp/Screen Shot 2018-07-20 at 12.54.19 AM.png" alt="img2" height=50% width=50%></img>
</p>

Above shows an image screenshot for tagging using NLTK's POS algorithm.
