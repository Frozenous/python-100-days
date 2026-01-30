print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input('You\'re at a Cross Roads, do you want to go "left" or "right"?\n').lower()
if first_choice == "left":
    print(r'''
         .-.                                    ,-.
  .-(   )-.                              ,-(   )-.
 (     __) )-.                        ,-(_      __)
  `-(       __)                      (_    )  __)-'
    `(____)-',                        `-(____)-'
  - -  :   :  - -
      / `-' \
    ,    |   .
         .                         _
                                  >')
               _   /              (\\         (W)
              =') //               = \     -. `|'
               ))////)             = ,-      \(| ,-
              ( (///))           ( |/  _______\|/____
~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::
            _                 ,----':::::::::::::::::
         {><_'c   _      _.--':::::::::::::::::::::::
__,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::
:.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:
.:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.
.....................................................
    ''')
    second_choice = input('You\'ve come upon a dock located on a wide fast moving river. '
                          'There is a sign stating that a boat will come every hour. '
                          'Do you want to "wait" or "swim" across?\n').lower()
    if second_choice == "wait":
        print(r'''
              ______
           ,-' ;  ! `-.
          / :  !  :  . \
         |_ ;   __:  ;  |
         )| .  :)(.  !  |
         |"    (##)  _  |
         |  :  ;`'  (_) (
         |  :  :  .     |
         )_ !  ,  ;  ;  |
         || .  .  :  :  |
         |" .  |  :  .  |
         |_____;----.___|
        ''')
        third_choice = input('The boat takes you to an island with a large building. '
                             'The building has doors of different colors; "Red", "Yellow", and "Blue". '
                             'Which door will you open?\n').lower()
        if third_choice == "yellow":
            print("You found the lost treasure and win!")
            print(r'''
             __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
            ''')
        elif third_choice == "blue":
            print("You stumble upon a monster's lair and get immediately gored to death!")
            print("GAME OVER")
            print(r'''
                                 (    )
                              ((((()))
                              |o\ /o)|
                              ( (  _')
                               (._.  /\__
                              ,\___,/ '  ')
                '.,_,,       (  .- .   .    )
                 \   \\     ( '        )(    )
                  \   \\    \.  _.__ ____( .  |
                   \  /\\   .(   .'  /\  '.  )
                    \(  \\.-' ( /    \/    \)
                     '  ()) _'.-|/\/\/\/\/\|
                         '\\ .( |\/\/\/\/\/|
                           '((  \    /\    /
                           ((((  '.__\/__.')
                            ((,) /   ((()   )
                             "..-,  (()("   /
                        pils  _//.   ((() ."
                      _____ //,/" ___ ((( ', ___
                                       ((  )
                                        / /
                                      _/,/'
                                    /,/,"
            ''')
        elif third_choice == "red":
            print("The room has a trap door and you fall into a burning pit of fire and die!")
            print("GAME OVER")
            print(r'''
                                       (  .      )
                       )           (              )
                             .  '   .   '  .  '  .
                    (    , )       (.   )  (   ',    )
                     .' ) ( . )    ,  ( ,     )   ( .
                  ). , ( .   (  ) ( , ')  .' (  ,    )
                 (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            ''')
        else:
            print("You failed to pick the right door in time and got shot with arrows from bandits crossing the lake!")
            print("GAME OVER")
            print(r'''
                             .... NO! ...                  ... MNO! ...
                       ..... MNO!! ...................... MNNOO! ...
                     ..... MMNO! ......................... MNNOO!! .
                    .... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
                     ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
                        ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
                       ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
                       ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
                        ....... MMMMM..    OPPMMP    .,OMI! ....
                         ...... MMMM::   o.,OPMP,.o   ::I!! ...
                             .... NNM:::.,,OOPM!P,.::::!! ....
                              .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
                             ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
                               .. MMMMMNNOOMMNNIIIPPPOO!! ......
                              ...... MMMONNMMNNNIIIOO!..........
                           ....... MN MOMMMNNNIIIIIO! OO ..........
                        ......... MNO! IiiiiiiiiiiiI OOOO ...........
                      ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
                       .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
                       ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
                          ...... OO! ................. ON! .......
                             ................................
                        ''')
    else:
        print("You get swept up in a current and drown!")
        print("GAME OVER")
        print(r'''
                 .... NO! ...                  ... MNO! ...
           ..... MNO!! ...................... MNNOO! ...
         ..... MMNO! ......................... MNNOO!! .
        .... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
         ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
            ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
           ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
           ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
            ....... MMMMM..    OPPMMP    .,OMI! ....
             ...... MMMM::   o.,OPMP,.o   ::I!! ...
                 .... NNM:::.,,OOPM!P,.::::!! ....
                  .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
                 ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
                   .. MMMMMNNOOMMNNIIIPPPOO!! ......
                  ...... MMMONNMMNNNIIIOO!..........
               ....... MN MOMMMNNNIIIIIO! OO ..........
            ......... MNO! IiiiiiiiiiiiI OOOO ...........
          ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
           .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
           ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
              ...... OO! ................. ON! .......
                 ................................
            ''')
else:
    print("You git bitten by a rattle snake and die!")
    print("GAME OVER")
    print(r'''
         .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
    ''')

