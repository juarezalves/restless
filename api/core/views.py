from django.shortcuts import render

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from core.models import Produto


class PostResource(DjangoResource):
    
    produto = [{'descricao':'Bicicleta'},{'descricao':'Mini system'}]

    # GET /api/posts/ (but not hooked up yet)
    def list(self):        
        return self.produto
    # GET /api/posts/<pk>/ (but not hooked up yet)

    def detail(self, pk):
        return self.produto

        #return Produto.objects.get(id=pk)      
       # Produto.objects.get(idCliente=id)                
        #return list(filter(lambda prod : prod.cliente==pk, self.produtos));

