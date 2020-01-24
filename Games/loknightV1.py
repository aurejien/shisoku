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
print(f"                   {game_name}                     ")
print("                hello@aurelienj.dev                 ")
print()
print("----------------------------------------------------")
player_name = input("Your name. \n> ").lower().title()
elixir = "Elixir de vie"
boost = "Boost d'attaque"
plus_vie = 0
plus_attaque = 0
argent = 500
xp = 0
bypass = 1
attaque_boost = 0
if player_name == "666":
  plus_vie = 1
  plus_attaque = 1
  argent = 1000
  print(f"Boost Hero")
  player_name = input("Your name. \n> ").lower().title()
rules = input("{1} Pour afficher les règles\n{2} Pour passer\n>  ")
if rules == "1":
  print()
  print()
  print(f"Bienvenue sur {game_name}, le jeu est encore en développement")
  print("Les règles sont simple, tu choisis un héro,\ntu choisis entrainement pour te battre contre des bots")
  print("Tu as 3 coups qui coutent des cristaux pour pouvoir attaquer")
  print("Chaque victoire te raporte des $ pour acheter des boosts")
  print("Bon jeu..")
  print("C'est un peu le fouilli désolé")
  print()
  print()
  print("Loading . . .")
  time.sleep(15)
else:
  print("Bon jeu alors")
  print("Loading . . .")
  time.sleep(1)
print()
print("----------------------------------------------------")
print()
print(f"Bienvenue {player_name}")
print("Jeu de combat tour par tour")
print()
print("----------------------------------------------------")
print()
print("Choisi ton hero")
print("{1} Cavalier: Attaque: +++    Vie: ++++ Cristaux ++")
print("{2} Archer:   Attaque: ++++   Vie: +++  Cristaux ++++")
print()
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

            gems_Un = 1
            gems_Deux = 5
            gems_Trois = 2

        elif hero_choix == 2:

            hero = "L'Archer"  # Archer
            attaque_un = 30            # fleche normal
            attaque_deux = 65          # fleche de feux
            contre = 40                # Pas chassé

            arme_un = "Simple flèche"
            arme_deux = "La fléche de feu"
            arme_trois = "Le pas chassé"

            arme_Un_un = "Simple flèche"
            arme_Un_deux = "la flèche de feu"
            arme_Un_trois = "Le pas chassé"

            gems_Un = 4
            gems_Deux = 7
            gems_Trois = 2
        else:
            raise ValueError
    except ValueError:
        print("Erreur des données.")
        hero_choix = -1
