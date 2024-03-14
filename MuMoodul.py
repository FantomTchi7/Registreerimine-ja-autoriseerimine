import string,random,smtplib,ssl,os
from email.message import EmailMessage

# Iseseisevtöö "Registreerimine ja autoriseerimine"

def konto_loomine(nimed:list,paroolid:list,emails:list)->any:
    """Selleks kulub kaks loendit, inimeste paroolid, väljundis redigeeritakse neid ja luuakse kasutaja, kus kasutajal ja paroolil on sama indeks.
    
    :param list nimed: Nimete järjend
    :param list paroolid: Paroolide järjend
    :param list emails: Emailide järjend
    :rtype: list,list,list
    """
    nimi=input("Sisesta nimi: ")
    if nimi in nimed:
        print("Konto on juba olemas.")
    else:
        valik=int(input("1) Sisestage parool ise. 2) Looge juhuslikult parool.\n"))
        if valik==1:
            parool=input("Sisesta parool: ")
        elif valik==2:
            randomparool=list(string.printable)
            random.shuffle(randomparool)
            parool = ''.join([random.choice(randomparool) for x in range(12)])
            print(parool)
            randomparool=list(string.printable)
            random.shuffle(randomparool)
            parool = ''.join([random.choice(randomparool) for x in range(12)])
            print(parool)
        nimed.append(nimi)
        paroolid.append(parool)
        emails.append(input("Sisesta email: "))
        print("Konto loomine õnnestus.")
        print([nimi,parool,emails])
    return nimed,paroolid,emails

def kontole_sisse_logida(nimed:list,paroolid:list,on_autoriseeritud:str)->str:
    """Konto sisselogimise funktsioon kontrollib loendis olevaid kasutajaid, tagastab sisestatud kasutaja nime "on_autoriseeritud".
    
    :param list nimed: Nimete järjend
    :param list paroolid: Paroolide järjend
    :param str on_autoriseeritud: Sisselogitud kasutaja nimi; kui kontole sisselogimist pole, tagastab see "False"
    :rtype: str
    """
    nimi=input("Sisesta nimi: ")
    if not(nimi in nimed):
        print("Selle nimega kontot pole.")
    for i in range(len(nimed)):
        if nimed[i]==nimi:
            parool=input("Sisesta parool: ")
            if paroolid[i]==parool:
                print("Login successful")
                on_autoriseeritud=nimi
            else:
                print("Vale parool.")
    return on_autoriseeritud

def muuda_salasona(nimed:list,paroolid:list,emails:list,on_autoriseeritud:str)->any:
    """Sisselogitud kasutaja parooli muutmine.
    
    :param list nimed: Nimete järjend
    :param list paroolid: Paroolide järjend
    :param list emails: Emailide järjend
    :param str on_autoriseeritud: Kontrollib, kas kasutaja on sisse logitud
    :rtype: list,list,list
    """
    if not(on_autoriseeritud=="False"):
        indeks=nimed.index(on_autoriseeritud)
        parool=input("Sisesta oma parool: ")
        if parool==paroolid[indeks]:
            valik=int(input("1) Sisestage parool ise. 2) Looge juhuslikult parool.\n"))
            if valik==1:
                parool=input("Sisesta uus parool: ")
            elif valik==2:
                randomparool=list(string.printable)
                random.shuffle(randomparool)
                parool = ''.join([random.choice(randomparool) for x in range(12)])
                print(parool)
            nimi=nimed[indeks]
            email=emails[indeks]
            nimed.pop(indeks)
            paroolid.pop(indeks)
            emails.pop(indeks)
            nimed.append(nimi)
            paroolid.append(parool)
            emails.append(email)
        else:
            print("Vale parool.")
    else:
        print("Pole autoriseeritud")
    return nimed,paroolid,emails

def muuda_nimi(nimed:list,paroolid:list,emails:list,on_autoriseeritud:str)->str:
    """Muudab kasutajanime ja lisab selle uusimasse indeksisse. Tagastab uue kasutajanime "on_autoriseritud".
    
    :param list nimed: Nimete järjend
    :param list paroolid: Paroolide järjend
    :param list emails: Emailide järjend
    :param str on_autoriseeritud: Kontrollib, kas kasutaja on sisse logitud
    :rtype: str
    """
    if not(on_autoriseeritud=="False"):
        indeks=nimed.index(on_autoriseeritud)
        parool=input("Sisesta oma parool: ")
        if parool==paroolid[indeks]:
            nimi=input("Sisesta uus nimi: ")
            parool=paroolid[indeks]
            email=emails[indeks]
            paroolid.pop(indeks)
            nimed.pop(indeks)
            emails.pop(indeks)
            nimed.append(nimi)
            paroolid.append(parool)
            emails.append(email)
            on_autoriseeritud=nimi
        else:
            print("Vale parool.")
    else:
        print("Pole autoriseeritud")
    return on_autoriseeritud

def parooli_taastamine(nimed:list,paroolid:list,on_autoriseeritud:str)->any:
    """
    
    :param list nimed: Nimete järjend
    :param list paroolid: Paroolide järjend
    :param str on_autoriseeritud: Kontrollib, kas kasutaja on sisse logitud
    :rtype: list,list
    """
    if not(on_autoriseeritud=="False"):
        valik=int(input("1) Sisestage parool ise. 2) Looge juhuslikult parool.\n"))
        if valik==1:
            parool=input("Sisesta uus parool: ")
        elif valik==2:
            randomparool=list(string.printable)
            random.shuffle(randomparool)
            parool = ''.join([random.choice(randomparool) for x in range(12)])
            print(parool)
        konto=loe_failist("konto")
        print(konto)
        to_email=konto[1]
        smtp_server="smtp.gmail.com"
        port=587
        sender_email=konto[3]
        password=konto[5]
        context=ssl.create_default_context()
        msg=EmailMessage()
        msg.set_content(f"Sinu uus parool on {parool}")
        msg['Subject']="Sinu uus parool!"
        msg['From']=sender_email
        msg['To']=to_email
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(msg)
        except Exception as e:
            print(e)
        finally:
            server.quit()
    else:
        print("Pole autoriseeritud")

def loe_failist(fail:str)->list:
    """Loeme failist read ja salvestame järjendisse. Funktsioon tagastab järjend.

    param str fail:
    :rtype: list
    """
    try:
        f=open(fail,'r',encoding="utf-8")
        järjend=[]
        for rida in f:
            järjend.append(rida.strip())
        f.close()
    except Exception as e:
        print(e)
    return järjend

def loe_pas_ja_log(fail:str)->any:
    """Loeb failist andmed, mis oli sisestatud formaadis "login:password:email" igas reas eraldi
    """
    fail=open(fail,"r",encoding="utf-8")
    log=[]
    pas=[]
    mail=[]
    for line in fail:
        n=line.find(":")
        p=line.find("|")
        log.append(line[0:n].strip())
        pas.append(line[n+1:p].strip())
        mail.append(line[p+1:len(line)].strip())
    fail.close()
    return log,pas,mail

def kirjuta_failisse(fail:str,nimed:list,paroolid:list,emails:list,jarjend=[]):
    """Funktsioon ümberkirjustab andmefailis.
    
    param int n: Elemendi number
    param str fail:
    param list jarjend:
    """
    jarjend=[]
    n,p,e=loe_pas_ja_log("konto")
    for i in range(len(n)):
        jarjend.append(f"{n[i]}:{p[i]}|{e[i]}")
    f=open(fail,'w',encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()