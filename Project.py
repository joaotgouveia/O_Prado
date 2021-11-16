# criar funcao auxiliar para ver se pos esta dentro do prado efetivo, x > 0 e y > 0 (funcao cria_prado, pos_possiveis e eh_prado)
#criar funcao auxiliar para atualizar os bichos do prado (funcao geracao)
#criar funcao auxiliar para sacar as configs do ficheiro (funcao simula_ecossistema)
#criar funcao auxiliar para criar os outputs (funcao simula_ecossistema)

# 2.1.1 TAD posicao

# Construtores

def cria_posicao(iX, iY):
    if type(iX) != int or type(iY) != int:
        raise ValueError("cria_posicao: argumentos invalidos")
    if iX < 0 or iY < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (iX, iY)

def cria_copia_posicao(pPosicao):
    if type(pPosicao) != tuple:
        raise ValueError("cria_copia_posicao: argumento invalido")
    if len(pPosicao) != 2:
        raise ValueError("cria_copia_posicao: argumento invalido")
    return cria_posicao(obter_pos_x(pPosicao), obter_pos_y(pPosicao))

# Seletores

def obter_pos_x(pPosicao):
    return pPosicao[0]

def obter_pos_y(pPosicao):
    return pPosicao[1]

# Reconhecedor

def eh_posicao(uArg):
    if type(uArg) != tuple:
        return False
    if len(uArg) != 2:
        return False
    if type(uArg[0]) != int or type(uArg[1]) != int:
        return False
    if obter_pos_x(uArg) < 0 or obter_pos_y(uArg) < 0:
        return False
    return True

# Teste

def posicoes_iguais(pPosicao1, pPosicao2):
    if obter_pos_x(pPosicao1) != obter_pos_x(pPosicao2) or obter_pos_y(pPosicao1) != obter_pos_y(pPosicao2):
        return False
    return True

# Transformador

def posicao_para_str(pPosicao):
    s = "(" + str(obter_pos_x(pPosicao)) + ", " + str(obter_pos_y(pPosicao)) + ")"
    return s

# Funções de alto nível associadas ao TAD posicao

def obter_posicoes_adjacentes(pPosicao):
    tPosicoesAdjacentes = ()
    if obter_pos_y(pPosicao) != 0:
        tPosicoesAdjacentes += (cria_posicao(obter_pos_x(pPosicao), obter_pos_y(pPosicao) - 1), )
    tPosicoesAdjacentes += (cria_posicao(obter_pos_x(pPosicao) + 1, obter_pos_y(pPosicao)), )
    tPosicoesAdjacentes += (cria_posicao(obter_pos_x(pPosicao), obter_pos_y(pPosicao) + 1), )
    if obter_pos_x(pPosicao) != 0:
        tPosicoesAdjacentes += (cria_posicao(obter_pos_x(pPosicao) - 1, obter_pos_y(pPosicao)), )
    
    return tPosicoesAdjacentes

def ordenar_posicoes(tPosicoes):
    lPosicoes = list(tPosicoes)
    bMudou = True
    # Bubble sort aplicado ao contexto em questão
    while bMudou:
            bMudou = False
            for i in range(len(lPosicoes)-1):
                if obter_pos_y(lPosicoes[i]) > obter_pos_y(lPosicoes[i + 1]):
                    lPosicoes[i], lPosicoes[i + 1] = lPosicoes[i + 1], lPosicoes[i]
                    bMudou = True

    bMudou = True
    # Bubble sort aplicado ao contexto em questão
    while bMudou:
        bMudou = False
        for i in range(len(lPosicoes)-1):
            if obter_pos_y(lPosicoes[i]) == obter_pos_y(lPosicoes[i + 1]):
                if obter_pos_x(lPosicoes[i]) > obter_pos_x(lPosicoes[i + 1]):
                    lPosicoes[i], lPosicoes[i + 1] = lPosicoes[i + 1], lPosicoes[i]
                    bMudou = True

    return tuple(lPosicoes)

# 2.1.2 TAD animal

# Construtores

