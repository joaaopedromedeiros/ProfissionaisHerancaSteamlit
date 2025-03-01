import json

class CRUD:
    __objetos = []

    @classmethod
    def Inserir(cls, obj):
        id = 0
        for i in cls.__objetos:
            if i.get_id() > id:
                id = i.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        obj.Salvar()
    
    @classmethod
    def Listar(cls):
        CRUD.Abrir()
        return cls.__objetos
    
    @classmethod
    def Listar_id(cls, obj):
        for i in cls.__objetos:
            if i.get_id() == obj.get_id():
                return i
    
    @classmethod
    def Excluir(cls, obj):
        CRUD.Abrir()
        objeto = CRUD.Listar_id(obj)
        cls.__objetos.remove(objeto)
        obj.Salvar() #mudança
    
    @classmethod
    def Atualizar(cls):
        pass

    @classmethod
    def Abrir(cls):
        pass

    @classmethod
    def Salvar(cls):
        pass

    @classmethod #pode isso? adiconado
    def get_objetos(self):
        return self.__objetos

class Profissional(CRUD):
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
    
    @classmethod
    def Atualizar(cls,obj):
        p = Profissional.Listar_id(obj)
        p.set_id(obj.get_id())
        p.set_nome(obj.get_nome())
        p.set_email(obj.get_email())
        p.set_especialidade(obj.get_especialidade())
        p.set_conselho(obj.get_conselho())
        p.set_senha(obj.get_senha())
        obj.Salvar() #mudança

    @classmethod
    def Abrir(cls):
        try:
            with open("profissionais.json", mode="r") as file:
                texto = json.load(file)
                for obj in texto:
                    p = Profissional(obj["_Profissional__id"],obj["_Profissional__nome"],obj["_Profissional__especialidade"],obj["_Profissional__conselho"],obj["_Profissional__email"],obj["_Profissional__senha"],)
                    lista = cls.get_objetos()
                    lista.append(p)
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        with open("profissionais.json", mode="w") as file:
            json.dump([vars(obj) for obj in cls.get_objetos()], file, default=vars, indent=1) # n sei 


joao = Profissional(0,"João Pedro","Médico","CRM","joão@gmail.com","Teste#1234")
pedro = Profissional(0,1,2,3,4,5)




Profissional.Inserir(joao)
Profissional.Inserir(pedro)