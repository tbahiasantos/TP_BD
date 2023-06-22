import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('sistema_de_matriculas.db')
cursor = conn.cursor()

# Função para inserir dados em uma tabela
def inserir_dados(tabela, dados):
    placeholders = ', '.join(['?' for _ in dados])
    query = f'INSERT INTO {tabela} VALUES ({placeholders})'
    cursor.execute(query, dados)
    conn.commit()

# Populando a tabela "aluno"
alunos = [
    (1, 'João', 'joao@gmail.com', 'Engenharia', '1990-01-01', 'Rua A, 123'),
    (2, 'Maria', 'maria@gmail.com', 'Medicina', '1992-05-10', 'Rua B, 456'),
    # Adicione mais alunos aqui
]
for aluno in alunos:
    inserir_dados('aluno', aluno)

# Populando a tabela "professor"
professores = [
    (1, 'Carlos', 'carlos@gmail.com', 'Engenharia', '1975-03-15', 'Rua C, 789'),
    (2, 'Ana', 'ana@gmail.com', 'Medicina', '1980-08-20', 'Rua D, 987'),
    # Adicione mais professores aqui
]
for professor in professores:
    inserir_dados('professor', professor)

# Populando a tabela "disciplina"
disciplinas = [
    (1, 'Matemática', 60),
    (2, 'Biologia', 45),
    # Adicione mais disciplinas aqui
]
for disciplina in disciplinas:
    inserir_dados('disciplina', disciplina)

# Populando a tabela "turma"
turmas = [
    (1, 'Sala 101', '8:00-10:00'),
    (2, 'Sala 201', '14:00-16:00'),
    # Adicione mais turmas aqui
]
for turma in turmas:
    inserir_dados('turma', turma)

# Populando a tabela "leciona"
lecionas = [
    (1, 1, 1),
    (2, 2, 2),
    # Adicione mais relações de leciona aqui
]
for leciona in lecionas:
    inserir_dados('leciona', leciona)

# Populando a tabela "matricula"
matriculas = [
    (1, 1),
    (2, 2),
    # Adicione mais matrículas aqui
]
for matricula in matriculas:
    inserir_dados('matricula', matricula)

# Fechando a conexão com o banco de dados
conn.close()
