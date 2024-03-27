from tkinter import *
from tkinter import ttk
import pandas as pd

class Pokedex:
    def __init__(self,root):

        self.root = root
        self.root.geometry('480x380')

        self.poke_df = pd.read_csv('Poke/poke.csv')

        self.style = ttk.Style()
        self.style.configure('TNotebook', tabposition='n')


        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both",expand= True)

        styl = ttk.Style()
        styl.configure('TSeparator', background='#db0f46')

        self.pokemon_tab_frame = Frame(self.tabs)
        self.tabs.add(self.pokemon_tab_frame,text="Pokemon")
        self.tab2 = Frame(self.tabs)
        self.tabs.add(self.tab2,text="Info")

        self.create_Pokemon_tab()
    

    def create_Pokemon_tab(self):


        styl = ttk.Style()
        styl.configure('TSeparator', background='grey')


        self.pokemon_list_frame = ttk.Frame(self.pokemon_tab_frame)
        self.pokemon_list_frame.pack(side='right', fill='y',expand= True)

        self.scrollbar = ttk.Scrollbar(self.pokemon_list_frame, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        self.pokemon_listbox = Listbox(self.pokemon_list_frame, yscrollcommand=self.scrollbar.set,background='#d3d9ce')
        self.pokemon_listbox.pack(side='left', fill='both', expand=True)

        self.scrollbar.config(command=self.pokemon_listbox.yview)
        print(self.pokemon_listbox.curselection())
        self.pokemon_listbox.bind('<Return>',self.poke_selected)
        pokemon_names = list(self.poke_df['name'])
        for name in pokemon_names:
            self.pokemon_listbox.insert('end', name)

        self.pokemon_display_frame = ttk.Frame(self.pokemon_tab_frame)
        self.pokemon_display_frame.pack(side='left', fill='both', expand=True)
        ttk.Separator(
        master=self.pokemon_tab_frame,
        orient=VERTICAL,
        style='TSeparator',
        class_= ttk.Separator,
        takefocus= 1,
        cursor='man').pack(fill=Y, expand=True)

        self.pokemon_image = Label(self.pokemon_display_frame, text="Pokemon Image", padx=10, pady=10)
        self.pokemon_image.pack()


        self.pokeimage = PhotoImage(file='Poke/images/1.png',).subsample(1)
        self.pokelabel = Label(self.pokemon_display_frame,image=self.pokeimage)
        self.pokelabel.pack()
        self.text = Text(self.pokemon_display_frame,height=5,width=40,bg='#d3d9ce')
        self.text.pack(side='bottom',anchor='sw',pady= 8)
        self.text.insert(END, """This is a short and sweet description of this pokemon""")     


    def poke_selected(self):
        return


    
    



if __name__ == "__main__":
    root = Tk()
    poke = Pokedex(root)
    root.mainloop()