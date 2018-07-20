import re
import nltk
from nltk.tag.stanford import StanfordNERTagger
from tkinter import *

root = Tk()

tokenizerVariable = IntVar()
taggerVariable = IntVar()
output = StringVar()
tokenCountOutput = StringVar()
tokCt = IntVar()

root.title('Tokenizer and Tagger Utility App')
frame = Frame(root, width=400, height=650)

sentenceLabel = Label(frame, text="Click below to type your sentences:")

textArea = Text(frame, height=10, width=60, wrap=WORD, bd=5, insertborderwidth=20)

tokenizerLabel = Label(frame, text="Tokenizer")
taggerLabel = Label(frame, text="Tagger")

tokenizerFrame = Frame(frame)

wordTokenizerRB = Radiobutton(tokenizerFrame, text="Word Tokenizer", padx=20, variable=tokenizerVariable, value=1)
sentenceTokenizerRB = Radiobutton(tokenizerFrame, text="Sentence Tokenizer", padx=20, variable=tokenizerVariable, value=2)
tokenCountCB = Checkbutton(frame, text="Display token count.", variable=tokCt)
tokenizeButton = Button(frame, text="Tokenize")

outputLabel = Label(frame, text="", textvariable=output)
tokenCountLabel = Label(frame, text="", textvariable=tokenCountOutput)

taggerFrame = Frame(frame)

stanfordNerRB = Radiobutton(taggerFrame, text="Stanford NER", padx=20, variable=taggerVariable, value=1)
nltkPosRB = Radiobutton(taggerFrame, text="NLTK POS", padx=20, variable=taggerVariable, value=2)
posPatternRB = Radiobutton(taggerFrame, text="POS Pattern", padx=20, variable=taggerVariable, value=3)
tagButton = Button(frame, text="Tag")

sentenceLabel.grid(row=0, sticky=W)

textArea.grid(row=1, columnspan=2)

tokenizerLabel.grid(row=2, sticky=W)
taggerLabel.grid(row=2, column=1, sticky=W)

wordTokenizerRB.select()
stanfordNerRB.select()

wordTokenizerRB.grid(row=0, sticky=W)
sentenceTokenizerRB.grid(row=1, sticky=W)
tokenizerFrame.grid(row=3, rowspan=2, sticky=W)
tokenCountCB.grid(row=5, sticky=W)

def tokenize(event):
    sentence = textArea.get("1.0",END)
    tokens = []
    ct = ''

    if tokenizerVariable.get() == 1:
        tokens = nltk.word_tokenize(sentence)
    else:
        tokens = nltk.sent_tokenize(sentence)

    if tokCt.get() == 1:
        ct = 'Token count: ' + str(len(tokens))
    else:
        ct = ''

    output.set(str(tokens))
    tokenCountOutput.set(ct)

def tag(event):
    sentence = textArea.get("1.0",END)
    jar = '/Applications/stanford-ner-tagger/stanford-ner-3.9.1.jar'
    model = '/Applications/stanford-ner-tagger/ner-model-english.ser.gz'
    nerTagger = StanfordNERTagger(model, jar, encoding='utf-8')

    tokens = nltk.word_tokenize(sentence)
    tagged = []

    if taggerVariable.get() == 1:
        tagged = nerTagger.tag(tokens)
    elif taggerVariable.get() == 2:
        tagged = nltk.pos_tag(tokens)
    else:
        tagged = ['Feature still unavailable']

    output.set(str(tagged))

tokenizeButton.bind("<Button-1>", tokenize)
tokenizeButton.grid(row=6)

outputLabel.grid(row=7, sticky = W)
tokenCountLabel.grid(row=8, sticky=W)

stanfordNerRB.grid(row=0, sticky=W)
nltkPosRB.grid(row=1,sticky=W)
posPatternRB.grid(row=2,sticky=W)

taggerFrame.grid(row=3, column=1, rowspan=3)

tagButton.bind("<Button-1>", tag)
tagButton.grid(row=6, column=1)
frame.pack()

root.mainloop()
