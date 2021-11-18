# 2.1.1 TAD posicao

# Construtores

def cria_posicao(x, y):
    """ cria_posicao: int × int → posicao
    Esta função recebe duas coordenadas
    e cria a posição correspondente.
    """
    if type(x) != int or type(y) != int:
        raise ValueError("cria_posicao: argumentos invalidos")
    if x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (x, y)

def cria_copia_posicao(pos):
    """ cria_copia_posicao: posicao → posicao
    Esta função recebe uma posição e cria uma
    cópia da mesma.
    """
    if type(pos) != tuple:
        raise ValueError("cria_copia_posicao: argumento invalido")
    if len(pos) != 2:
        raise ValueError("cria_copia_posicao: argumento invalido")
    return cria_posicao(obter_pos_x(pos), obter_pos_y(pos))

# Seletores

def obter_pos_x(pos):
    """ obter_pos_x : posicao → int
    Esta função recebe uma posição e devolve
    a sua abcissa.
    """
    return pos[0]

def obter_pos_y(pos):
    """ obter_pos_y : posicao → int
    Esta função recebe uma posição e devolve
    a sua ordenada.
    """
    return pos[1]

# Reconhecedor

def eh_posicao(arg):
    """ eh_posicao: universal → booleano
    Esta função avalia se o argumento que recebe
    se trata de um TAD posição.
    """
    if type(arg) != tuple:
        return False
    if len(arg) != 2:
        return False
    if type(arg[0]) != int or type(arg[1]) != int:
        return False
    if obter_pos_x(arg) < 0 or obter_pos_y(arg) < 0:
        return False
    return True

# Teste

def posicoes_iguais(pos1, pos2):
    """ posicoes_iguais: posicao × posicao → booleano
    Esta função avalia se duas posições são iguais.
    """
    return obter_pos_x(pos1) == obter_pos_x(pos2) and obter_pos_y(pos1) == obter_pos_y(pos2)

# Transformador

def posicao_para_str(pos):
    """ posicao_para_str : posicao → str
    Esta função devolve uma cadeia de caracteres na forma
    '(x, y)' que representa a posição que recebeu como argumento.
    """
    return "(" + str(obter_pos_x(pos)) + ", " + str(obter_pos_y(pos)) + ")"

# Funções de alto nível associadas ao TAD posicao

def obter_posicoes_adjacentes(pos):
    """ obter_posicoes_adjacentes: posicao → tuplo
    Esta função recebe uma posição e devolve as 4 (ou menos) posições que a rodeiam.
    """
    pos_adjacentes = ()

    if obter_pos_y(pos) != 0:
        pos_adjacentes += (cria_posicao(obter_pos_x(pos), obter_pos_y(pos) - 1), )
    pos_adjacentes += (cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos)), )
    pos_adjacentes += (cria_posicao(obter_pos_x(pos), obter_pos_y(pos) + 1), )
    if obter_pos_x(pos) != 0:
        pos_adjacentes += (cria_posicao(obter_pos_x(pos) - 1, obter_pos_y(pos)), )
    
    return pos_adjacentes

def ordenar_posicoes(tuplo_posicoes):
    """ordenar_posicoes: tuplo → tuplo
    Esta função recebe um tuplo com um conjunto de posições
    e ordena-as de acordo com a ordem de leitura do prado.
    """
    lista_posicoes = list(tuplo_posicoes)
    # Bubble sort aplicado ao contexto em questão
    mudou = True
    while mudou:
            mudou = False
            for i in range(len(lista_posicoes)-1):
                if obter_pos_y(lista_posicoes[i]) > obter_pos_y(lista_posicoes[i + 1]):
                    lista_posicoes[i], lista_posicoes[i + 1] = lista_posicoes[i + 1], lista_posicoes[i]
                    mudou = True

    # Bubble sort aplicado ao contexto em questão
    mudou = True
    while mudou:
        mudou = False
        for i in range(len(lista_posicoes)-1):
            if obter_pos_y(lista_posicoes[i]) == obter_pos_y(lista_posicoes[i + 1]):
                if obter_pos_x(lista_posicoes[i]) > obter_pos_x(lista_posicoes[i + 1]):
                    lista_posicoes[i], lista_posicoes[i + 1] = lista_posicoes[i + 1], lista_posicoes[i]
                    mudou = True

    return tuple(lista_posicoes)

