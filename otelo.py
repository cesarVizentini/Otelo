def main():
    TAMANHO =  8   
    BOLA    = 'O'
    XIS     = 'X'
    VAZIA   = '.'
    MOLDURA = '*'
    print ('ESTE É UM JOGO DE OTELO. PODE COMEÇAR!')
    print ()
    tabuleiro = inicialize_tabuleiro()
    exibe_tabuleiro(tabuleiro)
    pontos_x, pontos_o = conta_pontos(tabuleiro)
    print ('"X" tem %d marca(s) no tabuleiro' %(pontos_x))
    print ('"O" tem %d marca(s) no tabuleiro' %(pontos_o))
    print ()
    existe_jogadas = True
    jogador = XIS
    while existe_jogadas:
        if jogador == XIS:
            oponente = BOLA
        else:
            oponente = XIS
        print ("--->  Jogador da vez é '%s'" %(jogador))
        print ()
        existeM_x = existe_movimento(tabuleiro, XIS)
        existeM_o = existe_movimento(tabuleiro, BOLA)
        if not existeM_x and not existeM_o:
            existe_jogadas = False
        if jogador == XIS:
            if existeM_x:
                lin = int(input('Digite a linha da posição em que pretende jogar:'))
                col = int(input('Digite a coluna da posição em que pretende jogar:'))
                print ()
                print ("Jogador 'X' colocou sua marca na posição (%d, %d)." %(lin, col))
                numero_r = numero_reversoes(tabuleiro, jogador, lin, col)
                coloque_reverta_marca(tabuleiro, jogador, lin, col)
                print ("%d '%s'(s) revertido(s) para %s(s)." %(numero_r, oponente, jogador))
                print ()
            else:
                print ("Não há movimento válido para o jogador '%s'" %(jogador))
        if jogador == BOLA:
            if existeM_o:
                numero_r, lin, col = estrategia_jogo(tabuleiro, jogador)
                coloque_reverta_marca(tabuleiro, jogador, lin, col)
                print ("Jogador 'O' colocou sua marca na posiÃ§Ã£o (%d, %d)." %(lin, col))
                print ("%d '%s'(s) revertido(s) para %s(s)." %(numero_r, oponente, jogador))
                print ()
            else:
                print ("Não há movimento válido para o jogador '%s'" %(jogador))
        exibe_tabuleiro(tabuleiro)
        print ()
        pontos_x, pontos_o = conta_pontos(tabuleiro)
        print ("'X' tem %d marca(s) no tabuleiro" %(pontos_x))
        print ("'O' tem %d marca(s) no tabuleiro" %(pontos_o))
        print ()
        jogador = troca_jogador(jogador)
    print ('PARTIDA TERMINADA.')
    print ()
    if pontos_x < pontos_o:
        print ("Jogador 'O' venceu!!!")
    if pontos_x > pontos_o:
        print ("Jogador 'X' venceu!!!")
    if pontos_x == pontos_o:
        print ("Jogadores 'X' e 'O' empataram.")

def cria_matriz(nlin, ncol, valor):
    i = 0
    matriz = []
    while i < nlin:
        j = 0
        linha = []
        while j < ncol:
            linha.append(valor)
            j += 1
        matriz.append(linha)
        i += 1
    return matriz

def inicialize_tabuleiro():
    TAMANHO = 8
    VAZIA = '.'
    matriz = cria_matriz(TAMANHO, TAMANHO, VAZIA)
    MOLDURA = '*'
    i = 0
    tabuleiro = []
    while i < 10:
        j = 0
        linha = []
        while j < 10:
            if i == 0 or i == 9 or j == 0 or j == 9:
                linha.append(MOLDURA)
            else:
                linha.append(matriz[i-1][j-1])
            j += 1
        tabuleiro.append(linha)
        i += 1
    tabuleiro[4][4] = 'O'
    tabuleiro[4][5] = 'X'
    tabuleiro[5][4] = 'X'
    tabuleiro[5][5] = 'O'
    return tabuleiro

def exibe_tabuleiro(tabuleiro):
    TAMANHO = 8
 
    print()
    print('      ', end='')
    i = 1
    while i <= TAMANHO:
        print('   %d  ' %i, end='')
        i += 1
    print()
   
    print('      ', end='')
    i = 1
    while i <= TAMANHO:
        print('+-----', end='')
        i += 1
    print('+')

    i = 1 
    while i <= TAMANHO:
        print('%5d ' %i, end='')
        j = 1
        while j <= TAMANHO:
            print("|  %s  " %(tabuleiro[i][j]), end='')
            j += 1
        print('|')
        
        print('      ', end='')
        j = 1
        while j <= TAMANHO:
            print('+-----', end='')
            j += 1
        print('+')
 
        i += 1

    print()

