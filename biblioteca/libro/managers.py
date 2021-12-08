from django.db import models

class BookManager(models.Manager):
    def getKword(self, keyWord):
        a = self.filter(
            title__icontains=keyWord
        )
        return a

    def getAuthors(self, author):
        list = self.filter(
            authors__id=author
        )

        return list
