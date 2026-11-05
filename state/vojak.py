import random

while True:

    zdravi = 100
    zasah = 24
    obvaz = True
    pocet_zasahu = 0

    zabiti_pistoli = 0
    zabiti_mosinem = 0
    zabiti_granatem = 0
    zabiti_airstrikem = 0

    naboje_mosin = 5
    naboje_pistole = 12
    nase_granaty = 1
    nase_dymovnice = 1
    nase_flashbangy = 1
    prebijeni = 0

    killstreak = 0

    dovahkiin = random.randint(1, 3) == 1

    ma_vestu = True
    zivotnost_vesty = random.randint(1, 5)
    print(f"Mám plátovou vestu! Vydrží {zivotnost_vesty} zásahů.")

    kolo = 0
    evakuace = random.randint(10, 16)
    print("Rádio: 'Tady Valkyrie, přilétáme pro tebe. Vydrž!'")

    nepratele = ["odstřelovač", "kulometčík", "granátník"]

    while zdravi > 0:

        kolo += 1
        oslepeni_nepratele = False

        if kolo == 8 and dovahkiin:
            print("\n" + "="*60)
            print("!!! OBLOHA SE ROZTRHLA, PŘILÉTÁ OBŘÍ ČERNÝ DRAK !!!")
            print("Alduin se nadechne... ale něco se v tobě probudí. 🐉")
            print("Máš v sobě dračí krev! Zakřičíš zpátky: 'FUS RO DAH!!!'")
            print("Alduin se zapotácí, zařve a odlétá pryč.")
            print("Rádio: 'Valkyrie volá... vojáku, CO JSI ZAČ?!'")
            print("="*60 + "\n")
            zdravi = 100

        if kolo == 8 and not dovahkiin:
            print("\n" + "="*60)
            print("!!! OBLOHA SE ZATÁHLA A ROZTRHLA !!!")
            print("Rádio: 'Valkyrie volá základnu! Co to sakra je?! To není letadlo, to je obří černý DRAK!!!'")
            print("ALDUIN (Požírač světů) přistál přímo před tebe a zařval: 'FUS RO DAH!'")
            print("Poškození: 9999999 INF")

            zdravi = 0

            print("\n*Obrazovka kompletně zčernala...*")
            print("*Slyšíš drcení dřevěných kol a koňská kopyta...*")
            print("\nRalof: 'Hey you, you're finally awake. You were trying to cross the border, right?'")
            print("Ralof: 'Walked right into that Imperial ambush, same as us, and that thief over there.'")
            print("="*60 + "\n")
            break

        if kolo == evakuace - 5:
            print(">>> Rádio: 'Valkyrie na cestě, ETA 5 kol! Drž pozici!' <<<")

        if kolo == evakuace:
            print(">>> *dum dum dum* Vrtulník přistává! Naskakuju na palubu! <<<")
            if dovahkiin:
                print(">>> Pilot: 'Ten drak... to jsi byl ty?! Sedni si a nic nekřič, prosím.' <<<")
            break

        if prebijeni > 0:
            prebijeni -= 1
            if prebijeni == 0:
                naboje_mosin = 5
                print("*cvak* Mosin nabitý, 5 nábojů v zásobě.")

        if nase_dymovnice > 0 and random.randint(1, 5) == 1:
            nase_dymovnice -= 1
            oslepeni_nepratele = True
            print(f"POOF! Hodil jsi dýmovnici. Nepřátelé tě toto kolo nevidí a nezaútočí! (Zbývá dýmů: {nase_dymovnice})")

        elif nase_flashbangy > 0 and random.randint(1, 5) == 1:
            nase_flashbangy -= 1
            oslepeni_nepratele = True
            print(f"*BLESK-BLESK* Hodil jsi flashbang! Nepřátelé jsou oslepení a toto kolo neútočí! (Zbývá flashbangů: {nase_flashbangy})")

        if random.randint(1, 3) == 1:
            if nase_granaty > 0 and random.randint(1, 4) == 1:
                zbran = "granát"
            else:
                zbran = random.choice(["pistole", "mosin"])

            if zbran == "mosin" and naboje_mosin == 0:
                zbran = "pistole"
            if zbran == "pistole" and naboje_pistole == 0:
                if naboje_mosin > 0 and prebijeni == 0:
                    zbran = "mosin"
                else:
                    zbran = "pěsti"

            nasel_munici = False
            novi_mrtvi = 0

            if zbran == "granát":
                nase_granaty -= 1
                novi_mrtvi = random.randint(1, 3)
                zabiti_granatem += novi_mrtvi
                killstreak += novi_mrtvi
                print(f"KŘUP! Hodil jsem granát a rozmetal {novi_mrtvi} nepřátele! (Zbývá granátů: {nase_granaty}) -> KILLSTREAK: {killstreak}")
                nasel_munici = True

            elif zbran == "pistole":
                naboje_pistole -= 1
                zabiti_pistoli += 1
                killstreak += 1
                novi_mrtvi = 1
                print(f"BUM! Zastřelil jsem nepřítele pistolí! (Náboje: {naboje_pistole}) -> KILLSTREAK: {killstreak}")
                nasel_munici = True

            elif zbran == "mosin":
                naboje_mosin -= 1
                if random.randint(1, 3) == 1:
                    print(f"PRÁSK! ...vedle. (Náboje v Mosinu: {naboje_mosin})")
                else:
                    zabiti_mosinem += 1
                    killstreak += 1
                    novi_mrtvi = 1
                    print(f"PRÁSK! Mosin vyřadil nepřítele na dálku! (Náboje: {naboje_mosin}) -> KILLSTREAK: {killstreak}")
                    nasel_munici = True

                if naboje_mosin == 0:
                    print("Mosin prázdný! Nabíjím po jednom... (3 kola)")
                    prebijeni = 3
            else:
                print("Zkouším střílet, ale nemám munici! Klepám naprázdno!")

            if killstreak >= 10:
                print("\n☢️☢️☢️ !!! NUKE INCOMING !!! ☢️☢️☢️")
                print("Získal jsi 10 kills v řadě a odpaluješ taktickou jadernou bombu! Bojiště je vyhlazeno. INSTA WIN!")
                zabiti_granatem += 100
                break

            elif killstreak >= 5 and novi_mrtvi > 0 and (killstreak - novi_mrtvi < 5):
                mrtvi_airstrikem = random.randint(3, 6)
                zabiti_airstrikem += mrtvi_airstrikem
                killstreak += mrtvi_airstrikem
                print(f"✈️💨 >>> 5 KILLSTREAK: Volám AIRSTRIKE! Stíhačka pokropila bojiště a zabila dalších {mrtvi_airstrikem} nepřátel! -> KILLSTREAK: {killstreak}")

                if killstreak >= 10:
                    print("\n☢️☢️☢️ !!! NUKE INCOMING !!! ☢️☢️☢️")
                    print("Airstrike ti nasbíral dostatek kills na Nukleární bombu! INSTA WIN!")
                    break

            elif killstreak >= 2 and novi_mrtvi > 0 and (killstreak - novi_mrtvi < 2):
                naboje_mosin += 5
                naboje_pistole += 10
                nase_granaty += 1
                nase_dymovnice += 1
                nase_flashbangy += 1
                obvaz = True
                zivotnost_vesty += 3
                ma_vestu = True
                print("📦 >>> 2 KILLSTREAK: Shazuji SUPPLY DROP! Získáváš full munici, dým, flashbang, granát, lékárničku a opravu vesty!")

            if nasel_munici and random.randint(1, 2) == 1:
                loot = random.choice(["mosin", "pistole", "granát", "vesta", "dymovnice", "flashbang"])
                if loot == "mosin":
                    nalezeno = random.randint(1, 3)
                    naboje_mosin += nalezeno
                    print(f"  [LOOT] Prohledal jsem tělo a našel {nalezeno} náboje do Mosinu.")
                elif loot == "pistole":
                    nalezeno = random.randint(3, 8)
                    naboje_pistole += nalezeno
                    print(f"  [LOOT] Sebral jsem mrtvole zásobník s {nalezeno} náboji do pistole.")
                elif loot == "granát":
                    nase_granaty += 1
                    print("  [LOOT] Našel jsem u nepřítele v kapse funkční granát!")
                elif loot == "vesta":
                    novy_plat = random.randint(2, 4)
                    zivotnost_vesty += novy_plat
                    ma_vestu = True
                    print(f"  [LOOT] Našel jsem náhradní plát do vesty! (+{novy_plat} k životnosti, celkem: {zivotnost_vesty})")
                elif loot == "dymovnice":
                    nase_dymovnice += 1
                    print("  [LOOT] Našel jsem dýmovnici.")
                elif loot == "flashbang":
                    nase_flashbangy += 1
                    print("  [LOOT] Našel jsem flashbang.")

        if oslepeni_nepratele:
            continue

        if random.randint(1, 3) == 1:
            print("Uhnul jsem!")
            continue

        pocet_zasahu += 1
        strelec = random.choice(nepratele)
        poskozeni = zasah

        if strelec == "granátník" and random.randint(1, 5) == 1:
            print("Béééé! Granátník místo granátu hodil kozu! Nic se nestalo.")
            continue

        if strelec == "odstřelovač":
            if random.randint(1, 20) == 1:
                print("!!! HEADSHOT !!!")
                zdravi = 0
                break
            poskozeni = zasah * 2

        do_tela = poskozeni

        if ma_vestu and zivotnost_vesty > 0:
            zivotnost_vesty -= 1
            if strelec == "odstřelovač":
                print(f"Odstřelovač prostřelil vestu! (Životnost vesty: {zivotnost_vesty})")
            else:
                print(f"{strelec} trefil vestu! (Životnost vesty: {zivotnost_vesty})")
                do_tela = 0

            if zivotnost_vesty == 0:
                print("!!! Vesta se rozbila !!!")
                ma_vestu = False

        if do_tela > 0:
            if zdravi - do_tela <= 0 and obvaz:
                print("--- Tohle by mě zabilo! Na poslední chvíli používám lékárničku! ---")
                zdravi = 100
                obvaz = False
                killstreak = 0

            else:
                zdravi -= do_tela
                if zdravi < 0:
                    zdravi = 0
                print(f"Au, {strelec}! Zbývá zdraví: {zdravi}")
                killstreak = 0

    if zdravi > 0:
        print("\n--- EVAKUACE ÚSPĚŠNÁ NEBO JADERNÝ TRIUMF ---")
        print(f"Vyhrál jsi! Přežil jsi se {zdravi} zdravím a schytal {pocet_zasahu} zásahů.")
    else:
        print("\n--- KONEC HRY ---")
        print(f"Padl jsem v {kolo}. kole... Schytal jsem {pocet_zasahu} zásahů.")

    celkem_kills = zabiti_pistoli + zabiti_mosinem + zabiti_granatem + zabiti_airstrikem
    print(f"Moje skóre: {zabiti_pistoli} pistolí, {zabiti_mosinem} Mosinem, {zabiti_granatem} granátem, {zabiti_airstrikem} náletem.")
    print(f"Celkem zářezů: {celkem_kills}")

    znovu = input("\nHrát znovu? (a/n): ")
    if znovu != "a":
        print("Díky za hru, vojáku! 🫡")
        break
    print("\n" + "#"*60 + "\n")
