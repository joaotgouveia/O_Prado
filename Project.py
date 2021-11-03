# 2.1.1 TAD posicao

# Construtores

def cria_posicao(iX, iY):
    if type(iX) != int or type(iY) != int:
        raise ValueError("cria_posicao: argumentos invalidos")
    if iX < 0 or iY < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return (iX, iY)

def cria_copia_posicao(pPosicao):
    return pPosicao

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
    if aAnimal["FreqAlimentacao"] != 0:
        aAnimal["Fome"] = 0
    return aAnimal

# Reconhecedores

def eh_animal(uArg):
    if type(uArg) != dict:
        return False
    if len(uArg) != 5:
        return False
    if not "Especie" in uArg.keys() or "FreqReproducao"in uArg.keys() or "FreqAlimentacao"in uArg.keys() or "Fome"in uArg.keys() or "Idade"in uArg.keys():
        return False
    if type(obter_especie(uArg)) != str or type(obter_freq_reproducao(uArg)) != int or type(obter_freq_alimentacao(uArg)) != int or type(obter_fome(uArg)) != int or type(obter_idade(uArg)) != int:
        return False
    if len(obter_especie(uArg)) == 0:
        return False
    for char in obter_especie(uArg):
        if not char.isalpha():
            return False
    if obter_freq_reproducao(uArg) <= 0 or obter_freq_alimentacao(uArg) <= 0 or obter_fome(uArg) < 0 or obter_idade(uArg) < 0:
        return False
    return True

def eh_predador(aAnimal):
    if obter_freq_alimentacao(aAnimal) != 0:
        return True
    return False

def eh_presa(aAnimal):
    return not eh_predador(aAnimal)

# Teste

def animais_iguais(aAnimal1, aAnimal2):
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
    if obter_freq_alimentacao(aAnimal) <= obter_fome(aAnimal):
        return True
    return False

def reproduz_animal(aAnimal):
    reset_idade(aAnimal)
    return cria_animal(obter_especie(aAnimal), obter_freq_reproducao(aAnimal), obter_freq_alimentacao(aAnimal))

r1 = cria_animal("rabbit", 5, 0)
f1 = cria_animal("fox", 20, 10)
print(animal_para_str(r1))
print(animal_para_str(f1))
print(animal_para_char(r1))
print(animal_para_char(f1))
f2 = cria_copia_animal(f1)
f2 = aumenta_idade(aumenta_idade(f2))
f2 = aumenta_fome(f2)
print(animal_para_str(f1))
print(animal_para_str(f2))
print(animais_iguais(f1, f2))
f3 = reproduz_animal(f2)
print(animal_para_str(f2))
print(animal_para_str(f3))

