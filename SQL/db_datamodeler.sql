-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2023-06-22 14:27:21 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE aluno (
    id              NUMBER NOT NULL,
    nome            VARCHAR2(50),
    email           VARCHAR2(50),
    curso           VARCHAR2(50),
    data_nascimento VARCHAR2(50),
    endereco        VARCHAR2(50)
);

ALTER TABLE aluno ADD CONSTRAINT aluno_pk PRIMARY KEY ( id );

CREATE TABLE disciplina (
    id            NUMBER NOT NULL,
    nome          VARCHAR2(50),
    carga_horaria NUMBER
);

ALTER TABLE disciplina ADD CONSTRAINT disciplina_pk PRIMARY KEY ( id );

CREATE TABLE leciona (
    professor_id  NUMBER NOT NULL,
    disciplina_id NUMBER NOT NULL,
    turma_id      NUMBER NOT NULL
);

ALTER TABLE leciona
    ADD CONSTRAINT leciona_pk PRIMARY KEY ( professor_id,
                                            disciplina_id,
                                            turma_id );

CREATE TABLE matricula (
    aluno_id      NUMBER NOT NULL,
    disciplina_id NUMBER NOT NULL
);

ALTER TABLE matricula ADD CONSTRAINT matricula_pk PRIMARY KEY ( aluno_id,
                                                                disciplina_id );

CREATE TABLE professor (
    id              NUMBER NOT NULL,
    nome            VARCHAR2(50),
    departamento    VARCHAR2(50),
    email           VARCHAR2(50),
    data_nascimento VARCHAR2(50)
);

ALTER TABLE professor ADD CONSTRAINT professor_pk PRIMARY KEY ( id );

CREATE TABLE turma (
    id      NUMBER NOT NULL,
    sala    VARCHAR2(50),
    horario VARCHAR2(50)
);

ALTER TABLE turma ADD CONSTRAINT turma_pk PRIMARY KEY ( id );

ALTER TABLE leciona
    ADD CONSTRAINT leciona_disciplina_fk FOREIGN KEY ( disciplina_id )
        REFERENCES disciplina ( id );

ALTER TABLE leciona
    ADD CONSTRAINT leciona_professor_fk FOREIGN KEY ( professor_id )
        REFERENCES professor ( id );

ALTER TABLE leciona
    ADD CONSTRAINT leciona_turma_fk FOREIGN KEY ( turma_id )
        REFERENCES turma ( id );

ALTER TABLE matricula
    ADD CONSTRAINT matricula_aluno_fk FOREIGN KEY ( aluno_id )
        REFERENCES aluno ( id );

ALTER TABLE matricula
    ADD CONSTRAINT matricula_disciplina_fk FOREIGN KEY ( disciplina_id )
        REFERENCES disciplina ( id );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             11
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
