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
    return tuple(pos)

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
    """eh_animal: universal → booleano
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

def eh_animal_fertil(aAnimal):
    if obter_freq_reproducao(aAnimal) <= obter_idade(aAnimal):
        return True
    return False

def eh_animal_faminto(aAnimal):
    if eh_presa(aAnimal):
        return False
    if obter_freq_alimentacao(aAnimal) == obter_fome(aAnimal):
        return True
    return False

def reproduz_animal(aAnimal):
    reset_idade(aAnimal)
    return cria_animal(obter_especie(aAnimal), obter_freq_reproducao(aAnimal), obter_freq_alimentacao(aAnimal))

# TAD prado

# Construtores

def prado_efetivo(pPosCanto, pPos):
    if obter_pos_x(pPos) >= obter_pos_x(pPosCanto) or obter_pos_y(pPos) >= obter_pos_y(pPosCanto):
        return False
    if obter_pos_x(pPos) == 0 or obter_pos_y(pPos) == 0:
        return False
    return True

def cria_prado(pPosicao, tPosObstaculos, tAnimais, tPosAnimais):
    if not eh_posicao(pPosicao):
        raise ValueError("cria_prado: argumentos invalidos")
    if type(tPosObstaculos) != tuple or type(tAnimais) != tuple or type(tPosAnimais) != tuple:
        raise ValueError("cria_prado: argumentos invalidos")
    for posicao in tPosObstaculos:
        if not eh_posicao(posicao):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(posicao) >= obter_pos_x(pPosicao) or obter_pos_y(posicao) >= obter_pos_y(pPosicao):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0:
            raise ValueError("cria_prado: argumentos invalidos")
    if len(tAnimais) != len(tPosAnimais):
        raise ValueError("cria_prado: argumentos invalidos")
    for animal in tAnimais:
        if not eh_animal(animal):
            raise ValueError("cria_prado: argumentos invalidos")
    for posicao in tPosAnimais:
        if not eh_posicao(posicao):
            raise ValueError("cria_prado: argumentos invalidos")
        if not prado_efetivo(pPosicao, posicao):
            raise ValueError("cria_prado: argumentos invalidos")
    
    return {"PosCanto": pPosicao, "PosObstaculos": tPosObstaculos, "Animais": tAnimais, "PosAnimais": tPosAnimais}

def cria_copia_prado(prPrado):
    return dict(prPrado)

# Seletores

def obter_tamanho_x(prPrado):
    return obter_pos_x(prPrado["PosCanto"]) + 1 

def obter_tamanho_y(prPrado):
    return obter_pos_y(prPrado["PosCanto"]) + 1

def obter_numero_predadores(prPrado):
    iNumPredadores = 0
    for animal in prPrado["Animais"]:
        if eh_predador(animal):
            iNumPredadores += 1
    return iNumPredadores

def obter_numero_presas(prPrado):
    iNumPresas = 0
    for animal in prPrado["Animais"]:
        if eh_presa(animal):
            iNumPresas += 1
    return iNumPresas

def obter_posicao_animais(prPrado):
    return ordenar_posicoes(prPrado["PosAnimais"])

def obter_animal(prPrado, pPosicao):
    for i in range(len(prPrado["PosAnimais"])):
        if posicoes_iguais(prPrado["PosAnimais"][i], pPosicao):
            return prPrado["Animais"][i]

# Modificadores

def index(lPos, pPos):
    for i in range(len(lPos)):
        if posicoes_iguais(lPos[i], pPos):
            return i
    return False

def eliminar_animal(prPrado, pPosicao):
    lAnimais = list(prPrado["Animais"])
    lPosAnimais = list(prPrado["PosAnimais"])
    i = index(lPosAnimais, pPosicao)
    del lAnimais[i]
    del lPosAnimais[i]
    prPrado["Animais"] = tuple(lAnimais)
    prPrado["PosAnimais"] = tuple(lPosAnimais)
    return prPrado

def mover_animal(prPrado, pPosAnimal, pPosNova):
    lPosAnimais = list(prPrado["PosAnimais"])
    i = index(lPosAnimais, pPosAnimal)
    lPosAnimais[i] = pPosNova
    prPrado["PosAnimais"] = tuple(lPosAnimais)
    return prPrado

def inserir_animal(prPrado, aAnimal, pPosicao):
    prPrado["Animais"] += (cria_copia_animal(aAnimal), )
    prPrado["PosAnimais"] += (cria_copia_posicao(pPosicao), )
    return prPrado

# Reconhecedores

def eh_prado(uArg):
    if type(uArg) != dict:
        return False
    if len(uArg) != 4:
        return False
    if not "PosCanto" in uArg.keys() or not "PosObstaculos" in uArg.keys() or not "Animais" in uArg.keys() or not "PosAnimais" in uArg.keys():
        return False
    if not eh_posicao(uArg["PosCanto"]):
        return False
    if type(uArg["PosObstaculos"]) != tuple or type(uArg["Animais"]) != tuple or type(uArg["PosAnimais"]) != tuple:
        return False
    if len(uArg["Animais"]) != len(uArg["PosAnimais"]):
        return False
    
    for posicao in uArg["PosObstaculos"]:
        if not eh_posicao(posicao):
            return False
        if not prado_efetivo(uArg["PosCanto"], posicao):
            return False
    for animal in uArg["Animais"]:
        if not eh_animal(animal):
            return False
    for posicao in uArg["PosAnimais"]:
        if not eh_posicao(posicao):
            return False
        if not prado_efetivo(uArg["PosCanto"], posicao):
            return False

    for posicao in uArg["PosObstaculos"]:
        for pos in uArg["PosAnimais"]:
            if posicoes_iguais(posicao, pos):
                return False
    return True

def eh_posicao_animal(prPrado, pPosicao):
    for posicao in obter_posicao_animais(prPrado):
        if posicoes_iguais(posicao, pPosicao):
            return True
    return False

def eh_posicao_obstaculo(prPrado, pPosicao):
    if not prado_efetivo(cria_posicao(obter_tamanho_x(prPrado) - 1, obter_tamanho_y(prPrado) - 1), pPosicao):
            return True
    for posicao in prPrado["PosObstaculos"]:
        if posicoes_iguais(posicao, pPosicao):
            return True
    return False

def eh_posicao_livre(prPrado, pPosicao):
    if eh_posicao_animal(prPrado, pPosicao) or eh_posicao_obstaculo(prPrado, pPosicao):
        return False
    return True

# Teste

def prados_iguais(prPrado1, prPrado2):
    
    if len(obter_posicao_animais(prPrado1)) != len(obter_posicao_animais(prPrado2)):
        return False
    for i in range(len(obter_posicao_animais(prPrado1))):
        if not posicoes_iguais(obter_posicao_animais(prPrado1)[i], obter_posicao_animais(prPrado2)[i]):
            return False
    
    if len(prPrado1["PosObstaculos"]) != len(prPrado2["PosObstaculos"]):
        return False
    for i in range(len(prPrado1["PosObstaculos"])):
        if not posicoes_iguais(prPrado1["PosObstaculos"][i], prPrado2["PosObstaculos"][i]):
            return False

    for i in range(len(obter_posicao_animais(prPrado1))):
        if not animais_iguais(obter_animal(prPrado1,obter_posicao_animais(prPrado1)[i]), obter_animal(prPrado2,obter_posicao_animais(prPrado2)[i])):
            return False
    
    if not posicoes_iguais(prPrado1["PosCanto"], prPrado2["PosCanto"]):
        return False
    return True

# Transformador

def prado_para_str(prPrado):
    lMatrizPrado = [[] for y in range(obter_tamanho_y(prPrado))]
    sPrado = ""
    lMatrizPrado[0] = ["-" for x in range(obter_tamanho_x(prPrado))]
    lMatrizPrado[0][0] = "+"
    lMatrizPrado[0][-1] = "+"
    lMatrizPrado[-1] = lMatrizPrado[0]

    for y in range(1, len(lMatrizPrado) - 1):
        lMatrizPrado[y].append("|")
        for x in range(1,obter_tamanho_x(prPrado) - 1):
            if eh_posicao_livre(prPrado, cria_posicao(x,y)):
                lMatrizPrado[y].append(".")
            elif eh_posicao_obstaculo(prPrado, cria_posicao(x,y)):
                lMatrizPrado[y].append("@")
            else:
                lMatrizPrado[y].append(animal_para_char(obter_animal(prPrado, cria_posicao(x,y))))
        lMatrizPrado[y].append("|")
    
    for y in range(len(lMatrizPrado)):
        for char in lMatrizPrado[y]:
            sPrado += str(char)
        sPrado += "\n"

    return sPrado.rstrip("\n")

# Funções de alto nível associadas ao TAD prado

def obter_valor_numerico(prPrado, pPosicao):
    return obter_tamanho_x(prPrado)*obter_pos_y(pPosicao) + obter_pos_x(pPosicao)

def eh_posicao_presa(prPrado, pPosicao):
    if eh_posicao_animal(prPrado, pPosicao):
        if eh_presa(obter_animal(prPrado, pPosicao)):
            return True
    return False

def ordenar_movimentos(tPosicoes):
    lPosicoes = list(tPosicoes)
    bMudou = True
    # Bubble sort aplicado ao contexto em questão
    while bMudou:
        bMudou = False
        for i in range(len(lPosicoes) - 1):
            if obter_pos_y(lPosicoes[i]) > obter_pos_y(lPosicoes[i + 1]):
                lPosicoes[i], lPosicoes[i + 1] = lPosicoes[i + 1], lPosicoes[i]
                bMudou = True

    bMudou = True
    while bMudou:
        bMudou = False
        for i in range(1, len(lPosicoes) - 1):
            if obter_pos_x(lPosicoes[i]) < obter_pos_x(lPosicoes[i + 1]):
                lPosicoes[i], lPosicoes[i + 1] = lPosicoes[i + 1], lPosicoes[i]
                bMudou = True
    return lPosicoes

def pos_possiveis(prPrado, pPosicao, aAnimal):
    if eh_predador(aAnimal):
        lPosPossiveis = [pos for pos in ordenar_movimentos(obter_posicoes_adjacentes(pPosicao))\
            if eh_posicao_presa(prPrado, pos)]
        if lPosPossiveis == []:
            lPosPossiveis = [pos for pos in ordenar_movimentos(obter_posicoes_adjacentes(pPosicao))\
                if eh_posicao_livre(prPrado, pos)]
    else:
        lPosPossiveis = [pos for pos in ordenar_movimentos(obter_posicoes_adjacentes(pPosicao))\
            if eh_posicao_livre(prPrado, pos)]
    
    if lPosPossiveis != []:
        return lPosPossiveis
    return [pPosicao]

def obter_movimento(prPrado, pPosicao):
    aAnimal = obter_animal(prPrado,pPosicao)
    lPosPossiveis = pos_possiveis(prPrado, pPosicao, aAnimal)
    iValorPos = obter_valor_numerico(prPrado, pPosicao)
    return lPosPossiveis[iValorPos%(len(lPosPossiveis))]

# Funções adicionais

def atualiza_animal(prPrado, pPos, aAnimal):
    eliminar_animal(prPrado, pPos)
    inserir_animal(prPrado, aAnimal, pPos)

def cria_output(prPrado, iGen):
    sOutput = "Predadores: " + str(obter_numero_predadores(prPrado)) + " vs Presas: " + str(obter_numero_presas(prPrado)) + " (Gen. " + str(iGen) + ")\n"
    sOutput += prado_para_str(prPrado)
    return sOutput

def le_ficheiro(sLine, iInicial, bAlpha):
    sInf = ""
    if bAlpha:
        for j in range(iInicial, len(sLine)):
            if sLine[j].isalpha():
                sInf += sLine[j]
            else:
                iIndice = j
                break
    else:
        for j in range(iInicial, len(sLine)):
            if sLine[j].isnumeric():
                sInf += sLine[j]
            else:
                iIndice = j
                break
    return sInf, iIndice

def geracao(prPrado):
    tPosAnimais = obter_posicao_animais(prPrado)
    lPosEliminadas = []
    for pos in tPosAnimais:
        if type(index(lPosEliminadas, pos)) == bool:
            aAnimal = obter_animal(prPrado, pos)
            pMovimento = obter_movimento(prPrado, pos)
            aumenta_fome(aAnimal)
            aumenta_idade(aAnimal)
            atualiza_animal(prPrado, pos, aAnimal)
            if eh_predador(aAnimal):
                if not posicoes_iguais(pos, pMovimento):
                    if eh_posicao_presa(prPrado, pMovimento):
                        eliminar_animal(prPrado, pMovimento)
                        reset_fome(aAnimal)
                        atualiza_animal(prPrado, pos, aAnimal)
                        lPosEliminadas.append(pMovimento)
                    prPrado  = mover_animal(prPrado, pos, pMovimento)
                    if eh_animal_fertil(aAnimal):
                        aCria = reproduz_animal(aAnimal)
                        atualiza_animal(prPrado, pMovimento, aAnimal)
                        inserir_animal(prPrado, aCria, pos)
                    if eh_animal_faminto(aAnimal):
                        eliminar_animal(prPrado, pMovimento)
                else:
                    if eh_animal_faminto(aAnimal):
                        eliminar_animal(prPrado, pos)
            else:
                if not posicoes_iguais(pos, pMovimento):
                    mover_animal(prPrado, pos, pMovimento)
                    if eh_animal_fertil(aAnimal):
                        aCria = reproduz_animal(aAnimal)
                        atualiza_animal(prPrado, pMovimento, aAnimal)
                        inserir_animal(prPrado, aCria, pos) 

    return prPrado

def simula_ecossistema(sFicheiro, iNumGeracoes, bVerboso):
    fConfig = open(sFicheiro, 'r')
    lLines = fConfig.readlines()

    sX = le_ficheiro(lLines[0], 1, False)[0]
    iIndiceInicial =  le_ficheiro(lLines[0], 1, False)[1]
    sY = le_ficheiro(lLines[0], iIndiceInicial + 2, False)[0]
    pCanto = cria_posicao(int(sX), int(sY))

    tPosObstaculos = ()
    for i in range(1, len(lLines[1])):
        sX = ""
        sY = ""
        if lLines[1][i] == "(":
            sX = le_ficheiro(lLines[1], i + 1, False)[0]
            iIndiceInicial = le_ficheiro(lLines[1], i + 1, False)[1]
            sY = le_ficheiro(lLines[1], iIndiceInicial + 2, False)[0]
            tPosObstaculos += (cria_posicao(int(sX), int(sY)), )
    
    tAnimais = ()
    tPosAnimais = ()
    for i in range(2, len(lLines)):
        sEspecie = le_ficheiro(lLines[i], 2, True)[0]
        iIndiceInicial = le_ficheiro(lLines[i], 2, True)[1]
        sFreqReproducao = le_ficheiro(lLines[i], iIndiceInicial + 3, False)[0]
        iIndiceInicial = le_ficheiro(lLines[i], iIndiceInicial + 3, False)[1]
        sFreqAlimentacao = le_ficheiro(lLines[i], iIndiceInicial + 2, False)[0]
        iIndiceInicial = le_ficheiro(lLines[i], iIndiceInicial + 2, False)[1]
        sX = le_ficheiro(lLines[i], iIndiceInicial + 3, False)[0]
        iIndiceInicial= le_ficheiro(lLines[i], iIndiceInicial + 3, False)[1]
        sY = le_ficheiro(lLines[i], iIndiceInicial + 2, False)[0]
        tAnimais += (cria_animal(sEspecie, int(sFreqReproducao), int(sFreqAlimentacao)),)
        tPosAnimais += (cria_posicao(int(sX), int(sY)),)
    prPrado = cria_prado(pCanto, tPosObstaculos, tAnimais, tPosAnimais)

    print(cria_output(prPrado, 0))
    for i in range(iNumGeracoes):
        prPradoPassado = cria_copia_prado(prPrado)
        prPrado = geracao(prPrado)
        if bVerboso and (obter_numero_predadores(prPrado) != obter_numero_predadores(prPradoPassado) or obter_numero_presas(prPrado) != obter_numero_presas(prPradoPassado)):
            print(cria_output(prPrado, i + 1))
    
    if not bVerboso:
        print(cria_output(prPrado, iNumGeracoes))

    return (obter_numero_predadores(prPrado), obter_numero_presas(prPrado))