def numero_reversoes(tabuleiro, jogador, lin, col):
    #conferindo se a jogada é valida:
    if jogador == 'X':
        oponente = 'O'
    else:
        oponente = 'X'
    if lin > 8 or lin < 1 or col > 8 or col < 1:
        return 0
    if tabuleiro[lin][col] == 'X' or tabuleiro[lin][col] == 'O':
        return 0
    reversoes = 0
    #olhando para norte
    reversoes1 = 0
    if tabuleiro[lin - 1][col] == oponente:
        adja = 'norte'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin - 1
            while i > 0 and tabuleiro[i][col] != jogador:
                if tabuleiro[i][col] == oponente:
                    reversoes1 += 1
                i -= 1
    reversoes += reversoes1
    #olhando para nordeste
    reversoes2 = 0
    if tabuleiro[lin - 1][col + 1] == oponente:
        adja = 'nordeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin - 1
            j = col + 1
            while i > 0 and j < 9 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    reversoes2 += 1
                i -= 1
                j += 1
    reversoes += reversoes2
    #olhando para leste
    reversoes3 = 0
    if tabuleiro[lin][col + 1] == oponente:
        adja = 'leste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            j = col + 1
            while j < 9 and tabuleiro[lin][j] != jogador:
                if tabuleiro[lin][j] == oponente:
                    reversoes3 += 1
                j += 1
    reversoes += reversoes3
    #olhando para sudeste
    reversoes4 = 0
    if tabuleiro[lin + 1][col + 1] == oponente:
        adja = 'sudeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin + 1
            j = col + 1
            while i < 9 and j < 9 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    reversoes4 += 1
                i += 1
                j += 1
    reversoes += reversoes4
    #olhando para sul
    reversoes5 = 0
    if tabuleiro[lin + 1][col] == oponente:
        adja = 'sul'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin + 1
            while i < 9 and tabuleiro[i][col] != jogador:
                if tabuleiro[i][col] == oponente:
                    reversoes5 += 1
                i += 1
    reversoes += reversoes5
    #olhando para sudoeste
    reversoes6 = 0
    if tabuleiro[lin + 1][col - 1] == oponente:
        adja = 'sudoeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin + 1
            j = col - 1
            while i < 9 and j > 0 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    reversoes6 += 1
                i += 1
                j -= 1
    reversoes += reversoes6
    #olhando para oeste
    reversoes7 = 0
    if tabuleiro[lin][col - 1] == oponente:
        adja = 'oeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            j = col - 1
            while j > 0 and tabuleiro[lin][j] != jogador:
                if tabuleiro[lin][j] == oponente:
                    reversoes7 += 1
                j -= 1
    reversoes += reversoes7
    #olhando para noroeste
    reversoes8 = 0
    if tabuleiro[lin - 1][col - 1] == oponente:
        adja = 'noroeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin - 1
            j = col - 1
            while i > 0 and j > 0 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    reversoes8 += 1
                i -= 1
                j -= 1
    reversoes += reversoes8
    return reversoes

def existe_movimento(tabuleiro, jogador):
    i = 1
    linm = 9
    colm = 9
    existe_jogada = False
    while i < linm:
        j = 1
        while j < colm:
            if numero_reversoes(tabuleiro, jogador, i, j) > 0:
                existe_jogada = True
            j += 1
        i += 1
    return existe_jogada

def estrategia_jogo(tabuleiro, jogador):
    '''
    *Nesta funÃ§Ã£o, supÃµe-se que jogador Ã© o programa.
    *Obs.: A funÃ§Ã£o pode supor que, quando ela Ã© chamada, existe algum
    movimento vÃ¡lido para jogador.
    '''
    i = 1
    linm = 9
    colm = 9
    m_reversoes = 0
    lin = 0
    col = 0
    while i < linm:
        j = 1
        while j < colm:
            n = numero_reversoes(tabuleiro, jogador, i, j)
            if n > m_reversoes:
                m_reversoes = n
                lin = i
                col = j
            j += 1
        i += 1
    return m_reversoes, lin, col

