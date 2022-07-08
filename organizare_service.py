from domain.entitati import Eveniment,Persoana
from domain.validators import PersoanaValidator,EvenimentValidator
from exceptii.exceptions import ValidationException
from repository.eveniment_repo import PersoanaRepoFile,EvenimentRepoFile


class PersoanaService:
    def __init__(self,repo,validator):
        self.__repo=repo
        self.__validator=validator

    def add_persoana(self,id,nume,adresa):
        persoana=Persoana(id,nume,adresa)
        self.__validator.validate(persoana)
        self.__repo.store(persoana)

    def get_persoana(self):
      return self.__repo.get_all()

    def delete_by_id(self,id):
        return self.__repo.delete(id)

    def update_persoana(self,id,nume,adresa):
        persoana=Persoana(id,nume,adresa)
        self.__validator.validate(persoana)
        return self.__repo.update(persoana,id)
                

class EvenimentService:
    def __init__(self,repo,validator):
        self.__repo=repo
        self.__validator=validator

    def add_eveniment(self,id,data,timp):
        eveniment=Eveniment(id,data,timp)
        self.__validator.validate(eveniment)
        self.__repo.store(eveniment)

    def get_eveniment(self):
      return self.__repo.get_all()

    def delete_by_id(self):
        return self.__repo.delete(id)

    def update_eveniment(self,id,data,timp):
        eveniment=Eveniment(id,data,timp)
        self.__validator.validate(eveniment)
        return self.__repo.update(eveniment,id)