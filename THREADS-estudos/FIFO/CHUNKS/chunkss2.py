
listas = [c for c in range(0,3000)]

def chunks(tam:int):
    for c in range(0,len(listas),tam):
        yield listas[c:c+tam] #yield é um gerador que coloca os dados na memoria de pouco em pouco ao invés de colocar tudo de uma vez

        # o que muda aqui é o chunk que subdivide ainda mais os pedaços que serão colocados na memoria.
## simple chunk function