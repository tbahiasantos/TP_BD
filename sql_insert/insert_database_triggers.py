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

# Gatilho para travar exclusão de professor se lecionando disciplina
cursor.execute("""
CREATE TRIGGER IF NOT EXISTS validar_exclusao_professor
BEFORE DELETE ON professor
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN EXISTS (
            SELECT 1
            FROM leciona
            WHERE professor_id = OLD.id
        )
        THEN RAISE(ABORT, 'O professor está lecionando em disciplinas e não pode ser excluído.')
    END;
END;
""")

# Gatilho para remover todas as matrículas associadas a um aluno se excluido
cursor.execute("""
CREATE TRIGGER IF NOT EXISTS exclusao_cascata_matricula
AFTER DELETE ON aluno
FOR EACH ROW
BEGIN
    DELETE FROM matricula
    WHERE aluno_id = OLD.id;
END;
""")

# Gatilho para controlar a exclusão em cascata de disciplinas quando uma turma é excluída
cursor.execute("""
CREATE TRIGGER IF NOT EXISTS exclusao_cascata_disciplina
AFTER DELETE ON turma
FOR EACH ROW
BEGIN
    DELETE FROM disciplina
    WHERE id IN (
        SELECT disciplina_id
        FROM leciona
        WHERE turma_id = OLD.id
    );
END;
""")

# Confirmando as alterações e fechando a conexão
conn.commit()
conn.close()
