class Persoana:

    def __init__(self,id,nume,adresa):
        self.__id=id
        self.__nume=nume
        self.__adresa=adresa

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def set_id(self,value):
        self.__id=value

    def set_nume(self,value):
        self.__nume=value

    def set_adresa(self,value):
        self.__adresa=value

    def __eq__(self, other):
        
        if self.__id==other.get_id():
            return True
        return False  
    
    def __str__(self):
        return "ID :" + str(self.__id) + "Nume: "+ str(self.__nume) + "Adresa :"+ str(self.__adresa)

class Eveniment:

    def __init__(self,id,data,timp):
        self.__id=id
        self.__data=data
        self.__timp=timp

    def get_id(self):
        return self.__id

    def  get_data(self):
        return self.__data

    def get_timp(self):
        return self.__timp

    def set_data(self,value):
        self.__data=value

    def set_id(self,value):
        self.__id=value

    def set_timp(self,value):
        self.__timp=value

    def __eq__(self,other):
        if self.__id==other.get_id():
            return True
        return False

    def __str__(self):
        return "ID:"+ str(self.__id) + "Data :" +str(self.__data) +"Timp :"+ str(self.__timp)   