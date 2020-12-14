import graphene
import django_filters
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id

from .models import empleado,categoria, producto, factura
class empleadoNode (DjangoObjectType):
    class Meta:
        model = empleado
        filter_fields = ['usuarios','Contrasenia','Roles']
        interfaces = (graphene.relay.Node,)

class categoriaNode (DjangoObjectType):
    class Meta:
        model = categoria
        filter_fields=['nombre_categoria']
        interfaces = (graphene.relay.Node,)

class productoNode(DjangoObjectType):
    class Meta:
        model = producto
        filter_fields =['nombre_producto','Descripcion','Existencia','Precio','Categoria']
        interfaces = (graphene.relay.Node,)

class facturaNode(DjangoObjectType):
    class Meta:
        model = factura
        filter_fields=['Nombre_Cliente','Producto','serie','nit','cantidad','Fecha','total']
        interfaces = (graphene.relay.Node,)


class createEmpleado(graphene.relay.ClientIDMutation):
    Empleado = graphene.Field(empleadoNode)

    class Input:
        usuarios=  graphene.String()
        Contrasenia = graphene.String()
        Roles = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Empleado = empleado(
        usuarios = input.get('usuarios'),
        Contrasenia = input.get('Contrasenia'),
        Roles = input.get('Roles')
        )
        Empleado.save()
        return createEmpleado(Empleado = Empleado)


class UpdateEmpleado(graphene.relay.ClientIDMutation):
    Empleado = graphene.Field(empleadoNode)

    class Input:
        id = graphene.String()
        usuarios = graphene.String()
        Contrasenia = graphene.String()
        Roles = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Empleado = empleado.objects.get(
            pk =from_global_id(input.get('id'))[1])
        Empleado.usuarios = input.get('usuarios')
        Empleado.Contrasenia = input.get('Contrasenia')
        Empleado.Roles = input.get('Roles')
        Empleado.save()
        return UpdateEmpleado(Empleado=Empleado)

class DeleteEmpleado(graphene.relay.ClientIDMutation):
    Empleado = graphene.Field(empleadoNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root,info, **input):
        Empleado = empleado.objects.get(
            pk=from_global_id(input.get('id'))[1]
        )
        Empleado.delete()
        return DeleteEmpleado(Empleado = Empleado)


class CreateProducto(graphene.relay.ClientIDMutation):
    Producto = graphene.Field(productoNode)

    class Input:
        nombre_producto = graphene.String()
        Descripcion = graphene.String()
        Existencia = graphene.Int()
        Precio = graphene.Float()
        nombre_categoria= graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Producto = producto(
        nombre_producto = input.get('nombre_producto'),
        Descripcion = input.get('Descripcion'),
        Existencia = input.get('Existencia'),
        Precio = input.get('Precio'),
        Categoria = categoria.objects.get(
            nombre_categoria = input.get('nombre_categoria')
        )
        )
        Producto.save()
        return CreateProducto(Producto = Producto)

class UpdateProducto(graphene.relay.ClientIDMutation):
    Producto = graphene.Field(productoNode)

    class Input:
        id = graphene.String()
        nombre_producto = graphene.String()
        Descripcion = graphene.String()
        Existencia = graphene.Int()
        Precio = graphene.Float()
        nombre_categoria= graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Producto = producto.objects.get(
            pk = from_global_id(input.get('id'))[1])
        Producto.nombre_producto = input.get('nombre_producto')
        Producto.Descripcion = input.get('Descripcion')
        Producto.Existencia = input.get('Existencia')
        Producto.Precio = input.get('Precio')
        Producto.Categoria = categoria.objects.get(
            nombre_categoria = input.get('nombre_categoria')
        )
        Producto.save()
        return UpdateProducto(Producto=Producto)

