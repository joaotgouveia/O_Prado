# 2.1.1 TAD posicao

# Construtores

def cria_posicao(iX, iY):
    if type(iX) != int or type(iY) != int:
        raise ValueError("cria_posicao: argumentos invalidos")
    if iX < 0 or iY < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (iX, iY)

def cria_copia_posicao(pPosicao):
    if eh_posicao(pPosicao):
        return cria_posicao(obter_pos_x(pPosicao), obter_pos_y(pPosicao))
    raise ValueError("cria_copia_posicao: argumentos invalidos")


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
    iIntervalo = len(tPosicoes) // 2
    bMudou = True
    # Ordenamento Shell
    while iIntervalo != 0:
        while bMudou:
            bMudou = False
            for i in range(len(lPosicoes)-iIntervalo):
                if obter_pos_y(lPosicoes[i]) > obter_pos_y(lPosicoes[i + iIntervalo]):
                    lPosicoes[i], lPosicoes[i + iIntervalo] = lPosicoes[i + iIntervalo], lPosicoes[i]
                    bMudou = True
                if obter_pos_y(lPosicoes[i]) == obter_pos_y(lPosicoes[i + iIntervalo]):
                    if obter_pos_x(lPosicoes[i]) > obter_pos_x(lPosicoes[i + iIntervalo]):
                        lPosicoes[i], lPosicoes[i + iIntervalo] = lPosicoes[i + iIntervalo], lPosicoes[i]
                        bMudou = True
        iIntervalo //= 2
    
    return tuple(lPosicoes)
