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
    db_table: str = "user"
    user_name = CharField(max_length=30, unique=True)
    nick_name = CharField(max_length=30)
    password = CharField(max_length=30)
    create_time = DateTimeField("date created")

    def __str__(self) -> str:
        return self.nick_name

    class Meta:
        verbose_name: str = "用户列表"
        verbose_name_plural: str = "编辑用户"


class Subset(Model):
    db_table: str = "subset"
    name = CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name: str = "文章类别列表"
        verbose_name_plural: str = "文章类别"


class Article(Model):
    db_table: str = "article"
    user_id = ForeignKey(User, on_delete=CASCADE)
    subset_id = ForeignKey(Subset, on_delete=CASCADE)
    title = CharField(max_length=60)
    read = IntegerField(default=0)
    content = TextField()
    create_time = DateTimeField("date created")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name: str = "文章列表"
        verbose_name_plural: str = "文章"