# 2.1.2 TAD animal

# Construtores

def cria_animal(especie, freq_reproducao, freq_alimentacao):
    """cria animal: str × int × int → animal
    Esta função recebe uma espécie, uma frequência de reprodução
    e uma frequência de alimentação e cria o animal correspondente.
    """
    if type(especie) != str or type(freq_reproducao) != int or type(freq_alimentacao) != int:
        raise ValueError("cria_animal: argumentos invalidos")
    if len(especie) < 1 or freq_reproducao <= 0 or freq_alimentacao < 0:
        raise ValueError("cria_animal: argumentos invalidos")
    for char in especie:
        if not char.isalpha():
            raise ValueError("cria_animal: argumentos invalidos")
    return {"Especie": especie, "FreqReproducao": freq_reproducao,\
    "FreqAlimentacao": freq_alimentacao, "Fome": 0, "Idade": 0}

def cria_copia_animal(animal):
    """cria_copia_animal: animal → animal
    Esta função recebe um animal e cria uma
    cópia do mesmo.
    """
    return dict(animal)

# Seletores

def obter_especie(animal):
    """ obter_especie: animal → str
    Esta função recebe um animal e retorna a sua espécie.
    """
    return animal["Especie"]

def obter_freq_reproducao(animal):
    """ obter_freq_reproducao: animal → int
    Esta função recebe um animal e retorna a sua
    frquência de reprodução.
    """
    return animal["FreqReproducao"]

def obter_freq_alimentacao(animal):
    """ obter_freq_alimentacao: animal → int
    Esta função recebe um animal e retorna a sua
    frquência de alimentação.
    """
    return animal["FreqAlimentacao"]

def obter_idade(animal):
    """ obter_idade: animal → int
    Esta função recebe um animal e retorna a sua idade.
    """
    return animal["Idade"]

def obter_fome(animal):
    """ obter_fome: animal → int
    Esta função recebe um animal e retorna a sua fome.
    """
    return animal["Fome"]

# Modificadores

def aumenta_idade(animal):
    """ aumenta_idade: animal → animal
    Esta função aumenta destrutivamente a idade de um animal,
    retornando-o.
    """
    animal["Idade"] += 1
    return animal

def reset_idade(animal):
    """ reset_idade: animal → animal
    Esta função altera destrutivamente a idade de um animal para 0,
    retornando-o.
    """
    animal["Idade"] = 0
    return animal

def aumenta_fome(animal):
    """ aumenta_fome: animal → animal
    Esta função aumenta destrutivamente a fome de um animal,
    retornando-o.
    """
    if animal["FreqAlimentacao"] != 0:
        animal["Fome"] += 1
    return animal

def reset_fome(animal):
    """ reset_fome: animal → animal
    Esta função altera destrutivamente a fome de um animal para 0,
    retornando-o.
    """
    animal["Fome"] = 0
    return animal

# Reconhecedores

def eh_animal(arg):
    """ eh_animal: universal → booleano
    Esta função avalia se o argumento que recebe
    se trata de um TAD animal.
    """
    if type(arg) != dict:
        return False
    if len(arg) != 5:
        return False
    if not "Especie" in arg.keys() or not "FreqReproducao" in arg.keys() or not\
    "FreqAlimentacao" in arg.keys() or not "Fome" in arg.keys() or not "Idade"in arg.keys():
        return False
    if type(obter_especie(arg)) != str or type(obter_freq_reproducao(arg)) != int or\
    type(obter_freq_alimentacao(arg)) != int or type(obter_fome(arg)) != int or type(obter_idade(arg)) != int:
        return False
    if len(obter_especie(arg)) == 0:
        return False
    for char in obter_especie(arg):
        if not char.isalpha():
            return False
    if obter_freq_reproducao(arg) <= 0 or obter_freq_alimentacao(arg) < 0 or\
    obter_fome(arg) < 0 or obter_idade(arg) < 0:
        return False
    return True

