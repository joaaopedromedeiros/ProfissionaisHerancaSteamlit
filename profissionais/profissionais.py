from abc import ABC, abstractmethod
import json
import streamlit as st

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.__id = id
        self.__nome = nome
        self.__especialidade = especialidade
        self.__conselho = conselho
        self.__email = email
        self.__senha = senha
    
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
        self.__id = id
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade
    
    def set_conselho(self, conselho):
        self.__conselho = conselho
    
    def set_email(self, email):
        self.__email = email
    
    def set_senha(self, senha):
        self.__senha = senha
    
    def __str__(self):
        return f' {self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho} - {self.__email} - {self.__senha}'


class CRUD(ABC):

    objetos = []
    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        id = 0
        for i in cls.objetos:
            if i.get_id() > id:
                id = i.get_id()
        obj.set_id( id + 1)
        cls.objetos.append(obj)
        cls.Salvar()
    
    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.objetos
    
    @classmethod
    def Listar_Id(cls, id):
        cls.Abrir()
        for i in cls.objetos:
            if i.get_id() == id:
                return i
    
    @classmethod
    def Excluir(cls, obj):
        objeto = cls.Listar_Id(obj.get_id())
        cls.objetos.remove(objeto)
        cls.Salvar()
    
    @classmethod
    @abstractmethod
    def Atualizar(cls, obj):
        pass

    @classmethod
    @abstractmethod
    def Abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def Salvar(cls):
        pass

class Profissionais(CRUD):

    @classmethod
    def Atualizar(cls, obj):
        p = cls.Listar_Id(obj.get_id())
        p.set_id(obj.get_id())
        p.set_nome(obj.get_nome())
        p.set_especialidade(obj.get_especialidade())
        p.set_conselho(obj.get_conselho())
        p.set_email(obj.get_email())
        p.set_senha(obj.get_senha())
        cls.Salvar()
        

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
            with open("Profissionais.json", mode="r") as file:
                texto = json.load(file)
                for p in texto:
                    profissional = Profissional(p["_Profissional__id"],p["_Profissional__nome"],p["_Profissional__especialidade"],p["_Profissional__conselho"],p["_Profissional__email"],p["_Profissional__senha"])
                    cls.objetos.append(profissional)
        except FileNotFoundError:
            pass
    
    @classmethod
    def Salvar(cls):
        with open("Profissionais.json", mode="w") as file:
            json.dump(cls.objetos, file, default=vars, indent=1)


class Views:
    @classmethod
    def Profissionais_Listar(cls):
        return Profissionais.Listar()
    
    @classmethod
    def Profissionais_Inserir(cls, nome, especialidade, conselho, email, senha):
        p = Profissional(0,nome,especialidade,conselho,email,senha)
        Profissionais.Inserir(p)
        return
    
    @classmethod
    def Profissionais_Atualizar(cls,id, nome, especialidade, conselho, email, senha):
        p = Profissional(id, nome, especialidade, conselho, email, senha)
        Profissionais.Atualizar(p)
        return
    
    @classmethod
    def Profissionais_Excluir(cls, id):
        for i in Profissionais.Listar():
            if i.get_id() == id:
                Profissionais.Excluir(i)
        return


class ManterProfissionais:

    @classmethod
    def Main(cls):
        st.header("Gerenciador de profissionais")
        tab1, tab2, tab3 = st.tabs(["Inserir","Atualizar","Excluir"])
        with tab1: ManterProfissionais.Inserir()
        with tab2: ManterProfissionais.Atualizar()
        with tab3: ManterProfissionais.Excluir()
    
    @classmethod
    def Inserir(cls):
        nome = st.text_input("Nome do profisisonal ")
        especialidade = st.text_input("Especialidade ")
        conselho = st.text_input("Conselho")
        email = st.text_input("Email")
        senha = st.text_input("Senha")
        if st.button("Cadastrar"):
            Views.Profissionais_Inserir(nome, especialidade, conselho, email, senha)
            st.success("Profissional cadastrado")
            st.rerun()

    @classmethod
    def Atualizar(cls):
        lista = st.selectbox("Profisisonais para atualizar", Views.Profissionais_Listar())
        nome = st.text_input("Novo Nome do profisisonal ")
        especialidade = st.text_input("Novo Especialidade ")
        conselho = st.text_input("Novo Conselho")
        email = st.text_input("Novo Email")
        senha = st.text_input("Novo Senha")
        if st.button("Atualizar profissional"):
            Views.Profissionais_Atualizar(lista.get_id(),nome, especialidade, conselho, email, senha)
            st.success("Profissional atualizado")
            st.rerun()
        


    @classmethod
    def Excluir(cls):
        lista2 = st.selectbox("Profissionais para excluir", Views.Profissionais_Listar())
        if st.button("Excluir"):
            Views.Profissionais_Excluir(lista2.get_id())
            st.success("Profissionnal excluido")
            st.rerun()

ManterProfissionais.Main()





    


            