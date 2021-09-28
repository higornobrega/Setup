def origem_destino_iguais(origem, destino, lista_de_erros):
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destinos não podem ser iguais'

def campo_tem_algum_numero(valor_campo,nome_campo, lista_de_erros):
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua número neste campos'

def ida_antes_da_volta(ida, volta, lista_de_erros):
    if ida > volta:
        lista_de_erros['volta'] = 'Data de Ida depois da data de Volta'

def ida_antes_de_hoje(ida, hoje, lista_de_erros):
    if ida < hoje:
        lista_de_erros['ida'] = 'Data de Ida antes da data de hoje'