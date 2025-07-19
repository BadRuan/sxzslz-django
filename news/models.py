from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    TextField,
    IntegerField,
    ForeignKey,
    CASCADE,
)


class User(Model):
    user_name = CharField(max_length=30, unique=True)
    nick_name = CharField(max_length=30)
    password = CharField(max_length=30)
    create_time = DateTimeField("date created")

    def __str__(self) -> str:
        return self.nick_name


class Subset(Model):
    name = CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Article(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    subset_id = ForeignKey(Subset, on_delete=CASCADE)
    title = CharField(max_length=60)
    read = IntegerField(default=0)
    content = TextField()
    create_time = DateTimeField("date created")

    def __str__(self) -> str:
        return self.title
