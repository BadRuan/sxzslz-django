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
    user_name = CharField("用户名", max_length=30, unique=True)
    nick_name = CharField("昵称", max_length=30)
    password = CharField("密码", max_length=30)
    create_time = DateTimeField("创建时间")

    def __str__(self) -> str:
        return self.nick_name

    class Meta:
        verbose_name: str = "用户"
        verbose_name_plural: str = "用户"


class Subset(Model):
    db_table: str = "subset"
    name = CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name: str = "文章类别"
        verbose_name_plural: str = "文章类别"


class Article(Model):
    db_table: str = "article"
    user_id = ForeignKey(User, on_delete=CASCADE)
    subset_id = ForeignKey(Subset, on_delete=CASCADE)
    title = CharField("标题", max_length=60)
    read = IntegerField("浏览量", default=0)
    content = TextField("文章内容")
    create_time = DateTimeField("发布时间")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name: str = "文章"
        verbose_name_plural: str = "文章"
