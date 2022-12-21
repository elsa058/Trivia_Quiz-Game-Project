from colorama import Fore
import pyodbc


class Trivia_game():
    def game_1(self):
        print(Fore.LIGHTBLUE_EX + '\n\t\t\t\t\t\t.......WELCOME TO TRIVIA GAME........... \n' + Fore.RESET)
        user = int(input(Fore.LIGHTBLUE_EX + "\t\t Choose the Question what you want \n\n" + Fore.RESET +
                         Fore.LIGHTMAGENTA_EX +'1.Enter for General knowledge_Questions\n'+ Fore.RESET +
                         Fore.LIGHTMAGENTA_EX +'2.Enter for Mathematics Questions\n' + Fore.RESET +
                         Fore.LIGHTMAGENTA_EX + '3.Enter for Programming Questions \n' + Fore.RESET ))
        if user == 1:
            Generals = pyodbc.connect('Driver={SQL Server};'
                                      'Server=LAPTOP-G1C1N8VG;'
                                      'Database=Game;'
                                      'Trusted_Connection=yes;')

            X = 'SELECT Question,A,B,C,D ,Answer FROM dbo.Generals_Questions'
            cursor = Generals.cursor()
            cursor.execute(X)
            score = 0
            for i in cursor:
                print(i[0])
                print("A", i[1], "\n", "B", i[2], "\n", "C", i[3], "\n", "D", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "Choose the best  answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/10")

        elif user == 2:
            Maths_Questions = pyodbc.connect('Driver={SQL Server};'
                                    'Server=LAPTOP-G1C1N8VG;'
                                    'Database=Game;'
                                    'Trusted_Connection=yes;')

            Y = 'SELECT Question,A,B,C,D,Answer FROM dbo.Maths_Questions1'
            cursor = Maths_Questions.cursor()
            cursor.execute(Y)
            score = 0
            for i in cursor:
                print(i[0])
                print(i[1], "\n", i[2], "\n", i[3], "\n", i[4])
                Answer = input(Fore.LIGHTYELLOW_EX + "Choose the  best answer:" + Fore.RESET)
                if Answer == i[5]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
            print("yor final score is :", score, "/5")
        elif user == 3:
            Programming_Questions = pyodbc.connect('Driver={SQL Server};'
                                                   'Server=LAPTOP-G1C1N8VG;'
                                                   'Database=Game;'
                                                   'Trusted_Connection=yes;')
            Z= 'SELECT Question,True,false,Answer FROM dbo.Programming_Questions'
            cursor = Programming_Questions.cursor()
            cursor.execute(Z)
            score = 0
            for i in cursor:
                print(i[0])
                print(i[1],"\n",i[2])
                Answer = input(Fore.LIGHTYELLOW_EX + "Choose the  best answer:" + Fore.RESET)
                if Answer == i[2]:
                    score += 1
                    print(Fore.LIGHTBLUE_EX + "correct answer" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLUE_EX + "Incorrect answer" + Fore.RESET)
                    print("yor final score is :", score, "/10")
            else:
                print("Thank you good by")
                exit()



Quiz = Trivia_game()
Quiz.game_1()