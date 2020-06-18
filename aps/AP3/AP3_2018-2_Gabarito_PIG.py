#coding:utf8
#

class Turma(object):
	"""Representa uma turma de uma dada matéria."""

	def __init__(self, materia):
		"""Inicia uma turma, onde matéria é uma string."""

		self.materia = materia
		self.alunos = []

	def adiciona(self, aluno):
		"""(2.0 pontos) Acrescenta o aluno (objeto da classe Aluno)
		à turma."""

		self.alunos.append(aluno)

	def remove (self, nome):
		"""(3 pontos) Remove um aluno da turma dado seu nome. Caso 
		esse aluno não exista, ignore-o. Caso existam mais de um com o 
		mesmo nome, remove o último que foi adicionado esse nome."""

		n = -1
		for i,a in enumerate(self.alunos):
			if a.nome == nome: n = i
		if n != -1: del self.alunos[n]

	def media (self):
		"""(2.0 pontos) Retorna a média geral da turma, isto é, a média entre as
		médias dos alunos matriculados."""

		return sum([a.media() for a in self.alunos])*1.0/len(self.alunos)

	def aprovacao (self):
		"""(2.0 pontos) Retorna a percentagem de alunos aprovados em 
		relação ao total de alunos da turma."""

		return sum([1 for a in self.alunos if a.media()>=5])*100.0/len(self.alunos)
		


class Aluno(object):
	"""Representa um aluno e seu desempenho numa dada matéria."""

	def __init__(self, nome, p1, p2, pf=0):
		"""Inicializa um aluno com seu nome, e as notas das 3 provas
		sendo que a pf (prova final) só considerada se a média da
		p1 e a p2 é menor que 5."""

		self.nome, self.p1, self.p2, self.pf = nome,p1,p2,pf

	def media(self):
		"""(1.0 ponto) Retorna a média de um aluno na matéria que é:
		(1) a média entre a p1 e a p2 ou, 
		(2) se essa média for menor que 5, então 
		a média é computada entre a pf e a maior nota entre p1 e p2."""

		m = (self.p1+self.p2)*0.5
		if m<5: return (max(self.p1,self.p2)+self.pf)*0.5
		return m

t1 = Turma("AlgProg")
# uma lista de objetos Aluno
a = [Aluno("Joao",2,5,5), Aluno("Pedro",5,6), Aluno("Marta",2,9,8),
     Aluno("Joao",0,3,10), Aluno("Claudia",2,5,3)]
for x in a: 
    print (x.media(), end=" ")
    t1.adiciona(x)
t1.remove("Claudio")
t1.remove("Joao")
print ()
print (t1.media())
print (t1.aprovacao())
