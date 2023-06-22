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
    return redirect('/')

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
    return redirect('/')

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
    return redirect('/')

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run()
