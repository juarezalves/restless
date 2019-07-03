from django.shortcuts import render

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from core.models import Produto


class PostResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'cliente':'cliente',           
        'descricao': 'descricao',
    })

    produto = [{'descricao':'Bicicleta'},{'descricao':'Mini system'},]
    produtos = [{'cliente':1, 'descricao': 'produto 1'},
                {'cliente':1, 'descricao': 'produto 2'},
                {'cliente':3, 'descricao': 'produto 3'}]

    # GET /api/posts/ (but not hooked up yet)
    def list(self):        
        return self.produto
    # GET /api/posts/<pk>/ (but not hooked up yet)

    def detail(self, pk):
        #return Produto.objects.get(id=pk)      
       # Produto.objects.get(idCliente=id)                
        return list(filter(lambda prod : prod.cliente==pk, self.produtos));

