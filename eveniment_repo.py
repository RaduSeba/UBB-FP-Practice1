from os import remove
from domain.entitati import Eveniment,Persoana
from exceptii.exceptions import PersoananotFound,EvenimentnotFound,DuplicateIDException,EvenimetAlreadyAssinged

class PersoanaRepoFile:
    def __init__(self,filename):
        self.__filename=filename

    def __load_from_file(self):
        f=open(self.__filename,"r") 
        persons=[]
        lines=f.readlines()
        for line in lines :
            persoana_id,persoana_nume,persoana_adresa=[token.strip() for token in line.split(";") ]
            persoana=Persoana(persoana_id,persoana_nume,persoana_adresa)
            persons.append(persoana)

        f.close()
        return persons


    def __save_to_file(self,persoana_list):
        with open(self.__filename,"w") as f:
            for persoana in persoana_list:
                persoana_string=str(persoana.get_id())+";" + str(persoana.get_nume())+";"+str(persoana.get_adresa()) +"\n"
                f.write(persoana_string)

    def find(self,id):
        all_persoane=self.__load_from_file()
        for persoana in all_persoane:
            if persoana.get_id()==id:
                return persoana
        return None


    def __find_by_index(self,all_peroane,id):
        index=-1
        for i in range(len(all_peroane)):
            if all_peroane[i].get_id()==id:
                index=i
        return index        


    def store(self,persoana):
        all_persoane=self.__load_from_file()
        if persoana in all_persoane:
            raise DuplicateIDException()
        all_persoane.append(persoana)
        self.__save_to_file(all_persoane)

    

    def delete(self,id):
        all_persons=self.__load_from_file()
        p=self.find(id)
        if p is None:
            raise PersoananotFound()

    
        deleted=self.find(id)
        all_persons.remove(deleted)
        self.__save_to_file(all_persons)
        return deleted       

    def update(self,new_persoana,id):
        all_persoane=self.__load_from_file()
        index=self.__find_by_index(all_persoane,id)
        all_persoane[index]=new_persoana
        self.__save_to_file(all_persoane)
        return new_persoana

    def get_all(self):
        return self.__load_from_file()

    def size(self):
        return len(self.__load_from_file())     


class EvenimentRepoFile:
    def __init__(self,filename):
        self.__filename=filename

    def __load_from_file(self):
        f=open(self.__filename,"r") 
        evenimente=[]
        lines=f.readlines()
        for line in lines :
            eveniment_id,eveniment_data,eveniment_timp=[token.strip() for token in line.split(";") ]
            eveniment=Eveniment(eveniment_id,eveniment_data,eveniment_timp)
            evenimente.append(eveniment)
        f.close()
        return evenimente  



    def __save_to_file(self,evenimente_list):
        with open(self.__filename,"w") as f:
            for eveniment in evenimente_list:
                eveniment_string=str(eveniment.get_id()) +";" + str(eveniment.get_data())+";"+str(eveniment.get_timp())+"\n"

                f.write(eveniment_string)

    def find(self,id):
        all_persoane=self.__load_from_file()
        for persoana in all_persoane:
            if persoana.getid()==id:
                return persoana
        return None

    def store(self,eveniment):
        all_evenimente=self.__load_from_file()
        if eveniment in all_evenimente:
            raise DuplicateIDException()
        all_evenimente.append(eveniment)
        self.__save_to_file(all_evenimente)


    def delete(self,id):
        all_evenimente=self.__load_from_file()
        e=self.find(id)
        if e is None:
            raise PersoananotFound()

    
        deleted=all_evenimente[id]
        del all_evenimente[id]
        self.__save_to_file(all_evenimente)
        return deleted       


    def update(self,new_eveniment,id):
        all_evenimente=self.__load_from_file()
        p=self.find(id)
        all_evenimente[id]=new_eveniment
        self.__save_to_file(all_evenimente)
        return new_eveniment       

    def get_all(self):
        return self.__load_from_file()

    def size(self):
        return len(self.__load_from_file())     
