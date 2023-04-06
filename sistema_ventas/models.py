from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
    descripcion_categoria = models.CharField(max_length=150)

class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50)
    precio_actual = models.DecimalField(max_digits = 11 ,decimal_places=2)
    stock_producto = models.IntegerField(default=0)
    categoria_producto = models.ForeignKey(Categoria, on_delete = models.CASCADE)

class Ubigeo(models.Model):
    id_ubigeo = models.BigAutoField(primary_key=True) 
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)   
    nombre_proveedor = models.CharField(max_length=50)
    telefono_proveedor =models.CharField(max_length=9)
    pagina_web_proveedor = models.CharField(max_length=500)
    ubigeo_proveedor = models.OneToOneField(Ubigeo, on_delete=models.CASCADE)

class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)    
    nombre_cliente = models.CharField(max_length=50)
    ubigeo_cliente = models.OneToOneField(Ubigeo, on_delete=models.CASCADE)

class Contacto_cliente(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=9)

class Proveedor_Producto:
    id_proveedor = models.OneToOneField(Proveedor, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Venta(models.Model):
    num_factura = models.BigAutoField(primary_key=True)
    fecha_venta = models.DateField('date')
    id_cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits = 11 ,decimal_places=2)
    descuento_venta = models.DecimalField(max_digits = 11 ,decimal_places=2)
    monto_final = models.DecimalField(max_digits = 11 ,decimal_places=2)

class Detalle_Venta(models.Model):
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    precio_actual = models.DecimalField(max_digits = 11 ,decimal_places=2)
    cantidad = models.IntegerField(default=0)
    monto_producto = models.DecimalField(max_digits = 11 ,decimal_places=2)
