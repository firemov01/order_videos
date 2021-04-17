import os
import datetime
import shutil

nume_videoclipuri = os.listdir()
inceput_facultate = datetime.datetime.strptime('2021-2-8','%Y-%m-%d')
path = os.path.dirname(os.path.abspath(__file__))

def check_para_impara(ziua):
    if (int(str((ziua - inceput_facultate)/7).split(" ")[0])+1)%2==1:
        return False
        # print("saptamana impara")
    else:
        # print("saptamana para")
        return True

def ordonare():
    orar = open("Orar.txt", "r")
    linii  = orar.readlines()
    for x in nume_videoclipuri:
        if ".mp4" in x:
            data_fisier = x.split(' ')[0]
            ora_fisier = int(x.split(' ')[1].split('.')[0].split('-')[0])
            minut_fisier = int(x.split(' ')[1].split('.')[0].split('-')[1])
            timp_fisier = datetime.datetime.strptime(data_fisier, '%Y-%m-%d').strftime('%A')
            zi_fisier = datetime.datetime.strptime(data_fisier, '%Y-%m-%d')
            print(timp_fisier, ' - ' ,ora_fisier,':',minut_fisier)
            for linie in linii:
                ore_curs = linie.split("(")[1].split("-")
                for ora_curs in ore_curs:
                    if linie.split("(")[0] in timp_fisier:
                        if ((int(ora_curs.split("_")[1].split(":")[0])-1==ora_fisier and minut_fisier>=50 and minut_fisier<=59) or (int(ora_curs.split("_")[1].split(":")[0])==ora_fisier and minut_fisier>=0 and minut_fisier<=29)):
                            if ora_curs.split("_")[0]=="M":
                                shutil.move('{}'.format(x),'{}/{}/{}'.format(path, ora_curs.split("_")[2],x))
                                print("{} mutat in {}".format(ora_curs.split("_")[2],x))
                            elif ora_curs.split("_")[0]=="P":
                                if check_para_impara(zi_fisier) == True:
                                    shutil.move('{}'.format(x),'{}/{}/{}'.format(path, ora_curs.split("_")[2],x))
                                    print("{} mutat in {}".format(ora_curs.split("_")[2],x))
                                else:
                                    pass
                            elif ora_curs.split("_")[0]=="I":
                                if check_para_impara(zi_fisier) == False:
                                    shutil.move('{}'.format(x),'{}/{}/{}'.format(path, ora_curs.split("_")[2],x))
                                    print("{} mutat in {}".format(ora_curs.split("_")[2],x))
                                else:
                                    pass
def main():
    ordonare()

if __name__ == "__main__":
    main()


