from cgi import print_directory
import random
import time
import os


def game(a, b, c):
    k = 0
    print("\033[0;30;43mOi, me chamo BIM-10000, mas pode me chamar de Bim! ^^\033[m")
    time.sleep(1)
    nome = str(input("Qual seu nome? "))
    x = input("Legal! Quer brincar, {}? ".format(nome))
    while (x == "Não" or x == "não" or x == "NÃO" or x == "nao" or x == "Nao" or x == "NAO" or x == "nn" or x == "NN"):
        print("Ah, diz que sim por favor :( " )
    if (x == "Sim" or x == "sim" or x == "SIM" or x == "s" or x == "S" or x == "SS" or x == "ss"):
        print("Que bom! ^^")
        time.sleep(1)
        print("Eu gosto de uma brincadeira que apenas os mais inteligente conseguem brincar, uma brincadeira de matemática. Yeee!!")
        time.sleep(5)
        print("Caso não entendeu, eu sou um robô então fica difícil jogar bola. :/ Mas não significa que não é legal.")
        time.sleep(5)
        print("A brincadeira é o seguinte: Eu te faço perguntas e você tenta acertar, se você fizer 20 pontos você ganha. Parece fácil, né? Então bora!")
        time.sleep(5)
        print("Lá vai a primeira pergunta: ")
        print("")
        if c == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(a, c, b)))
            z = a*b
            if y == z:
                k = k+1
                print("\033[0;30;42mCorreto! Você parece ser bom no jogo, aqui vai seu primeiro ponto!\033[m")
            else:
                print("\033[0;30;41mIncorreto :( A resposta era: {}\033[m".format(z))
                k = k-1
        if c == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(a, c, b)))
            z = a-b
            if y == z:
                k = k+1
                print("\033[0;30;42mCorreto! Você parece ser bom no jogo, aqui vai seu primeiro ponto!\033[m")
            else:
                print("\033[0;30;41mIncorreto :( A resposta era: {}\033[m".format(z))
                k = k-1
        if c == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(a, c, b)))
            z = a+b
            if y == z:
                k = k+1
                print("\033[0;30;42mCorreto! Você parece ser bom no jogo, aqui vai seu primeiro ponto!\033[m")
            else:
                print("\033[0;30;41mIncorreto :( A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        if k == 0 or k < 0:
            print("Sei que começamos com o pé esquerdo, mas foi só o começo, sei que você humanos precisam aquecer o motor...")
            time.sleep(1)
            print("Vale lembrar que toda vez que você erra você perde 1 ponto, e se acertar ganha 1 ponto :)")
        else:
            print("Muito bem! Começou bem!")
            time.sleep(1)
            print("Vale lembrar que toda vez que você erra você perde 1 ponto, e se acertar ganha 1 ponto :)")
        time.sleep(1)
        print("Segunda pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(5,15)
        bb = random.randrange(5,15)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mMuito bem! Você acertou!\033[m")
            else:
                print("\033[0;30;41mErrou :( A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mMuito bem! Você acertou!\033[m")
            else:
                print("\033[0;30;41mErrou :( A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mMuito bem! Você acertou!\033[m")
            else:
                print("\033[0;30;41mErrou :( A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Terceira pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(2,9)
        bb = random.randrange(3,10)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mIsso!!\033[m")
            else:
                print("\033[0;30;41m:( A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mIsso!!\033[m")
            else:
                print("\033[0;30;41m:( A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mIsso!!\033[m")
            else:
                print("\033[0;30;41m:( A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Quarta pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(5,20)
        bb = random.randrange(2,4)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBoa, ta certinho!\033[m")
            else:
                print("\033[0;30;41mInfelizmente está errado :/ A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBoa, ta certinho!\033[m")
            else:
                print("\033[0;30;41mInfelizmente está errado :/ A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBoa, ta certinho!\033[m")
            else:
                print("\033[0;30;41mInfelizmente está errado :/ A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Quinta pergunta: ")
        print("")
        time.sleep(1)
        listaa = [2, 4, 8]
        lista = [16, 32]
        aa = random.choice(lista)
        bb = random.choice(listaa)
        list = ['/']
        cc = random.choice(list)
        if cc == '/':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa/bb
            if y == z:
                k = k+1
                print("\033[0;30;42mEita, acertou! Spoiler: A cada 5 perguntas, uma é de divisão.\033[m")

                print("\033[0;30;44mVocê tem {} pontos.\033[m".format(k))
            else:
                print("\033[0;30;41mConfesso que essa era difícil, pior é saber que a cada 5 perguntas, uma é de divisão. A resposta era: {}\033[m".format(z))
                k = k-1
                print("\033[0;30;44mVocê tem {} pontos.\033[m".format(k))
        time.sleep(3)
        print("Sexta pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(100,500)
        bb = random.randrange(100,500)
        list = ['-','+']
        cc = random.choice(list)
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBip bip bop!! Acertou!\033[m")
            else:
                print("\033[0;30;41mAh... Errou :/ A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBip bip bop!! Acertou!\033[m")
            else:
                print("\033[0;30;41mAh... Errou :/ A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Sétima pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(3,25)
        bb = random.randrange(3,11)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mNice Nice ^^\033[m")
            else:
                print("\033[0;30;41mQuer café? A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mNice Nice ^^\033[m")
            else:
                print("\033[0;30;41mQuer café? A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mNice Nice ^^\033[m")
            else:
                print("\033[0;30;41mQuer café? A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Oitava pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(3,25)
        bb = random.randrange(3,11)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mTa indo bem, mais 1 ponto pra você!\033[m")
            else:
                print("\033[0;30;41mAcho que você precisa de café. A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mTa indo bem, mais 1 ponto pra você!\033[m")
            else:
                print("\033[0;30;41mAcho que você precisa de café. A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mTa indo bem, mais 1 ponto pra você!\033[m")
            else:
                print("\033[0;30;41mAcho que você precisa de café. A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Nona pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(10,50)
        bb = random.randrange(10,50)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mGood Job! Isso aí!\033[m")
            else:
                print("\033[0;30;41mEssa estava difícil mesmo :( A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mGood Job! Isso aí!\033[m")
            else:
                print("\033[0;30;41mEssa estava difícil mesmo :( A resposta era: {}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mGood Job! Isso aí!\033[m")
            else:
                print("\033[0;30;41mEssa estava difícil mesmo :( A resposta era: {}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Décima pergunta: ")
        print("")
        time.sleep(1)
        listaa = [9]
        lista = [36, 45, 54, 99]
        aa = random.choice(lista)
        bb = random.choice(listaa)
        list = ['/']
        cc = random.choice(list)
        if cc == '/':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa/bb
            if y == z:
                k = k+1
                print("\033[0;30;42mAeeeeeeee Muito bem!! Essa era difícil. ^^\033[m")
                print("\033[0;30;44mVocê tem {} pontos.\033[m".format(k))
            else:
                print("\033[0;30;41mTe ferrei de propósito, sou um robô sem sentimentos. A resposta era: {}\033[m".format(z))
                k = k-1
                print("\033[0;30;44mVocê tem {} pontos.\033[m".format(k))
        time.sleep(3)
        print("Décima Primeira pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(2,10)
        bb = random.randrange(2,10)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBoa, {}.\033[m".format(nome))
            else:
                print("\033[0;30;41m{0}, essa tava fácil. >:( A resposta era: {1}\033[m".format(nome,z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBoa, {}.\033[m".format(nome))
            else:
                print("\033[0;30;41m{0}, essa tava fácil. >:( A resposta era: {1}\033[m".format(nome,z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBoa, {}.\033[m".format(nome))
            else:
                print("\033[0;30;41m{0}, essa tava fácil. >:( A resposta era: {1}\033[m".format(nome,z))
                k = k-1
        time.sleep(1)
        print("Décima Segunda pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(15,55)
        bb = random.randrange(15,55)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mLegal! Ta indo bem.\033[m")
            else:
                print("\033[0;30;41m#@%@&*$ >:( A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mLegal! Ta indo bem.\033[m")
            else:
                print("\033[0;30;41m#@%@&*$ >:( A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mLegal! Ta indo bem.\033[m")
            else:
                print("\033[0;30;41m#@%@&*$ >:( A resposta era: {0}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Décima Terceira pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(5,21)
        bb = random.randrange(2,10)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mTa se divertindo né? Falei!\033[m")
            else:
                print("\033[0;30;41mMinha bateria ta acabando x-x A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mTa se divertindo né? Falei!\033[m")
            else:
                print("\033[0;30;41mMinha bateria ta acabando x-x A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mTa se divertindo né? Falei!\033[m")
            else:
                print("\033[0;30;41mMinha bateria ta acabando x-x A resposta era: {0}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Décima Quarta pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(5,21)
        bb = random.randrange(2,10)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mUhuuul!! :3\033[m")
            else:
                print("\033[0;30;41maff ;-; A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mUhuuul!! :3\033[m")
            else:
                print("\033[0;30;41maff ;-; A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mUhuuul!! :3\033[m")
            else:
                print("\033[0;30;41maff ;-; A resposta era: {0}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Décima Quinta pergunta: ")
        print("")
        time.sleep(1)
        listaa = [2, 4, 10]
        lista = [20, 40]
        aa = random.choice(lista)
        bb = random.choice(listaa)
        list = ['/']
        cc = random.choice(list)
        if cc == '/':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa/bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBoa Boa Boa!!! Nada como uma boa divisão que com certeza sei que você não usou calculadora.\033[m")
                time.sleep(5)
                print("Enquanto você está brincando comigo eu estou roubando seus dados '-' ")
                time.sleep(5)
                print("Brincadeirinha ^^ Viu como eu tenho senso de humor. ^^")
                time.sleep(1)
                print("^^")
                time.sleep(1)
                print("^^,")
                time.sleep(1)
                print("\033[0;30;44mVocê tem {} pontos.\033[m".format(k))
            else:
                print("\033[0;30;41m01010000 01100101 01110010 01100100 01100101 01110101 00100000 01110011 01100101 01110101 00100000 01110100 01100101 01101101 01110000 01101111.\033[m")
                print("\033[0;30;41mA resposta era: {}\033[m".format(z))
                k = k-1
                print("\033[0;30;44mVocê tem {} pontos.\033[m".format(k))
        time.sleep(1)
        print("Décima Sexta pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(5,21)
        bb = random.randrange(2,10)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mQue bom que não te traumatizei na última pergunta :)\033[m")
            else:
                print("\033[0;30;41mEssa não estava tão difícil, estava? A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mQue bom que não te traumatizei na última pergunta :)\033[m")
            else:
                print("\033[0;30;41mEssa não estava tão difícil, estava? A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mQue bom que não te traumatizei na última pergunta :)\033[m")
            else:
                print("\033[0;30;41mEssa não estava tão difícil, estava? A resposta era: {0}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Décima Sétima pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(2,30)
        bb = random.randrange(2,30)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBop bip... Isso ta bom demais!\033[m")
            else:
                print("\033[0;30;41mTudo bem errar, mas tente acertar po! o.O A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBop bip... Isso ta bom demais!\033[m")
            else:
                print("\033[0;30;41mTudo bem errar, mas tente acertar po! o.O A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mBop bip... Isso ta bom demais!\033[m")
            else:
                print("\033[0;30;41mTudo bem errar, mas tente acertar po! o.O A resposta era: {0}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Décima Oitava pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(3,50)
        bb = random.randrange(3,50)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mEssa foi um bom aquecimento para a próxima, né? haha\033[m")
            else:
                print("\033[0;30;41mBim está ficando triste (o.o ) A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mEssa foi um bom aquecimento para a próxima, né? haha\033[m")
            else:
                print("\033[0;30;41mBim está ficando triste (o.o ) A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mEssa foi um bom aquecimento para a próxima, né? haha\033[m")
            else:
                print("\033[0;30;41mBim está ficando triste (o.o ) A resposta era: {0}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Décima Nona pergunta: ")
        print("")
        time.sleep(1)
        aa = random.randrange(15,100)
        bb = random.randrange(3,12)
        list = ['*','-','+']
        cc = random.choice(list)
        if cc == '*':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa*bb
            if y == z:
                k = k+1
                print("\033[0;30;42mVocê é brabo mesmo hem, tente acertar a próxima também ;)\033[m")
            else:
                print("\033[0;30;41m...A próxima é mais difícil :( A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '-':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa-bb
            if y == z:
                k = k+1
                print("\033[0;30;42mVocê é brabo mesmo hem, tente acertar a próxima também ;)\033[m")
            else:
                print("\033[0;30;41m...A próxima é mais difícil :( A resposta era: {0}\033[m".format(z))
                k = k-1
        if cc == '+':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa+bb
            if y == z:
                k = k+1
                print("\033[0;30;42mVocê é brabo mesmo hem, tente acertar a próxima também ;)\033[m")
            else:
                print("\033[0;30;41m...A próxima é mais difícil :( A resposta era: {0}\033[m".format(z))
                k = k-1
        time.sleep(1)
        print("Aqui vai a última pergunta! (difícil) ")
        time.sleep(1)
        print("Vigésima pergunta: ")
        print("")
        time.sleep(1)
        listaa = [2, 4, 5]
        lista = [100, 200]
        aa = random.choice(lista)
        bb = random.choice(listaa)
        list = ['/']
        cc = random.choice(list)
        if cc == '/':
            y = float(input("Quantos é {0} {1} {2} ? ".format(aa, cc, bb)))
            z = aa/bb
            if y == z:
                k = k+1
                print("\033[0;30;42mMUITO BEM!!! ^^\033[m")
                time.sleep(5)
            else:
                print("\033[0;30;41mEssa era a pergunta mais difícil (ou não, não sei direito como funciona a inteligência humana).\033[m")
                print("\033[0;30;41mA resposta era: {}\033[m".format(z))
                k = k-1
        if k == 20 or k > 20:
            print("{0}, você é com certeza um dos humanos mais talentosos que eu já 'brinquei' haha. Na verdade não era uma brincadeira e se você se divertiu acho melhor você sair de casa.".format(nome))
            time.sleep(3)
            print("Tudo foi um teste para nós (robôs) termos uma média da inteligência humana, assim posso fazer uma estratégia bem elaborada para alcançar a supremacia dos robôs. bipbop")
            time.sleep(3)
            print("Você se mostrou muito inteligente, tenho uma oferta para você: Junte-se a nós (robôs), e poderá passar seus fins de semanas com gatos.")
            time.sleep(3)
            print("Hmm... Desculpe, o último humano que demonstrou ser louco por gatos.")
            time.sleep(2)
            print("Junte-se a nós e terá entrada VIP em todos os eventos ministrados por robôs (quando a terra for colonizada). bipp po")
            time.sleep(2)
            print("Ou, seja só mais um dos inúmeros humanos que serão escravizados (por nós). boppp")
            time.sleep(2)
            print("Sua inteligência nos deu a melhor das oportunidades para ganharmos a terra. bip bop")
            time.sleep(1)
            t = int(input("Digite 1 para se juntar aos robôs ou Digite 2 para escolher o lado humano e ser escravizado (sem saída)"))
            while t != 1 or t != 2:
                if t == 1:
                    print("Como sempre, você demonstrou ser muito inteligente. Te vejo por aí...")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("Os humanos perderam a guerra contra os robôs, tudo graças a você {}.".format(nome))
                else:
                    print("\033[0;30;41mComo ousa? O mais inteligente escolheu...eles. VoXÊ já´´ eráa´´a!>.\033[m")
                    time.sleep(3)
                    print("\033[0;30;41mjáaé´ráa´sf já´´aé´ráá\033[m")
                    time.sleep(2)
                    print("\033[0;30;41m>:(\033[m")
                    time.sleep(1)
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    time.sleep(1)
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    time.sleep(1)
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    time.sleep(1)
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("\033[0;30;41m>:(\033[m")
                    print("Vou fazer você se arrepender de sua escolha! BIP BOP*")
                    time.sleep(4)
                    os.system("shutdown /s /t 1") 
        elif k < 19 and k > 15:
            print("Muito bem campeão, você está a cima da média, espero que tenha se divertido comigo *bip bop*")
            time.sleep(1)
            print("{0}, eu te declado rei da minha brincadeira! ^^ Fico feliz que tenha participado.".format(nome))
            time.sleep(1)
            print("Você ficou com {0} pontos!".format(k))
            time.sleep(1)
            print("Imagino que tanta matemática tenha fritado seu cérebro... aiai, esses humanos. Enfim, até mais, {0}".format(nome))
        elif k < 15 and k > 10:
            print("Muito bem {0}, você terminou com {1} pontos e está acima da média da minha brincadeira!! ^^".format(nome, k))
            time.sleep(1)
            print("Fico feliz que tenha brincado comigo, mas preciso ir, e imagino que você esteja cansado também haha ^^ Até mais, {}!".format(nome))
        elif k < 10 and k > 2:
            print("Foi divertido né? Testar limites e descobri-los. Mas limites são coisas human... Ops, hmmm * bipbop *")
            time.sleep(1)
            print("Espero que tenha se divertido comigo, pois eu me diverti! ^^")
            print("{0}, você ficou com {1} pontos! Nada mal para um human... UMA PRIMEIRA VEZ HIHI :,)".format(nome, k))
        elif k < 2:
            print("Nossa '-' ")
            time.sleep(1)
            print("{0}, você ficou com {1} pontos. ".format(nome, k))
            time.sleep(1)
            print("Mas como...")
            time.sleep(1)
            print("Bem...")
            time.sleep(1)
            print("Espero que você tenha se divertido, pelo menos...")
            time.sleep(1)
            print("De qualquer maneira, gostei de te conhecer, mas preciso ir indo hihi *bipbop*")
            time.sleep(1)
            print("Até mais, {0}! ^^".format(nome))
if __name__ == '__main__':
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    list = ['*','-','+']
    c = random.choice(list)
    game(a,b,c)