from tkinter import *

def save():
    pass

def create():

    fen = Tk()

    fen.geometry("800x600")

    description = "KAPERON vous permet enregidtrer des informations sur los employes de votre entreprise, \nde lister tous les employes, de supprimer un employe, de modifier les informations de \nl\' employe"
    labelListing = "Lister les employes   "
    labelCreate = "Enregistrer un employe"
    labelUpdate = "Editer un employe     "
    labelDelete = "Supprimer un employe  "

    lblnbre1 = Label(fen, text="Bienvenu sur KAPERON",font=('broadway' , 18), bg='blue' , width=25)
    lblnbre1.place(x=200, y=50)

    contenu = Label(fen, text=description)
    contenu.place(x=150, y=100)

    lblnbre1 = Label(fen, text=labelCreate,font=('broadway' , 12), bg='blue' , width=25)
    lblnbre1.place(x=200, y=150)

    l1 = Button(fen, text="Enregistrer", command=save, background="green") 
    l1.place(x=350, y=200) 



    fen.mainloop()

create()