import tkinter as tk
from tkinter.font import Font


# randomly finds a movie and its description
def randomMovie():
    import requests
    import random
    for num in range(0,5):
        randomNum = random.randrange(55,1000000)
        apiKey = "d0f71e5ec3da4111a18552789bf14157"
        section = "/movie/"
        baseurl = "https://api.themoviedb.org/3"+ section + str(randomNum) +"?api_key=" + apiKey
        response = requests.get(baseurl)
        randMovieDict = response.json()
        if list(randMovieDict.keys())[0] == "succuess" and list(randMovieDict.values())[0] == True:
            continue
        elif list(randMovieDict.keys())[0] == "adult":
            randMovie = randMovieDict["original_title"]
            desc = randMovieDict["overview"]
            lang = randMovieDict["original_language"]
            randomMovieDisplay(randMovie, desc, lang)
            break




# Handles double button commands - closes current page and/or opens home/new movie page
def homeFunction(window):
    window.destroy()
    root.deiconify()
def anotherRMovieFunction(window):
    window.destroy()
    randomMovie()
def anotherGMovieFunction(window):
    window.destroy()
    gMovie()
def exitMovieFunction(window):
    window.destroy()
    root.destroy()


# Give display for random movie generated
def randomMovieDisplay(name, descript,lang):
    try:
        root.withdraw()
    except:
        print("Root hidden")
    finally:
       page2 = tk.Tk()
       page2.config(bg="cadetblue4")
       page2.title("Does \"" + name + "\"sound interesting?")
       movie = tk.Text(page2, font=30,height= 20,width= 50, bg="cadetblue4")
       movie.pack()
       movie.insert(tk.END, name + "\n\n" + "language: " + lang + "\n\n" + "synopsis: " + descript)
       exit = tk.Button(page2,text="exit",padx=10, pady=5, command=lambda: exitMovieFunction(page2))
       home = tk.Button(page2, text="home", padx=10, pady=5, command=lambda: homeFunction(page2))
       new = tk.Button(page2,text="another movie",padx=10, pady=5, command=lambda: anotherRMovieFunction(page2))
       exit.place(x=75,y=250)
       home.place(x=190,y=250)
       new.place(x=300,y=250)
       tk.mainloop()

# finds random ghibli movie and description
def gMovie():
    import requests
    import random
    num = random.randrange(0,21)
    baseurl = "https://ghibliapi.herokuapp.com/films"
    response = requests.get(baseurl)
    glist = response.json()
    name = glist[num]["title"]
    desc = glist[num]["description"]
    gMovieDisplay(name, desc)

# Gives display for random ghibli movie
def gMovieDisplay(name, desc):
    #nameFont = Font(family="Courier", size=15, weight="bold")
    #descFont = Font(family="Courier", size=10, slant="italic")
    try:
        root.withdraw()
    except:
        print("Root hidden")
    finally:
        page3 = tk.Tk()
        page3.config(bg="cadetblue4")
        page3.title("Is " + name + " the vibe?")
        movie = tk.Text(page3, font=50,height= 20,width= 50, bg="cadetblue4")
        movie.pack()
        movie.insert(tk.END, name + "\n\n" + "synopsis: " + desc)
        exit = tk.Button(page3,text="exit",padx=10, pady=5, command=lambda: exitMovieFunction(page3))
        home = tk.Button(page3,text="home",padx=10, pady=5, command=lambda: homeFunction(page3))
        new = tk.Button(page3,text="another movie",padx=10, pady=5, command=lambda: anotherGMovieFunction(page3))
        exit.place(x=75,y=250)
        home.place(x=190,y=250)
        new.place(x=300,y=250)
        tk.mainloop()


# home window display
root = tk.Tk()
root.config(bg="black")
root.title("Movie Generator")
root.geometry("500x300")
mainFont = Font(family="Courier", size=30, weight="bold")
random = tk.Button(root, text="MOVIE", padx=10, pady=20,fg="cyan4",highlightbackground="cadetblue4",font=mainFont, command=lambda: randomMovie())
fav = tk.Button(root, text="FAVORITES", padx=10, pady=20,fg="cyan4",highlightbackground="cadetblue4",font=mainFont)
ghibli = tk.Button(root, text="GHIBLI", padx=10, pady=20,fg="cyan4",highlightbackground="cadetblue4",font=mainFont,command=lambda: gMovie())
random.place(x=15, y=100)
fav.place(x=150, y=100)
ghibli.place(x=350, y=100)
root.mainloop()
