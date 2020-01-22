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
gems = 10
bypass = 1
rules = input("{1} Pour afficher les règles\n{2} Pour passer\n>  ")
if rules == "1":
  print()
  print()
  print(f"Bienvenue sur {game_name}, le jeu est encore en développement")
  print("Les règles sont simple, tu choisis un héro,\ntu choisis entrainement pour te battre contre des bots")
  print("Tu as 3 coups qui coutent des cristaux pour pouvoir attaquer")
  print("C'est un tour par tour, tu attaques, le bot il t'attaque,\ncelui qui a plus de vie a perdu, ou plus de cristaux")
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
print("{1} Cavalier: Attaque: +++    Vie: ++++")
print("{2} Archer:   Attaque: ++++   Vie: +++")
print()
print("{-} Mage:     Bientôt disponible")
print("{-} Barbare:  Bientôt disponible")
hero_choix = -1
while hero_choix <= 0:
    hero_choix = input("Choisi ton hero:\n> ")
    try:
        hero_choix = int(hero_choix)
        if hero_choix == 1:

            hero = "Le Cavalier"       # Cavalier
            attaque_un = 25            # coup de point
            attaque_deux = 50          # epee
            contre = 60                # bouclier

            arme_un = "de point"
            arme_deux = "d'épée"
            arme_trois = "bouclier"

            arme_Un_un = "le coup de point"
            arme_Un_deux = "l'épée"
            arme_Un_trois = "le bouclier"

        elif hero_choix == 2:

            hero = "L'Archer"  # Archer
            attaque_un = 30            # fleche normal
            attaque_deux = 65          # fleche de feux
            contre = 90                # Pas chassé

            arme_un = "Simple flèche"
            arme_deux = "La fléche de feu"
            arme_trois = "Le pas chassé"

            arme_Un_un = "Simple flèche"
            arme_Un_deux = "la flèche de feu"
            arme_Un_trois = "Le pas chassé"

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
        vie = 150

    print("----------------------------------------------------")
    print(f"{player_name}")
    print(f"  {gems}◊")
    print(f"  {xp}xp")
    print(f"  Argent {argent}$")
    print()
    time.sleep(2)
    print(f"{hero}: vie {vie}")
    print(f"  ↓1◊ ↑3◊  {arme_Un_un}: -{attaque_un}")
    print(f"  ↓5◊ ↑1◊  {arme_Un_deux}: -{attaque_deux}")
    print(f"  ↓2◊ ↑3◊  {arme_Un_trois} reduit de {contre}% l'attaque ennemi")
    print()
    time.sleep(2)
    print("Combats")
    print("  {-} Combat. Bientôt disponible\n  {2} Entrainement\n")
    print()
    time.sleep(0.5)
    print("Shop Bientôt disponible")
    print("  {-} Elixir de vie: 100$ \n  {-} Épée fer:+25dp 300$\n  {-} Épée or: +50dp 600$   ")
    print()
    menu_choix = -1
    while menu_choix <= 0:
        menu_choix = input("Faite votre choix\n> ")
        print("----------------------------------------------------")
        print()
        time.sleep(2)
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
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print()

                            list_attaque = [10, 25, 50, 20, 35]
                            bot_hero = "bot_111"
                            bot_vie = vie - 100


                            xp_up = 200
                            argent_up = 75

                            break
                        # =========================== BOT NORMAL
                        elif bot_level == 2:
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print()

                            list_attaque = [50, 15, 20, 60, 40]
                            bot_hero = "bot_444"
                            bot_vie = vie - 60

                            xp_up = 500
                            argent_up = 150

                            break
                        # =========================== BOT DIFFICILE
                        elif bot_level == 3:
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print()

                            list_attaque = [20, 60, 75, 50, 55, 65]
                            bot_hero = "bot_666"
                            bot_vie = vie - 40
                            
                            xp_up = 1000
                            argent_up = 300

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
                play = input("> ")
                tour = 1
                while tour != 0:
                    if vie <= 0:
                        argent_up = 0
                        xp_up = 0
                        print()
                        print(f"{player_name} votre {hero} est mort\n Tu me gagnes rien.")
                        print(f"{player_name} vous avez gagné\nVous remportez {xp_up} {argent_up}$")
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        break
                    elif bot_vie <= 0:
                        print()
                        print(f"{player_name} vous avez gagné\nVous remportez {xp_up} {argent_up}$")
                        argent += argent_up
                        xp += xp_up
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        break
                    elif bypass <= 0:
                        argent_up = 0
                        xp_up = 0
                        print()
                        print(f"{player_name} vous n'avez plus assé de cristaux pour attaquer")
                        print(f"{player_name} vous avez gagné\nVous remportez {xp_up} {argent_up}$")
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        break
                    combat = -1
                    while combat <= 0:
                        print("----------")
                        print(f"tour {tour}  |")
                        print("----------------------------------------------------")
                        print()
                        print(f"   vie {vie} - {hero}")
                        print(f"   vie {bot_vie} - {bot_hero}")
                        print()
                        print(f"   {gems}◊ restant")
                        print()
                        print("----------------------------------------------------")
                        print(f"{{1}} |  ↓1◊ ↑3◊  {arme_Un_un}: -{attaque_un}")
                        print(f"{{2}} |  ↓5◊ ↑1◊  {arme_Un_deux}: -{attaque_deux}")
                        print(f"{{3}} |  ↓2◊ ↑3◊  {arme_Un_trois} reduit de {contre}% l'attaque ennemi")
                        print()
                        combat = int(input("> "))
                        print("----------------------------------------------------")
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
                                print()
                                print(f"{hero}")
                                print(f"Vous attaquez. .. !\n")
                                time.sleep(1)
                                print("---- - ->")
                                print("---- - ->")
                                print()
                                print(f"Un coup {arme_un}  // {degats} Dégats")
                                print()
                                time.sleep(2)
                                print("----- tour ennemi -------")
                                print()
                                print(f"{bot_hero}")
                                print(f"Il attaque. .. !\n")
                                time.sleep(1)
                                print("---- - ->")
                                print("---- - ->")
                                print()
                                print(f"Un coup aléatoire // {bot_degats} Dégats")
                                print()
                                print(f"Fin du tour {tour}")
                                print("----------------------------------------------------")
                                print("chargement. . .")
                                time.sleep(5)
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
                                print()
                                print(f"{hero}")
                                print(f"Vous attaquez. .. !\n")
                                time.sleep(1)
                                print("---- - ->")
                                print("---- - ->")
                                print()
                                print(f"Un coup {arme_deux}  // {degats} Dégats")
                                print()
                                time.sleep(2)
                                print("----- tour ennemi -------")
                                print()
                                print(f"{bot_hero}")
                                print(f"Il attaque. .. !\n")
                                time.sleep(1)
                                print("---- - ->")
                                print("---- - ->")
                                print()
                                print(f"Un coup aléatoire // {bot_degats} Dégats")
                                print()
                                print(f"Fin du tour {tour}")
                                print("----------------------------------------------------")
                                print("chargement. . .")
                                time.sleep(5)
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
                                degats = 0
                                bot_degats = int(bot_attaque-((bot_attaque * contre)/100))
                                bot_vie += degats
                                vie -= bot_degats

                                print()
                                print(f"{hero}")
                                print(f"Vous attaquez. .. !\n")
                                time.sleep(1)
                                print("---- - ->")
                                print("---- - ->")
                                print()
                                print(f"Un coup {arme_trois}  // {degats} Dégats")
                                print()
                                time.sleep(2)
                                print("----- tour ennemi -------")
                                print()
                                print(f"{bot_hero}")
                                print(f"Il attaque. .. !\n")
                                time.sleep(1)
                                print("---- - ->")
                                print("---- - ->")
                                print()
                                print(f"Un coup aléatoire //  {bot_attaque} / -{bot_degats}Dégats")
                                print()
                                print(f"Fin du tour {tour}")
                                print("----------------------------------------------------")
                                print("chargement. . .")
                                time.sleep(5)
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
