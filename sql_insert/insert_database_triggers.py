import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('../sistema_de_matriculas.db')
cursor = conn.cursor()

# Gatilho para verificar matrículas duplicadas
cursor.execute('''
    CREATE TRIGGER IF NOT EXISTS check_existing_matricula
    BEFORE INSERT ON matricula
    FOR EACH ROW
    BEGIN
        SELECT
            CASE
                WHEN EXISTS (
                    SELECT 1 FROM matricula
                    WHERE aluno_id = NEW.aluno_id AND disciplina_id = NEW.disciplina_id
                ) THEN
                    RAISE(ABORT, 'O aluno já está matriculado nesta disciplina.')
            END;
    END;
''')

# Gatilho que impede a modificação do nome de um aluno
cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS bloqueio_nome_aluno_before
    BEFORE UPDATE ON aluno
    FOR EACH ROW
    WHEN NEW.nome <> OLD.nome
    BEGIN
        UPDATE aluno SET nome = OLD.nome WHERE id = OLD.id;
        SELECT RAISE(ABORT, 'Modificação do nome de aluno não permitida');
    END;
""")

# Gatilho para verificar a idade dos alunos cadastrados
cursor.execute("""
CREATE TRIGGER IF NOT EXISTS verificar_idade_aluno
BEFORE INSERT ON aluno
FOR EACH ROW
WHEN NEW.data_nascimento IS NOT NULL
BEGIN
    -- Verifica se a idade é menor que a idade mínima permitida
    SELECT CASE
        WHEN (CAST((strftime('%Y', 'now') - strftime('%Y', NEW.data_nascimento)) AS INTEGER) < 18) THEN
            RAISE(ABORT, 'Idade mínima não atingida. Alunos devem ter pelo menos 18 anos.')
        ELSE
            NULL
    END;
END;
""")

# Confirmando as alterações e fechando a conexão
conn.commit()
conn.close()
