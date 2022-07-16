from django.db import models

class Creator(models.Model):
    creator_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=12)
    link_tree = models.CharField(max_length = 100)

class Piece(models.Model):
    piece_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    content = models.CharField(max_length=200)

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)

class ItemTag(models.Model):
    piece_id = models.IntegerField()
    tag_id = models.IntegerField()