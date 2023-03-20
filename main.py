from tkinter import *
from tkinter import ttk
from bdd import BddManagement

bdd = BddManagement('root', '', 'boutique', 'localhost')


#fonctions de manipulation de la bdd
def ajouter():
    nom = entrerNom.get()
    description = entrerDescription.get()
    prix = entrerPrix.get()
    quantite = entrerQuantite.get()
    categorie = entrerCategorie.get()
    id = bdd.addProduitToBdd(nom, description, prix, quantite, categorie)
    table.insert('', 'end', values=bdd.getOneProduits(id)[0])


def modifier():
    nom = entrerNom.get()
    description = entrerDescription.get()
    prix = entrerPrix.get()
    quantite = entrerQuantite.get()
    categorie = entrerCategorie.get()
    selection = table.item(table.selection())['values'][0]
    bdd.modifierProduit(selection, nom, description, prix, quantite, categorie)
    for row in table.get_children():
        table.delete(row)
    for row in bdd.getAllProduits():
        table.insert('', 'end', values=row)



def supprimer():
    selection = table.item(table.selection())['values'][0]
    bdd.deleteProduit(selection)
    table.delete(table.selection())

#fonctions de manipulation de la bdd


#gestion de tkinter et de la fenetre
fenetre=Tk()
fenetre.geometry("900x900")
table = ttk.Treeview(fenetre, columns=(1, 2, 3, 4, 5, 6), height = 5, show="headings")
table.place(x=50, y=0, width=800, height=600)

table.heading(1, text="id")
table.heading(2, text="nom")
table.heading(3, text="description")
table.heading(4, text="prix")
table.heading(5, text="quantite")
table.heading(6, text="categorie")

table.column(1, width=100, anchor='center')
table.column(2, width=100, anchor='center')
table.column(3, width=100, anchor='center')
table.column(4, width=100, anchor='center')
table.column(5, width=100, anchor='center')
table.column(6, width=100, anchor='center')

for row in bdd.getAllProduits():
    table.insert('', 'end', values=row)


labelNom = Label(fenetre, text = "Nom Produit")
labelNom.place(x=50,y=650,width=100)
entrerNom = Entry(fenetre)
entrerNom.place(x=150,y=650,width=150,height=30)


labelDescription = Label(fenetre, text = "Description Produit")
labelDescription.place(x=320,y=650,width=130)
entrerDescription = Entry(fenetre)
entrerDescription.place(x=460,y=650,width=150,height=30)

labelPrix = Label(fenetre, text = "Prix Produit")
labelPrix.place(x=630,y=650,width=100)
entrerPrix = Entry(fenetre)
entrerPrix.place(x=730,y=650,width=70,height=30)

labelQuantite = Label(fenetre, text = "Quantite Produit")
labelQuantite.place(x=250,y=700,width=120)
entrerQuantite = Entry(fenetre)
entrerQuantite.place(x=370,y=700,width=70,height=30)

labelCategorie = Label(fenetre, text = "id Categorie")
labelCategorie.place(x=460,y=700,width=100)
entrerCategorie = Entry(fenetre)
entrerCategorie.place(x=560,y=700,width=70,height=30)


labelTuto = Label(fenetre, text = "Pour ajouter un produit : remplir tout les champs et cliquez sur ajouter, pour modifier un produit : sélectionner le produit puis remplir tout les champs même ceux inchangés et cliquez sur modifier, pour supprimer un produit sélectionner le puis cliquez sur supprimer", wraplength=700)
labelTuto.place(x=50,y=740,width=800)




btnAjouter = Button(fenetre, text = "Enregistrer", command = ajouter)
btnAjouter.place(x=50, y= 800, width=200)


btnModifier = Button(fenetre, text = "Modifier", command = modifier)
btnModifier.place(x=350, y= 800, width=200)


btnSupprimer = Button(fenetre, text = "Supprimer", command = supprimer)
btnSupprimer.place(x=650, y= 800, width=200)




fenetre.mainloop()