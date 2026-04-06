# filepath: d:\ved_clg\sem4\mini_proj\python_M\pokedex\pokedex_project\Pokedex\models.py
from django.db import models

class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image_url = models.TextField()
    height = models.IntegerField()
    weight = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()  # Add this field
    special_defense = models.IntegerField()  # Add this field
    speed = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'pokemon'
        ordering = ['id']  # Order by Pokémon ID by default

    def __str__(self):
        return f"#{self.id} - {self.name}"