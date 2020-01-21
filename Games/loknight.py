from random import randint
from random import choice
import time

game_name = "Loknight V1"
print()
print("----------------------------------------------------")
print()
print("                Coded by åurejien                   ")
print("             www.github.com/aurejien                ")
print()
print(f"                   {game_name}                       ")
print("                hello@aurelienj.dev                 ")
print()
print("----------------------------------------------------")
player_name = input("Your name. \n> ").lower().title()
xp = 0
gems = 0
bypass = 1
rules = input("{1} Pour afficher les règles\n{2} Pour passer\n>  ")
if rules == "1":
  print()
  print()
  print(f"Bienvenue sur {game_name}, le jeu est encore en développement")
  print("Les règles sont simple, tu choisis un héro, tu choisis entrainement pour te battre contre des bots")
  print("Tu as 3 coups qui coutent des cristaux pour pouvoir attaquer")
  print("C'est un tour par tour, tu attaques, le bot il t'attaque, celui qui a plus de vie a perdu, ou plus de cristaux")
  print("Pour une attaque de base tu dépenses 1 cristal et tu en gagnes 3,\nPour une grosse attaque tu dépenses 5 cristaux mais tu en gagnes que 1,\nPour une défense tu dépenses 2 cristaux mais tu en gagnes 3.")
  print("Bon jeu..")
  print("C'est un peu le fouilli désolé")
  print()
  print()
  print("Loading . . .")
  time.sleep(15)
else:
  print("Bon jeu alors")
  print("Loading . . .")
  time.sleep(2)
print()
print("----------------------------------------------------")
print()
print(f"Bienvenue {player_name}")
print("Jeu de combat tour par tour")
print()
print("----------------------------------------------------")
print()
print("Choisi ton hero")
print("{1} Cavalier: Attaque+++    Vie++++")
print("{-} Archer:   Bientôt disponible")
print("{-} Mage:     Bientôt disponible")
print("{-} Barbare:  Bientôt disponible")
hero_choix = -1
while hero_choix <= 0:
    hero_choix = input("Choisi ton hero:\n> ")
    try:
        hero_choix = int(hero_choix)
        if hero_choix == 1:

            hero = "Cavalier"  # Cavalier
            attaque_un = 25            # coup de point
            attaque_deux = 50          # epee
            contre = 60                # bouclier

            arme_un = "de point"
            arme_deux = "épée"
            arme_trois = "bouclier"

            arme_Un_un = "le coup de point"
            arme_Un_deux = "l'épée"
            arme_Un_trois = "le bouclier"

            #elif hero_choix == 2:

            #hero = "Archer"  # Archer
            #attaque_un = 30            # fleche normal
            #attaque_deux = 75          # fleche de feux
            #contre = 90                # Pas chassé

            #arme_un = "flèche"
            #arme_deux = "fléche de feu"
            #arme_trois = "invisible"

            #arme_Un_un = "la flèche"
            #arme_Un_deux = "la flèche de feu"
            #arme_Un_trois = "se rend invisible"

        else:
            raise ValueError
    except ValueError:
        print("Erreur des données.")
        hero_choix = -1
print(f"{player_name} tu as choisis {hero}")
print()
print("Loading . . .\n")
time.sleep(1)
level = 1
argent = 100

