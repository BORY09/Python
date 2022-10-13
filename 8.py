import random
start = input('Type "Y" to start a game : ')
opcje = ['papier','kamień','nożyce']

if start == "y":
        while quit != "n":
               
                wyborCP = random.choice(opcje)
                wyborGracza = input('Wybór gracza: ')
                if (wyborCP == wyborGracza):
                    print("Remis")
                elif wyborCP == 'nożyce':
                      if wyborGracza == 'kamień':
                          print("Wygrałeś")
                      else:
                          print("Przegrałeś :D")
                elif wyborCP =='papier':
                       if wyborGracza == 'nożyce':
                           print("Wygrałeś")
                       else:
                           print("Przegrałeś :D")
                elif wyborCP == 'kamień':
                        if wyborGracza == 'papier':
                            print("Wygrałeś")
                        else:
                            print("Przegrałeś :D")
                else:
                    print("Zły guzik")
                print("Ty: " + wyborGracza + " Komputer: " + wyborCP)
                quit = input('Jeszcze raz: [y/n]')


    
