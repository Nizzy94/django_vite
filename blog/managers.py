from django.db import models


class CommentManager(models.Manager):
    def parent(self):
        return self.filter(parent=None)

    def children_com(self, id):
        return self.filter(parent=id)
