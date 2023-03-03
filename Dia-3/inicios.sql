-- Run on active connection | = Select block

-- Para crear una base de datos

CREATE DATABASE 





CREATE TYPE tipo_sexo AS ENUM('MASCULINO', 'FEMENINO', 'PANSEXUAL', 'DONUTSEXUAL', 'OTRES');
CREATE TYPE

-- SECREA UNA TABLA EN LA BASE DE DATOS
pruebas=# CREATE TABLE alumnos (
pruebas(# id SERIAL NOT NULL PRIMARY KEY,
pruebas(# nombre TEXT NOT NULL,
pruebas(# apellido VARCHAR(50),
pruebas(# sexo tipo_sexo DEFAULT 'OTRES', -- si utilizamos un ENUM se pue
pruebas(# fecha_creacion TIMESTAMP(3) DEFAULT CURRENT_TIMESTAMP,
pruebas(# matriculado BOOLEAN DEFAULT FALSE
pruebas(#);
