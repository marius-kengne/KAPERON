from tkinter import *
#import create
#import create as cr
#import create as vs

def action():
    pass

def save():
    pass

def viewCreate():
    #vs
    #pass
    fen1 = Tk()

    fen1.geometry("800x600")

    description = "KAPERON vous permet enregidtrer des informations sur los employes de votre entreprise, \nde lister tous les employes, de supprimer un employe, de modifier les informations de \nl\' employe"
    labelListing = "Lister les employes   "
    labelCreate = "Enregistrer un employe"
    labelUpdate = "Editer un employe     "
    labelDelete = "Supprimer un employe  "

    lblnbre1 = Label(fen1, text="Bienvenu sur KAPERON",font=('broadway' , 18), bg='blue' , width=25)
    lblnbre1.place(x=200, y=50)

    contenu = Label(fen1, text=description)
    contenu.place(x=150, y=100)

    lblnbre1 = Label(fen1, text=labelCreate,font=('broadway' , 12), bg='blue' , width=25)
    lblnbre1.place(x=200, y=150)

    l1 = Button(fen1, text="Enregistrer", command=save, background="green") 
    l1.place(x=350, y=200) 

    fen1.mainloop()
    

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

listing = Button(fen, text=labelListing, command=action, background="green") 
listing.place(x=350, y=200) 

btnCreate = Button(fen, text=labelCreate, command=viewCreate(), background="green") 
btnCreate.place(x=350, y=250)

update = Button(fen, text=labelUpdate, command=action, background="green") 
update.place(x=350, y=300)

delete = Button(fen, text=labelDelete, command=action, background="green") 
delete.place(x=350, y=350)


fen.mainloop()
