import graphene
import json

class Query(graphene.ObjectType):
    hello = graphene.String()

    is_admin = graphene.Boolean()

    # resolver function
    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True


schema = graphene.Schema(query=Query) # auto_camelcase=False makes snakecase is default

result = schema.execute(
    '''
    {
        isAdmin
    }
    '''
)

# print(result.data.items())

dictResult = dict(result.data.items())
print(json.dumps(dictResult))