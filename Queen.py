import random
import time

def cakısmaSayısı(eleman):
    cakısmaSayac=0
    for i in range(1,8):
        for j in range(i):
            if( eleman[i]==eleman[j] or abs(eleman[i]-eleman[j]) == i-j ):
                cakısmaSayac+=1
    return cakısmaSayac

def tırman(şimdikiKonum,cakısma):
    mincakısma=cakısma
    minkonum=şimdikiKonum
    for i in range(0,8):
        geçicikonum=şimdikiKonum.copy()
        for j in range(1,9):
            geçicikonum[i]=j
            x=cakısmaSayısı(geçicikonum)
            if(x==0):
                return geçicikonum
            if(x<mincakısma):
                mincakısma=x
                minkonum=geçicikonum.copy()

    return minkonum


def randomkonum():

    rakamlar = [0, 0, 0, 0, 0, 0, 0, 0]
    rakamlar[0] = random.randint(1,8)
    rakamlar[1] = random.randint(1,8)
    rakamlar[2] = random.randint(1,8)
    rakamlar[3] = random.randint(1,8)
    rakamlar[4] = random.randint(1,8)
    rakamlar[5] = random.randint(1,8)
    rakamlar[6] = random.randint(1,8)
    rakamlar[7] = random.randint(1,8)
    return rakamlar

def tahtayıçizdir(konum):

    print("   A  ", "B  ", "C  ", "D  ", "E  ", "F  ", "G  ", "H  ")
    for i in range(8):
        print(8-i,end="| ")
        for j in range(8):
            if(j==konum.index(8-i)):
                if(j!=7):
                    print("Q | ",end="")
                else:
                    print("Q | ")
            else:
                if (j != 7):
                    print("  | ", end="")
                else:
                    print("  | ")
        print("  ---","--- "*7)

def tabloçizdir(yerdeğiştirmeler,restartlar,süreler):
    print("    Yer Değiştirme     Restart          Süre ")
    for i in range(20):
        print(i+1,"       ",yerdeğiştirmeler[i],"             ",restartlar[i],"        ",süreler[i]," ")

    print("ort      ",sum(yerdeğiştirmeler)/20,"          ",sum(restartlar)/20,"        ",sum(süreler)/20)



def main():
    restartlar=[]
    yerdeğiştirmeler=[]
    süreler=[]

    for i in range(20):
        start=time.time()
        konum = randomkonum()
        cakısma = cakısmaSayısı(konum)
        randomrestart = 0
        yerdeğiştirme = 0
        while (cakısma != 0):
            yenikonum = tırman(konum, cakısma)
            if (yenikonum == konum):
                randomrestart += 1
                konum = randomkonum()
                cakısma = cakısmaSayısı(konum)
            else:
                yerdeğiştirme += 1
                konum = yenikonum
                cakısma = cakısmaSayısı(konum)

        finish=time.time()
        süre=finish-start
        süreler.append(süre)

        print(i+1,". döngü sonucu bulunan sonuç: ",konum)
        print("Sonucun Satranç tahtasındaki Gösterimi:")
        tahtayıçizdir(konum)
        print(i+1,". döngüdeki yer değiştirme sayısı: ",yerdeğiştirme)
        print(i+1, ". döngüdeki restart sayısı: ", randomrestart)
        print("-----------------------------------")

        restartlar.append(randomrestart)
        yerdeğiştirmeler.append(yerdeğiştirme)

    tabloçizdir(yerdeğiştirmeler, restartlar, süreler)


main()




