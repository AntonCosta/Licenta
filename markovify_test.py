import glob
import tkinter
import markovify
import os
from tkinter import *



def createText(nrSentences=10, nrWords=150):
    text_model2 = None

    for filename in glob.glob(os.path.join('DataSet', '*.txt')):
        with open(filename, encoding='utf8') as f:
            print(filename)
            try:
                text = f.read()
            except UnicodeDecodeError as uniDecErr:
                continue
        text_model = markovify.Text(text)
        if text_model2:
            text_model2 = markovify.combine([text_model, text_model2])
        else:
            text_model2 = text_model

    for i in range(nrSentences):
        result = text_model2.make_short_sentence(nrWords)
        print(result)
        outp.insert(INSERT, result)


window = tkinter.Tk()
# Code to add widgets will go here...
window.geometry("800x600")
window.pack_propagate(0)

variable = StringVar(window)
variable.set("one") # default value



w = OptionMenu(window, variable, "one", "two", "three")
nrSentences = Entry(window)
nrWords = Entry(window)
sentences = Label(window, text = "Number of sentences:")
words = Label(window, text = "Number of words per sentence:")
sentences.place(x=200, y=0)
words.place(x=150, y=20)


w.place(x=0, y=10)
nrSentences.pack()
nrWords.pack()

button = Button(window, text="Print Me", command=lambda: createText(int(nrSentences.get()), int(nrWords.get())))
button.pack()

outp = Text(window, height=24, width=100)
outp.config(wrap=WORD)
outp.place(x=0, y=200)








# # Get raw text as string.
# with open('kidStories.txt', encoding='utf8') as f:
#     text = f.read()
#
#
# with open('fiftyShadesOfGrey.txt', encoding='utf8') as f:
#     text2 = f.read()
#
# # Build the model.
# text_model = markovify.Text(text)
# text_model2 = markovify.Text(text2)
# #
# test_model3 = markovify.combine([text_model, text_model2])
# Print five randomly-generated sentences




# Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))


window.mainloop()