def eh_predador(animal):
    """eh_predador: animal → booleano
    Esta função avalia se o animal que recebe
    se trata de um predador.
    """
    if not eh_animal(animal):
        return False
    if obter_freq_alimentacao(animal) != 0:
        return True
    return False

def eh_presa(animal):
    """eh_presa: animal → booleano
    Esta função avalia se o animal que recebe
    se trata de uma presa.
    """
    if not eh_animal(animal):
        return False
    return not eh_predador(animal)

# Teste

def animais_iguais(animal1, animal2):
    """ animais_iguais: animal × animal → booleano
    Esta função avalia se dois animais são iguais.
    """
    if not eh_animal(animal1) or not eh_animal(animal2):
        return False
    if obter_especie(animal1) != obter_especie(animal2):
        return False
    if obter_freq_reproducao(animal1) != obter_freq_reproducao(animal2):
        return False
    if obter_freq_alimentacao(animal1) != obter_freq_alimentacao(animal2):
        return False
    if obter_idade(animal1) != obter_idade(animal2):
        return False
    if obter_fome(animal1) != obter_fome(animal2):
        return False
    return True

# Transformadores

def animal_para_char(animal):
    """ animal_para_char : animal → str
    Esta função devolve uma cadeia de caracteres constituída
    pela letra inicial da espécie do animal recebido como argumento,
    em letras maiúsculas caso seja um predador e em letras minúsculas
    caso contrário.
    """
    if eh_predador(animal):
        return obter_especie(animal)[0].upper()
    return obter_especie(animal)[0].lower()

def animal_para_str(animal):
    """ animal_para_str : animal → str
    Esta função devolve uma cadeia de caracteres na forma
    'espécie [idade/freq reprodução]', no caso do animal ser uma presa,
    ou 'espécie [idade/freq reprodução;fome/freq alimentação]',
    no caso do animal ser um predador, que representa o animal
    que recebeu como argumento.
    """
    # Esta string contém a parte que será comum na representação dos animais,
    # independentemente destes se tratarem de presas ou predadores. 
    str_animal = (obter_especie(animal) + " [" + str(obter_idade(animal)) +"/"\
    + str(obter_freq_reproducao(animal)))

    if eh_predador(animal):
        return str_animal + ";" + str(obter_fome(animal)) + "/" + str(obter_freq_alimentacao(animal)) + "]"
    return str_animal + "]"

# Funções de alto nível associadas ao TAD animal

def eh_animal_fertil(animal):
    """ eh_animal_fertil: animal → booleano
    Esta função avalia se o animal passado como argumento
    já atingiu a idade de reprodução.
    """
    if obter_freq_reproducao(animal) <= obter_idade(animal):
        return True
    return False

def eh_animal_faminto(animal):
    """ eh_animal_faminto: animal → booleano
    Esta função avalia se o animal passado como argumento
    já atingiu fome igual à sua frequência de alimentação,
    devolve automaticamente falso caso o animal se trate
    de uma presa.
    """
    if eh_presa(animal):
        return False
    if obter_freq_alimentacao(animal) == obter_fome(animal):
        return True
    return False

def reproduz_animal(animal):
    """ reproduz_animal: animal → animal
    Esta função devolve um animal da mesma 
    espécie do animal passado como argumento
    com idade e fome iguais a 0, altera
    destrutivamente para 0 a idade do animal
    passado como argumento.
    """
    reset_idade(animal)
    return cria_animal(obter_especie(animal), obter_freq_reproducao(animal), obter_freq_alimentacao(animal))