while True:
    if hero_choix == 1:
        vie = 200
    elif hero_choix == 2:
        vie = 120

    print("----------------------------------------------------")
    print(f"- {player_name}")
    print()
    print(f"- {xp}xp")
    print(f"- {gems}◊ Les cristaux sont utilisés pour attaquer")
    print(f"- Niveau { level}")
    print(f"- Argent {argent}$")
    print()
    time.sleep(2)
    print(f"{hero}:")
    print(f"    vie: {vie}")
    print(f"-  1◊  {arme_Un_un}: -{attaque_un}")
    print(f"-  5◊  {arme_Un_deux}: -{attaque_deux}")
    print(f"-  3◊  {arme_Un_trois} reduit de {contre}% l'attaque ennemi")
    print()
    time.sleep(2)
    print("{-} Combat. Bientôt disponible\n{2} Entrainement\n")
    print()
    print("Shop Bientôt disponible")
    print("{-} Elixir de vie: 100$ \n{-} Épée fer:+25dp 300$\n{-} Épée or: +50dp 600$   ")
    print("----------------------------------------------------")
    print()
    time.sleep(2)
    menu_choix = -1
    while menu_choix <= 0:
        menu_choix = input("> ")
        try:
            menu_choix = int(menu_choix)
            if menu_choix == 1:
                print("Jour de combat")
                print("Pas encore disponible")
                menu_choix = int(input("> "))
            elif menu_choix == 2:
                print(
                    "Bienvenue a l'entrainement...\nChoisis la difficulté d'entrainement")
                bot_level = -1
                while bot_level <= 0:
                    print()
                    bot_level = input(
                        "{1}Facile - {2}Normal - {3}Difficile\n> ")
                    try:
                        bot_level = int(bot_level)
                        # =========================== BOT FACILE
                        if bot_level == 1:
                            gems = 15
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print("-------------")
                            print(f"{gems}◊")
                            print("-------------")
                            print()

                            list_attaque = [10, 25, 50, 20, 35]
                            bot_hero = "bot_111"
                            bot_vie = vie - 100


                            xp = 1000
                            argent = 200

                            break
                        # =========================== BOT NORMAL
                        elif bot_level == 2:
                            gems = 10
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print("-------------")
                            print(f"{gems}◊")
                            print("-------------")
                            print()

                            list_attaque = [50, 15, 20, 60, 40]
                            bot_hero = "bot_444"
                            bot_vie = vie - 60

                            xp = 5000
                            argent = 500

                            break
                        # =========================== BOT DIFFICILE
                        elif bot_level == 3:
                            gems = 10
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print("-------------")
                            print(f"{gems}◊")
                            print("-------------")
                            print()

                            list_attaque = [20, 60, 75, 50, 55, 65]
                            bot_hero = "bot_666"
                            bot_vie = vie - 40
                            
                            xp = 10000
                            argent = 1000

                            break
                        # ===========================
                        else:
                            raise ValueError
                    except ValueError:
                        print("Value Error")
                        bot_level = -1
                print(f"{bot_hero} est pret pour t'entrainer")
                print()
                print(f"{hero} contre {bot_hero}")
                print("Ready? {1}")
                play = int(input("> "))
                print("------------------")
                print(f"{hero}: vie {vie}  ")
                print(f"{bot_hero}: vie {bot_vie}  ")
                print(f"{gems}◊ restant")
                tour = 1
                while tour != 0:
                    if vie <= 0:
                        print()
                        print(f"{player_name} votre {hero} est mort\n Tu me gagnes rien.")
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        break
                    elif bot_vie <= 0:
                        print()
                        print(f"{player_name} vous avez gagné\nVous remportez 500xp 50$")
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        argent += 50
                        xp += 500
                        break
                    elif bypass <= 0:
                        print()
                        print(f"{player_name} vous n'avez plus assé de cristaux pour attaquer")
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        break
                    combat = -1
                    while combat <= 0:
                      
                        print()
                        print("----------------------------")
                        print(f"tour {tour}")
                        print("----------------------------")
                        combat = int(input(
                            f"{{1}}: 1◊ {arme_Un_un}\n{{2}}: 5◊ {arme_Un_deux}\n{{3}}: 2◊ {arme_Un_trois}\n>"))
                        try:
                            combat = int(combat)
                            if combat == 1:
                                if gems <= 0:
                                  print(f"{gems}◊ restant")
                                  print("Tu ne peux pas utiliser coup de point, tu as plus de cristal")
                                  bypass = 0
                                  break
                                gems -= 1
                                bot_attaque = choice(list_attaque)
                                bot_vie -= attaque_un
                                vie -= bot_attaque
                                degats = attaque_un
                                bot_degats = bot_attaque
                                print(f"{hero} inflige un coup {arme_un}")
                                print(f"Dégats -{degats}")
                                print()
                                print(f"{bot_hero} attaque. . .")
                                print()
                                time.sleep(2)
                                print(f"{bot_hero} inflige un coup aléatoire")
                                print(f"Dégats -{bot_degats}")
                                print()
                                print("------------------")
                                print(f"{hero}: vie {vie}  ")
                                print(f"{bot_hero}: vie {bot_vie}  ")
                                print(f"{gems}◊ restant")
                                time.sleep(2.4)
                                print()
                                tour += 1
                                gems += 3
                            elif combat == 2:
                                
                                if gems <= 4:
                                  print(f"{gems}◊ restant")
                                  print("Tu ne peux pas utiliser l'épée, tu as plus de cristal")
                                  break
                                gems -= 5
                                bot_attaque = choice(list_attaque)
                                bot_vie -= attaque_deux
                                vie -= bot_attaque
                                degats = attaque_deux
                                bot_degats = bot_attaque
                                print(f"{hero} inflige un coup {arme_deux}")
                                print(f"Dégats -{degats}")
                                print()
                                print(f"{bot_hero} attaque. . .")
                                print()
                                time.sleep(2)
                                print(f"{bot_hero} inflige un coup aléatoire")
                                print(f"Dégats -{bot_degats}")
                                print()
                                print("------------------")
                                print(f"{hero}: vie {vie}  ")
                                print(f"{bot_hero}: vie {bot_vie}  ")
                                print(f"{gems}◊ restant")
                                time.sleep(2.4)
                                print()
                                tour += 1
                                gems += 1
                            elif combat == 3:
                                if gems <= 1:
                                  print(f"{gems}◊ restant")
                                  print("Tu ne peux pas utilisé le bouclier, tu as plus de cristal")
                                  break
                                gems -= 2
                                bot_attaque = choice(list_attaque)
                                bot_degats = 0
                                vie = vie - int(bot_attaque -
                                                ((bot_attaque * contre)/100))
                                degats = int(
                                    bot_attaque-((bot_attaque * contre)/100))
                                print(f"{bot_hero} attaque. . .")
                                print()
                                time.sleep(2)
                                print(f"{bot_hero} inflige un coup aléatoire")
                                print(f"Dégats -{degats}")
                                print()
                                print(f"{hero} utilise la défence {arme_trois}")
                                print(f"Dégats -{bot_degats}")
                                print()
                                print("------------------")
                                print(f"{hero}: vie {vie}  ")
                                print(f"{bot_hero}: vie {bot_vie}  ")
                                print(f"{gems}◊ restant")
                                time.sleep(2.4)
                                print()
                                tour += 1
                                gems += 3
                            else:
                              raise ValueError
                        except ValueError:
                          print("Value Error")
                          combat = -1
                break
            else:
                raise ValueError
        except ValueError:
            print("Value Error")
            menu_choix = -1
