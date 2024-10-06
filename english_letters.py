import random

letters = [["branches", "gałęzie"], ["whether", "czy"], ["substitute", "zastąpić"], ["semicolon", "średnik"], ["colon", "dwukropek"], ["slash", "ukośnik"], ["combine", "połączyć"], ["compare", "porównać"], ["scope", "zakres"], ["ternary", "trójskładnikowy"], ["advantage", "korzyść"], ["evaluation", "ocena"], ["currency", "waluta"],
["tie", ["krawat", "remis"]], ["reuse", "ponowne użycie"], ["execute", "wykonać"], ["tabs", "zakładki"], ["comma", "przecinek"], ["associated", "powiązany"], ["template", "szablon"], ["insert", "wstawić"], ["overwrite", "nadpisać"], ["square brackets", "nawiasy kwadratowe"], ["curly brackets", "nawiasy klamrowe"], ["nested", "zagnieżdżony"],
["provide", "dostarczać"], ["built-in", "wbudowany"], ["store", "przechowywać"], ["permanently", "na stałe"], ["temporary", "tymczasowy"], ["dash", "myślnik"], ["assign", "przypisać"], ["reassign", "ponownie przypisać"], ["truthy", "prawdziwy"], ["falsely", "fałszywy"], ["inherit", "dziedziczyć"], ["linked", "połączony"], ["injected", "wstrzyknięty"],
["otherwise", "w przeciwnym razie"], ["coercion", "przymus"], ["further", "dalej"], ["overcome", "pokonać"], ["several", "kilka"], ["range", "rozpiętość"], ["as well", "również"], ["typing", "pisanie"], ["void", "pusty"], ["so far", "dotychczas"], ["in due", "we właściwym czasie"], ["equal", "równa się"], ["consecutive", "kolejny"], ["instantly", "natychmiast"],
["pattern", "wzór"], ["above", "powyżej"], ["justify", "uzasadnić"], ["adjustment", "modyfikacja"], ["stretch", "rozciągać się"], ["remainder", "reszta"], ["walkthrough", "solucja"], ["hoisting", "podnoszenie"], ["immediately", "bezpośrednio"], ["bash", "grzmotnąć"], ["bashful", "wstydliwy"], ["struggle", "walka"], ["bred", "wychowany"], ["raise", ["wychować", "wznosić"]],
["involve", "zaangażowany"], ["conquering", "zdobywanie"], ["constrains", "ograniczenia"], ["pressure", "ciśnienie"], ["disposing", "utylizacja"], ["income", "dochód"], ["bodily fluids", "płyny ustrojowe"], ["internal", "wewnętrzny"], ["rendering", "czynić"], ["capacity", "pojemność"], ["distinct", "odrębny"], ["diverse", "różnorodny"], ["creepvine", "pełzający"],
["environment", "środowisko"], ["blow up", "wysadzić"], ["shallow", "płytki"], ["sparse", "rzadki"], ["wave", "fala"], ["flow", "przepływ"], ["humiliating", "poniżający"], ["delay", "opóźnienie"], ["immediate", "natychmiast"], ["multiply", "pomnożyć"], ["closure", "zamknięcie"], ["enclosed", "załączenie"], ["ensure", "zapewnić"], ["thoroughly", "dokładnie"], ["examine", "zbadać"],
["contribute", "brać udział"], ["suspended", "zawieszony"], ["recharge", "naładować"], ["track", "śledzić"], ["underscore", "podkreślnik"], ["exclamation mark", "wykrzyknik"], ["mention", "wzmianka"], ["undo", "cofnąć"], ["directly", "bezpośrednio"], ["inner", "wewnętrzny"], ["intermediate", "pośredni"], ["template string", "ciąg szablonowy"], ["decimal", "dziesiętny"],
["commit", "popełnić"], ["commit on", "zobowiązać się"], ["relate", "odnieść się"], ["attach", "dołączyć"], ["syntax", "składnia"], ["particular", "konkretny"], ["inspect", "sprawdzać"], ["facility", "obiekt"], ["resolution", "rezolucja"], ["breaker room", "pokój wyłącznika"], ["rather", "raczej"], ["beside it", "poza tym"], ["along", "wzdłuż"], ["summary", "streszczenie"],
["utils", "użytkowe"], ["senses", "zmysły"], ["sensitive", "wrażliwe"], ["so you can", "więc możesz"], ["assembled", "zmontowane"], ["pollution", "zanieczyszczenie"], ["external", "zewnętrzny"], ["actions", "czyny"], ["the one", "ten"], ["shift", "zmiana"], ["whistleblower", "informator"], ["wardrobe", "szafa"], ["spyglass", "luneta"], ["drawer", "szuflada"], ["stand out", "wyróżniać się"],
["coil", ["cewka", "zwój"]], ["wedding", "ślub"], ["wire", "drut"], ["mess", "bałagan"], ["messed", ["zepsute", "namieszać"]], ["device", "urządzenie"], ["feel free", "nie krępuj się"], ["firmware", "oprogramowanie"], ["according", "według"], ["healthy habits", "zdrowe nawyki"], ["strict", "wymagający"], ["check out", "wymeldować się"], ["either", "też"], ["accompany", "odprowadzić"],
["pull", "ciągnąć"], ["got under his skin", "zalazło mu za skórę"], ["reluctantly", "niechętnie"], ["subtract", "odejmować"], ["by", "za"], ["refuse", "odmawiać"], ["blanket", "koc"], ["literally", "dosłownie"], ["remains", "pozostaje"], ["commonly", "powszechnie"], ["regretted", "żałowałem"], ["thanks for reaching out", "dziękuję za kontakt"], ["regarding", "w sprawie"], ["certain", "pewien"],
["valuable", "wartościowe"], ["hence", "stąd"], ["exact", "dokładny"], ["approach", "podejście"], ["deprecated", "przestarzałe"], ["catcher", "łapacz"], ["capture", "schwytać"], ["subfield", "podpole"], ["hilarious", "zabawne"], ["jealous", "zazdrosny"], ["boarding pass", "karta pokładowa"], ["cord", "przewód"], ["neat", "czystą"], ["lot", "działka"], ["obtained", "uzyskany"], ["below", "poniżej"],
["wont mind", "nie mieć nic przeciwko"], ["catch", "zrozumieć"], ["twin primes", "liczby pierwsze"], ["disadvantages", "niedogodności"], ["to stage", "przedstawić"], ["aborts", "przerywa"], ["tricky", "zdradliwy"], ["suite", "zestaw"], ["execution policy", "polityka wykonania"], ["release", "uwolnienie"], ["recently", "ostatnio"], ["though", "chociaż"], ["expect", "oczekiwać"], ["approved", "zatwierdzony"],
["spreadsheet", "arkusz"], ["is meant", "jest przeznaczony"], ["on the other hand", "z drugiej strony"], ["supposedly", "rzekomo"], ["exhausted", "wyczerpany"], ["motion", "ruch"], ["bear with me", "proszę o chwile cierpliwości"], ["bug", "robak"], ["accurate", "dokładny"], ["augmentation", "powiększenie"], ["blueprint", "projekt"], ["certainly", "z pewnością"], ["straight", "prosty"], ["outer", "zewnętrzny"],
["beyond", "poza"], ["comprehension", "zrozumienie"], ["amalgamations", "połączenie"], ["prophet", "prorok"], ["unleashed", "uwolniony"], ["hang out", "spędzać"], ["mocked", "wyśmiewany"], ["at some point", "w pewnym momencie"], ["spy", "szpieg"], ["spy on", "szpiegować"], ["entities", "podmioty"], ["species", "gatunek"], ["broadcast", "audycja"], ["intended", "przeznaczony"], ["assessment", "ocena"], ["resemblance", "podobieństwo"],
["weaponry", "broń"], ["in mind", "w zamyśle"], ["precaution", "środki ostrożności"], ["rifle", "karabin"], ["rusty", ["zardzewiały", "zaniedbały"]], ["malfunctioned", "niesprawny"], ["entire", "cały"], ["query", "zapytanie"], ["repetitive", "powtarzalne"], ["regardless", "mimo wszystko"], ["supervisor", "kierownik"], ["odorless", "bezwonny"], ["wisp", "wiązka"], ["homeowner", "właściciel"], ["infested", "zainfekowani"], ["inability", "niezdolność"],
["soul", "dusza"], ["chase", "ścigać"], ["chase down prey", "ścigać zdobycz"], ["pose", "sprawiać"], ["consists", "składa się"], ["mammals", "ssaki"], ["hiss", "syk"], ["growl", "warczenie"], ["lurking", "przyczajony"], ["creaking", "skrzypienie"], ["slug", "ślimak"], ["slippage", "poślizg"], ["sprite", "krasnoludek"], ["digging", "kopanie"], ["secretions", "wydzieliny"], ["rapid", "szybko"], ["causing", "powodując"], ["ingested", "spożyty"],
["odor", "zapach"], ["susceptible", "podatny"], ["foul", "obrzydliwy"], ["under any circumstances", "pod żadnym pozorem"], ["grieving", "opłakiwać"], ["refrain", "wystrzegać się"], ["fae flu", "grypa"], ["dizziness", "zawroty głowy"], ["fatigue", "zmęczenie"], ["collective", "zbiorowa"], ["consciousness", "świadomość"], ["awareness", "świadomość"], ["silly",  "głupi"], ["slightly", "nieznacznie"], ["suppose", "przypuszczać"], ["cheeks", "policzki"],
["core", "rdzeń"], ["addition", "dodatkowy"], ["in addition", ["ponadto", "oprócz"]], ["inhabit", "zamieszkać"], ["enhanced", "wzmocniony"], ["invoices", "faktury"], ["abandon", "opuścić"], ["shall", "być"], ["convenience", "wygoda"], ["chart", "wykres"], ["trunk", ["bagażnik", "trąba słonia"]], ["appliance", "urządzenie"], ["warranty", "gwarancja"], ["kettle", "czajnik"], ["up on you", "na ciebie"], ["schemes", "schematy"], ["uncovered", "odkryte"],
["baselines", "linie bazowe"], ["reinforce", "wzmocnienie"], ["getting owned", "zostać zdobytym"], ["fella", "kolega"], ["in a bit", "za chwilę"], ["thresholds", "progi"], ["stare", "gapić się"], ["overlay", "nakładka"], ["exhibit", "dowód"], ["flatten", "spłaszczyć"], ["properly", "odpowiednio"], ["ceiling", "sufit"], ["resist", "oprzeć się"], ["proficiency", "biegłość"], ["consent", "zgoda"], ["sink", "zlew"], ["jack", "lewarek"],
["playthrough", "rozgrywka"], ["rotten", "zgniły"], ["beside", "obok"], ["breaks it down", "rozbija to"], ["back and forth", "tam i z powrotem"], ["figure", "wymyślić"], ["independently", "niezależnie"], ["appreciated", "doceniony"], ["curse", "przekleństwo"], ["furnace", "piec"], ["paper clip", "spinacz do papieru"], ["throbbing", "pulsujący"], ["carry", "nosić"], ["tied", "związany"], ["indestructible", "niezniszczalny"],
["digit", "cyfra"], ["power", "pierwiastek"], ["root", "pierwiastek"], ["inclusive", "obejmujący"], ["apparently", "najwyraźniej"], ["premise", "przesłanka"], ["tends", "tendencja"], ["needless to say", "nie trzeba dodawać że"], ["unearthed", "odkopany"], ["fae", "wróżka"], ["reboot", "ponowne uruchomienie"], ["rigged", "sfałszowany"], ["lettuce", "sałata"], ["chew", "żuć"], ["digest", "strawić"], ["poll", "głosowanie"], ["change", "drobne"],
["cheesy", ["serowy", "tandetny"]], ["stabb", "dźgnięty"], ["buns", "bułki"], ["insulting", "obraźliwy"], ["harrasing", "niepokojenie"], ["landlord", "gospodarz"], ["lets get down business", "zabierajmy się do pracy"], ["puberty", "dojrzewanie"], ["heavily", "mocno"], ["tuple", "krotka"], ["blank", "pusty"], ["blank", "czyste"], ["carry-on", "bagaż podręczny"], ["oughta", "powinien"], ["napkin", "serwetka"], ["drowned", "utonął"], ["raw", "surower"]]

