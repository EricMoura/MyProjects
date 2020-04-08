from Banco import Banco

class Usuarios(object):

    def __init__(self, idusuario=0, nome="", ra="", materia="", media=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.materia = materia
        self.ra = ra
        self.media = media

    def insertUser(self):
        self.banco = Banco()
        try:

            c = self.banco.conn.cursor()

            c.execute("insert into usuarios (nome, ra, materia, media) values('" + self.nome + "', '" + self.ra + "', '" + self.materia + "', '" + self.media + "' )")

            self.banco.conn.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except ValueError:
            return "Ocorreu um erro na inserção do usuário"


    def updateUser(self):
        banco = Banco()
        try:

            c = banco.conn.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "',ra = '" + self.ra + "',materia = '" + self.materia + "',media = '" + self.media + "' where idusuario = " + self.idusuario + " ")

            banco.conn.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"


    def deleteUser(self):
        banco = Banco()
        try:

            c = banco.conn.cursor()

            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")

            banco.conn.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"


    def selectUser(self, idusuario):
        banco = Banco()
        try:

            c = banco.conn.cursor()

            c.execute("select * from usuarios where idusuario =" + idusuario + " ")

            for item in c:
                self.idusuario = item[0]
                self.nome = item[1]
                self.ra = item[2]
                self.materia = item[3]
                self.media = item[4]

            c.close()

            return "Busca feita com sucesso!"

        except ValueError:
            return "Ocorreu um erro na busca do usuário"