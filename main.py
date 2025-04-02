from tkinter import *
from tkinter import messagebox as mbox
from PIL import Image, ImageTk
from mal import AnimeSearch
import webbrowser as wb


def search(*args):
    entry = search_entry.get()
    name = AnimeSearch(entry)
    global finds, finds_details
    finds = [(x.title, x, x.url) for i, x in enumerate(name.results) if i < number.get()]
    finds_details = [(x.type, x.episodes, x.synopsis) for i, x in enumerate(name.results) if i < number.get()]

    w2 = Tk()
    w2.config(pady=30, padx=20, background='black')
    w2.minsize(300, 150)
    w2.resizable(False, False)
    w2.attributes('-alpha', 0.9)
    w2.title('Search Results')

    global all_results
    all_results = Listbox(w2, bg='black', fg='white', width=50, height=1*number.get())

    i = 0
    for anime, obj, _ in finds:
        all_results.insert(i, f'{anime} | ({obj.score}*)')
        i += 1

    upper_text = Label(w2, text='Title | Score', bg='black', fg='purple')
    upper_text.pack()

    all_results.pack(pady=25)
    all_results.bind('<<ListboxSelect>>', weblink)


def weblink(*args):
    index = all_results.curselection()[0]
    confirm = mbox.askyesno(title='Redirect to website?',message=f'Type: {finds_details[index][0]}\nEpisodes: {finds_details[index][1]}\nSynopsis: {finds_details[index][2]}')

    if confirm:
        site = finds[index][2]
        wb.open_new(site)


if __name__ == "__main__":
    w = Tk()
    w.title('Mini MAL - PerSky <3')
    w.resizable(False, False)
    w.config(pady=30, padx=20, background='black')
    w.minsize(300, 400)
    w.attributes('-alpha', 1.0)

    image = (Image.open('v f x.png'))
    resized_avatar = image.resize((100, 100))
    img = ImageTk.PhotoImage(resized_avatar)

    canvas = Canvas(width=100, height=100, highlightthickness=0)
    canvas.create_image(50, 50, image=img)
    canvas.place(relx=0.5, rely=0.02, anchor=N)

    search_text = Label(text='Search: ', bg='black', fg='purple')
    search_text.place(relx=0.01, rely=0.45, anchor=W)

    sv = StringVar()
    search_entry = Entry(width=30, textvariable=sv)

    search_entry.focus()
    search_entry.place(relx=0.22, rely=0.45, anchor=W)

    number = IntVar()
    number_scale = Scale(w, bg='black', fg='white', length=250, from_=1, to=20, orient=HORIZONTAL, highlightthickness=0, activebackground='black', label='Number of results:', variable=number)
    number_scale.place(relx=0.01, rely=0.65, anchor=W)

    w.bind('<Return>', search)

    w.mainloop()
