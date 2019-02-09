class Prepod():
     def __init__(self, name, discipline, cabinet):
         
        self.name = name
        self.discipline = discipline
        self.cabinet = cabinet
        
     def show_prepod(self):
        discription = (self.name + " Discipline is: " + self.discipline + " Cabinet is " + str(self.cabinet)).title()
        print(discription)
     def rename_prepod(self):
        x = input()
        self.name = x
        print(self.name)

prepod1 = Prepod("YesenbayevZh", "Data structure and Agorithms, LECTION", 403)
prepod2 = Prepod("IslamgozhaevT", "Data structure and Agorithms,SEMINAR", 320)

prepod1.show_prepod()
prepod2.show_prepod()

prepod1.rename_prepod()

