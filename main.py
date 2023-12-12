import random
# fait tout le jeu
def main(): 
    niveau_vie = 20
    nombre_victoires = 0
    nombre_defaites = 0
    numero_combat = 0
    boss = 0
    boss_absent = 0
    # pendant que le joueur nest pas mort, il peut continuer le jeu
    while niveau_vie > 0:
        numero_adversaire = nombre_victoires + nombre_defaites + 1

        if nombre_victoires > 0 and nombre_victoires % 3 == 0:
            if boss_absent == 0:
                print("Vous tombez face à face avec un boss!")
                force_adversaire = random.randint(5, 5*2)
                boss = 1
        else:
            boss_absent = 0
            boss = 0
            force_adversaire = random.randint(1, 5*2)
    
        print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)
        print("Que voulez-vous faire ?")
        print("1- Combattre cet adversaire")
        print("2- Contourner cet adversaire et aller ouvrir une autre porte")
        print("3- Afficher les règles du jeu")
        print("4- Quitter la partie")

        choix = input("Votre choix : ")
        # choix de combattre enemi
        if choix == '1': 
            numero_combat += 1
            score_des = random.randint(1, 6) + random.randint(1, 6)
            print(f"Lancer des dés : {score_des}")
            # ce qui arrive quand on gagne
            if score_des > force_adversaire: 
                combat_statut = "victoire"
                niveau_vie += force_adversaire
                nombre_victoires += 1
                print(f"Dernier combat = {combat_statut}")
                print(f"Niveau de vie : {niveau_vie}")
            # ce qui arrive quand on perd
            else: 
                combat_statut = "defaite"
                niveau_vie -= force_adversaire
                nombre_defaites += 1
                print(f"Dernier combat = {combat_statut}")
                print(f"Niveau de vie : {niveau_vie}")
                if boss == 1:
                    boss_absent = 1
                    
        elif choix == '2':
            niveau_vie -= 1
            nombre_defaites += 1
            print("Vous contournez l'adversaire, mais cela vous coûte 1 point de vie.")
        # affiche les regles
        elif choix == '3': 
            print("Pour réussir un combat, il faut que la somme des valeurs des dés lancés soit supérieure à la force de l'adversaire.")
            print("Dans ce cas, le niveau de vie de l'usager est augmenté de la force de l'adversaire.")
            print("Une défaite a lieu lorsque la somme des valeurs des dés lancés par l'usager est inférieure ou égale à la force de l'adversaire.")
            print("Dans ce cas, le niveau de vie de l'usager est diminué de la force de l'adversaire.")
            print("La partie se termine lorsque les points de vie de l'usager tombent sous 0.")
            print("L'usager peut combattre ou éviter chaque adversaire, dans le cas de l'évitement, il y a une pénalité de 1 point de vie.")
            
        elif choix == '4':
            print("Merci et au revoir...")
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")

        print(f"Adversaire : {numero_adversaire}")
        print(f"Force de l'adversaire : {force_adversaire}")
        print(f"Niveau de vie de l'usager : {niveau_vie}")
        print(f"Combat {numero_combat} : {nombre_victoires} vs {nombre_defaites} \n")

    print(f"La partie est terminée. Vous avez vaincu {nombre_victoires} monstre(s) dont le redoutable BOSS !")

main()