# TAD prado

    # Função auxiliar index, ajuda a reduzir a repetição de código e a respeitar a abstração de dados nas funções eliminar_animal, mover_animal e geracao.

def index(posicoes, pos):
    """ index: lista posicoes × posicao → int ou booleano
    Esta função recebe uma lista e uma posição e devolve
    o indíce dessa posição na lista, devolvendo False caso
    a posição não esteja na lista. Serve como uma alternativa
    que respeita a abstração de dados para as funções "index"
    e "in" do python.
    """
    for i in range(len(posicoes)):
        if posicoes_iguais(posicoes[i], pos):
            return i
    return False


    # Função auxiliar prado_efetivo, ajuda a reduzir a repetição de código nas funções cria_prado, eh_prado e eh_posicao_obstaculo.

def prado_efetivo(pos_canto, pos):
    """ prado_efetivo: posicao × posicao → booleano
    Esta função recebe a posição de um canto do prado e uma posição
    e avalia se a posição se encontra dentro dos limites do prado,
    excluindo a zona das montanhas que rodeiam o prado.
    """
    if obter_pos_x(pos) >= obter_pos_x(pos_canto) or obter_pos_y(pos) >= obter_pos_y(pos_canto):
        return False
    if obter_pos_x(pos) == 0 or obter_pos_y(pos) == 0:
        return False
    return True

# Construtores

def cria_prado(pos, pos_obstaculos, animais, pos_animais):
    """ cria_prado: posicao × tuplo × tuplo × tuplo → prado
    Esta função recebe uma posição que corresponde ao canto
    inferior direito do prado, um tuplo com a posição dos
    rochedos do prado, e dois tuplos, um com os animais que habitam
    o prado e outro com as respetivas posições e cria o prado
    correspondente.
    """
    if not eh_posicao(pos):
        raise ValueError("cria_prado: argumentos invalidos")
    if type(pos_obstaculos) != tuple or type(animais) != tuple or type(pos_animais) != tuple:
        raise ValueError("cria_prado: argumentos invalidos")
    for posicao in pos_obstaculos:
        if not eh_posicao(posicao):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(posicao) >= obter_pos_x(pos) or obter_pos_y(posicao) >= obter_pos_y(pos):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0:
            raise ValueError("cria_prado: argumentos invalidos")
    if len(animais) != len(pos_animais):
        raise ValueError("cria_prado: argumentos invalidos")
    for animal in animais:
        if not eh_animal(animal):
            raise ValueError("cria_prado: argumentos invalidos")
    for posicao in pos_animais:
        if not eh_posicao(posicao):
            raise ValueError("cria_prado: argumentos invalidos")
        if not prado_efetivo(pos, posicao):
            raise ValueError("cria_prado: argumentos invalidos")
    
    return {"PosCanto": pos, "PosObstaculos": pos_obstaculos, "Animais": animais, "PosAnimais": pos_animais}

def cria_copia_prado(prado):
    """cria_copia_prado: prado → prado
    Esta função recebe um prado e cria uma
    cópia do mesmo.
    """
    return dict(prado)

# Seletores

def obter_tamanho_x(prado):
    """ obter_tamanho_x: prado → int
    Esta função recebe um prado e
    devolve a sua largura.
    """
    return obter_pos_x(prado["PosCanto"]) + 1 

def obter_tamanho_y(prado):
    """ obter_tamanho_y: prado → int
    Esta função recebe um prado e
    devolve a sua altura.
    """
    return obter_pos_y(prado["PosCanto"]) + 1

def obter_numero_predadores(prado):
    """ obter_numero_predadores: prado → int
    Esta função recebe um prado e
    devolve a quantidade de predadores
    que o habitam.
    """
    num_predadores = 0
    for animal in prado["Animais"]:
        if eh_predador(animal):
            num_predadores += 1
    return num_predadores

