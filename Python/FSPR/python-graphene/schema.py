import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()

class Query(graphene.ObjectType):
    
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()
    is_admin = graphene.Boolean()

    # resolver function
    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info, limit=None):
        return [
            User(id="1", username="Terrell", created_at=datetime.now()),
            User(id="2", username="Fred", created_at=datetime.now())
        ][:limit]

schema = graphene.Schema(query=Query) # auto_camelcase=False makes snakecase is default

result = schema.execute(
    '''
    {
        users {
            id
            username
            createdAt
        }
    }
    '''
)

# print(result.data.items())

dictResult = dict(result.data.items())
print(json.dumps(dictResult))