def cria_animal(sEspecie, iFreqReproducao, iFreqAlimentacao):
    if type(sEspecie) != str or type(iFreqReproducao) != int or type(iFreqAlimentacao) != int:
        raise ValueError("cria_animal: argumentos invalidos")
    if len(sEspecie) < 1 or iFreqReproducao <= 0 or iFreqAlimentacao < 0:
        raise ValueError("cria_animal: argumentos invalidos")
    for char in sEspecie:
        if not char.isalpha():
            raise ValueError("cria_animal: argumentos invalidos")
    return {"Especie": sEspecie, "FreqReproducao": iFreqReproducao, "FreqAlimentacao": iFreqAlimentacao, "Fome": 0, "Idade": 0}

def cria_copia_animal(aAnimal):
    return dict(aAnimal)

# Seletores

def obter_especie(aAnimal):
    return aAnimal["Especie"]

def obter_freq_reproducao(aAnimal):
    return aAnimal["FreqReproducao"]

def obter_freq_alimentacao(aAnimal):
    return aAnimal["FreqAlimentacao"]

def obter_idade(aAnimal):
    return aAnimal["Idade"]

def obter_fome(aAnimal):
    return aAnimal["Fome"]

# Modificadores

def aumenta_idade(aAnimal):
    aAnimal["Idade"] += 1
    return aAnimal

def reset_idade(aAnimal):
    aAnimal["Idade"] = 0
    return aAnimal

def aumenta_fome(aAnimal):
    if aAnimal["FreqAlimentacao"] != 0:
        aAnimal["Fome"] += 1
    return aAnimal

def reset_fome(aAnimal):
    aAnimal["Fome"] = 0
    return aAnimal

# Reconhecedores

def eh_animal(uArg):
    if type(uArg) != dict:
        return False
    if len(uArg) != 5:
        return False
    if not "Especie" in uArg.keys() or not "FreqReproducao" in uArg.keys() or not "FreqAlimentacao" in uArg.keys() or not "Fome" in uArg.keys() or not "Idade"in uArg.keys():
        return False
    if type(obter_especie(uArg)) != str or type(obter_freq_reproducao(uArg)) != int or type(obter_freq_alimentacao(uArg)) != int or type(obter_fome(uArg)) != int or type(obter_idade(uArg)) != int:
        return False
    if len(obter_especie(uArg)) == 0:
        return False
    for char in obter_especie(uArg):
        if not char.isalpha():
            return False
    if obter_freq_reproducao(uArg) <= 0 or obter_freq_alimentacao(uArg) < 0 or obter_fome(uArg) < 0 or obter_idade(uArg) < 0:
        return False
    return True

def eh_predador(aAnimal):
    if not eh_animal(aAnimal):
        return False
    if obter_freq_alimentacao(aAnimal) != 0:
        return True
    return False

def eh_presa(aAnimal):
    if not eh_animal(aAnimal):
        return False
    return not eh_predador(aAnimal)

# Teste

def animais_iguais(aAnimal1, aAnimal2):
    if not eh_animal(aAnimal1) or not eh_animal(aAnimal2):
        return False
    if obter_especie(aAnimal1) != obter_especie(aAnimal2):
        return False
    if obter_freq_reproducao(aAnimal1) != obter_freq_reproducao(aAnimal2):
        return False
    if obter_freq_alimentacao(aAnimal1) != obter_freq_alimentacao(aAnimal2):
        return False
    if obter_idade(aAnimal1) != obter_idade(aAnimal2):
        return False
    if obter_fome(aAnimal1) != obter_fome(aAnimal2):
        return False
    return True

# Transformadores

def animal_para_char(aAnimal):
    if eh_predador(aAnimal):
        return obter_especie(aAnimal)[0].upper()
    return obter_especie(aAnimal)[0].lower()

