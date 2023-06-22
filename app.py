from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Aluno ----------------------------------------------------------------------------------------------------------------
@app.route('/')
def index():
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Consultando os alunos do banco de dados
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    return render_template('index.html', alunos=alunos)

@app.route('/inserir', methods=['POST'])
def inserir():
    # Recuperando os dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    curso = request.form['curso']
    data_nascimento = request.form['data_nascimento']
    endereco = request.form['endereco']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Inserindo um novo aluno na tabela
    cursor.execute("INSERT INTO aluno (nome, email, curso, data_nascimento, endereco) VALUES (?, ?, ?, ?, ?)",
                   (nome, email, curso, data_nascimento, endereco))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/')

@app.route('/remover/<int:aluno_id>')
def remover(aluno_id):
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Removendo o aluno da tabela
    cursor.execute("DELETE FROM aluno WHERE id=?", (aluno_id,))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/')

@app.route('/atualizar/<int:aluno_id>', methods=['POST'])
def atualizar(aluno_id):
    # Recuperando os dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    curso = request.form['curso']
    data_nascimento = request.form['data_nascimento']
    endereco = request.form['endereco']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Atualizando os dados do aluno na tabela
    cursor.execute("UPDATE aluno SET nome=?, email=?, curso=?, data_nascimento=?, endereco=? WHERE id=?",
                   (nome, email, curso, data_nascimento, endereco, aluno_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/')
# ----------------------------------------------------------------------------------------------------------------------

# Professor ------------------------------------------------------------------------------------------------------------
@app.route('/professores')
def listar_professores():
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Consultando os professores do banco de dados
    cursor.execute("SELECT * FROM professor")
    professores = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    return render_template('professores.html', professores=professores)
@app.route('/inserir_professor', methods=['POST'])
def inserir_professor():
    # Recuperando os dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    curso = request.form['curso']
    data_nascimento = request.form['data_nascimento']
    endereco = request.form['endereco']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Inserindo um novo professor na tabela
    cursor.execute("INSERT INTO professor (nome, email, curso, data_nascimento, endereco) VALUES (?, ?, ?, ?, ?)",
                   (nome, email, curso, data_nascimento, endereco))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página de professores
    return redirect('/professores')

@app.route('/remover_professor/<int:professor_id>')
def remover_professor(professor_id):
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Removendo o professor da tabela
    cursor.execute("DELETE FROM professor WHERE id=?", (professor_id,))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página de professores
    return redirect('/professores')

@app.route('/atualizar_professor/<int:professor_id>', methods=['POST'])
def atualizar_professor(professor_id):
    # Recuperando os dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    curso = request.form['curso']
    data_nascimento = request.form['data_nascimento']
    endereco = request.form['endereco']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Atualizando os dados do professor na tabela
    cursor.execute("UPDATE professor SET nome=?, email=?, curso=?, data_nascimento=?, endereco=? WHERE id=?",
                   (nome, email, curso, data_nascimento, endereco, professor_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página de professores
    return redirect('/professores')
# ----------------------------------------------------------------------------------------------------------------------

# Disciplina------------------------------------------------------------------------------------------------------------
@app.route('/disciplinas')
def disciplinas():
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Obtendo todas as disciplinas da tabela
    cursor.execute("SELECT * FROM disciplina")
    disciplinas = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    # Renderizando o template disciplina.html e passando as disciplinas como argumento
    return render_template('disciplina.html', disciplinas=disciplinas)


@app.route('/inserir_disciplina', methods=['POST'])
def inserir_disciplina():
    # Recuperando os dados do formulário
    nome = request.form['nome']
    carga_horaria = request.form['carga_horaria']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Inserindo uma nova disciplina na tabela
    cursor.execute("INSERT INTO disciplina (nome, carga_horaria) VALUES (?, ?)",
                   (nome, carga_horaria))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/disciplinas')

@app.route('/remover_disciplina/<int:disciplina_id>')
def remover_disciplina(disciplina_id):
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Removendo a disciplina da tabela
    cursor.execute("DELETE FROM disciplina WHERE id=?", (disciplina_id,))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/disciplinas')

@app.route('/atualizar_disciplina/<int:disciplina_id>', methods=['POST'])
def atualizar_disciplina(disciplina_id):
    # Recuperando os dados do formulário
    nome = request.form['nome']
    carga_horaria = request.form['carga_horaria']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Atualizando os dados da disciplina na tabela
    cursor.execute("UPDATE disciplina SET nome=?, carga_horaria=? WHERE id=?",
                   (nome, carga_horaria, disciplina_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/disciplinas')

# ----------------------------------------------------------------------------------------------------------------------

# Turmas ---------------------------------------------------------------------------------------------------------------
@app.route('/turmas')
def turmas():
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Obtendo todas as turmas da tabela
    cursor.execute("SELECT * FROM turma")
    turmas = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    # Renderizando o template turma.html e passando as turmas como argumento
    return render_template('turma.html', turmas=turmas)


@app.route('/inserir_turma', methods=['POST'])
def inserir_turma():
    # Recuperando os dados do formulário
    sala = request.form['sala']
    horario = request.form['horario']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Inserindo uma nova turma na tabela
    cursor.execute("INSERT INTO turma (sala, horario) VALUES (?, ?)",
                   (sala, horario))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/turmas')

@app.route('/remover_turma/<int:turma_id>')
def remover_turma(turma_id):
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Removendo a turma da tabela
    cursor.execute("DELETE FROM turma WHERE id=?", (turma_id,))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/turmas')

@app.route('/atualizar_turma/<int:turma_id>', methods=['POST'])
def atualizar_turma(turma_id):
    # Recuperando os dados do formulário
    sala = request.form['sala']
    horario = request.form['horario']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Atualizando os dados da turma na tabela
    cursor.execute("UPDATE turma SET sala=?, horario=? WHERE id=?",
                   (sala, horario, turma_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/turmas')

# ----------------------------------------------------------------------------------------------------------------------

# Matrícula ------------------------------------------------------------------------------------------------------------
@app.route('/matriculas')
def matriculas():
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Obtendo todas as matrículas da tabela
    cursor.execute("SELECT * FROM matricula")
    matriculas = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    # Renderizando o template matricula.html e passando as matrículas como argumento
    return render_template('matricula.html', matriculas=matriculas)


@app.route('/inserir_matricula', methods=['POST'])
def inserir_matricula():
    # Recuperando os dados do formulário
    aluno_id = request.form['aluno_id']
    disciplina_id = request.form['disciplina_id']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Inserindo uma nova matrícula na tabela
    cursor.execute("INSERT INTO matricula (aluno_id, disciplina_id) VALUES (?, ?)",
                   (aluno_id, disciplina_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/matriculas')

@app.route('/remover_matricula/<int:aluno_id>/<int:disciplina_id>')
def remover_matricula(aluno_id, disciplina_id):
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Removendo a matrícula da tabela
    cursor.execute("DELETE FROM matricula WHERE aluno_id=? AND disciplina_id=?",
                   (aluno_id, disciplina_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/matriculas')

@app.route('/atualizar_matricula/<int:aluno_id>/<int:disciplina_id>', methods=['POST'])
def atualizar_matricula(aluno_id, disciplina_id):
    # Recuperando os dados do formulário
    novo_aluno_id = request.form['aluno_id']
    nova_disciplina_id = request.form['disciplina_id']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Atualizando os dados da matrícula na tabela
    cursor.execute("UPDATE matricula SET aluno_id=?, disciplina_id=? WHERE aluno_id=? AND disciplina_id=?",
                   (novo_aluno_id, nova_disciplina_id, aluno_id, disciplina_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/matriculas')


# ----------------------------------------------------------------------------------------------------------------------

# Leciona --------------------------------------------------------------------------------------------------------------
@app.route('/leciona')
def lecionas():
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Obtendo todas as relações "leciona" da tabela
    cursor.execute("SELECT * FROM leciona")
    lecionas = cursor.fetchall()

    # Fechando a conexão com o banco de dados
    conn.close()

    # Renderizando o template leciona.html e passando as relações "leciona" como argumento
    return render_template('leciona.html', lecionas=lecionas)


@app.route('/inserir_leciona', methods=['POST'])
def inserir_leciona():
    # Recuperando os dados do formulário
    professor_id = request.form['professor_id']
    disciplina_id = request.form['disciplina_id']
    turma_id = request.form['turma_id']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Inserindo uma nova relação "leciona" na tabela
    cursor.execute("INSERT INTO leciona (professor_id, disciplina_id, turma_id) VALUES (?, ?, ?)",
                   (professor_id, disciplina_id, turma_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/leciona')

@app.route('/remover_leciona/<int:professor_id>/<int:disciplina_id>/<int:turma_id>')
def remover_leciona(professor_id, disciplina_id, turma_id):
    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Removendo a relação "leciona" da tabela
    cursor.execute("DELETE FROM leciona WHERE professor_id=? AND disciplina_id=? AND turma_id=?",
                   (professor_id, disciplina_id, turma_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/leciona')

@app.route('/atualizar_leciona/<int:professor_id>/<int:disciplina_id>/<int:turma_id>', methods=['POST'])
def atualizar_leciona(professor_id, disciplina_id, turma_id):
    # Recuperando os dados do formulário
    novo_professor_id = request.form['professor_id']
    nova_disciplina_id = request.form['disciplina_id']
    nova_turma_id = request.form['turma_id']

    # Conectando ao banco de dados
    conn = sqlite3.connect('sistema_de_matriculas.db')
    cursor = conn.cursor()

    # Atualizando os dados da relação "leciona" na tabela
    cursor.execute("UPDATE leciona SET professor_id=?, disciplina_id=?, turma_id=? WHERE professor_id=? AND disciplina_id=? AND turma_id=?",
                   (novo_professor_id, nova_disciplina_id, nova_turma_id, professor_id, disciplina_id, turma_id))

    # Salvando as alterações e fechando a conexão com o banco de dados
    conn.commit()
    conn.close()

    # Redirecionando de volta para a página inicial
    return redirect('/leciona')


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run()
