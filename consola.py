import datetime
from exceptii.exceptions import DuplicateIDException, ValidationException,PersoananotFound,EvenimentnotFound,EvenimetAlreadyAssinged


class Conslola:
    def __init__(self,srvPersoana,srvEveniment):
        self.__srv_persoana=srvPersoana
        self.__srv_eveniment=srvEveniment

    def __print_menu(self):
        print("Comenzi disponibile pentu Persoane, Evenimet adaugati sufixul __persoana sau _eveniment dupa orice comanda:") 
        print("Comenzi : add,delete,update")
  
    def __show_lists_of_persoane(self,persoane):

        if len(persoane)==0 :
            print("Nu exsita persoane in lista")
        else :
            print("Lista de produse este :")
            for persoana in  persoane:
                print("ID :",persoana.get_id(),"-Nume :",persoana.get_nume(),"-Adresa:",persoana.get_adresa())

    def __show_lists_of_evenimente(self,evenimente):
        if len(evenimente)==0:
            print("Nu exista evenimente programate.")
        else:
            print("Evenimentele disponbiblile sunt :")
            for eveniment in evenimente:
            
                print("Id :",eveniment.get_id(),"-Data:",eveniment.get_data(),"-Timp :",eveniment.get_timp())

    def __add_persoana(self):
        id=input("Id persoana:")
        nume=input("Nume persoana:")
        adresa=input("Adresa persoana:")
        try:
            added_persoana=self.__srv_persoana.add_persoana(id,nume,adresa)
            print("Persoana:",added_persoana,"a fost adaugata cu succes")
        except ValidationException as ve:
            print(str(ve))
        except DuplicateIDException:
            print("Exista deja o perosana cu id-ul acesta")

    def __add_eveniment(self):
        id=input("ID:")
        date_tranzactie = input('Adugati data evenimetului (YYYY-MM-DD format) :')
        year, month, day = map(int, date_tranzactie.split('-'))
        data = datetime.date(year, month, day)
        timp_eveniment=input("Adaugati timpul desfasurarii evenimetului:")
        hour,minutes=map(int,timp_eveniment.split(":"))
        timp=datetime.time(hour,minutes)
        try:
            added_eveniment=self.__srv_eveniment.add_eveniment(id,data,timp)
            print("Evenimentul:",added_eveniment,"a fost adaugat cu succes")
        except ValidationException as ve :
            print(str(ve))
        except DuplicateIDException:
            print("Exista deja un eveniment cu acest id")


    def __delete_persoana(self):
        id=input("Id persoana")

        try:
            deleted_persoana=self.__srv_persoana.delete_by_id(id)
            print("Persoana:",deleted_persoana,"a fost stearsa cu succes")
        except PersoananotFound as ve:
            print(str(ve))

    def __delete_eveniment(self):
        id=input("ID eveniment")
        try: 
            deleted_eveniment=self.__srv_eveniment.delete_by_id(id)
            print("Evenimentul:",deleted_eveniment,"a fost sters cu succes")
        except EvenimentnotFound as ve:
            print(str(ve))

    def __update_evenimet(self):
        id=input("ID:")
        date_tranzactie = input('Adugati data evenimetului nou (YYYY-MM-DD format) :')
        year, month, day = map(int, date_tranzactie.split('-'))
        data = datetime.date(year, month, day)
        timp_eveniment=input("Adaugati timpul evenimetului nou:")
        hour,minutes=map(int,timp_eveniment.split(":"))
        timp=datetime.time(hour,minutes)
        try:
            updated_eveniment=self.__srv_eveniment.update_eveniment(id,data,timp)
            print("Evenimetul",updated_eveniment,"a fost actualizat cu succes")
        except ValidationException as ve:
            print(str(ve))
        except EvenimentnotFound as v:
            print(str(v))

    def __update_persoana(self):
        id=input("Id persoana :")
        nume=input("Nume persoana noua:")
        adresa=input("Adresa persoana noua:")
        try:
            updated_persoana=self.__srv_persoana.update_persoana(id,nume,adresa)
            print("Persoana ",updated_persoana,"a fost actualizata cu succes")
        except ValidationException as ve:
            print(str(ve))
        except PersoananotFound as e:
            print(str(e))

    def show_ui(self):
        while True:
            self.__print_menu()
            cmd=input("Comanda este:")
            cmd=cmd.lower().strip()
            if cmd=="add_persoana":
                self.__add_persoana()
            elif cmd=="delete_persoana":
                self.__delete_persoana()
            elif cmd=="update_persoana":
                self.__update_persoana()
            elif cmd=="add_eveniment":
                self.__add_eveniment()
            elif cmd=="delete_eveniment":
                self.__delete_eveniment()
            elif cmd=="update_eveniment":
                self.__update_evenimet()
            elif cmd=="get_all_persoane":
                self.__show_lists_of_persoane(self.__srv_persoana.get_persoana())
            elif cmd=="get_all_evenimente":
                self.__show_lists_of_evenimente(self.__srv_eveniment.get_eveniment())
            elif cmd=="exit":
                return
            else:
                print("Comanda invalida.")                                   



