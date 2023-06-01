""" boucles sur une liste de nombres pour stocker une liste de nombres
 paires en uilisant les comprehensions de listes """

nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs=[i for i in nombres if i % 2 ==0]
print(nombres_pairs)

#idenfies une liste de nombres positifs dans une séquence de nombres entiers

nombres = range(-10, 10)
nombres_positifs =[x for x in nombres if x>=0]
print(nombres_positifs)

#on stockera tous les chiffres négtifs qui ne respecteront pas la condition ainsi que les nombres pairs

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]
print(nombres_inverses)





