from django.db import models

class Empresa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nombre_empresa= models.CharField(db_column='Nombre_empresa', max_length=100)  
    rubro = models.CharField(db_column='Rubro', max_length=100)  

    class Meta:
        db_table = 'empresa'  # 

    def __str__(self):
        return self.nombre_empresa


class Trabajador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nombre_trabajador = models.CharField(db_column='Nombre_trabajador', max_length=100)  
    cargo = models.CharField(db_column='Cargo', max_length=100)  
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,  
        db_column='EmpresaID',
        related_name='trabajadores'  
    )

    class Meta:
        db_table = 'trabajador'  

    def __str__(self):
        return self.nombre_trabajador


class Documento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    tipo = models.CharField(db_column='Tipo', max_length=100) 
    fecha = models.DateField(db_column='Fecha')  
    trabajador = models.ForeignKey(
        Trabajador,
        on_delete=models.CASCADE,  
        db_column='TrabajadorID',
        related_name='documentos' 
    )

    class Meta:
        db_table = 'documento'  

    def __str__(self):
        return f"{self.tipo} - {self.trabajador.nombre}"
