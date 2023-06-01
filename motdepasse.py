mdp= input("entrez un mot de passe (min , 8 caractères) : ")


mot_de_passe_trop_court = "votre mot de passe est trop court"



if mdp is None or len(mdp) ==0:
    print(mot_de_passe_trop_court.upper())
elif len(mdp) < 8:
    print(mot_de_passe_trop_court.capitalize())
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres")
else:
    print("Inscription terminée")


