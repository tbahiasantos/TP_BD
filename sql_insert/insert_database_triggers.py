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

#  Gatilho que impede a modificação do nome de um aluno
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

# Confirmando as alterações e fechando a conexão
conn.commit()
conn.close()
