import json
import streamlit as st
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
        cls.Salvar()
    
    @classmethod
    def listar(cls):
        cls.Abrir()
        return cls.objetos
    
    @classmethod
    def Listar_id(cls, id):
        cls.Abrir()
        for i in cls.objetos:
            if i.get_id() == id:
                return i
    
    @classmethod
    def Excluir(cls, obj):
        objeto = cls.Listar_id(obj.get_id())
        if objeto != None:
            cls.objetos.remove(objeto)
            cls.Salvar()
        else:
            raise ValueError("Item não encontrado")
    
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
    
class Perfil:
    def __init__(self, id, nome, descricao, beneficios):
        if id == '':
            raise ValueError("Id não informado")
        else:
            self.__id = id
        
        if nome == '':
            raise ValueError("Nome não informado")
        else:
            self.__nome = nome
        
        if descricao == '':
            raise ValueError("Descrição vazia")
        else:
            self.__descricao = descricao
        
        if beneficios == '':
            raise ValueError("Benefícios não informados")
        else:
            self.__beneficios = beneficios
    #gets
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def get_beneficios(self):
        return self.__beneficios
    #sets
    def set_id(self, id):
        if id == '':
            raise ValueError("Id não informado")
        else:
            self.__id = id
    def set_nome(self, nome):
        if nome == '':
            raise ValueError("Nome não informado")
        else:
            self.__nome = nome
    def set_descricao(self, descricao):
        if descricao == '':
            raise ValueError("Descrição vazia")
        else:
            self.__descricao = descricao
    def set_beneficios(self, beneficios):
        if beneficios == '':
            raise ValueError("Benneficios não informados")
        else:
            self.__beneficios = beneficios
    
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__descricao} - {self.__beneficios}'
    

class Perfis(CRUD):
    
    @classmethod
    def Atualizar(cls, obj):
        p = cls.Listar_id(obj.get_id())
        p.set_id(obj.get_id())
        p.set_nome(obj.get_nome())
        p.set_descricao(obj.get_descricao())
        p.set_beneficios(obj.get_beneficios())
        cls.Salvar()
    
    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
            with open("perfis.json", mode="r") as file:
                texto = json.load(file)
                for i in texto:
                    p = Perfil(i["_Perfil__id"],i["_Perfil__nome"],i["_Perfil__descricao"],i["_Perfil__beneficios"])
                    cls.objetos.append(p)
        except FileNotFoundError:
            pass
    
    @classmethod
    def Salvar(cls):
        with open("perfis.json", mode="w") as file:
            json.dump(cls.objetos, file, default=vars, indent=1)



class Views:

    @classmethod
    def Perfis_Listar(cls):
        return Perfis.listar()
    
    @classmethod
    def Perfis_Inserir(cls, nome, descricao, beneficios):
        p = Perfil(0,nome,descricao,beneficios)
        Perfis.Inserir(p)
        return
    
    @classmethod
    def perfis_Excluir(cls, id):
        objetoo = Perfis.Listar_id(id)
        Perfis.Excluir(objetoo)
        return 
    
    @classmethod
    def Perfis_Atualizar(cls, id, nome, descricao, beneficios):
        p = Perfil(id, nome, descricao, beneficios)
        Perfis.Atualizar(p)
        return 







class ManterPerfil:
    
    @classmethod
    def Main(cls):
        st.sidebar._selectbox("Menu",[1,2,3,4])
        tab1, tab2, tab3, tab4 = st.tabs(["Listar","Inserir","Excluir","Atualizar"])
        with tab1: ManterPerfil.Listar()
        with tab2: ManterPerfil.Inserir()
        with tab3: ManterPerfil.Excluir()
        with tab4: ManterPerfil.Atualizar()
    
    @classmethod
    def Listar(cls):
        st.header("Listar perfis")
    
    @classmethod
    def Inserir(cls):
        st.header("Inserir perfil")
        nome = st.text_input("Nome do perfil")
        descricao = st.text_input("Nome da descrição")
        beneficios = st.text_input("Nome dos benefícios")
        if st.button("Cadastrar perfil"):
            Views.Perfis_Inserir(nome, descricao, beneficios)
            st.success("perfil cadastrado com sucesso")
            st.rerun()
    
    @classmethod
    def Atualizar(cls):
        lista = Views.Perfis_Listar()
        st.header("Atualizar perfis")
        st.selectbox("Perfis registrados no sistema",lista)
    
    @classmethod
    def Excluir(cls):
        st.header("Excluir Perfis")

ManterPerfil.Main()


        







