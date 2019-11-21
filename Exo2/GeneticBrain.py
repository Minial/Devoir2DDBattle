#Pour le cerveau, on vas faire un algo genetic
#on crée plusieurs instance en // du terrain
#sur chacun, chaque mob a son propre reseau de neurone (100 neurone ? p-e plus ?)
#faire un reseau un neurone en entré pour chaque mob et de la profondeur
#chaque reseau prend en entré coord X et Y et la vie et le taco de tout le monde
#la sortie sera la position final du mob, comment il attaque et la liste des mobs qu'il tape
#si ce qu'il dit est impossible, on tue le mob (pour eviter de contourner les regles)
#au bout de 20 tour ou quand un camp est mort, on compte les points de chaque mob
#+ point si dégat aux ennemies +bcp point si ennemie mort
#faire gaffe que les mobs d'un camp coopère entre eux
#on peut aussi ne pas le faire et voir si ça apparait tout seul
#a la fin on sélectionne de chaque type de mob le reseau de neurone avec le meilleure code
#on fait des mutations aleatoire
#on recommence avec reseau muté !