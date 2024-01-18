from mongoengine import connect, Document
from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import StringField, IntField

connect(
    host="mongodb+srv://magnetonbohra:I7RL0iG8DxTNXVJi@cluster0.wellc9q.mongodb.net/",
    db="example",
    ssl=True
)


class Users(Document):
    name = StringField()
    email = StringField()
    age = IntField()
    
    def __str__(self):
        return f"User(name={self.name}, email={self.email}, age={self.age})"


user = Users(name="Bob Marley", email="bob@example.com", age=42)
user.save()

for user in Users.objects():
    print(user)