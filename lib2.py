import csv 
import os 
import keyboard 
import sys
import datetime

#creating instance
class LibraryManager():
    def __init__(self): 
        
        self.logo = """
                         __    _ __                                     
                        / /   (_) /_  _________ ________  __            
                       / /   / / __ \/ ___/ __ `/ ___/ / / /            
                      / /___/ / /_/ / /  / /_/ / /  / /_/ /             
            __  ___  /_____/_/_.___/_/   \__,_/_/   \__, /           __ 
           /  |/  /___ _____  ____ _____ ____  ____/____/___  ____  / /_
          / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ __ `__ \/ _ \/ __ \/ __/
         / /  / / /_/ / / / / /_/ / /_/ /  __/ / / / / /  __/ / / / /_  
        /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/ /_/ /_/\___/_/ /_/\__/  
                                 /____/                                              
        """
        
        self.error = """
         ______                     __
        / ____/_____________  _____/ /
       / __/ / ___/ ___/ __ \/ ___/ / 
      / /___/ /  / /  / /_/ / /  /_/  
     /_____/_/  /_/   \____/_/  (_)   
     """
     
        self.search = """
         _____                      __    __
        / ___/___  ____ ___________/ /_  / /
        \__ \/ _ \/ __ `/ ___/ ___/ __ \/ / 
       ___/ /  __/ /_/ / /  / /__/ / / /_/  
      /____/\___/\__,_/_/   \___/_/ /_(_)   
     """
    
        self.student_detail_logo = """
        _____ __            __           __     ____       __        _ __ 
       / ___// /___  ______/ /__  ____  / /_   / __ \___  / /_____ _(_) / 
       \__ \/ __/ / / / __  / _ \/ __ \/ __/  / / / / _ \/ __/ __ `/ / /  
      ___/ / /_/ /_/ / /_/ /  __/ / / / /_   / /_/ /  __/ /_/ /_/ / / /___
     /____/\__/\__,_/\__,_/\___/_/ /_/\__/  /_____/\___/\__/\__,_/_/_____/
     """
     
        self.result_logo = """
         ____                  ____       __
        / __ \___  _______  __/ / /______/ /
       / /_/ / _ \/ ___/ / / / / __/ ___/ / 
      / _, _/  __(__  ) /_/ / / /_(__  )_/  
     /_/ |_|\___/____/\__,_/_/\__/____(_)   
     """
        self.book_detail_logo = """
         ____              __      ____       __        _ __ 
        / __ )____  ____  / /__   / __ \___  / /_____ _(_) / 
       / __  / __ \/ __ \/ //_/  / / / / _ \/ __/ __ `/ / /  
      / /_/ / /_/ / /_/ / ,<    / /_/ /  __/ /_/ /_/ / / /___
     /_____/\____/\____/_/|_|  /_____/\___/\__/\__,_/_/_____/
                                                             
     """
        self.issue_logo = """
         ____                        ____              __        __
        /  _/___________  _____     / __ )____  ____  / /_______/ /
        / // ___/ ___/ / / / _ \   / __  / __ \/ __ \/ //_/ ___/ / 
      _/ /(__  |__  ) /_/ /  __/  / /_/ / /_/ / /_/ / ,< (__  )_/  
     /___/____/____/\__,_/\___/  /_____/\____/\____/_/|_/____(_)   
                                                                   
     """   
        self.issued_books = """
         ____                         __   ____              __        __
        /  _/___________  _____  ____/ /  / __ )____  ____  / /_______/ /
        / // ___/ ___/ / / / _ \/ __  /  / __  / __ \/ __ \/ //_/ ___/ / 
      _/ /(__  |__  ) /_/ /  __/ /_/ /  / /_/ / /_/ / /_/ / ,< (__  )_/  
     /___/____/____/\__,_/\___/\__,_/  /_____/\____/\____/_/|_/____(_)   
                                                                         
     """                           
        self.dash = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
        self.returnbooks_logo = """
         ____       __                      ____              __        __
        / __ \___  / /___  ___________     / __ )____  ____  / /_______/ /
       / /_/ / _ \/ __/ / / / ___/ __ \   / __  / __ \/ __ \/ //_/ ___/ / 
      / _, _/  __/ /_/ /_/ / /  / / / /  / /_/ / /_/ / /_/ / ,< (__  )_/  
     /_/ |_|\___/\__/\__,_/_/  /_/ /_/  /_____/\____/\____/_/|_/____(_)   
                                                                        
     """
        self.editdetailslogo = """
         ______    ___ __     ____       __        _ __     __
        / ____/___/ (_) /_   / __ \___  / /_____ _(_) /____/ /
       / __/ / __  / / __/  / / / / _ \/ __/ __ `/ / / ___/ / 
      / /___/ /_/ / / /_   / /_/ /  __/ /_/ /_/ / / (__  )_/  
     /_____/\__,_/_/\__/  /_____/\___/\__/\__,_/_/_/____(_)   
                                                            
     """  
        self.modifystudentlogo = """
         __  ___          ___ ____         _____ __            __           __  __
        /  |/  /___  ____/ (_) __/_  __   / ___// /___  ______/ /__  ____  / /_/ /
       / /|_/ / __ \/ __  / / /_/ / / /   \__ \/ __/ / / / __  / _ \/ __ \/ __/ / 
      / /  / / /_/ / /_/ / / __/ /_/ /   ___/ / /_/ /_/ / /_/ /  __/ / / / /_/_/  
     /_/  /_/\____/\__,_/_/_/  \__, /   /____/\__/\__,_/\__,_/\___/_/ /_/\__(_)   
                              /____/                                              
     """
        self.addstudentlogo = """
         ___       __    __   _____ __            __           __  __
        /   | ____/ /___/ /  / ___// /___  ______/ /__  ____  / /_/ /
       / /| |/ __  / __  /   \__ \/ __/ / / / __  / _ \/ __ \/ __/ / 
      / ___ / /_/ / /_/ /   ___/ / /_/ /_/ / /_/ /  __/ / / / /_/_/  
     /_/  |_\__,_/\__,_/   /____/\__/\__,_/\__,_/\___/_/ /_/\__(_)   
                                                                     
     """        
        self.removestudentlogo = """
         ____                                    _____ __            __           __  __
        / __ \___  ____ ___  ____ _   _____     / ___// /___  ______/ /__  ____  / /_/ /
       / /_/ / _ \/ __ `__ \/ __ \ | / / _ \    \__ \/ __/ / / / __  / _ \/ __ \/ __/ / 
      / _, _/  __/ / / / / / /_/ / |/ /  __/   ___/ / /_/ /_/ / /_/ /  __/ / / / /_/_/  
     /_/ |_|\___/_/ /_/ /_/\____/|___/\___/   /____/\__/\__,_/\__,_/\___/_/ /_/\__(_)   
                                                                                        
     """
        self.editstudentlogo = """
         ______    ___ __     _____ __            __           __  __
        / ____/___/ (_) /_   / ___// /___  ______/ /__  ____  / /_/ /
       / __/ / __  / / __/   \__ \/ __/ / / / __  / _ \/ __ \/ __/ / 
      / /___/ /_/ / / /_    ___/ / /_/ /_/ / /_/ /  __/ / / / /_/_/  
     /_____/\__,_/_/\__/   /____/\__/\__,_/\__,_/\___/_/ /_/\__(_)   
     """                   
        self.modifybooklogo = """
         __  ___          ___ ____         ____              __        __
        /  |/  /___  ____/ (_) __/_  __   / __ )____  ____  / /_______/ /
       / /|_/ / __ \/ __  / / /_/ / / /  / __  / __ \/ __ \/ //_/ ___/ / 
      / /  / / /_/ / /_/ / / __/ /_/ /  / /_/ / /_/ / /_/ / ,< (__  )_/  
     /_/  /_/\____/\__,_/_/_/  \__, /  /_____/\____/\____/_/|_/____(_)   
                              /____/                                     
     """
        self.addbooklogo = """
         ___       __    __   ____              __        __
        /   | ____/ /___/ /  / __ )____  ____  / /_______/ /
       / /| |/ __  / __  /  / __  / __ \/ __ \/ //_/ ___/ / 
      / ___ / /_/ / /_/ /  / /_/ / /_/ / /_/ / ,< (__  )_/  
     /_/  |_\__,_/\__,_/  /_____/\____/\____/_/|_/____(_)   
     """
        self.editbooklogo = """
         ______    ___ __     ____              __        __
        / ____/___/ (_) /_   / __ )____  ____  / /_______/ /
       / __/ / __  / / __/  / __  / __ \/ __ \/ //_/ ___/ / 
      / /___/ /_/ / / /_   / /_/ / /_/ / /_/ / ,< (__  )_/  
     /_____/\__,_/_/\__/  /_____/\____/\____/_/|_/____(_)   
     """
        self.removebooklogo = """
         ____                                    ____              __        __
        / __ \___  ____ ___  ____ _   _____     / __ )____  ____  / /_______/ /
       / /_/ / _ \/ __ `__ \/ __ \ | / / _ \   / __  / __ \/ __ \/ //_/ ___/ / 
      / _, _/  __/ / / / / / /_/ / |/ /  __/  / /_/ / /_/ / /_/ / ,< (__  )_/  
     /_/ |_|\___/_/ /_/ /_/\____/|___/\___/  /_____/\____/\____/_/|_/____(_)   
     """
        self.MainWindow()
    
    def _pause(self): 
        os.system("pause >NUL")
    
    def _clear(self): 
        os.system("cls")
    
    def _exit(self): 
        os.system("exit >NUL")

    def _input(self, preferred): 
        
        user_input = input(": ").strip()
        
        if not user_input in preferred: 
            raise Exception("You entered wrong choice! Please try again :/")
        else : 
            return user_input.lower()
            
    def get_int_input(self): 
        
        user_input = input(": ").strip()
        if user_input == "!":
                return "!"
        else:
            try: 
                user_input = int(user_input)

            except (ValueError, TypeError): 
                raise Exception("You must give an integer type input. Please try again.")
        
            else: 
                return user_input
            
        
    def MainWindow(self): 

        while True : 
            
            self._clear()
            print(self.logo)
            
            print("")
            print("Enter 1 for student and book details.")
            print("Enter 2 for book issue and return.")
            print("Enter 3 to edit details.")
            print("Enter 4 to exit.")
                
            acpreferred1 = ["1", "2", "3", "4"]
            try : 
                acinp1 = self._input(acpreferred1)
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            else : 
                break
                            
        if acinp1 == "1": 
            self.search_detail()
            
        elif acinp1 == "2": 
            self.issue()
        elif acinp1 == "3": 
            self.editdetails() 
        elif acinp1 == "4": 
            self._exit()

        self._pause()

    def search_detail(self): 
        
        while True : 
            self._clear()
            print(self.search)
            print("")
            
            print("")
            print("Enter 1 to search student details.")
            print("Enter 2 to search book details.")
            print("Enter 3 to get full table of students' detail.")
            print("Enter 4 to get full table of books' detail")
            print("Enter 5 to go back to main page")
            
            adpreferred1 = ["1", "2", "3", "4", "5"]

            try : 
                adinp1 = self._input(adpreferred1)
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            else : 
                break
        
        if adinp1 == "1": 
            self.student_detail()
        elif adinp1 == "2": 
            self.book_detail()
        elif adinp1 == "3": 
            self.all_detail_student() 
        elif adinp1 == "4": 
            self.all_detail_book()
        elif adinp1 == "5":
            self.MainWindow()
            
    def student_detail(self): 
        
        while True: 
            self._clear()
            print(self.student_detail_logo)
            print("\nEnter ! (exclamation mark) to go back", self.dash, "\n\n")
            print("Enter admission number of the student")

            
            try : 
                aeinp1 = self.get_int_input()
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if aeinp1 == "!":
                    self.search_detail()
                else:
                    aeinp1 = str(aeinp1)
                    break
                
        with open("data/student.csv", "r") as aefile1: 
            aeread1 = csv.reader(aefile1)
            aelist1 = []
            
            aehead1 = next(aeread1)
            for ae1 in aeread1: 
                if ae1:
                    aelist1.append(ae1[0])
            

        if aeinp1 not in aelist1: 
            self._clear()
            print(self.error)
            print("")
            print(f"No data found for student with admission number :- {aeinp1}")
            self._pause()
            self.student_detail()
        
        else : 
            self._clear()
            print(self.result_logo)
            print("")
            
            with open("data/student.csv", "r") as aefile2: 
                aeread2 = csv.reader(aefile2)
                for ae2 in aeread2 :
                    if ae2: 
                        if ae2[0] == aeinp1: 
                            aedata1 = ae2
            
            for name, value in zip(aehead1, aedata1): 
                name = "%10s"%name 
                
                print(f"{name} : {value}")
                
        self._pause()
        self.search_detail()
        
    def book_detail(self): 
        
        while True: 
            self._clear()
            print(self.book_detail_logo)
            print("\nEnter ! (exclamation mark) to go back to the Main Menu", self.dash, "\n\n")
            print("Enter the Book ID")
            
            afinp1 = input(": ").strip()
            if not afinp1: 
                self._clear()
                print(self.error)
                print("")
                print("Book ID cant be empty!!")
            else: 
                if afinp1 == "!":
                    self.MainWindow()
                else:
                    break
                
        with open("data/books.csv", "r") as affile1: 
            afread1 = csv.reader(affile1)
            aflist1 = []
            
            afhead1 = next(afread1)
            for af1 in afread1: 
                if af1:
                    aflist1.append(af1[0])
            
        if afinp1 not in aflist1: 
            self._clear()
            print(self.error)
            print("")
            print(f"No data found for book with Book ID :- {afinp1}")
            self._pause()
            self.student_detail()
        
        else : 
            self._clear()
            print(self.result_logo)
            print("")
            
            with open("data/books.csv", "r") as affile2: 
                afread2 = csv.reader(affile2)

                for af2 in afread2 :
                    if af2:
                        if af2[0] == afinp1: 
                            afdata1 = af2            
            for name, value in zip(afhead1, afdata1): 
                name = "%10s"%name 
                
                print(f"{name} : {value}")
                
        self._pause()
        self.search_detail()
            
    def all_detail_student(self): 
        self._clear()
        
        with open("data/student.csv", "r") as agfile1: 
            agread1 = csv.reader(agfile1)
            aghead1 = next(agread1)

            agentries = {}
            agentcount = 0
            agcolwid = {}
            for ag1 in agread1:
                if ag1:
                    agentcount += 1
                    agentries[agentcount] = ag1

            if agentries:
                for aga in range(1,6):
                    aglarge = len(aghead1[aga-1])
                    for agb in range(1,agentcount+1):
                        if len(agentries[agb][aga-1]) > aglarge:
                            aglarge = len(agentries[agb][aga-1])
                        agcolwid[aga] = aglarge
            else:
                for aga in range(1,6):
                    agcolwid[aga] = len(aghead1[aga])

            print(self.result_logo, self.dash, "\n\n")

            ageql = '='
            agdash = '-'
            agspc = ' '
            for agc in range (1,6):
                print ("+="+ageql*agcolwid[agc]+"=",end="")
            print("+")
            for agd in range (1,6):
                print("| "+aghead1[agd-1]+(agcolwid[agd]-len(aghead1[agd-1]))*agspc+" ",end="")
            print("|")
            for age in range (1,6):
                print ("+="+ageql*agcolwid[age]+"=",end="")
            print("+")

            for agf in range (1,agentcount+1):
                for agg in range(1,6):
                    print("| "+agentries[agf][agg-1]+(agcolwid[agg]-len(agentries[agf][agg-1]))*agspc+" ",end="")
                print("|")

            for agh in range (1,6):
                print ("+-"+agdash*agcolwid[agh]+"-",end="")
            print("+")


        self._pause()
        self.search_detail()
                
    def all_detail_book(self): 
        self._clear()
        
        with open("data/Books.csv", "r") as ahfile1: 
            ahread1 = csv.reader(ahfile1)
            ahhead1 = next(ahread1)

            ahentries = {}
            ahcolwid = {}
            ahentcount = 0
            for ah1 in ahread1:
                if ah1:
                    ahentcount += 1
                    ahentries[ahentcount] = ah1

            
            if ahentries:
                for aha in range(1,9):
                    ahlarge = len(ahhead1[aha-1])
                    for ahb in range(1,ahentcount+1):
                        if len(ahentries[ahb][aha-1]) > ahlarge:
                            ahlarge = len(ahentries[ahb][aha-1])
                        ahcolwid[aha] = ahlarge
            else:
                for aha in range(1,9):
                    ahcolwid[aha] = len(ahhead1[aha])

            print(self.result_logo, self.dash, "\n\n")

            aheql = '='
            ahdash = '-'
            ahspc = ' '
            for ahc in range (1,9):
                print ("+="+aheql*ahcolwid[ahc]+"=",end="")
            print("+")
            for ahd in range (1,9):
                print("| "+ahhead1[ahd-1]+(ahcolwid[ahd]-len(ahhead1[ahd-1]))*ahspc+" ",end="")
            print("|")
            for ahe in range (1,9):
                print ("+="+aheql*ahcolwid[ahe]+"=",end="")
            print("+")

            for ahf in range (1,ahentcount+1):
                for ahg in range(1,9):
                    print("| "+ahentries[ahf][ahg-1]+(ahcolwid[ahg]-len(ahentries[ahf][ahg-1]))*ahspc+" ",end="")
                print("|")

            for ahh in range (1,9):
                print ("+-"+ahdash*ahcolwid[ahh]+"-",end="")
            print("+")

        self._pause()
        self.search_detail()

    def issue(self):
        while True:

            self._clear()
            print(self.issue_logo)

            print("\nEnter 1 to Issue new Books.")
            print("Enter 2 to return books.")
            print("Enter 3 to get list of issued books")
            print("Enter 4 to go back to main window")
                
            aipreferred1 = ["1", "2", "3", "4"]
            try : 
                ainp1 = self._input(aipreferred1)
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            else : 
                break
                            
        if ainp1 == "1": 
            self.issuenew()
        elif ainp1 == "2": 
            self.returnbooks()
        elif ainp1 == "3": 
            self.issuelist()
        else:
            self.MainWindow()

        self._pause()

    def issuenew(self):
        while True:

            self._clear()
            print(self.issue_logo)
            print("\nEnter ! (exclamation mark) to go back",self.dash, "\n\n")
            print("Enter admission number of the student")

            try : 
                ajadmno = self.get_int_input()

            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if str(ajadmno) == "!":
                    self.issue()
                else:
                    ajadmno = str(ajadmno)
                    break

        with open("data/student.csv", "r") as ajfile1: 
            ajread1 = csv.reader(ajfile1)
            ajlist1 = []
            
            ajhead1 = next(ajread1)
            for aj1 in ajread1: 
                if aj1:
                    ajlist1.append(aj1[0])

            if ajadmno not in ajlist1:
                self._clear()
                print(self.error)
                print("")
                print(f"No data found for student with admission number :- {ajadmno}")
                self._pause()
                self.issuenew()

        
            else : 
                self._clear()
                print(self.issue_logo)
                print("\nEnter ! (exclamation mark) to go back",self.dash,"\n\n")


        with open("data/student.csv", "r") as ajfile2: 
            ajread2 = csv.reader(ajfile2)
            ajlist2 = [] 

            for aj2 in ajread2:
                if aj2 and aj2[0] == ajadmno:
                    ajdata1 = aj2

            for name, value in zip(ajhead1, ajdata1): 
                name = "%10s"%name 
                print(f"{name} : {value}")

        print ("\nEnter the book ID of the book to be issued")

        ajbookid = input(": ").strip()
        if not ajbookid: 
            self._clear()
            print(self.error)
            print("")
            print("Book ID cant be empty!!")
        elif ajbookid == "!":
            self.issue()
                
        with open("data/books.csv", "r") as ajfile3: 
            ajread3 = csv.reader(ajfile3)
            ajlist3 = []
            
            ajhead3 = next(ajread3)
            for aj3 in ajread3: 
                if aj3:    
                    ajlist3.append(aj3[0])
            
            if ajbookid not in ajlist3: 
                self._clear()
                print(self.error)
                print("")
                print(f"No data found for book with Book ID :- {ajbookid}")
                self._pause()
                self.issuenew()
                        
            else : 
                print("")
                        
        with open("data/books.csv", "r") as ajfile4: 
            ajread4 = csv.reader(ajfile4)

            for aj4 in ajread4 :
                if aj4 and aj4[0] == ajbookid: 
                    ajdata4 = aj4
                            
            for name, value in zip(ajhead3, ajdata4): 
                name = "%10s"%name 
                                
                print(f"{name} : {value}")

            print(self.dash, "\n")

        while True:
            print("Confirm book issue? y/n")

            ajpreferred5 = ["y", "Y", "n", "N"]
            try : 
                ajinp5 = self._input(ajpreferred5)
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            else : 

                if ajinp5 == "y" or "Y":
                    with open('data/borrow.csv', 'r') as ajfile5:
                        ajread5 = csv.reader(ajfile5)
                        ajhead5 = next(ajread5)
                         
                        for aj5 in ajread5:
                            if aj5:
                                if aj5[0] == ajbookid:
                                    self._clear()
                                    print(self.error, self.dash, "\n\n")
                                    print("This book has already been issued to admission no.: " ,aj5[1])
                                    print("Please choose a different book or get this book returned first.")
                                    self._pause()
                                    self.issue()
                                elif aj5[1] == ajadmno:
                                    self._clear()
                                    print(self.error, self.dash, "\n\n")
                                    print("This student has already been issued a book with Book ID: ",aj5[0])
                                    print("Please return Book ID: ", aj5[0], " to issue a new book.")
                                    self._pause()
                                    self.issue()

                            
                    self._clear()
                    print(self.issue_logo)
                    print("\n",self.dash, "\n\n")
                    ajdate = datetime.date.today()
                    with open('data/borrow.csv','r') as ajinp6:
                        ajread6 = csv.reader(ajinp6)
                        ajcontent = {}
                        ajentcount = 0
                        for aj6 in ajread6:
                            if aj6:
                                ajentcount += 1
                                ajcontent[ajentcount] = aj6
                        ajcontent[ajentcount+1] = [ajbookid,ajadmno,ajdate]

                    with open('data/borrow.csv','w') as ajoutp7:
                        ajwriter7 = csv.writer(ajoutp7)
                        for aj7 in range(1,ajentcount+2):
                            ajwriter7.writerow(ajcontent[aj7])

                    print('Book successfully issued!')

                    self._pause()
                    self.issue()
                else:
                    self.issuenew()#issue books


    def returnbooks(self):
        while True:
            self._clear()
            print(self.returnbooks_logo,"\n","Enter ! (exclamation mark) to go back\n\n", self.dash)
            print("Enter Book ID of the book to be returned")

            akinp1 = input(": ").strip()
            if not akinp1: 
                self._clear()
                print(self.error)
                print("")
                print("Book ID cant be empty!!")
                self._pause()
            else: 
                if akinp1 == "!":
                    self.issue()
                else:
                    break
                    
        with open("data/books.csv", "r") as akfile1: 
            akread1 = csv.reader(akfile1)
            aklist1 = []
                
            akhead1 = next(akread1)
            for ak1 in akread1:
                if ak1: 
                    aklist1.append(ak1[0])

        if akinp1 not in aklist1: 
            self._clear()
            print(self.error)
            print("")
            print(f"No data found for book with Book ID :- {akinp1}")
            self._pause()
            self.returnbooks()

        with open("data/borrow.csv", "r") as akfile2:
            akread2 = csv.reader(akfile2)
            aklist2 = []
            akhead2 = next(akread2)
            for ak2 in akread2:
                if ak2:
                    aklist2.append(ak2[0])

        if akinp1 not in aklist2:
            self._clear()
            print(self.error)
            print("")
            print(f"The book has not been issued previously and is available in the library!")
            self._pause()
            self.returnbooks()
        else:
            print("\nThe book:\n")
            with open("data/books.csv", "r") as akfile3: 
                akread3 = csv.reader(akfile3)
                akhead3 = next(akread3)
                for ak3 in akread3 :
                    if ak3 and ak3[0] == akinp1: 
                        akdata3 = ak3
            
            for name, value in zip(akhead3, akdata3): 
                name = "%10s"%name 
                
                print(f"{name} : {value}")
            print("\nBorrowed by student:~\n")

            with open("data/borrow.csv", "r") as akfile4:
                akread4 = csv.reader(akfile4)
                aklist4 = []
                for ak4 in akread4:
                    if ak4:
                        if akinp1 == ak4[0]:
                            akadm = ak4[1]
            with open("data/student.csv", "r") as akfile5:
                akread5 = csv.reader(akfile5)
                akhead5 = next(akread5)
                for ak5 in akread5 : 
                    if ak5 and ak5[0] == akadm: 
                        akdata5 = ak5
            
                for name, value in zip(akhead5, akdata5): 
                    name = "%10s"%name 
                
                    print(f"{name} : {value}")

            while True:

                print(self.dash,"\nConfirm book return? y/n")
                akpreferred2 = ["y", "Y", "n", "N"]
                try : 
                    akinp2 = self._input(akpreferred2)
                except Exception as err: 
                    self._clear()
                    print(self.error)
                    print("")
                    print(err)
                    self._pause()
                    continue
                else :
                    if akinp2 == "y" or "Y":
                        with open('data/borrow.csv', 'r') as akinp6:
                            akread6 = csv.reader(akinp6)
                            akcontent = {}
                            akentcount = 0
                            for ak6 in akread6:
                                if ak6:
                                    if ak6[0] != akinp1:
                                        akentcount += 1
                                        akcontent[akentcount] = ak6


                        with open('data/borrow.csv', 'w') as akoutp7:
                            akwriter7 = csv.writer(akoutp7)
                            for ak7 in range(1,akentcount+1):
                                akwriter7.writerow(akcontent[ak7])
                        self._clear()
                        print(self.returnbooks_logo, self.dash,"\n\n\n")
                        print("Book successfully returned!")
                        self._pause()
                        self.issue()

                    else:
                        self.returnbooks()

    def issuelist(self):
        self._clear()
        print(self.issued_books, self.dash, "\n\n")
        with open('data/borrow.csv', 'r') as i1:
            readi1 = csv.reader(i1)

            headi1 = next(readi1)
            

            
            borrowcontents = {} # mapped rows in csv
            count = 0
            colwid2 = {}
            
            for i1 in readi1:
                if i1:
                    
                    count += 1
                    borrowcontents[count] = i1

            
            if borrowcontents:
                for a in range(1,4):
                    large = len(headi1[a-1])
                    for b in range(1,count+1):
                        if len(borrowcontents[b][a-1]) > large:
                            large = len(borrowcontents[b][a-1])
                        colwid2[a] = large
            else:
                for a in range(1,4):
                    colwid2[a] = len(headi1[a])
           
            eql = '='
            dash = '-'
            spc = ' '
            for c in range (1,4):
                print ("+="+eql*colwid2[c]+"=",end="")
            print("+")
            for d in range (1,4):
                print("| "+headi1[d-1]+(colwid2[d]-len(headi1[d-1]))*spc+" ",end="")
            print("|")
            for e in range (1,4):
                print ("+="+eql*colwid2[e]+"=",end="")
            print("+")

            for f in range (1,count+1):
                for g in range(1,4):
                    print("| "+borrowcontents[f][g-1]+(colwid2[g]-len(borrowcontents[f][g-1]))*spc+" ",end="")
                print("|")

            for h in range (1,4):
                print ("+-"+dash*colwid2[h]+"-",end="")
            print("+")


        self._pause()
        self.issue()
    
    def editdetails(self):
        while True:
            self._clear()
            print(self.editdetailslogo, self.dash,"\n\n")
            print("Enter 1 to modify student details.")
            print("Enter 2 to modify book details.")
            print("Enter 3 to go back")
                
            ampreferred1 = ["1", "2", "3"]

            try : 
                aminp1 = self._input(ampreferred1)
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            else : 
                break
        
        if aminp1 == "1":
            self.modifystudent()
        elif aminp1 == "2":
            self.modifybook()
        else:
            self.MainWindow()

    def modifystudent(self):
        while True : 
                
            self._clear()
            print(self.modifystudentlogo, self.dash, "\n\n")
            print("Enter 1 to add new student data")
            print("Enter 2 to remove existing student data")
            print("Enter 3 to EDIT existing student data")
            print("Enter 4 to go back")
            
                              
            anprefer1= ["1", "2", "3", "4"]
            try : 
                cho = self._input(anprefer1)
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            else : 
                break
                            
        if cho == "1": 
            self.addstudent()
                
        elif cho == "2": 
            self.removestudent()
        elif cho == "3": 
            self.editstudent() 
        else: 
            self.editdetails()

        self._pause()

    def addstudent(self):

        while True : 
                
            self._clear()
            print(self.addstudentlogo,"\nEnter ! (exclamation mark) to go back", self.dash, "\n\n")
            print("Enter the admission number of the new student", end = '' )
            
            try : 
                aqadmno = self.get_int_input()
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if aqadmno == "!":
                    self.editdetails()
                else:
                    aqadmno = str(aqadmno)
                    break
            
        with open('data/student.csv', 'r') as aqfile1:
            aqread1 = csv.reader(aqfile1)
            aqhead1 = next(aqread1)
                         
            for aq1 in aqread1:
                if aq1:
                    if aq1[0] == aqadmno:
                        self._clear()
                        print(self.error, self.dash, "\n\n")
                        print("This admission number already has a record with name: " ,aq1[1])
                        print("Please use a different admission number to make a new entry")
                        self._pause()
                        self.addstudent()
                    else:
                        aqname = input("Enter Name: ",).strip()
                        if self.checkmodstu(aqname) == 1:
                            self.modifystudent()
                        elif self.checkmodstu(aqname) == 2:
                            print("Input can't be empty!!!")
                            self._pause()
                            self.addstudent()
                        else:
                            aqclss = input("Enter Class: ").strip()
                            if self.checkmodstu(aqclss) == 1:
                                self.modifystudent()
                            elif self.checkmodstu(aqclss) == 2:
                                print("Input can't be empty!!!")
                                self._pause()
                                self.addstudent()
                            else:
                                aqsex = input("Enter Sex: ").strip()
                                if self.checkmodstu(aqsex) == 1:
                                    self.modifystudent()
                                elif self.checkmodstu(aqsex) == 2:
                                    print("Input can't be empty!!!")
                                    self._pause()
                                    self.addstudent()
                                else:
                                    aqcontact = input("Enter Contact: ").strip()
                                    if self.checkmodstu(aqcontact) == 1:
                                        self.modifystudent()
                                    elif self.checkmodstu(aqcontact) == 2:
                                        print("Input can't be empty!!!")
                                        self._pause()
                                        self.addstudent()
                                    else:
                                        while True: 
                                            print(self.dash, "\nConfirm new entry? y/n")
                                            aqpreferred1 = ["y", "Y", "n", "N"]
                                            try : 
                                                aqinp1 = self._input(aqpreferred1)
                                            except Exception as err: 
                                                self._clear()
                                                print(self.error)
                                                print("")
                                                print(err)
                                                self._pause()
                                                continue
                                            else : 
                                                if aqinp1 == "y" or "Y":
                                                    self._clear()
                                                    print(self.addstudentlogo)
                                                    print("\n",self.dash, "\n\n")
                                                    with open('data/student.csv','r') as aqinp2:
                                                        aqread2 = csv.reader(aqinp2)
                                                        aqcontent = {}
                                                        aqentcount = 0
                                                        for aq2 in aqread2:
                                                            if aq2:
                                                                aqentcount += 1
                                                                aqcontent[aqentcount] = aq2
                                                            aqcontent[aqentcount+1] = [aqadmno,aqname,aqclss,aqsex,aqcontact]

                                                    with open('data/student.csv','w') as aqoutp3:
                                                        aqwriter3 = csv.writer(aqoutp3)
                                                        for aq3 in range(1,aqentcount+2):
                                                            aqwriter3.writerow(aqcontent[aq3])
                                                        print('New student succesfully added!')

                                                    self._pause()
                                                    self.modifystudent()
                                                else:
                                                    self.addstudent()#issue books
    def removestudent(self):
        while True : 
                
            self._clear()
            print(self.removestudentlogo,"\nEnter ! (exclamation mark) to go back", self.dash, "\n\n")
            print("Enter the admission number of the student to remove", end = '' )
            
            try : 
                asadmno = self.get_int_input()
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if asadmno == "!":
                    self.editdetails()
                else:
                    asadmno = str(asadmno)
                    break
        with open("data/student.csv", "r") as asfile1: 
            asread1 = csv.reader(asfile1)
            aslist1 = []
                
            ashead1 = next(asread1)
            for as1 in asread1: 
                if as1:
                    aslist1.append(as1[0])

        if asadmno not in aslist1: 
            self._clear()
            print(self.error)
            print("")
            print(f"No student found with the admission number :- {asadmno}")
            self._pause()
            self.removestudent()

        else:
            with open("data/student.csv", "r") as asfile2: 
                asread2 = csv.reader(asfile2)
                ashead2 = next(asread2)
                for as2 in asread2 : 
                    if as2:
                        if as2[0] == asadmno: 
                            asdata1 = as2
            print("\n")
            for name, value in zip(ashead2, asdata1): 
                name = "%10s"%name 
                
                print(f"{name} : {value}")
            
            while True: 
                print(self.dash, "\nConfirm removing entry? y/n")
                aspreferred1 = ["y", "Y", "n", "N"]
                try : 
                    asinp1 = self._input(aspreferred1)
                except Exception as err: 
                    self._clear()
                    print(self.error)
                    print("")
                    print(err)
                    self._pause()
                    continue
                else : 
                    if asinp1 == "y" or "Y":
                        with open('data/student.csv', 'r') as asfile3:
                            asread3 = csv.reader(asfile3)
                            ascontent = {}
                            asentcount = 0
                            for as3 in asread3:
                                if as3 and as3[0] != asadmno:
                                    asentcount += 1
                                    ascontent[asentcount] = i
                            
                        with open('data/student.csv','w') as asoutp4:
                            aswriter4 = csv.writer(asoutp4)
                            for as4 in range(1,asentcount+1):
                                aswriter4.writerow(content[as4])
                            print('Student succesfully removed!')
                            self._pause()
                            self.modifystudent()
                    else:
                        self.removestudent()

    def editstudent(self):
        while True : 
                
            self._clear()
            print(self.editstudentlogo,"\nEnter ! (exclamation mark) to go back", self.dash, "\n\n")
            print("Enter the admission number of the student to edit.", end = '' )
            
            try : 
                abadm = self.get_int_input()
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if abadm == "!":
                    self.editdetails()
                else:
                    abadm = str(abadm)
                    break
        with open("data/student.csv", "r") as abfile1: 
            abread1 = csv.reader(abfile1)
            ablist1 = []
                
            abhead1 = next(abread1)
            for ab1 in abread1: 
                if ab1:
                    ablist1.append(ab1[0])

        if abadm not in ablist1: 
            self._clear()
            print(self.error)
            print("")
            print(f"No student found with the admission number :- {abadm}")
            self._pause()
            self.editstudent()

        else:
            with open("data/student.csv", "r") as abfile2: 
                abread2 = csv.reader(abfile2)
                abhead2 = next(abread2)
                for ab2 in abread2 : 
                    if ab2:
                        if ab2[0] == abadm: 
                            abdata = ab2
            print("\n")
            for name, value in zip(abhead2, abdata): 
                name = "%10s"%name 
                
                print(f"{name} : {value}")
            
            while True: 
                print(self.dash, "\nEdit the entry? y/n")
                abpreferred1 = ["y", "Y", "n", "N"]
                try : 
                    abinp1 = self._input(abpreferred1)
                except Exception as err: 
                    self._clear()
                    print(self.error)
                    print("")
                    print(err)
                    self._pause()
                    continue
                else : 
                    if abinp1 == "y" or "Y":
                        with open('data/student.csv', 'r') as abfile3:
                            abread3 = csv.reader(abfile3)
                            abcontent = {}
                            abentcount = 0
                            abspecial = 0
                            for ab3 in abread3:
                                if ab3:
                                    
                                    abentcount += 1
                                    abcontent[abentcount] = ab3
                                    if ab3[0] == abadm:
                                        abspecial = abentcount

                        abname = input("Enter Name: ",).strip()
                        if self.checkmodstu(abname) == 1:
                            self.modifystudent()
                        elif self.checkmodstu(abname) == 2:
                            print("Input can't be empty!!!")
                            self._pause()
                            self.addstudent()
                        else:
                            abclss = input("Enter Class: ").strip()
                            if self.checkmodstu(abclss) == 1:
                                self.modifystudent()
                            elif self.checkmodstu(abclss) == 2:
                                print("Input can't be empty!!!")
                                self._pause()
                                self.addstudent()
                            else:
                                absex = input("Enter Sex: ").strip()
                                if self.checkmodstu(absex) == 1:
                                    self.modifystudent()
                                elif self.checkmodstu(absex) == 2:
                                    print("Input can't be empty!!!")
                                    self._pause()
                                    self.addstudent()
                                else:
                                    abcontact = input("Enter Contact: ").strip()
                                    if self.checkmodstu(abcontact) == 1:
                                        self.modifystudent()
                                    elif self.checkmodstu(abcontact) == 2:
                                        print("Input can't be empty!!!")
                                        self._pause()
                                        self.addstudent()
                                    else:
                                        while True: 
                                            print(self.dash, "\nConfirm the edit? y/n")
                                            abpreferred2 = ["y", "Y", "n", "N"]
                                            try : 
                                                abinp2 = self._input(abpreferred2)
                                            except Exception as err: 
                                                self._clear()
                                                print(self.error)
                                                print("")
                                                print(err)
                                                self._pause()
                                                continue
                                            else : 
                                                if abinp2 == "y" or "Y":
                                                    with open('data/student.csv','w') as aboutp:
                                                        abwriter = csv.writer(aboutp)
                                                        for ab4 in range(1,abentcount+1):
                                                            if ab4 == abspecial:
                                                                abcontent[ab4] = [abadm, abname, abclss, absex, abcontact]
                                                                abwriter.writerow(abcontent[ab4])
                                                            else:
                                                                abwriter.writerow(abcontent[ab4])
                                                        print('Entry successfully edited!')
                                                        self._pause()
                                                        self.modifystudent()
                                                else:
                                                    self.editstudent()
                    else:
                        self.editstudent()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def modifybook(self):
        while True : 
                
            self._clear()
            print(self.modifybooklogo, self.dash, "\n\n")
            print("Enter 1 to add new book data")
            print("Enter 2 to remove existing book data")
            print("Enter 3 to EDIT existing book data")
            print("Enter 4 to go back")
            
                              
            atprefer1= ["1", "2", "3", "4"]
            try : 
                atinp1 = self._input(atprefer1)
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            else : 
                break
                            
        if atinp1 == "1": 
            self.addbook()
                
        elif atinp1 == "2": 
            self.removesbook()
        elif atinp1 == "3": 
            self.editbook() 
        else: 
            self.editdetails()

        self._pause()

    def addbook(self):

        while True : 
                
            self._clear()
            print(self.addbooklogo,"\nEnter ! (exclamation mark) to go back", self.dash, "\n\n")
            print("Enter the book ID of the new book", end = '' )
            
            try : 
                atadmno = self.get_int_input()
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if atadmno == "!":
                    self.editdetails()
                else:
                    atadmno = str(atadmno)
                    break
            
        with open('data/books.csv', 'r') as atfile1:
            atread1 = csv.reader(atfile1)
            athead1 = next(atread1)
                         
            for at1 in atread1:
                if at1:
                    if at1[0] == atadmno:
                        self._clear()
                        print(self.error, self.dash, "\n\n")
                        print("This book ID already has a record with name: " ,at1[2])
                        print("Please use a different admission number to make a new entry")
                        self._pause()
                        self.addbook()
                    else:
                        atisbn = input("Enter isbn: ",).strip()
                        if self.checkmodstu(atisbn) ==1:
                            self.modifybook()
                        elif self.checkmodstu(atisbn) ==2:
                            print("Input can't be emptyyyy!")
                            self._pause()
                            self.addbook()
                        else:
                            attitle = input("Enter Title: ").strip()
                            if self.checkmodstu(attitle) ==1:
                                self.modifybook()
                            elif self.checkmodstu(attitle) ==2:
                                print("Input can't be emptyyyy!")
                                self._pause()
                                self.addbook()
                            else:
                                atauthor = input("Enter Author: ").strip()
                                if self.checkmodstu(atauthor) ==1:
                                    self.modifybook()
                                elif self.checkmodstu(atauthor) ==2:
                                    print("Input can't be emptyyyy!")
                                    self._pause()
                                    self.addbook()
                                else:
                                    atpublisher = input("Enter Publisher: ").strip()
                                    if self.checkmodstu(atpublisher) ==1:
                                        self.modifybook()
                                    elif self.checkmodstu(atpublisher) ==2:
                                        print("Input can't be emptyyyy!")
                                        self._pause()
                                        self.addbook()
                                    else:
                                        atpubdate = input("Enter Publishing Date: ").strip()
                                        if self.checkmodstu(atpubdate) ==1:
                                            self.modifybook()
                                        elif self.checkmodstu(atpubdate) ==2:
                                            print("Input can't be emptyyyy!")
                                            self._pause()
                                            self.addbook()
                                        else:
                                            atgenre = input("Enter Genres separated by commas :").strip()
                                            if self.checkmodstu(atgenre) ==1:
                                                self.modifybook()
                                            elif self.checkmodstu(atgenre) ==2:
                                                print("Input can't be emptyyyy!")
                                                self._pause()
                                                self.addbook()
                                            else:
                                                atformatt = input("Enter Format (Hardcover/Paperback) :").strip()
                                                if self.checkmodstu(atformatt) ==1:
                                                    self.modifybook()
                                                elif self.checkmodstu(atformatt) ==2:
                                                    print("Input can't be emptyyyy!")
                                                    self._pause()
                                                    self.addbook()
                                                else:
                                                    while True: 
                                                        print(self.dash, "\nConfirm new entry? y/n")
                                                        atpreferred2 = ["y", "Y", "n", "N"]
                                                        try : 
                                                            atinp2 = self._input(atpreferred2)
                                                        except Exception as err: 
                                                            self._clear()
                                                            print(self.error)
                                                            print("")
                                                            print(err)
                                                            self._pause()
                                                            continue
                                                        else : 
                                                            if atinp2 == "y" or "Y":
                                                                self._clear()
                                                                print(self.addbooklogo)
                                                                print("\n",self.dash, "\n\n")
                                                                with open('data/books.csv','r') as atinp:
                                                                    atread2 = csv.reader(atinp)
                                                                    atcontent = {}
                                                                    atentcount = 0
                                                                    for at2 in atread2:
                                                                        if at2:
                                                                            atentcount += 1
                                                                            atcontent[atentcount] = i
                                                                        atcontent[atentcount+1] = [atstadmno,atisbn,attitle,atauthor,atpublisher,atpubdate,atgenre,atformatt]

                                                                with open('data/books.csv','w') as atoutp:
                                                                    atwriter = csv.writer(atoutp)
                                                                    for at3 in range(1,atentcount+2):
                                                                        atwriter.writerow(atcontent[at3])
                                                                    print('New book succesfully added!')

                                                                self._pause()
                                                                self.modifybook()
                                                            else:
                                                                self.addbook()#issue books
    def removebook(self):
        while True : 
                
            self._clear()
            print(self.removebooklogo,"\nEnter ! (exclamation mark) to go back", self.dash, "\n\n")
            print("Enter the book ID of the book to remove", end = '' )
            
            try : 
                avadmno = self.get_int_input()
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if avadmno == "!":
                    self.editdetails()
                else:
                    avadmno = str(avadmno)
                    break
        with open("data/books.csv", "r") as avfile1: 
            avread1 = csv.reader(avfile1)
            avlist1 = []
                
            avhead1 = next(avread1)
            for av1 in avread1: 
                if av1:
                    avlist1.append(av1[0])

        if avadmno not in avlist1: 
            self._clear()
            print(self.error)
            print("")
            print(f"No book found with the Book ID :- {avadmno}")
            self._pause()
            self.removebook()

        else:
            with open("data/books.csv", "r") as avfile2: 
                avread2 = csv.reader(avfile2)
                avhead2 = next(avread2)
                for av2 in avread2 : 
                    if av2:
                        if av2[0] == avadmno: 
                            avdata1 = av2
            print("\n")
            for name, value in zip(avhead2, avdata1): 
                name = "%10s"%name 
                
                print(f"{name} : {value}")
            
            while True: 
                print(self.dash, "\nConfirm removing entry? y/n")
                avpreferred1 = ["y", "Y", "n", "N"]
                try : 
                    avinp1 = self._input(avpreferred1)
                except Exception as err: 
                    self._clear()
                    print(self.error)
                    print("")
                    print(err)
                    self._pause()
                    continue
                else : 
                    if avinp1 == "y" or "Y":
                        with open('data/books.csv', 'r') as avfile3:
                            avread3 = csv.reader(avfile3)
                            avcontent = {}
                            aventcount = 0
                            for av3 in avread3:
                                if av3 and i[0] != avadmno:
                                    aventcount += 1
                                    avcontent[aventcount] = i
                            
                        with open('data/books.csv','w') as avoutp:
                            avwriter = csv.writer(avoutp)
                            for av4 in range(1,aventcount+1):
                                avwriter.writerow(avcontent[av4])
                            print('Books succesfully removed!')
                            self._pause()
                            self.modifybook()
                    else:
                        self.removebook()

    def editbook(self):
        while True : 
                
            self._clear()
            print(self.editbooklogo,"\nEnter ! (exclamation mark) to go back", self.dash, "\n\n")
            print("Enter the Book ID of the book to edit.", end = '' )
            
            try : 
                awadm = self.get_int_input()
            except Exception as err: 
                self._clear()
                print(self.error)
                print("")
                print(err)
                self._pause()
                continue
            
            else:
                if awadm == "!":
                    self.editdetails()
                else:
                    awadm = str(awadm)
                    break
        with open("data/books.csv", "r") as awfile1: 
            awread1 = csv.reader(awfile1)
            awlist1 = []
                
            awhead1 = next(awread1)
            for aw1 in awread1: 
                if aw1:
                    awlist1.append(aw1[0])

        if awadm not in awlist1: 
            self._clear()
            print(self.error)
            print("")
            print(f"No book found with the Book ID :- {awadm}")
            self._pause()
            self.editbook()

        else:
            with open("data/books.csv", "r") as awfile2: 
                awread2 = csv.reader(awfile2)
                abhead2 = next(abread2)
                for aw2 in awread2 : 
                    if aw2:
                        if aw2[0] == awadm: 
                            awdata = aw2
            print("\n")
            for name, value in zip(awhead2, awdata): 
                name = "%10s"%name 
                
                print(f"{name} : {value}")
            
            while True: 
                print(self.dash, "\nEdit the entry? y/n")
                awpreferred1 = ["y", "Y", "n", "N"]
                try : 
                    awinp1 = self._input(awpreferred1)
                except Exception as err: 
                    self._clear()
                    print(self.error)
                    print("")
                    print(err)
                    self._pause()
                    continue
                else : 
                    if awinp1 == "y" or "Y":
                        with open('data/books.csv', 'r') as awfile3:
                            awread3 = csv.reader(awfile3)
                            awcontent = {}
                            awentcount = 0
                            awspecial = 0
                            for aw3 in awread3:
                                if aw3:
                                    
                                    awentcount += 1
                                    awcontent[awentcount] = aw3
                                    if aw3[0] == awadm:
                                        awspecial = awentcount

                        awisbn = input("Enter isbn: ",).strip()
                        if self.checkmodstu(awisbn) ==1:
                            self.modifybook()
                        elif self.checkmodstu(awisbn) ==2:
                            print("Input can't be emptyyyy!")
                            self._pause()
                            self.modifybook()
                        else:
                            awtitle = input("Enter Title: ").strip()
                            if self.checkmodstu(awtitle) ==1:
                                self.modifybook()
                            elif self.checkmodstu(awtitle) ==2:
                                print("Input can't be emptyyyy!")
                                self._pause()
                                self.modifybook()
                            else:
                                awauthor = input("Enter Author: ").strip()
                                if self.checkmodstu(awauthor) ==1:
                                    self.modifybook()
                                elif self.checkmodstu(awauthor) ==2:
                                    print("Input can't be emptyyyy!")
                                    self._pause()
                                    self.modifybook()
                                else:
                                    awpublisher = input("Enter Publisher: ").strip()
                                    if self.checkmodstu(awpublisher) ==1:
                                        self.modifybook()
                                    elif self.checkmodstu(awpublisher) ==2:
                                        print("Input can't be emptyyyy!")
                                        self._pause()
                                        self.modifybook()
                                    else:
                                        awpubdate = input("Enter Publishing Date: ").strip()
                                        if self.checkmodstu(awpubdate) ==1:
                                            self.modifybook()
                                        elif self.checkmodstu(awpubdate) ==2:
                                            print("Input can't be emptyyyy!")
                                            self._pause()
                                            self.modifybook()
                                        else:
                                            awgenre = input("Enter Genres separated by commas :").strip()
                                            if self.checkmodstu(awgenre) ==1:
                                                self.modifybook()
                                            elif self.checkmodstu(awgenre) ==2:
                                                print("Input can't be emptyyyy!")
                                                self._pause()
                                                self.modifybook()
                                            else:
                                                awformatt = input("Enter Format (Hardcover/Paperback) :").strip()
                                                if self.checkmodstu(awformatt) ==1:
                                                    self.modifybook()
                                                elif self.checkmodstu(awformatt) ==2:
                                                    print("Input can't be emptyyyy!")
                                                    self._pause()
                                                    self.modifybook()
                                                else:
                                                    while True: 
                                                        print(self.dash, "\nConfirm the edit? y/n")
                                                        awpreferred2 = ["y", "Y", "n", "N"]
                                                        try : 
                                                            awinp2 = self._input(awpreferred2)
                                                        except Exception as err: 
                                                            self._clear()
                                                            print(self.error)
                                                            print("")
                                                            print(err)
                                                            self._pause()
                                                            continue
                                                        else : 
                                                            if awinp2 == "y" or "Y":
                                                                with open('data/books.csv','w') as awoutp:
                                                                    awwriter = csv.writer(awoutp)
                                                                    for aw4 in range(1,awentcount+1):
                                                                        if aw4 == awspecial:
                                                                            awcontent[ab4] = [awadmno, awisbn, awtitle, awauthor, awpublisher, awpubdate, awgenre, awformatt]
                                                                            awwriter.writerow(awcontent[aw4])
                                                                        else:
                                                                            awwriter.writerow(awcontent[aw4])
                                                                    print('Entry successfully edited!')
                                                                    self._pause()
                                                                    self.modifybook()
                                                            else:
                                                                self.editbook()
                    else:
                        self.editbook()

    def checkmodstu(self, a):
        if not a:
            return 2
        elif a == "!":
            return 1
        else:
            return 0
    
#Calling our instance
if __name__ == "__main__": 
    LibraryManager()
