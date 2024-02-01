from django.db import models 

class Text(models.Model): #Text este denumirea tabelului din baza de date
    content = models.TextField() #content este un camp/ o coloana de tip text din tabelul Text
    
    def __str__(self):
        return self.content #returneaza continutul coloanei/campului content din tabelul Text