def obter_numero_presas(prPrado):
    """ obter_numero_presas: prado → int
    Esta função recebe um prado e
    devolve a quantidade de presas
    que o habitam.
    """
    num_presas = 0
    for animal in prPrado["Animais"]:
        if eh_presa(animal):
            num_presas += 1
    return num_presas

def obter_posicao_animais(prado):
    """ obter_posicao_animais: prado → tuplo posicoes
    Esta função recebe um prado e devolve um tuplo
    com as posições dos animais que o habitam,
    ordenadas de acordo com a ordem de leitura do
    prado.
    """
    return ordenar_posicoes(prado["PosAnimais"])

def obter_animal(prado, pos):
    for i in range(len(prado["PosAnimais"])):
        if posicoes_iguais(prado["PosAnimais"][i], pos):
            return prado["Animais"][i]

# Modificadores

def eliminar_animal(prado, pos):
    """ eliminar_animal: prado × posicao → prado
    Esta função recebe um prado e uma posição e
    altera destrutivamente o prado, eliminando
    o animal na posição passada como argumento. 
    """
    animais = list(prado["Animais"])
    pos_animais = list(prado["PosAnimais"])
    i = index(pos_animais, pos)
    del animais[i]
    del pos_animais[i]
    prado["Animais"] = tuple(animais)
    prado["PosAnimais"] = tuple(pos_animais)
    return prado

def mover_animal(prado, pos_animal, pos_nova):
    """ mover_animal: prado × posicao × posicao → prado
    Esta função recebe um prado e duas posição e
    altera destrutivamente o prado, movimentando
    o animal na preimeira posição passada como argumento
    para a segunda posição.
    """
    pos_animais = list(prado["PosAnimais"])
    i = index(pos_animais, pos_animal)
    pos_animais[i] = pos_nova
    prado["PosAnimais"] = tuple(pos_animais)
    return prado

def inserir_animal(prado, animal, pos):
    """ mover_animal: prado × animal × posicao → prado
    Esta função recebe um prado, um animal e uma posição
    e altera destrutivamente o prado, acrescentado o animal
    passado como argumento na posição passada como argumento.
    """
    prado["Animais"] += (cria_copia_animal(animal), )
    prado["PosAnimais"] += (cria_copia_posicao(pos), )
    return prado

# Reconhecedores

def eh_prado(arg):
    """ eh_prado: universal → booleano
    Esta função avalia se o argumento que recebe
    se trata de um TAD prado.
    """
    if type(arg) != dict:
        return False
    if len(arg) != 4:
        return False
    if not "PosCanto" in arg.keys() or not "PosObstaculos" in arg.keys() or not "Animais" in arg.keys() or not "PosAnimais" in arg.keys():
        return False
    if not eh_posicao(arg["PosCanto"]):
        return False
    if type(arg["PosObstaculos"]) != tuple or type(arg["Animais"]) != tuple or type(arg["PosAnimais"]) != tuple:
        return False
    if len(arg["Animais"]) != len(arg["PosAnimais"]):
        return False
    
    for posicao in arg["PosObstaculos"]:
        if not eh_posicao(posicao):
            return False
        if not prado_efetivo(arg["PosCanto"], posicao):
            return False
    for animal in arg["Animais"]:
        if not eh_animal(animal):
            return False
    for posicao in arg["PosAnimais"]:
        if not eh_posicao(posicao):
            return False
        if not prado_efetivo(arg["PosCanto"], posicao):
            return False

    for posicao in arg["PosObstaculos"]:
        for pos in arg["PosAnimais"]:
            if posicoes_iguais(posicao, pos):
                return False
    return True

def eh_posicao_animal(prado, pos):
    """ eh_posicao_animal: prado × posicao → booleano
    Esta função avalia se a posição que recebe
    se trata da posição de um animal no prado
    passado como argumento.
    """
    for posicao in obter_posicao_animais(prado):
        if posicoes_iguais(posicao, pos):
            return True
    return False

