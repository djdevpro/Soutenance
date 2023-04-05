import streamlit as st


title = "Nettoyage et sélection des données "
sidebar_name = "Sélection des données"


def run():
    
    st.title(title)

    st.markdown("---")
    
    st.markdown("## Pre-processing et feature engineering :")



    st.markdown(
        """
    Le jeu de données présente un grand nombre de valeurs manquantes. Ainsi, seulement 0.83% des lignes du jeu de données ne présentent pas de valeurs manquantes dans l’une des colonnes.

En supprimant les colonnes n’ayant pas d’intérêt dans la prédiction du temps de réponse, ce taux remonte à 2.3%.

D’autre part, le jeu de données possède une variable DelayCodeId qui prend une valeur uniquement si la mobilisation et la réponse des pompiers ont rencontré un délai supplémentaire exceptionnel. On remplace pour cette variable, l’absence de valeur par un nouveau DelayCodeId tel que 0.

De la même manière, le jeu de données présente une variable SpecialServiceType ayant une valeur uniquement si l’incident appartient à la catégorie SpecialService.

On affecte à l’absence de valeur prise par la variable StopCodeDescription pour la même observation. Ainsi, le taux précédent passe à 38%.

Enfin, les dernières variables présentant un nombre important de valeurs manquantes sont la latitude et la longitude de l’accident. Ces informations permettent de calculer la distance entre la station de pompiers et l’accident, variable qui joue un rôle important dans l’estimation du temps de réponse des pompiers. Ainsi, il est nécessaire de considérer des observations possédant des valeurs pour ces variables ce qui nous amène à supprimer les observations n’ayant pas de latitude et longitude pour l’accident. Suite à cette opération, le nombre d'observations restantes est de 196346 ( 515347 observations à l’origine ).


Suite à la gestion des valeurs manquantes, il est nécessaire de sélectionner les observations présentant un intérêt pour l’estimation du temps de réponse.


Ainsi, concernant la variable DelayCodeId, nous allons uniquement sélectionner les observations ne présentant pas de délai exceptionnel ( DelayCodeId = 0 ). En effet, la présence d’un délai n’étant pas connu à l’avance lorsqu’un accident se présente, on ne peut pas utiliser cette variable comme variable explicative dans la modélisation. Comme la situation la plus présente est celle de l’absence de délai ( 73.8% des observations restantes, 145000 observations à peu près ), on va effectuer l’analyse et la modélisation des données sur les observations sans délai.
    """
    )

    st.markdown("---")

    st.markdown(

        """
        D’autre part, il y a un certain nombre de valeurs qui présentent un temps de réponse trop faible par rapport à la distance entre la station de pompiers et le lieu de l’accident si l’on considère que le camion de pompiers est bien parti de la caserne. En effet, si l’on considère qu’un temps de mobilisation minimum est de 10 secondes et que le camion de pompiers roule à 90km/h en moyenne. Alors, le temps de réponse minimal en fonction de la distance est : 

        ### y = 10 + ( 3.6 / 90 ) * distance

        De ce fait, on supprime toutes les observations avec un temps de réponse inférieur au temps de réponse minimal. On considère que ces temps correspondent soit à une erreur de remplissage soit à une réponse des pompiers n’étant pas dans la caserne. Les observations supprimées dans ce cas représentent 1.26 % des données. 

        """
    )