class DeleteProducto(graphene.relay.ClientIDMutation):
    Producto = graphene.Field(productoNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Producto = producto.objects.get(
            pk = from_global_id(input.get('id'))[1])
        Producto.delete()
        return DeleteProducto(Producto=Producto)

class createCategoria(graphene.relay.ClientIDMutation):
    Categoria = graphene.Field(categoriaNode)

    class Input:
        nombre_categoria=  graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Categoria = categoria(
        nombre_categoria = input.get('nombre_categoria'),
        )
        Categoria.save()
        return createCategoria(Categoria = Categoria)

class UpdateCategoria(graphene.relay.ClientIDMutation):
    Categoria = graphene.Field(categoriaNode)

    class Input:
        id = graphene.String()
        nombre_categoria = graphene.String()


    def mutate_and_get_payload(root, info, **input):
        Categoria = categoria.objects.get(
            pk =from_global_id(input.get('id'))[1])
        Categoria.nombre_categoria = input.get('nombre_categoria')
        Categoria.save()
        return UpdateCategoria(Categoria=Categoria)

class DeleteCategoria(graphene.relay.ClientIDMutation):
    Categoria = graphene.Field(categoriaNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root,info, **input):
        Categoria = categoria.objects.get(
            pk=from_global_id(input.get('id'))[1]
        )
        Categoria.delete()
        return DeleteCategoria(Categoria = Categoria)

class createFactura(graphene.relay.ClientIDMutation):
    Factura = graphene.Field(facturaNode)
    class Input:
        Nombre_Cliente =  graphene.String()
        nombre_producto = graphene.String()
        serie = graphene.Int()
        nit = graphene.String()
        cantidad = graphene.Int()
        Fecha = graphene.Date()
        total = graphene.Float()

    def mutate_and_get_payload(root, info, **input):
        Factura = factura(
        Nombre_Cliente = input.get('Nombre_Cliente'),
        Producto= producto.objects.get(
        nombre_producto= input.get('nombre_producto')),
        serie= input.get('serie'),
        cantidad = input.get('cantidad'),
        nit = input.get('nit'),
        Fecha = input.get('Fecha'),
        total = input.get('total'),
)
        Factura.save()
        return createFactura(Factura = Factura)

class UpdateFactura(graphene.relay.ClientIDMutation):
    Factura = graphene.Field(facturaNode)

    class Input:
        id = graphene.String()
        Nombre_Cliente =  graphene.String()
        nombre_producto = graphene.String()
        serie = graphene.Int()
        nit = graphene.String()
        cantidad = graphene.Int()
        Fecha = graphene.Date()
        total = graphene.Float()
        usuarios = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Factura = factura.objects.get(
            pk =from_global_id(input.get('id'))[1])
        Factura.Nombre_Cliente = input.get('Nombre_Cliente')
        Factura.Producto= producto.objects.get(
            nombre_producto= input.get('nombre_producto'))
        Factura.serie = input.get('serie')
        Factura.nit = input.get('nit')
        Factura.cantidad = input.get('cantidad')
        Factura.Fecha = input.get('Fecha')
        Factura.total = input.get('total')
        Factura.save()
        return UpdateFactura(Factura=Factura)

class DeleteFactura(graphene.relay.ClientIDMutation):
    Factura = graphene.Field(facturaNode)

    class Input:
        id = graphene.String()


    def mutate_and_get_payload(root, info, **input):
        Factura = factura.objects.get(
            pk =from_global_id(input.get('id'))[1])

        Factura.delete()
        return DeleteFactura(Factura=Factura)

class Query(object):
    empleado = graphene.relay.Node.Field(empleadoNode)
    all_empleados = DjangoFilterConnectionField(empleadoNode)

    categoria = graphene.relay.Node.Field(categoriaNode)
    all_categorias = DjangoFilterConnectionField(categoriaNode)

    producto = graphene.relay.Node.Field(productoNode)
    all_productos = DjangoFilterConnectionField(productoNode)

    factura = graphene.relay.Node.Field(facturaNode)
    all_facturas = DjangoFilterConnectionField(facturaNode)


class Mutation(graphene.AbstractType):
    create_Empleado = createEmpleado.Field()
    update_Empleado = UpdateEmpleado.Field()
    delete_Empleado = DeleteEmpleado.Field()
    create_Producto = CreateProducto.Field()
    update_Producto = UpdateProducto.Field()
    delete_Producto = DeleteProducto.Field()
    create_Categoria = createCategoria.Field()
    update_Categoria= UpdateCategoria.Field()
    delete_Categoria = DeleteCategoria.Field()
    create_Factura = createFactura.Field()
    update_Factura = UpdateFactura.Field()
    delete_Factura = DeleteFactura.Field()
