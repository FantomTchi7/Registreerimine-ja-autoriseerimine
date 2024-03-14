import MuMoodul
nimed,paroolid,emails=MuMoodul.loe_pas_ja_log("konto")
on_autoriseeritud="False"
while True:
    print("0) Näita kontosid.\n1) Loo konto\n2) Logige oma kontole sisse\n3) Muutke parool\n4) Muuda nime\n5) Parooli taastamine\n6) Exit")
    if on_autoriseeritud=="False":
        print("Not logged in.")
    else:
        print("Logged in as",on_autoriseeritud)
    valik=int(input())
    if valik==0:
        print(nimed)
        print(paroolid)
        print(emails)
    elif valik==1:
        MuMoodul.konto_loomine(nimed,paroolid,emails)
        MuMoodul.kirjuta_failisse("konto",nimed,paroolid,emails)
    elif valik==2:
        on_autoriseeritud=MuMoodul.kontole_sisse_logida(nimed,paroolid,on_autoriseeritud)
    elif valik==3:
        MuMoodul.muuda_salasona(nimed,paroolid,emails,on_autoriseeritud)
        MuMoodul.kirjuta_failisse("konto",nimed,paroolid,emails)
    elif valik==4:
        on_autoriseeritud=MuMoodul.muuda_nimi(nimed,paroolid,emails,on_autoriseeritud)
        MuMoodul.kirjuta_failisse("konto",nimed,paroolid,emails)
    elif valik==5:
        MuMoodul.parooli_taastamine(nimed,paroolid,emails,on_autoriseeritud)
        MuMoodul.kirjuta_failisse("konto",nimed,paroolid,emails)
    elif valik==6:
        break