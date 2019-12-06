Cet exercice comprend :

- Un crawler, qui parcoure les différents bestiaires, et les différents monstres. Il créé une base de données MongoDB avec chaque monstre
ainsi que les sorts qu'il peut lancer. Attention, on considère bien chaque monstre, par exemple si Démon rouge et Démon bleu sont deux monstres différents
rangés sur la page Démon, on aura l'entrée "Démon rouge" et "Démon bleu", mais pas l'entrée "Démon"

- Un index inversé qui, à tout sort, associe les monstres qui peuvent le lancer

- Une interface qui affiche : 
	- Tous les monstres pouvant lancer le sort sélectionné
	- Tous les sorts que peut lancer un monstre sélectionné
	- Un hyperlien vers le sort ou le monstre sélectionné
	- Un bouton Recrawl pour relancer le crawler
