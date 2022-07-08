from domain.entitati import Eveniment,Persoana
from exceptii.exceptions import ValidationException

class PersoanaValidator:

    def validate(self,persoana):
        errors=[]
        if persoana.get_nume()=="":
            errors.append("Numele persoanei  nu exista")

        if persoana.get_adresa()=="":
            errors.append("Adresa persoanei lipseste")

        if len(errors)>0:
            raise ValidationException(errors)

class EvenimentValidator:

    def validate(self,eveniment):
        errors=[]
        if eveniment.get_data()=="":
            errors.append("Data trebuie specificata.")

        if eveniment.get_timp()=="":
            errors.append("Timpul trebuie specificat.")  

        if len(errors)>0:
            raise ValidationException(errors)


