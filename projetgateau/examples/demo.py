from projetgateau.recettes import *
from graphlib import *

ListeNomsSousProduits = ["Fraises coupées","Pâte à tarte", "Pâte à chou", "Pâte à chou reposée", "Choux vides",
                            "Choux à la crème","Crème patissière", "Pâte à tarte cuite",
                            "Pâte à tarte cuite et froide", "Tarte aux fraises"]

ListeSousProduits = [sousProduit(nom) for nom in ListeNomsSousProduits]

EtapesTarteAuFraise = [
        etape("Couper les fraises", produitFinal=sousProduit("Fraises coupées"), duree = 10),
        etape("Préparer crème patissière", produitFinal=sousProduit("Crème patissière"), duree = 30),
        etape("Prep pâte à tarte", produitFinal=sousProduit("Pâte à tarte"), duree =5),
        etape("Prep pâte à chou", produitFinal=sousProduit("Pâte à chou"), duree = 15),
        etape("Cuisson pâte à tarte", produitFinal=sousProduit("Pâte à tarte cuite"), duree = 45,
                    besoinFour = True, etapeActive = False, sousProduitNecessaires=[sousProduit("Pâte à tarte")]),
        etape("Attendre pâte tarte froide", produitFinal=sousProduit("Pâte à tarte cuite et froide"), duree = 30,
                    etapeActive = False, sousProduitNecessaires=[sousProduit("Pâte à tarte cuite")]),
]
EtapesChoux=[
        etape("Dressage tarte aux fraises", produitFinal=sousProduit("Tarte aux fraises"), duree = 10,
                    sousProduitNecessaires=[sousProduit("Pâte à tarte cuite et froide"), sousProduit("Fraises coupées"), sousProduit("Crème patissière")]),
        etape("Faire reposer pâte chou", produitFinal=sousProduit("Pâte à chou reposée"), duree = 60,
                    etapeActive = False, sousProduitNecessaires=[sousProduit("Pâte à chou")]),
        etape("Cuisson choux", produitFinal=sousProduit("Choux vides"), duree = 25,
                    besoinFour = True, etapeActive = False, sousProduitNecessaires=[sousProduit("Pâte à chou reposée")]),
        etape("Dressage choux", produitFinal=sousProduit("Choux à la crème"), duree = 20,
                    sousProduitNecessaires=[sousProduit("Choux vides"), sousProduit("Crème patissière")])
                    ]

RecetteTarteAuxFraises = recette(EtapesTarteAuFraise)
RecetteChoux = recette(EtapesChoux)

MonPlanning = planing(  (RecetteChoux, RecetteTarteAuxFraises) )
MonPlanning.genererplaning()
print(MonPlanning)
