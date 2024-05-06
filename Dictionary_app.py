import customtkinter
from customtkinter import *
from ttkbootstrap import ttk , Style
import requests


def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = data[0]['meanings']
            definitions = []
            for meaning in meanings:
                definitions.append(f"• Meaning: {meaning['partOfSpeech']}\nDefinition: {meaning['definitions'][0]['definition']}\n")
            return '\n'.join(definitions)
        return "No Defintion found."

def search_definition():
    word = entry_word.get()
    defintion = get_definition(word)
    text_output.configure(state=NORMAL)
    text_output.delete('1.0', 'end')
    text_output.insert('end', defintion)
    text_output.configure(state=DISABLED, width=550, height=600)



root = CTk()
style = Style("flatly")
root.title("Dictionary app")

root.geometry("600x300")

frame_search = CTkFrame(root)
frame_search.pack(padx=20, pady=20)

label_word = CTkLabel(frame_search, text="Enter a word:", font=("TkDefaultFont", 15, 'bold') )
label_word.grid(row=0, column=0, padx=5, pady=5)

entry_word = CTkEntry(frame_search, width=200, font=("TkDefaultFont", 15))
entry_word.grid(row=0, column=1, padx=5, pady=5)

button_search = CTkButton(frame_search, text='Search', command=search_definition)
button_search.grid(row=0, column=2
                   , padx=5, pady=5)

frame_output = CTkFrame(root)
frame_output.pack(padx=20, pady=10)

text_output = CTkTextbox(frame_output, height=10, state=DISABLED, font=("TkDefaultFont", 15))
text_output.pack()

root.mainloop()