print(f"{player_name} tu as choisis {hero}")
print()
print("Loading . . .\n")
time.sleep(1)
while True:
    if hero_choix == 1:
        vie = 200
    elif hero_choix == 2:
        vie = 150
    gems = 10
    print("----------------------------------------------------")
    print(f"{player_name}")
    print(f"  {gems}◊")
    print(f"  {xp}xp")
    print(f"  Argent {argent}$")
    print(f"  {plus_vie} {elixir} - {plus_attaque} {boost}")
    print()
    time.sleep(2)
    print(f"{hero}: vie {vie}")
    print(f"  ↓{gems_Un}◊  {arme_Un_un}: -{attaque_un}")
    print(f"  ↓{gems_Deux}◊  {arme_Un_deux}: -{attaque_deux}")
    print(f"  ↑{gems_Trois}◊  {arme_Un_trois} reduit de {contre}% l'attaque ennemi")
    print()
    print("Shop")
    print(f"  {10} 400$ {elixir} +50%\n  {11} 300$ {boost} +50\n")
    print()
    print("Combats")
    print("  {-} Combat. Bientôt disponible\n  {2} Entrainement\n")
    print()
    menu_choix = -1
    while menu_choix <= 0:
        menu_choix = input("Faite votre choix\n> ")
        print("----------------------------------------------------")
        print()
        time.sleep(2)
        try:
            menu_choix = int(menu_choix)
            if menu_choix == 10:
              if argent > 399:
                plus_vie += 1
                argent -= 400
                print(f"Vous avez {plus_vie} {elixir}")
                print(f" il vous reste {argent}$")
                print()
                break
              else:
                print(f"{player_name} vous n'avez pas assé d'argent!")
                print(f"il vous reste {argent}$")
                print()
                break
            elif menu_choix == 11:
              if argent > 299:
                plus_attaque += 1
                argent -= 300
                print(f"Vous avez {plus_attaque} {boost}")
                print(f"il vous reste {argent}$")
                print()
                break
              else:
                print(f"{player_name} vous n'avez pas assé d'argent!")
                print(f" il vous reste {argent}$")
                print()
                break
              print(f"Vous obtenez {plus_attaque} {boost}")
              print(f" il vous reste {argent}$")
              print()
              menu_choix = input("Faite votre choix\n> ")
              menu_choix = int(menu_choix)
            elif menu_choix == 1:
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

                            list_attaque = [10, 25, 0, 5, 50, 20, 35]
                            bot_hero = "bot_111"
                            bot_vie = vie - 50


                            xp_up = 200
                            argent_up = 75

                            break
                        # =========================== BOT NORMAL
                        elif bot_level == 2:
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print()

                            list_attaque = [0, 50, 15, 5, 20, 60, 40]
                            bot_hero = "bot_444"
                            bot_vie = vie - 20

                            xp_up = 500
                            argent_up = 150

                            break
                        # =========================== BOT DIFFICILE
                        elif bot_level == 3:
                            print()
                            print("Création du bot. . .")
                            time.sleep(1.5)
                            print()

                            list_attaque = [0, 20, 20, 60, 75, 50, 50, 50, 55, 65]
                            bot_hero = "bot_666"
                            bot_vie = vie
                            
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
                        print(f"{player_name} vous avez perdu \nVous remportez {xp_up}xp {argent_up}$")
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        break
                    elif bot_vie <= 0:
                        print()
                        print(f"{player_name} vous avez gagné\nVous remportez {xp_up}xp {argent_up}$")
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
                        print(f"{player_name} vous avez perdu\nVous remportez {xp_up}xp {argent_up}$")
                        print()
                        print("Retour au menu. . .")
                        print()
                        time.sleep(2)
                        break
                    combat = -1
                    while combat <= 0:
                        print("--------")
                        print(f"tour {tour}  |")
                        print("----------------------------------------------------")
                        print()
                        print(f"   vie {vie} - {hero}")
                        print(f"   vie {bot_vie} - {bot_hero}")
                        print()
                        print(f"   {gems}◊ restant")
                        print()
                        print("----------------------------------------------------")
                        print(f"{{1}} ↓{gems_Un}◊  {arme_Un_un}: -{attaque_un}")
                        print(f"{{2}} ↓{gems_Deux}◊  {arme_Un_deux}: -{attaque_deux}")
                        print(f"{{3}} ↑{gems_Trois}◊  {arme_Un_trois} reduit de {contre}% l'attaque ennemi")
                        print(f"{{10}} {plus_vie} {elixir} - {{11}} {plus_attaque} {boost}")
                        print()
                        combat = int(input("> "))
                        print("----------------------------------------------------")
                        try:
                            combat = int(combat)
                            if combat == 10:
                              if plus_vie > 0:
                                print(f"Vous utilisez {elixir}, Vie {vie}!")
                                print("Gloouuuu GLouuuuu")
                                plus_vie -= 1
                                time.sleep(1)
                                vie_demi = int(vie/2)
                                vie = int(vie + vie_demi)
                                print(f"Vous gagnez +{vie_demi} de vie, Vie {vie}")
                                print(f"Retour au combat")
                                time.sleep(1.5)
                              else:
                                print(f"Vous ne pouvez pas utiliser l'{elexir}")
                                print(f"Vous avez {plus_vie}")
                                print(f"Retour au combat")
                                time.sleep(1.5)
                              tour += 1
                            elif combat == 11:
                              if plus_attaque > 0:
                                print(f"Vous utilisez {boost}!")
                                print("Gloouuuu GLouuuuu")
                                plus_attaque -=1
                                attaque_boost = 50
                                time.sleep(1)
                                print(f"{player_name} attention tu ne peux pas cummuler les boosts d'attaque")
                                print(f"Vous boostez +50% votre prochaine attaque")
                                print(f"Retour au combat")
                                time.sleep(1.5)
                              else:
                                print(f"Vous ne pouvez pas utiliser le {boost}")
                                print(f"Vous avez {plus_attaque}{boost}")
                                print(f"Retour au combat")
                                time.sleep(1.5)
                              tour += 1
                            elif combat == 1:
                                if gems <= 0:
                                  print(f"{gems}◊ restant")
                                  bypass = 0
                                  break
                                elif hero_choix == 1:
                                  if gems < 1:
                                    print(f"{gems}◊ restant")
                                    print(f"Tu ne peux pas utiliser {arme_Un_un}, tu n'as pas assé de cristaux.")
                                    break
                                  gems -= 1
                                elif hero_choix == 2:
                                  if gems < 4:
                                    print(f"{gems}◊ restant")
                                    print(f"Tu ne peux pas utiliser {arme_Un_un}, tu n'as pas assé de cristaux.")
                                    break
                                  gems -= 4
                                bot_attaque = choice(list_attaque)
                                bot_vie -= attaque_un + attaque_boost
                                vie -= bot_attaque
                                degats = attaque_un + attaque_boost
                                bot_degats = bot_attaque
                                print()
                                print(f"{hero}")
                                print(f"Vous attaquez. .. !\n")
                                if attaque_boost == 50:
                                  attaque_boost = 0
                                  print("Ton attaque est boosté +50")
                                  print(f"Un coup {arme_un}  // {degats} Dégats")
                                else:
                                  print(f"Un coup {arme_un}  // {degats} Dégats")
                                print()
                                time.sleep(2)
                                print("----- tour ennemi -------")
                                print()
                                print(f"{bot_hero}")
                                print(f"Il attaque. .. !\n")
                                print(f"Un coup aléatoire // {bot_degats} Dégats")
                                print()
                                print(f"Fin du tour {tour}")
                                print("----------------------------------------------------")
                                print("chargement. . .")
                                time.sleep(5)
                                print()
                                tour += 1
                            elif combat == 2:
                                if gems <= 0:
                                  print(f"{gems}◊ restant")
                                  bypass = 0
                                  break
                                if hero_choix == 1:
                                  if gems < 5:
                                    print(f"{gems}◊ restant")
                                    print(f"Tu ne peux pas utiliser {arme_Un_deux}, tu n'as pas assé de cristaux.")
                                    break
                                  gems -= 5
                                elif hero_choix == 2:
                                  if gems < 7:
                                    print(f"{gems}◊ restant")
                                    print(f"Tu ne peux pas utiliser {arme_Un_deux}, tu n'as pas assé de cristaux.")
                                    break
                                  gems -= 7
                                bot_attaque = choice(list_attaque)
                                bot_vie -= attaque_deux + attaque_boost
                                vie -= bot_attaque
                                degats = attaque_deux + attaque_boost
                                bot_degats = bot_attaque
                                print()
                                print(f"{hero}")
                                print(f"Vous attaquez. .. !\n")
                                if attaque_boost == 50:
                                  attaque_boost = 0
                                  print("Ton attaque est boosté +50")
                                  print(f"Un coup {arme_deux}  // {degats} Dégats")
                                else:
                                  print(f"Un coup {arme_deux}  // {degats} Dégats")
                                print()
                                time.sleep(2)
                                print("----- tour ennemi -------")
                                print()
                                print(f"{bot_hero}")
                                print(f"Il attaque. .. !\n")
                                print(f"Un coup aléatoire // {bot_degats} Dégats")
                                print()
                                print(f"Fin du tour {tour}")
                                print("----------------------------------------------------")
                                print("chargement. . .")
                                time.sleep(5)
                                print()
                                tour += 1
                            elif combat == 3:
                                if gems <= 0:
                                  print(f"{gems}◊ restant")
                                  bypass = 0
                                  break
                                if hero_choix == 1:
                                  gems += 2
                                elif hero_choix == 2:
                                  gems += 2
                                bot_attaque = choice(list_attaque)
                                degats = 0
                                bot_degats = int(bot_attaque-((bot_attaque * contre)/100))
                                bot_vie += degats
                                vie -= bot_degats
                                print()
                                print(f"{hero}")
                                print(f"Vous attaquez. .. !\n")
                                print(f"Un coup {arme_trois}  // {degats} Dégats")
                                print()
                                time.sleep(2)
                                print("----- tour ennemi -------")
                                print()
                                print(f"{bot_hero}")
                                print(f"Il attaque. .. !\n")
                                print(f"Un coup aléatoire //  {bot_attaque} / -{bot_degats}Dégats")
                                print()
                                print(f"Fin du tour {tour}")
                                print("----------------------------------------------------")
                                print("chargement. . .")
                                time.sleep(5)
                                tour += 1
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