def animal_para_str(aAnimal):
    sStrAnimal = obter_especie(aAnimal) + " [" + str(obter_idade(aAnimal)) +"/" + str(obter_freq_reproducao(aAnimal))
    if eh_predador(aAnimal):
        return sStrAnimal + ";" + str(obter_fome(aAnimal)) + "/" + str(obter_freq_alimentacao(aAnimal)) + "]"
    return sStrAnimal + "]"

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
        if obter_pos_x(posicao) >= obter_pos_x(pPosicao) or obter_pos_y(posicao) >= obter_pos_y(pPosicao):
            raise ValueError("cria_prado: argumentos invalidos")
        if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0:
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

def eliminar_animal(prPrado, pPosicao):
    lAnimais = list(prPrado["Animais"])
    lPosAnimais = list(prPrado["PosAnimais"])
    del lAnimais[lPosAnimais.index(pPosicao)]
    del lPosAnimais[lPosAnimais.index(pPosicao)]
    prPrado["Animais"] = tuple(lAnimais)
    prPrado["PosAnimais"] = tuple(lPosAnimais)
    return prPrado

def mover_animal(prPrado, pPosAnimal, pPosNova):
    lPosAnimais = list(prPrado["PosAnimais"])
    lPosAnimais[lPosAnimais.index(pPosAnimal)] = pPosNova
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
        if obter_pos_x(posicao) >= obter_pos_x(uArg["PosCanto"]) or obter_pos_y(posicao) >= obter_pos_y(uArg["PosCanto"]):
            return False
        if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0:
           return False
    for animal in uArg["Animais"]:
        if not eh_animal(animal):
            return False
    for posicao in uArg["PosAnimais"]:
        if not eh_posicao(posicao):
            return False
        if obter_pos_x(posicao) >= obter_pos_x(uArg["PosCanto"]) or obter_pos_y(posicao) >= obter_pos_y(uArg["PosCanto"]):
            return False
        if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0:
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
    if obter_pos_x(pPosicao) == 0 or obter_pos_y(pPosicao) == 0:
        return True
    if obter_pos_x(pPosicao) == obter_tamanho_x(prPrado) - 1 or obter_pos_y(pPosicao) == obter_tamanho_y(prPrado) - 1:
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

def geracao(prPrado):
    tPosAnimais = obter_posicao_animais(prPrado)
    lPosEliminadas = []
    for pos in tPosAnimais:
        if not pos in lPosEliminadas:
            aAnimal = obter_animal(prPrado, pos)
            pMovimento = obter_movimento(prPrado, pos)
            aAnimal = aumenta_fome(aAnimal)
            aAnimal = aumenta_idade(aAnimal)
            prPrado = eliminar_animal(prPrado, pos)
            prPrado = inserir_animal(prPrado, aAnimal, pos)
            if eh_predador(aAnimal):
                if not posicoes_iguais(pos, pMovimento):
                    if eh_posicao_presa(prPrado, pMovimento):
                        prPrado = eliminar_animal(prPrado, pMovimento)
                        aAnimal = reset_fome(aAnimal)
                        prPrado = eliminar_animal(prPrado, pos)
                        prPrado = inserir_animal(prPrado, aAnimal, pos)
                        lPosEliminadas.append(pMovimento)
                    prPrado  = mover_animal(prPrado, pos, pMovimento)
                    if eh_animal_fertil(aAnimal):
                        aCria = reproduz_animal(aAnimal)
                        prPrado = eliminar_animal(prPrado, pMovimento)
                        prPrado = inserir_animal(prPrado, aAnimal, pMovimento)
                        prPrado = inserir_animal(prPrado, aCria, pos)
                    if eh_animal_faminto(aAnimal):
                        prPrado = eliminar_animal(prPrado, pMovimento)
                else:
                    if eh_animal_faminto(aAnimal):
                        prPrado = eliminar_animal(prPrado, pos)
            else:
                if not posicoes_iguais(pos, pMovimento):
                    prPrado = mover_animal(prPrado, pos, pMovimento)
                    if eh_animal_fertil(aAnimal):
                        aCria = reproduz_animal(aAnimal)
                        prPrado = eliminar_animal(prPrado, pMovimento)
                        prPrado = inserir_animal(prPrado, aAnimal, pMovimento)
                        prPrado = inserir_animal(prPrado, aCria, pos) 

    return prPrado