start = input("POL - UK ? : ")

if start.lower() == "pol":
    # Główna pętla programu
    while True:
        # Losowanie słowa
        x = random.randint(0, len(letters) - 1)  # Losowanie słowa z listy
        word_pair = letters[x]  # Wylosowana para słów

        # Sprawdzanie, czy angielskie słowo ma jedno czy więcej tłumaczeń
        if isinstance(word_pair[1], list):
            correct_translation = random.choice(word_pair[1])  # Wybór jednego z tłumaczeń, jeśli jest ich więcej
        else:
            correct_translation = word_pair[1]

        # Pytanie użytkownika
        print(f"\nCo to znaczy: {word_pair[0]} (wpisz 'exit', aby zakończyć)")

        # Pętla do zgadywania
        while True:
            user_input = input("Twoja odpowiedź: ")

            # Sprawdzenie, czy użytkownik chce zakończyć program
            if user_input.lower() == "exit":
                print("Zakończono program.")
                exit()  # Zakończenie działania programu

            # Sprawdzenie poprawności odpowiedzi
            if user_input.lower() == correct_translation.lower():
                print(f"Dobrze! {word_pair[0]} to {correct_translation}.")
                break  # Wyjście z pętli i losowanie nowego słowa
            else:
                print("Źle. Spróbuj jeszcze raz.")
elif start.lower() == "uk":
    # Główna pętla programu
    while True:
        # Losowanie słowa
        x = random.randint(0, len(letters) - 1)  # Losowanie słowa z listy
        word_pair = letters[x]  # Wylosowana para słów

        # Sprawdzanie, czy angielskie słowo ma jedno czy więcej tłumaczeń
        if isinstance(word_pair[1], list):
            pol_word = random.choice(word_pair[1])  # Wybór jednego z tłumaczeń, jeśli jest ich więcej
        else:
            pol_word = word_pair[1]

        # Pytanie użytkownika
        print(f"\nCo to znaczy: {pol_word} (wpisz 'exit', aby zakończyć)")

        # Pętla do zgadywania
        while True:
            user_input = input("Twoja odpowiedź: ")

            # Sprawdzenie, czy użytkownik chce zakończyć program
            if user_input.lower() == "exit":
                print("Zakończono program.")
                exit()  # Zakończenie działania programu

            # Sprawdzenie poprawności odpowiedzi
            if user_input.lower() == word_pair[0]:
                print(f"Dobrze! {pol_word} to {word_pair[0]}.")
                break  # Wyjście z pętli i losowanie nowego słowa
            else:
                print("Źle. Spróbuj jeszcze raz.")