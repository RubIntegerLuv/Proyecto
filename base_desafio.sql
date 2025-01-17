-- Crear la base de datos
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'desafio_kis')
BEGIN
    CREATE DATABASE desafio_kis;
END;
GO

-- Usar la base de datos
USE desafio_kis;
GO

-- Tabla Empresa
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Empresa' AND xtype='U')
BEGIN
    CREATE TABLE Empresa (
        ID INT IDENTITY(1,1) PRIMARY KEY,
        Nombre_empresa NVARCHAR(100) NOT NULL,
        Rubro NVARCHAR(100) NOT NULL
    );
END;
GO

-- Tabla Trabajador
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Trabajador' AND xtype='U')
BEGIN
    CREATE TABLE Trabajador (
        ID INT IDENTITY(1,1) PRIMARY KEY,
        Nombre_trabajador NVARCHAR(100) NOT NULL,
        Cargo NVARCHAR(100) NOT NULL,
        EmpresaID INT NOT NULL,
        FOREIGN KEY (EmpresaID) REFERENCES Empresa(ID) ON DELETE CASCADE
    );
END;
GO

-- Tabla Documento
IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Documento' AND xtype='U')
BEGIN
    CREATE TABLE Documento (
        ID INT IDENTITY(1,1) PRIMARY KEY,
        Tipo NVARCHAR(100) NOT NULL,
        Fecha DATE NOT NULL,
        TrabajadorID INT NOT NULL,
        FOREIGN KEY (TrabajadorID) REFERENCES Trabajador(ID) ON DELETE CASCADE
    );
END;
GO

-- Insertar datos de ejemplo en Empresa
IF NOT EXISTS (SELECT * FROM Empresa)
BEGIN
    INSERT INTO Empresa (Nombre_empresa, Rubro) VALUES
    ('KIS S.P.A', 'Tecnología'),
    ('Empresa X', 'Finanzas'),
    ('Empresa Y', 'Construcción');
END;
GO

-- Insertar datos de ejemplo en Trabajador
IF NOT EXISTS (SELECT * FROM Trabajador)
BEGIN
    INSERT INTO Trabajador (Nombre_trabajador, Cargo, EmpresaID) VALUES
    ('Juan Pérez', 'Gerente', 1),
    ('Ana Gómez', 'Operador', 1),
    ('Carlos Díaz', 'Analista', 2),
    ('Laura Torres', 'Ingeniero', 3),
    ('Pedro Morales', 'Ingeniero', 3),
    ('María López', 'Gerente', 2),
    ('Jorge Castillo', 'Ingeniero', 1),
    ('Pablo Herrera', 'Operador', 2),
    ('Sofía Morales', 'Analista', 3),
    ('Andrés Gómez', 'Gerente', 1);
END;
GO

-- Insertar datos de ejemplo en Documento
IF NOT EXISTS (SELECT * FROM Documento)
BEGIN
    INSERT INTO Documento (Tipo, Fecha, TrabajadorID) VALUES
    ('Contrato', '2025-01-01', 1),
    ('Certificado', '2025-01-02', 2),
    ('Informe', '2025-01-03', 3),
    ('Manual', '2025-01-04', 4),
    ('Contrato', '2025-01-05', 5),
    ('Certificado', '2025-01-06', 6),
    ('Informe', '2025-01-07', 7),
    ('Manual', '2025-01-08', 8),
    ('Certificado', '2025-01-09', 9),
    ('Contrato', '2025-01-10', 10),
    ('Informe', '2025-01-11', 1),
    ('Certificado', '2025-01-12', 3),
    ('Manual', '2025-01-13', 5);
END;
GO