def simula_ecossistema(sFicheiro, iNumGeracoes, bVerboso):
    fConfig = open(sFicheiro, 'r')
    fLines = fConfig.readlines()
    sOutput = ""
    sX = ""
    sY = ""
    for i in range(1, len(fLines[0])):
        if fLines[0][i].isnumeric():
            sX += fLines[0][i]
        else:
            iIndiceInicial = i + 2
            break
    
    for i in range(iIndiceInicial, len(fLines[0])):
        if fLines[0][i].isnumeric():
            sY += fLines[0][i]
        else:
            break
    
    pCanto = cria_posicao(int(sX), int(sY))

    tPosObstaculos = ()
    for i in range(1, len(fLines[1])):
        sX = ""
        sY = ""
        if fLines[1][i] == "(":
            for j in range(i + 1, len(fLines[1])):
                if fLines[1][j].isnumeric():
                    sX += fLines[1][j]
                else:
                    iIndiceInicial = j
                    break
    
            for j in range(iIndiceInicial + 2, len(fLines[1])):
                if fLines[1][j].isnumeric():
                    sY += fLines[1][j]
                else:
                    break
        
            tPosObstaculos += (cria_posicao(int(sX), int(sY)), )
    
    tAnimais = ()
    tPosAnimais = ()
    for i in range(2, len(fLines)):
        sEspecie = ""
        sFreqReproducao = ""
        sFreqAlimentacao = ""
        sX = ""
        sY = ""
        for j in range(2, len(fLines[i])):
            if fLines[i][j].isalpha():
                sEspecie += fLines[i][j]
            else:
                iIndiceInicial = j + 3
                break
    
        for j in range(iIndiceInicial, len(fLines[i])):
            if fLines[i][j].isnumeric():
                sFreqReproducao += fLines[i][j]
            else:
                iIndiceInicial = j + 2
                break
        
        for j in range(iIndiceInicial, len(fLines[i])):
            if fLines[i][j].isnumeric():
                sFreqAlimentacao += fLines[i][j]
            else:
                iIndiceInicial = j + 3
                break
        
        for j in range(iIndiceInicial, len(fLines[i])):
            if fLines[i][j].isnumeric():
                sX += fLines[i][j]
            else:
                iIndiceInicial = j + 2
                break
        
        for j in range(iIndiceInicial, len(fLines[i])):
            if fLines[i][j].isnumeric():
                sY += fLines[i][j]
            else:
                break
        
        tAnimais += (cria_animal(sEspecie, int(sFreqReproducao), int(sFreqAlimentacao)),)
        tPosAnimais += (cria_posicao(int(sX), int(sY)),)
    prPrado = cria_prado(pCanto, tPosObstaculos, tAnimais, tPosAnimais)
    sOutput = "Predadores: " + str(obter_numero_predadores(prPrado)) + " vs Presas: " + str(obter_numero_presas(prPrado)) + " (Gen. 0)\n"
    sOutput += prado_para_str(prPrado)
    print(sOutput)

    for i in range(iNumGeracoes):
        prPradoPassado = cria_copia_prado(prPrado)
        prPrado = geracao(prPrado)
        if bVerboso and (obter_numero_predadores(prPrado) != obter_numero_predadores(prPradoPassado) or obter_numero_presas(prPrado) != obter_numero_presas(prPradoPassado)):
            sOutput = "Predadores: " + str(obter_numero_predadores(prPrado)) + " vs Presas: " + str(obter_numero_presas(prPrado)) + " (Gen. " + str(i + 1) + ")\n"
            sOutput += prado_para_str(prPrado)
            print(sOutput)
    
    if not bVerboso:
        sOutput = "Predadores: " + str(obter_numero_predadores(prPrado)) + " vs Presas: " + str(obter_numero_presas(prPrado)) + " (Gen. " + str(iNumGeracoes) + ")\n"
        sOutput += prado_para_str(prPrado)
        print(sOutput)
    
    return (obter_numero_predadores(prPrado), obter_numero_presas(prPrado))

