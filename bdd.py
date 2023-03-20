import mysql.connector

class BddManagement():

    def __init__(self, user, password, database, host='localhost'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.connexion = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        self.cursor = self.connexion.cursor()



    def addProduitToBdd(self, nom, description, prix, quantite, id_categorie):
        query = ("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)")
        values = (nom, description, prix, quantite, id_categorie)
        self.cursor.execute(query, values)
        self.connexion.commit()
        return self.cursor.lastrowid

    def modifierProduit(self, id, nom, description, prix, quantite, id_categorie):
        query = "UPDATE produit SET nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s"
        values = (nom, description, prix, quantite, id_categorie, id)
        self.cursor.execute(query, values)
        self.connexion.commit()

    def updateQuantity(self, quantite):
        query = f"UPDATE produit SET quantite = {quantite}"
        self.cursor.execute(query)
        self.connexion.commit()
    

    def deleteProduit(self, id):
        query = f"DELETE FROM produit WHERE id = {id}"
        self.cursor.execute(query)
        self.connexion.commit()

    def addCategorieToBdd(self, nom):
        query = ("INSERT INTO categorie (nom) VALUES (%s)")
        values = (nom)
        self.cursor.execute(query, values)
        self.connexion.commit()

    def deleteCategorie(self, id):
        query = f"DELETE FROM categorie WHERE id = {id}"
        self.cursor.execute(query)
        self.connexion.commit()


    def getAllProduits(self):
        query = ("SELECT produit.id, produit.nom, produit.description, produit.prix, produit.quantite, categorie.nom FROM produit INNER JOIN categorie ON produit.id_categorie = categorie.id")
        self.cursor.execute(query)
        return(self.cursor.fetchall())

    def getOneProduits(self, id):
        query = f"SELECT produit.id, produit.nom, produit.description, produit.prix, produit.quantite, categorie.nom FROM produit INNER JOIN categorie ON produit.id_categorie = categorie.id WHERE produit.id = {id}"
        self.cursor.execute(query)
        return(self.cursor.fetchall())