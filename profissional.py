import json
from abc import ABC, abstractmethod

class CRUD(ABC):
    objetos = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0
        for i in cls.objetos:
            if i.get_id() > id:
                id = i.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.Salvar() # precisa ser CLS, pois vai acionar a classe específica seja Profissional ou outra que estiver executando
    
    @classmethod
    def Listar(cls):
        for i in cls.objetos:
            print(i)
        return cls.objetos
    
    @classmethod
    def Listar_id(cls, obj):
        for i in cls.objetos:
            if i.get_id() == obj.get_id():
                return i
    
    @classmethod
    def Excluir(cls, obj):
        objeto = CRUD.Listar_id(obj)
        cls.objetos.remove(objeto)
        cls.Salvar()

    @classmethod
    @abstractmethod
    def Atualizar(cls):
        pass

    @classmethod
    @abstractmethod
    def Abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def Salvar(cls):
        pass

        
class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.__id = id
        self.__nome = nome
        self.__especialidade = especialidade
        self.__conselho = conselho
        self.__email = email
        self.__senha = senha
    
    #get

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_especialidade(self):
        return self.__especialidade
    
    def get_conselho(self):
        return self.__conselho
    
    def get_email(self):
        return self.__email
    
    def get_senha(self):
        return self.__senha
    
    #sets

    def set_id(self, id):
        if id == '':
            raise ValueError("O id está vazio")
        else:
            self.__id = id
    
    def set_nome(self, nome):
        if nome == '':
            raise ValueError("O nome está vazio")
        else:
            self.__nome = nome
    
    def set_especialidade(self, especialidade):
        if especialidade == '':
            raise ValueError("A especialidade está vazia")
        else:
            self.__especialidade = especialidade
    
    def set_conselho(self, conselho):
        if conselho == '':
            raise ValueError("O conselho está vazio")
        else:
            self.__conselho = conselho
    
    def set_email(self, email):
        if email == '':
            raise ValueError("O email está vazio")
        else:
            self.__email = email
    
    def set_senha(self, senha):
        if senha == '':
            raise ValueError("A senha está vazia")
        else:
            self.__senha = senha
    
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__email} - {self.__especialidade} - {self.__conselho} - {self.__senha} '


class Profissionais(CRUD):
    @classmethod
    def Atualizar(cls, obj):
        p = Profissionais.Listar_id(obj)
        p.set_id(obj.get_id())
        p.set_nome(obj.get_nome())
        p.set_especialidade(obj.get_especialidade())
        p.set_email(obj.get_email())
        p.set_conselho(obj.get_conselho())
        p.set_senha(obj.get_senha())
        cls.Salvar()
    
    @classmethod
    def Salvar(cls):
        with open("profissionais.json", mode='w') as file:
            json.dump([vars(obj) for obj in cls.objetos], file, default=vars, indent=1)
    
    @classmethod
    def Abrir(cls):
        try:
            with open("profisisonais.json", mode="r") as file:
                texto = json.load(file)
                for i in texto:
                    p = Profissional(i["_Profisisonal__id"],i["_Profisisonal__nome"],i["_Profisisonal__especialidade"],i["_Profisisonal__conselho"],i["_Profisisonal__email"],i["_Profisisonal__senha"])
                    cls.objetos.append(p)
        except FileNotFoundError:
            pass


joao = Profissional(0,"João",2,3,4,5)
pedro = Profissional(0,"Pedro",2,3,4,5)
Profissionais.Inserir(joao)
Profissionais.Inserir(pedro)
pedroV2 = Profissional(2,"PedroV2",2,3,4,5)
Profissionais.Atualizar(pedroV2)
Profissionais.Excluir(pedroV2)
Profissionais.Listar()

# falta apenas conseguir captura os dados do json, pois ele sempre reinicia


   