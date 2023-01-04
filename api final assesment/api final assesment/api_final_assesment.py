
import requests
from tkinter import * # GUI
#from PIL import ImageTk, Image # GUI image

root = Tk() # make main window

root.title("Tkinter Programming") # Window Title
root.geometry("450x300") # Window Size
root.config(bg="#FFFFFF") # Background Color

# Initialise
cocktailName = ""
cocktailInstruc = ""

# Function for searching cocktail
def search():
    # Referencing global variables
    global cocktailName
    global cocktailInstruc

    # Get input from search bar
    get_cocktailName = searchBar.get()

    # Get API link
    cocktail_request = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={get_cocktailName}")

    # Get "Cocktail Name" Data from API
    cocktailName = cocktail_request.json()["drinks"][0]["strDrink"]
    text.config(text="Cocktail name: " + cocktailName)

    # Get "Cocktail Instruction" Data from API
    cocktailInstruc = cocktail_request.json()["drinks"][0]["strInstructions"]
    text_box.insert('end', 'Instructions on How to make drink:\n' + cocktailInstruc)

# Search Bar
searchBar = Entry()
searchBar.place(x=0,y=0)

# Search Button
button = Button(text="Search", command=search)
button.place(x=0,y=20)

# Create Text (Cocktail name)
text = Label(text="Cocktail name:", fg="black")
text.place(x=0,y=50)

# Create Textbox (Cocktail Instructions)
text_box = Text(
    root,
    height=100,
    width=150,
    bg="black",
    fg="white",
    wrap=WORD
)
text_box.place(x=0, y=100)


root.mainloop()



# margarita
# a1
# bijou
# caipirinha
# coffee-vodka
# derby