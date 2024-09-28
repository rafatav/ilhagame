print('''
                             ___....___
                     __..-:'':__:..:__:'':-..__
                 _.-:__:.-:'':  :  :  :'':-.:__:-._
               .':.-:  :  :  :  :  :  :  :  :  :._:'.
            _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
           [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
  :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
  !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
  ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
           [ ]                                        [ ]
           [ ]                                        [ ]
     jgs   [ ]                                        [ ]
   ~~^_~^~/   \~^-~^~ _~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/   \~^ ~~_ ^
''')
play = True
while play:
    print("Bem vindo à ILHA DO FUNDÃO!")
    print("Sua missão é encontrar um baú cheio de ***** escondido na UFRJ.")
    lado = input('Você chegou a uma encruzilhada na Linha Vermelha a caminho da ilha. Pra que lado você vai? Digite "esquerda" ou "direita". ')
    lado = lado.lower()

    print(lado)
    if lado == "esquerda":
      nadar_esperar = input('Muito bem! Mas a ponte de entrada da ilha caiu por falta de verba. Digite "nadar" se for apressadinho(a) ou digite "esperar" se for sensato(a). ')
      nadar_esperar = nadar_esperar.lower()
      if nadar_esperar == "esperar":
        baus = ["vermelho", "amarelo", "azul"]
        baus = input('O prefeito Dudu Paes apareceu de helicóptero e te deu uma carona até a UFRJ! Você achou três baús de cores diferentes. Qual cor você escolhe? Digite "vermelho", "amarelo" ou "azul". ')
        baus = baus.lower()
        if baus.count("amarelo"):
          print("DING-DING-DING! Você achou o baú cheio de ***** e acabou convulsionando de tanta felicidade!")
          print("FIM DO JOGO.")
        elif baus.count("vermelho"):
          print("Armadilha! O baú vermelho estava cheio de pó de Antraz e você morreu intoxicado. Fim do Jogo.")
        else:
          print("Armadilha! O baú azul estava cheio de filmes do Rob Schneider e você morreu de tanto tédio. Fim do Jogo.")
      else:
        print("Você engoliu água contaminada da Baía de Guanabara e morreu de leptospirose. Fim do Jogo.")
    else:
      print("Você entrou na Favela da Maré por engano e morreu em uma operação policial. Fim do Jogo.")

    if input("Deseja jogar novamente? 's' ou 'n'? ") == "s":
        play = True