def eh_posicao_obstaculo(prado, pos):
    """ eh_posicao_obstaculo: prado × posicao → booleano
    Esta função avalia se a posição que recebe
    se trata da posição de um obstaculo no prado
    passado como argumento.
    """
    if not prado_efetivo(cria_posicao(obter_tamanho_x(prado) - 1, obter_tamanho_y(prado) - 1), pos):
            return True
    for posicao in prado["PosObstaculos"]:
        if posicoes_iguais(posicao, pos):
            return True
    return False

def eh_posicao_livre(prado, pos):
    """ eh_posicao_livre: prado × posicao → booleano
    Esta função avalia se a posição que recebe
    se trata da posição de uma posição livre no prado
    passado como argumento, ou seja, se se encontra sem animais
    nem obstáculos.
    """
    if eh_posicao_animal(prado, pos) or eh_posicao_obstaculo(prado, pos):
        return False
    return True

# Teste

def prados_iguais(prado1, prado2):
    """ prados_iguais: prado × prado → booleano
    Esta função avalia se dois prados são iguais.
    """
    if len(obter_posicao_animais(prado1)) != len(obter_posicao_animais(prado2)):
        return False
    for i in range(len(obter_posicao_animais(prado1))):
        if not posicoes_iguais(obter_posicao_animais(prado1)[i], obter_posicao_animais(prado2)[i]):
            return False
    
    if len(prado1["PosObstaculos"]) != len(prado2["PosObstaculos"]):
        return False
    for i in range(len(prado1["PosObstaculos"])):
        if not posicoes_iguais(prado1["PosObstaculos"][i], prado2["PosObstaculos"][i]):
            return False

    for i in range(len(obter_posicao_animais(prado1))):
        if not animais_iguais(obter_animal(prado1,obter_posicao_animais(prado1)[i]), obter_animal(prado2,obter_posicao_animais(prado2)[i])):
            return False
    
    if not posicoes_iguais(prado1["PosCanto"], prado2["PosCanto"]):
        return False
    return True

# Transformador

def prado_para_str(prado):
    """ prado_para_str : prado → str
    Esta função devolve uma cadeia de caracteres que
    representa o prado que recebeu como argumento, os
    animais são representados pela sua representação em char,
    os obstáculos por "@" e as posições livres por ".".
    """
    # Criação de uma matriz com linhas vazias com o tamanho do prado,
    # exceto os contornos superiores e inferiores.
    matriz_prado = [[] for y in range(obter_tamanho_y(prado))]
    matriz_prado[0] = ["-" for x in range(obter_tamanho_x(prado))]
    matriz_prado[0][0] = "+"
    matriz_prado[0][-1] = "+"
    matriz_prado[-1] = matriz_prado[0]
    str_prado = ""

    # Preenchimento das linhas da matriz com os animais, obstáculos e posições vazias.
    for y in range(1, len(matriz_prado) - 1):
        matriz_prado[y].append("|")
        for x in range(1,obter_tamanho_x(prado) - 1):
            if eh_posicao_livre(prado, cria_posicao(x,y)):
                matriz_prado[y].append(".")
            elif eh_posicao_obstaculo(prado, cria_posicao(x,y)):
                matriz_prado[y].append("@")
            else:
                matriz_prado[y].append(animal_para_char(obter_animal(prado, cria_posicao(x,y))))
        matriz_prado[y].append("|")
    
    # Transformação da matriz numa string correspondente
    for y in range(len(matriz_prado)):
        for char in matriz_prado[y]:
            str_prado += str(char)
        str_prado += "\n"

    return str_prado.rstrip("\n")

# Funções de alto nível associadas ao TAD prado

    # Função auxiliar eh_posicao_presa, ajuda a reduzir a repetição de código nas funções pos_possiveis e geracao.