def coloque_reverta_marca(tabuleiro, jogador, lin, col):
    tabuleiro[lin][col] = jogador
    BOLA    = 'O'
    XIS     = 'X'
    if jogador == XIS:
        oponente = BOLA
    else:
        oponente = XIS
    #olhando para norte
    if tabuleiro[lin - 1][col] == oponente:
        adja = 'norte'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin - 1
            while i > 0 and tabuleiro[i][col] != jogador:
                if tabuleiro[i][col] == oponente:
                    tabuleiro[i][col] = jogador
                i -= 1
    #olhando para nordeste
    if tabuleiro[lin - 1][col + 1] == oponente:
        adja = 'nordeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin - 1
            j = col + 1
            while i > 0 and j < 9 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    tabuleiro[i][j] = jogador
                i -= 1
                j += 1
    #olhando para leste
    if tabuleiro[lin][col + 1] == oponente:
        adja = 'leste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            j = col + 1
            while j < 9 and tabuleiro[lin][j] != jogador:
                if tabuleiro[lin][j] == oponente:
                    tabuleiro[lin][j] = jogador
                j += 1
    #olhando para sudeste
    if tabuleiro[lin + 1][col + 1] == oponente:
        adja = 'sudeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin + 1
            j = col + 1
            while i < 9 and j < 9 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    tabuleiro[i][j] = jogador
                i += 1
                j += 1
    #olhadno para sul
    if tabuleiro[lin + 1][col] == oponente:
        adja = 'sul'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin + 1
            while i < 9 and tabuleiro[i][col] != jogador:
                if tabuleiro[i][col] == oponente:
                    tabuleiro[i][col] = jogador
                i += 1
    #olhando para sudoeste
    if tabuleiro[lin + 1][col - 1] == oponente:
        adja = 'sudoeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin + 1
            j = col - 1
            while i < 9 and j > 0 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    tabuleiro[i][j] = jogador
                i += 1
                j -= 1
    #olhando para oeste
    if tabuleiro[lin][col - 1] == oponente:
        adja = 'oeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            j = col - 1
            while j > 0 and tabuleiro[lin][j] != jogador:
                if tabuleiro[lin][j] == oponente:
                    tabuleiro[lin][j] = jogador
                j -= 1
    #olhando para noroeste
    if tabuleiro[lin - 1][col - 1] == oponente:
        adja = 'noroeste'
        cerco = cerco_ok(tabuleiro, jogador, lin, col, adja)
        if cerco:
            i = lin - 1
            j = col - 1
            while i > 0 and j > 0 and tabuleiro[i][j] != jogador:
                if tabuleiro[i][j] == oponente:
                    tabuleiro[i][j] = jogador
                i -= 1
                j -= 1
                
def troca_jogador(jogador):
    if jogador == 'X':
        jogador_x = True
    else:
        jogador_x = False
    if jogador_x:
        jogador = 'O'
    else:
        jogador = 'X'
    return jogador

def conta_pontos(tabuleiro):
    BOLA    = 'O'
    XIS     = 'X'
    pontos_x = 0
    pontos_o = 0
    i = 1
    while i < 9:
        j = 1
        while j < 9:
            if tabuleiro[i][j] == XIS:
                pontos_x += 1
            if tabuleiro[i][j] == BOLA:
                pontos_o += 1
            j += 1
        i += 1
    return pontos_x, pontos_o

def cerco_ok(tabuleiro, jogador, lin, col, adja):
    lista =[]
    achei_jogador = False
    if adja == 'norte':
        i = lin - 1
        while i > 0 and tabuleiro[i][col] != '.' and not achei_jogador:
            if tabuleiro[i][col] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[i][col])
            i -= 1
    if adja == 'nordeste':
        i = lin - 1
        j = col + 1
        while i > 0 and j < 9 and tabuleiro[i][j] != '.' and not achei_jogador:
            if tabuleiro[i][j] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[i][j])
            i -= 1
            j += 1
    if adja == 'leste':
        j = col + 1
        while j < 9 and tabuleiro[lin][j] != '.' and not achei_jogador:
            if tabuleiro[lin][j] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[lin][j])
            j += 1
    if adja == 'sudeste':
        i = lin + 1
        j = col + 1
        while i < 9 and j < 9 and tabuleiro[i][j] != '.' and not achei_jogador:
            if tabuleiro[i][j] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[i][j])
            i += 1
            j += 1
    if adja == 'sul':
        i = lin + 1
        while i < 9 and tabuleiro[i][col] != '.' and not achei_jogador:
            if tabuleiro[i][col] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[i][col])
            i += 1
    if adja == 'sudoeste':
        i = lin + 1
        j = col - 1
        while i < 9 and j > 0 and tabuleiro[i][j] != '.' and not achei_jogador:
            if tabuleiro[i][j] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[i][j])
            i += 1
            j -= 1
    if adja == 'oeste':
        j = col - 1
        while j > 0 and tabuleiro[lin][j] != '.' and not achei_jogador:
            if tabuleiro[lin][j] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[lin][j])
            j -= 1
    if adja == 'noroeste':
        i = lin - 1
        j = col - 1
        while i > 0 and j > 0 and tabuleiro[i][j] != '.' and not achei_jogador:
            if tabuleiro[i][j] == jogador:
                achei_jogador = True
            lista.append(tabuleiro[i][j])
            i -= 1
            j -= 1
    tamanho = len(lista)
    if lista[tamanho - 1] == jogador:
        return True
    else:
        return False
        
main()
