import graphene
import carp2.schema

class Query(carp2.schema.Query, graphene.ObjectType):
    pass

class Mutation(carp2.schema.Mutation, graphene.ObjectType):
    pass

schema =graphene.Schema(query=Query, mutation=Mutation)