def eh_posicao_presa(prado, pos):
    """ eh_posicao_presa: prado × posicao → booleano
    Esta função avalia se a posição que recebe
    se trata da posição de uma presa.
    """
    if eh_posicao_animal(prado, pos):
        if eh_presa(obter_animal(prado, pos)):
            return True
    return False

def obter_valor_numerico(prado, pos):
    """ obter_valor_numerico: prado × posicao → int
    Esta função recebe um prado e uma posição e cálcula
    o valor numérico associado a essa posição, de acordo
    com a ordem de leitura do prado.
    """
    return obter_tamanho_x(prado)*obter_pos_y(pos) + obter_pos_x(pos)

    # Função auxiliar ordenar_movimentos, ajuda a organizar o código na função pos_possiveis.

def ordenar_movimentos(posicoes):
    """ ordenar_movimentos: lista posicoes → lista posicoes
    Esta função recebe uma lista de posições que correspondem
    a possíveis movimentos e ordena-as em sentido horário.
    """
    lista_posicoes = list(posicoes)
    mudou = True
    # Bubble sort aplicado ao contexto em questão
    while mudou:
        mudou = False
        for i in range(len(lista_posicoes) - 1):
            if obter_pos_y(lista_posicoes[i]) > obter_pos_y(lista_posicoes[i + 1]):
                lista_posicoes[i], lista_posicoes[i + 1] = lista_posicoes[i + 1], lista_posicoes[i]
                mudou = True

    mudou = True
    while mudou:
        mudou = False
        for i in range(1, len(lista_posicoes) - 1):
            if obter_pos_x(lista_posicoes[i]) < obter_pos_x(lista_posicoes[i + 1]):
                lista_posicoes[i], lista_posicoes[i + 1] = lista_posicoes[i + 1], lista_posicoes[i]
                mudou = True
    return lista_posicoes

    # Função auxiliar pos_possiveis, ajuda a organizar o código na função obter_movimento.

def pos_possiveis(prado, pos, animal):
    """ pos_possiveis: prado × posicao × animal → lista posicoes
    Esta função recebe um prado, uma posição e um animal e retorna
    a lista dos seus movimentos possíveis, ordenados em sentido horário.
    """
    if eh_predador(animal):
        posicoes_possiveis = [pos for pos in ordenar_movimentos(obter_posicoes_adjacentes(pos))\
            if eh_posicao_presa(prado, pos)]
        if posicoes_possiveis == []:
            posicoes_possiveis = [pos for pos in ordenar_movimentos(obter_posicoes_adjacentes(pos))\
                if eh_posicao_livre(prado, pos)]
    else:
        posicoes_possiveis = [pos for pos in ordenar_movimentos(obter_posicoes_adjacentes(pos))\
            if eh_posicao_livre(prado, pos)]
    
    if posicoes_possiveis != []:
        return posicoes_possiveis
    return [pos]

def obter_movimento(prado, pos):
    """ obter_movimento: prado × posicao → posicao
    Esta função recebe um prado e uma posição e devolve a posição
    seguinte do animal na posição passada como argumento dentro
    do prado passado como argumento de acordo com as regras de
    movimento dos animais no prado.
    """
    animal = obter_animal(prado,pos)
    posicoes_possiveis = pos_possiveis(prado, pos, animal)
    valor_pos = obter_valor_numerico(prado, pos)
    return posicoes_possiveis[valor_pos%(len(posicoes_possiveis))]

# Funções adicionais

    # Função auxiliar atualiza_animal, ajuda a reduzir a repetição de código na função geracao.

def atualiza_animal(prado, pos, animal):
    """ atualiza_animal: prado × posicao × animal → posicao
    Esta função recebe um prado, uma posição e o animal do
    prado nessa posição e altera destrutivamente o prado,
    atualizando o animal.
    """
    eliminar_animal(prado, pos)
    inserir_animal(prado, animal, pos)

    # Função auxiliar cria_output, ajuda a reduzir a repetição de código na função simula_ecossistema.

