from tkinter import *
from tkinter import ttk as ttk
import pandas as pd

class Pokedex:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x440')
        self.root.title("Pokedex")

        self.curr_index = 0

        self.poke_df = pd.read_csv('Poke/poke.csv')

        self.style = ttk.Style()
        self.style.configure('TNotebook', tabposition='n')

        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True)

        styl = ttk.Style()
        styl.configure('TSeparator', background='#db0f46')

        self.pokemon_tab_frame = Frame(self.tabs)
        self.tabs.add(self.pokemon_tab_frame, text="Pokemon")
        self.info_tab = Frame(self.tabs)
        self.tabs.add(self.info_tab, text="Info")

        self.create_Pokemon_tab()
        self.create_Info_tab()

    def create_Pokemon_tab(self):
        styl = ttk.Style()
        styl.configure('TSeparator', background='grey')

        self.pokemon_list_frame = ttk.Frame(self.pokemon_tab_frame)
        self.pokemon_list_frame.pack(side='right', fill='y', expand=True)

        self.scrollbar = ttk.Scrollbar(self.pokemon_list_frame, orient='vertical')
        self.scrollbar.pack(side='right', fill='y')

        self.pokemon_listbox = Listbox(self.pokemon_list_frame, yscrollcommand=self.scrollbar.set,
                                       background='#ad2f4c', width=23, fg='white',
                                       font=('Helvetica', 10, "bold"))
        self.pokemon_listbox.pack(side='left', fill='both', expand=True)

        self.scrollbar.config(command=self.pokemon_listbox.yview)

        self.pokemon_listbox.bind('<Return>', lambda x: self.poke_selected())

        pokemon_names = list(self.poke_df['name'])
        for name in pokemon_names:
            self.pokemon_listbox.insert('end', name)

        self.pokemon_display_frame = Frame(self.pokemon_tab_frame)
        self.pokemon_display_frame.pack(side='left', fill='both', expand=True)
        ttk.Separator(
            master=self.pokemon_tab_frame,
            orient=VERTICAL,
            style='TSeparator',
            class_=ttk.Separator,
            takefocus=1,
            cursor='man').pack(fill=Y, expand=True)

        self.pokemon_name_label = Label(self.pokemon_display_frame, text="Bulbasaur", padx=10, pady=10,
                                        bg='#f5edef',
                                        font=('Helvetica', 12, "bold"))
        self.pokemon_name_label.pack(pady=5, expand=True)

        self.pokemon_display_frame.config(bg='#f5edef')

        self.pokeimage = PhotoImage(file='Poke/images/1.png', ).subsample(1)
        self.pokelabel = Label(self.pokemon_display_frame, image=self.pokeimage, bg='#f5edef')
        self.pokelabel.pack()
        self.pokelabel.configure(image=self.pokeimage, bg='#f5edef')

        self.text = Text(self.pokemon_display_frame, height=10, width=40, bg='#e6e1e2')
        self.text.pack(side='bottom', anchor='sw')
        self.text.insert(END, self.poke_df.loc[0, 'Description'])

    def create_Info_tab(self):
        self.info_frame = Frame(self.info_tab)
        self.info_frame.pack(fill='both', expand=True)

        self.pokemon_info_image_label = Label(self.info_frame, bg='white')

        self.pokemon_info_image_label.config(image=self.pokeimage)

        self.pokemon_info_image_label.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        self.attribute_sliders_frame = Frame(self.info_frame)
        self.attribute_sliders_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nw')

        attributes = ['HP', 'Attack', 'Defense', 'Sp_Attack', 'Sp_Defense','Speed']
        colors = ['#08d141', '#c7042b', '#f76a05', '#f705b3', '#f7f705','#058ef7'] 

        self.progress_bars = []

        for i, (attr, color) in enumerate(zip(attributes, colors)):
            Label(self.attribute_sliders_frame, text=attr, padx=10, pady=10, font=('Helvetica', 10, 'bold')).grid(row=i, column=0, sticky='w')
            s = ttk.Style()
            s.theme_use('default')
            s.configure(f"{attr}.Horizontal.TProgressbar", background=color)  
            progressbar = ttk.Progressbar(self.attribute_sliders_frame, orient=HORIZONTAL, 
                                        length=100, 
                                        mode='determinate', value=self.poke_df.loc[self.curr_index, attr.lower()], 
                                        style=f"{attr}.Horizontal.TProgressbar")  
            progressbar.grid(row=i, column=1, padx=10, sticky='w')
            self.progress_bars.append(progressbar)

        self.pokemon_listbox.bind('<Return>', lambda x: self.poke_selected())



    def poke_selected(self):
        self.curr_index = self.pokemon_listbox.curselection()[0]
        self.pokemon_name_label.config(text=str(self.poke_df.loc[self.curr_index, 'name'][4:]))

        # Update image
        image_path = self.poke_df.loc[self.curr_index, 'images'].strip()
        self.update_pokemon_image(image_path)
        self.pokeimage = PhotoImage(file=str(self.poke_df.loc[self.curr_index,'images']).strip()).subsample(1)
        self.pokelabel.configure(image=self.pokeimage)

        attributes = ['HP', 'Attack', 'Defense', 'Sp_Attack', 'Sp_Defense','Speed']
        for bar,attr in zip(self.progress_bars,attributes):
            bar.config(value=self.poke_df.loc[self.curr_index, attr.lower()])

    def update_pokemon_image(self, image_path):
        try:
            pokemon_image = PhotoImage(file=image_path).subsample(1)
            self.pokelabel.configure(image=self.pokeimage)
            self.pokemon_info_image_label.config(image=pokemon_image)
            self.pokemon_info_image_label.image = pokemon_image  
        except:
            default_image = PhotoImage(file='Poke/images/2.png').subsample(1)
            self.pokelabel.configure(image=self.pokeimage)
            self.pokemon_info_image_label.config(image=default_image)
            self.pokemon_info_image_label.image = default_image 
        


if __name__ == "__main__":
    root = Tk()
    poke = Pokedex(root)
    root.mainloop()
