class EvenimentException(Exception):
    pass

class ValidationException(EvenimentException):
    def __init__(self,msg) -> None:
        self.__er_msg=msg

    def getMessage(self):
        return self.__er_msg

    def __str__(self) :
        return "VAlidation Exception"+ str(self.__er_msg)

class RepositoryException(EvenimentException):
    def __init__(self,msg) -> None:
        self.__er_msg=msg

    def getMessage(self):
        return self.__er_msg

    def __str__(self) :
        return "Repositiry exception :"+ str(self.__er_msg)

class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Id duplicat")

class EvenimetAlreadyAssinged(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Eveniment deja existent")

class EvenimentnotFound(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Evenimentul nu exista")

class PersoananotFound(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self,"Persoana  nu exista")

        