def cria_output(prado, gen):
    """ cria_output: prado × int → str
    Esta função recebe um prado e a geração em que este prado
    se encontra e cria o output que lhe corresponde.
    """
    output = "Predadores: " + str(obter_numero_predadores(prado)) + " vs Presas: " + str(obter_numero_presas(prado)) + " (Gen. " + str(gen) + ")\n"
    output += prado_para_str(prado)
    return output

def geracao(prado):
    """ geracao: prado → prado
    Esta função modifica o prado passado como argumento de
    acordo com a evolulção correspondente a uma geração completa.
    """
    pos_animais = obter_posicao_animais(prado)
    pos_eliminadas = []
    for pos in pos_animais:
        if type(index(pos_eliminadas, pos)) == bool:
            animal = obter_animal(prado, pos)
            movimento = obter_movimento(prado, pos)
            aumenta_fome(animal)
            aumenta_idade(animal)
            atualiza_animal(prado, pos, animal)
            if eh_predador(animal):
                if not posicoes_iguais(pos, movimento):
                    if eh_posicao_presa(prado, movimento):
                        eliminar_animal(prado, movimento)
                        reset_fome(animal)
                        atualiza_animal(prado, pos, animal)
                        pos_eliminadas.append(movimento)
                    mover_animal(prado, pos, movimento)
                    if eh_animal_fertil(animal):
                        cria = reproduz_animal(animal)
                        atualiza_animal(prado, movimento, animal)
                        inserir_animal(prado, cria, pos)
                    if eh_animal_faminto(animal):
                        eliminar_animal(prado, movimento)
                else:
                    if eh_animal_faminto(animal):
                        eliminar_animal(prado, pos)
            else:
                if not posicoes_iguais(pos, movimento):
                    mover_animal(prado, pos, movimento)
                    if eh_animal_fertil(animal):
                        cria = reproduz_animal(animal)
                        atualiza_animal(prado, movimento, animal)
                        inserir_animal(prado, cria, pos) 

    return prado

def simula_ecossistema(ficheiro, geracoes, verboso):
    """ geracao: str × int × booleano → tuplo
    Esta função simula o passar das gerações num prado, recebe
    uma cadeia de caracteres que contém o nome de um ficheiro
    com configurações para o prado, um número inteiro que
    corresponde ao número de gerações a simular e um booleano,
    que corresponde à ativação (ou não) do modo verboso.
    """
    with open(ficheiro, 'r') as config:
        lines = config.readlines()

    x = eval(lines[0])[0]
    y = eval(lines[0])[1]
    pos_canto = cria_posicao(x, y)

    obstaculos = eval(lines[1])
    pos_obstaculos = ()
    for t in obstaculos:
        x = t[0]
        y = t[1]
        pos_obstaculos += (cria_posicao(x, y), )
    
    animais = ()
    pos_animais = ()
    for i in range(2, len(lines)):
        animal = eval(lines[i])
        especie = animal[0]
        freq_reproducao = animal[1]
        freq_alimentacao = animal[2]
        x = animal[3][0]
        y = animal[3][1]
        animais += (cria_animal(especie, freq_reproducao, freq_alimentacao),)
        pos_animais += (cria_posicao(x, y),)
    prado = cria_prado(pos_canto, pos_obstaculos, animais, pos_animais)

    print(cria_output(prado, 0))
    for i in range(geracoes):
        prado_passado = cria_copia_prado(prado)
        geracao(prado)
        if verboso and (obter_numero_predadores(prado) != obter_numero_predadores(prado_passado) or obter_numero_presas(prado) != obter_numero_presas(prado_passado)):
            print(cria_output(prado, i + 1))
    
    if not verboso:
        print(cria_output(prado, geracoes))

    return (obter_numero_predadores(prado), obter_numero_presas(prado))