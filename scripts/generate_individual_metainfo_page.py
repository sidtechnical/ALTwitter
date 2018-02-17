#!/usr/bin/env python
from __future__ import unicode_literals
from tqdm import tqdm
import tweepy
import numpy
import argparse
import collections
from collections import OrderedDict
import datetime
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
import urlparse
import urllib

import os.path

import gc





try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

from secrets import consumer_key, consumer_secret, access_token, access_token_secret

__version__ = '0.2-dev'

plt.style.use('seaborn-white')

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Ubuntu'
plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.titlesize'] = 12


# Set an aspect ratio
width, height = 22, 12
fig = plt.figure(figsize=(width,height), dpi=600)

# full_list_mep = ["1PavelSvoboda", "a_chauprade", "a_jongerius", "AdamGierek", "adamkosamep", "AgeaLaura", "akhanmep", "AKRajewicz", "AlainCadec", "ALamassoure", "Albert_Dess_MEP", "Alberto_Cirio", "Ale_Mussolini_", "alessiamosca", "ALewerMEP", "alexlmayer", "AlynSmithMEP", "AmjadBashirMEP", "AnaGomesMEP", "AndersVistisen", "andicristeamep", "AndorDeli", "Andreas_Schwab", "AndrejsMamikins", "andreykovatchev", "AndreyNovakov", "Andrikiene", "androulakisnick", "AngelaVallina", "AngelikaMlinar", "AngeloCiocca", "ANiebler", "anjahazekamp", "AnnaHedh", "AnnaMariaCB", "AnnaZaborska", "anneleen_vb", "AnnelieseDodds", "AnneMarieMineur", "AnnieSchreijer", "anthea_mcintyre", "Antonio_Tajani", "AntonioPanzeri", "ArnaudDanjean", "Arne_Gericke", "ArneLietz", "ASanderMEP", "Ashleyfoxmep", "AxelVossMdEP", "ayuso_pilar", "BalasGuillaume", "balcytis", "BarbaraKudrycka", "BarbaraMatera", "BartStaes", "BasBelderMEP", "BasEickhout", "BeataGosiewska", "Beatrix_vStorch", "beatrizbecerrab", "beghin_t", "BendtEU", "bernard_monot", "Bernd_Koelmel", "berndlange", "BerndLucke", "BiljanaBorzan", "BillDudleyNorth", "BirgitSippelMEP", "biuroposelskie", "BLiberadzki", "blochbihler", "bodilvalero", "borrellidavid", "brandobenifei", "BranoSkripek", "brianhayesMEP", "BriceHortefeux", "BronisRopeLT", "brunogollnisch", "buba0769", "bueti", "BZdrojewski", "C_Stihler_MEP", "Caninator", "CarlosCoelhoPE", "carlositurgaiz", "CarolinaPunset", "caspary", "Catalin_Ivan", "CaterinaChinnic", "catherinemep", "cdallonnes", "CDPreda", "CeciliaWikstrom", "charanzova", "CharlesGoerens", "CharlesTannock", "Chrysogonos_K", "ckyenge", "ClaraAguilera7", "ClareMoodyMEP", "ClaudeMoraesMEP", "clauderolin", "ClaudeTurmes", "ClaudiaTapardel", "clegrip", "cmonteiroaguiar", "Cofferati", "comilara", "ComodiniCachia", "ConstanzeKrehl", "cozzolino62", "csakypal", "curziomaltesetw", "CvNieuwenhuizen", "czorrinho", "CzSiekierski", "DacianaSarbu", "dajcstomi", "damiandraghici", "DamianoZoffoli", "DanielaAiuto", "danieleviotti", "DanielJHannan", "DantiNicola", "danutahuebner", "DariuszRosati", "datirachida", "DavidCasaMEP", "DavidCoburnUKip", "davidmartinmep", "davidmcallister", "DavidSassoli", "DavorSkrlec", "DCBMEP", "ddalton40", "DdJong", "DeirdreCluneMEP", "Delahaye_Europe", "delcastillop", "DemPapadakis", "derekvaughan", "desarnez", "DianeDoddsMEP", "DianeJamesMEP", "DJazlowiecka", "DMartinFN", "DominiqueBilde", "DominiqueRiquet", "Dr_KlausBuchner", "dubravkasuica", "e_ferrand", "edouardmartinEU", "EduardKukan", "EGardiazabal", "EGardini", "elena_gentile", "ElenaValenciano", "EleonoraEvi", "eleonoraforenza", "ElliKoestinger", "ellyesse", "ElmarBrok_MEP", "Emil_Radev", "EmmaMcClarkin", "emmanuelmaurel", "emorinchartier", "enricogasbarra", "EnriqueCalvet", "EpitidGeorgios", "EricAndrieuEU", "ernesturtasun", "ErnstCornelia", "Esther_de_Lange", "etorrespodemos", "EugenAFreund", "EuropaJens", "EUTheurer", "EvaJoly", "EvaKaili", "evapaunova", "Evelyn_Regner", "EvzenTosenovsky", "f_philippot", "FabioDeMasi", "federley", "fernandoruas", "fgambus_eu", "fjavilopez", "Fjellner", "flaviozanonato", "fmarcellesi", "FMCastaldo", "Fontana3Lorenzo", "FountoulisLampr", "Franc_Bogovic", "franckproust", "franzobermayr", "Frederiqueries", "fulviomartuscie", "GabiZimmerMEP", "GabrielePreuss", "GabrielMariya", "GabrielMatoA", "gannemans", "georgmayermep", "GerardBattenMEP", "gerardeprez", "Gerbrandy", "gesine_meissner", "ghokmark", "giannipittella", "Gilles_Lebreton", "gillespargneaux", "gimenezbarbat", "GiorgosKyrtsos", "giovannilavia", "GiuliaMoi_M5S", "GlenisWillmott", "GoffredoBettini", "gonzalezpons", "GoulardSylvie", "GQuisthoudt", "GreenJeanMEP", "GreenKeithMEP", "GrosseteteF", "GrzybAndrzej", "gualtierieurope", "GuyVerhofstadt", "Halla_aho", "hans_van_baalen", "HansOlafHenkel", "HeidiHautala", "HelgaTruepel", "HelmutScholzMEP", "HennaVirkkunen", "HerbertDorfmann", "Hetman_K", "hildevautmans", "hreul", "HTakkula", "hudghtonmepSNP", "HuguesBayet", "IanDuncanMEP", "IAyalaSender", "ignaziocorrao", "ilhankyuchyuk", "indrektarand", "IneseVaidere", "inge_graessle", "ioanmirceapascu", "IratxeGarper", "Isa_Adinolfi", "Isabel_thomasEU", "IsabellaDeMonte", "IsmailErtug", "isoltesEP", "istvan_ujhelyi", "IuliuWinkler", "ivajgl", "IvanJakovcic", "IvanStefanec", "IvetaGrigule", "IvoBelet", "IzaskunBilbaoB", "J_Lewandowski", "j_wisniewska", "Jaakonsaari", "jaatteenmaki", "JakopDalunde", "JamesJimCarver", "JanAlbrecht", "Jane_CollinsMEP", "Janice4Brexit", "JanOlbrycht", "JanuszZemke", "jasenkos", "javorbenedek", "Jbergeronmep", "JeanArthuis", "JeanMarieCAVADA", "jensni", "JeppeKofod", "jeroen_lenaers", "JerzyBuzek", "JezekCZ", "JFJalkh", "JFLopezAguilar", "jfostermep", "jhuitema", "JillEvansMEP", "jlavrilleux", "JLMelenchon", "JLSchaffhauser", "JMFernandesEU", "jmterricabras", "JNicholsonMEP", "jo_leinen", "joachimzeller", "JoelleMelinFN", "jonasfernandez", "JonathanArnott", "jordisolef", "josebove", "JoseFariaMEP", "Josu_Juaristi", "jozorados", "jpdenanot", "JProcterMEP", "JSaryuszWolski", "JSeymourUKIP", "JStarbatty", "Jude_KD", "judithineuropa", "julia_reid", "julie4nw", "juliegirling", "JuttaSteinruck", "JytteGuteland", "kajakallas", "Kalniete", "KarimaDelli", "karinkadenbach", "KatiPiri", "KaufmannSylvia", "KaySwinburneMEP", "KellerHonza", "kkuneva", "kmujazdowski", "knufleckenstein", "KohlicekJaromir", "kokokansanpaavo", "Konecna_K", "korwinmikke", "kouroumbashev", "krisjaniskarins", "KristinaWinberg", "KrystynaLybacka", "kvanbrempt", "KyllonenMerja", "L_Cesa", "Ladaktusson", "Lambsdorff", "langen_werner", "LauristinMarju", "LefChristoforou", "lepenjm", "LFerraraM5S", "LiadhNiRiadaMEP", "libertarofuturo", "lidiageringer", "LidiaSenra", "LieveWierinck", "LilianaMEP", "LindaMcAvanMEP", "LinneaEngstrom", "LJManscour", "LNBDublin", "Loekkegaard_MEP", "lojzepeterle", "LolaPodemos", "louis_aliot", "LouisMichel", "LucyAndersonMEP", "LudekNie", "luigi_morgano", "lukeming", "LvNistelrooij", "M_AndersonSF", "M_DiaconuMEP", "m_giuffrida", "M_Kefalogiannis", "mady_delvaux", "MaireadMcGMEP", "maitepagaza", "MaleticIvana", "MalinBjork_EU", "MAlliotMarie", "ManfredWeber", "MarcJoulaud", "marcoaffronte", "MarcoValliM5S", "Marcozanni86", "MarcoZullo", "marctarabella", "MarcusPretzell", "marek_plura", "marekjurek", "MargotLJParker", "MargreteAuken", "MariaGrapini", "MariaHeubuch", "MarianHarkin", "MarianMarinescu", "MariaSpyraki", "Mariearenaps", "MarietjeSchaake", "marijana_petir", "MarinaAlbiol", "marinhoepinto", "MarioBorghezio", "maritaulvskog", "markdemesmaeker", "MarkusFerber", "markuspieperMEP", "MarleneMizzi", "martina_michels", "MartinaWernerEU", "MartinHaeusling", "MartinSchulz", "MartinSonneborn", "maryhoneyball", "MassimoPaolucc6", "mattcarthy", "matteosalvinimi", "MatthijsvMilt", "mauriceponga", "MaxAndersson", "MaxSalini", "MCArnautu", "MCVergiat", "Mdlabajova", "MEPDanielBuda", "MEPDohrmann", "MepMCramer", "mercedesbresso", "MeszericsT", "miapetrakumpula", "michaelgahler", "MichalBoni", "MichelDANTIN", "MicheleRivasi", "michelreimon", "MiguelUrban", "MikeHookemMEP", "MilanZver", "MireilledOrnano", "Miriamdalli", "miromikolasik", "MJRLdeGraaff", "MJRodriguesEU", "MLP_officiel", "mmatias_", "MollyScottCato", "momchilnekov", "MonicaMacovei1", "MonikaFlaBenova", "MonikaHohlmeier", "MonikaVana", "mortenhelveg", "MrMesserschmidt", "msojdrova", "nadine__morano", "NagyJozsefEU", "NathanGillMEP", "NBarekov", "NChildersMEP", "NeenaGmep", "negrescuvictor", "ngriesbeck", "NicolaCaputo", "nicolasbayfn", "NiedermullerMEP", "Nigel_Farage", "NikosChountis", "NilsTorvalds", "NirjDeva", "Norica_Nicolai", "Notis_Marias", "NunoMeloCDS", "oflynnmep", "OlafStuger", "OleEU", "OlgaSehnalova", "olleludvigsson", "othmar_karas", "Pabriks", "palomalopezB", "paolodecastro", "papadimoulis", "PASCALARIMONT", "PatricielloAldo", "PatricijaSulin", "PatrickLeHyaric", "PaulBrannenNE", "paulnuttallukip", "PaulRuebig", "paultang", "PavelEmilian", "pavelpoc", "PDurandOfficiel", "PediciniM5S", "pepeblancoEP", "PervencheBeres", "peter_jahr", "peterliese", "PeterSimonMEP", "petervdalen", "petras_petras", "petrisarvamaa", "PetrMachMEP", "ph_lamberts", "ph_loiseau", "philippejuvin", "pinapic", "PocheMEP", "Pospisil_Jiri", "profKarski", "r_czarnecki", "RaffaeleFitto", "RamonaManescu", "ramontremosa", "raymondfinch", "RCorbettMEP", "RebHarms", "renatabriano", "renateweber", "renatosoru", "RenaudMuselier", "RichardAshMEP", "rinakari", "RJaureguiA", "RobertaMetsola", "robertrochefort", "robertszile", "RodriguezPinero", "RogerHelmerMEP", "rohde_jens", "RolandasPaksas", "RomanaTomc", "rosadamato634", "rozathun", "RuzaTomasic", "sabineverheyen", "SalvoCicu", "SalvoPogliese", "SanderLoones", "SantAlfred", "SantiagoFisas", "SaudargasA", "SchaldemoseMEP", "Schmidt_Clau", "schopflinMEP", "schulzeeuropa", "SeanKellyMEP", "SebDance", "Senficon", "SergeiStanishev", "Sergio_GP", "SernagiottoRemo", "SHKMEP", "SilviaCostaEU", "simonabonafe", "sionsimon", "SkaKeller", "SmolkovaMonika", "SMuresan", "SofiaHRibeiro", "SofiaSakorafa", "SoledadCabezon", "Sophie_Montel", "SophieintVeld", "SorayaPostFi", "sorinmoisa", "spietikainen", "stanislavpolcak", "SteeveBriois", "Stefan_Eck_MEP", "stefanomaullu", "SteliosKoul", "StetinaEP", "Steven_Woolfe", "StevensHelga", "SulikRichard", "sven_giegold", "SvMalinov", "SyedKamall", "sylikiotis", "Sylvie_Goddyn", "sylvieguillaume", "Synadinos_Eleft", "szanyitibor", "szejnfeld", "TadeuszZwiefka", "tamburrano", "TaniaGonzalezPs", "Tatjana_Zdanoka", "Telicka", "TeresaJBecerril", "TerryReintke", "tfajon", "thadjigeorgiou", "thaendel", "THEOCHAROUSE", "TheodorStolojan", "TheresaMEP", "Tim_Aker", "toiapatrizia", "TokiaSaifi", "TomaszPoreba", "tomvdkendelaere", "TomZdechovsky", "TonoEPP", "TonyGuoga", "TPicula", "TraianUngureanu", "TrebesiusMdEP", "Troszczynski_FN", "turcanu2014", "UdoBullmann", "udovoigt", "UliMuellerMdEP", "UlrikeLunacek", "UlrikeRodust", "Urmaspaet", "urutchev", "ValentinasMazu1", "vickyford", "VickyMaeijer", "VictorBostinaru", "ViktorUspaskich", "vilimsky", "Vincent_Peillon", "VioricaDancila", "VivianeRedingEU", "vozemberg", "VRoziere", "WalesaMEP", "Weidenholzer", "WernerKuhnMdEP", "WestphalKerstin", "WimvandeCamp", "woelken", "xabierbenito", "YanaToom", "yjadot", "younousomarjee", "ZahradilJan", "zalaboris", "ZbigniewKuzmiuk", "ZdzKrasnodebski", "ZeljanaZovko"]

full_list_mep = ["Ladaktusson", "Isa_Adinolfi", "marcoaffronte", "AgeaLaura", "ClaraAguilera7", "DanielaAiuto", "Tim_Aker", "MarinaAlbiol", "JanAlbrecht", "louis_aliot", "MAlliotMarie", "LucyAndersonMEP", "M_AndersonSF", "MaxAndersson", "EricAndrieuEU", "Andrikiene", "androulakisnick", "gannemans", "Mariearenaps", "PASCALARIMONT", "MCArnautu", "JonathanArnott", "JeanArthuis", "RichardAshMEP", "Janice4Brexit", "MargreteAuken", "petras_petras", "IAyalaSender", "ayuso_pilar", "hans_van_baalen", "BalasGuillaume", "balcytis", "buba0769", "NBarekov", "AmjadBashirMEP", "GerardBattenMEP", "nicolasbayfn", "HuguesBayet", "catherinemep", "beatrizbecerrab", "beghin_t", "BasBelderMEP", "IvoBelet", "BendtEU", "brandobenifei", "xabierbenito", "PervencheBeres", "Jbergeronmep", "GoffredoBettini", "IzaskunBilbaoB", "DominiqueBilde", "MalinBjork_EU", "pepeblancoEP", "Franc_Bogovic", "simonabonafe", "MichalBoni", "MarioBorghezio", "borrellidavid", "BiljanaBorzan", "VictorBostinaru", "josebove", "LNBDublin", "PaulBrannenNE", "mercedesbresso", "renatabriano", "SteeveBriois", "ElmarBrok_MEP", "Dr_KlausBuchner", "MEPDanielBuda", "UdoBullmann", "bueti", "JerzyBuzek", "SoledadCabezon", "AlainCadec", "EnriqueCalvet", "WimvandeCamp", "DCBMEP", "NicolaCaputo", "mattcarthy", "JamesJimCarver", "DavidCasaMEP", "caspary", "FMCastaldo", "delcastillop", "JeanMarieCAVADA", "L_Cesa", "charanzova", "a_chauprade", "NChildersMEP", "CaterinaChinnic", "NikosChountis", "OleEU", "LefChristoforou", "Chrysogonos_K", "SalvoCicu", "AngeloCiocca", "Alberto_Cirio", "DeirdreCluneMEP", "DavidCoburnUKip", "CarlosCoelhoPE", "Cofferati", "Jane_CollinsMEP", "comilara", "ComodiniCachia", "AnnaMariaCB", "RCorbettMEP", "ignaziocorrao", "SilviaCostaEU", "Caninator", "cozzolino62", "MepMCramer", "andicristeamep", "csakypal", "r_czarnecki", "petervdalen", "Miriamdalli", "ddalton40", "JakopDalunde", "rosadamato634", "SebDance", "VioricaDancila", "ArnaudDanjean", "DantiNicola", "MichelDANTIN", "datirachida", "paolodecastro", "Delahaye_Europe", "AndorDeli", "KarimaDelli", "mady_delvaux", "FabioDeMasi", "markdemesmaeker", "IsabellaDeMonte", "jpdenanot", "gerardeprez", "desarnez", "Albert_Dess_MEP", "dajcstomi", "NirjDeva", "M_DiaconuMEP", "Mdlabajova", "AnnelieseDodds", "DianeDoddsMEP", "MEPDohrmann", "HerbertDorfmann", "MireilledOrnano", "damiandraghici", "IanDuncanMEP", "PDurandOfficiel", "Stefan_Eck_MEP", "BasEickhout", "LinneaEngstrom", "EpitidGeorgios", "ErnstCornelia", "IsmailErtug", "BillDudleyNorth", "JillEvansMEP", "EleonoraEvi", "tfajon", "Nigel_Farage", "JoseFariaMEP", "federley", "MarkusFerber", "JMFernandesEU", "jonasfernandez", "e_ferrand", "LFerraraM5S", "raymondfinch", "SantiagoFisas", "RaffaeleFitto", "Fjellner", "lukeming", "MonikaFlaBenova", "knufleckenstein", "Fontana3Lorenzo", "vickyford", "eleonoraforenza", "jfostermep", "FountoulisLampr", "Ashleyfoxmep", "EugenAFreund", "GabrielMariya", "michaelgahler", "fgambus_eu", "IratxeGarper", "EGardiazabal", "EGardini", "enricogasbarra", "EuropaJens", "elena_gentile", "Gerbrandy", "Arne_Gericke", "lidiageringer", "sven_giegold", "AdamGierek", "NathanGillMEP", "NeenaGmep", "gimenezbarbat", "juliegirling", "m_giuffrida", "Sylvie_Goddyn", "CharlesGoerens", "brunogollnisch", "AnaGomesMEP", "TaniaGonzalezPs", "gonzalezpons", "BeataGosiewska", "GoulardSylvie", "MJRLdeGraaff", "MariaGrapini", "inge_graessle", "ngriesbeck", "TheresaMEP", "IvetaGrigule", "GrosseteteF", "GrzybAndrzej", "gualtierieurope", "sylvieguillaume", "TonyGuoga", "JytteGuteland", "Sergio_GP", "thadjigeorgiou", "Halla_aho", "thaendel", "DanielJHannan", "MarianHarkin", "RebHarms", "MartinHaeusling", "HeidiHautala", "brianhayesMEP", "anjahazekamp", "AnnaHedh", "RogerHelmerMEP", "HansOlafHenkel", "Hetman_K", "MariaHeubuch", "MonikaHohlmeier", "ghokmark", "maryhoneyball", "MikeHookemMEP", "BriceHortefeux", "danutahuebner", "hudghtonmepSNP", "jhuitema", "SophieintVeld", "carlositurgaiz", "Catalin_Ivan", "Jaakonsaari", "jaatteenmaki", "yjadot", "peter_jahr", "IvanJakovcic", "JFJalkh", "DianeJamesMEP", "RJaureguiA", "javorbenedek", "DJazlowiecka", "JezekCZ", "TeresaJBecerril", "EvaJoly", "DdJong", "a_jongerius", "MarcJoulaud", "Josu_Juaristi", "marekjurek", "philippejuvin", "karinkadenbach", "EvaKaili", "kajakallas", "Kalniete", "SyedKamall", "othmar_karas", "rinakari", "SHKMEP", "krisjaniskarins", "profKarski", "KaufmannSylvia", "M_Kefalogiannis", "KellerHonza", "SkaKeller", "SeanKellyMEP", "akhanmep", "Jude_KD", "JeppeKofod", "KohlicekJaromir", "Bernd_Koelmel", "Konecna_K", "korwinmikke", "adamkosamep", "ElliKoestinger", "SteliosKoul", "kouroumbashev", "andreykovatchev", "AKRajewicz", "ZdzKrasnodebski", "ConstanzeKrehl", "BarbaraKudrycka", "WernerKuhnMdEP", "EduardKukan", "miapetrakumpula", "kkuneva", "ZbigniewKuzmiuk", "ckyenge", "KyllonenMerja", "GiorgosKyrtsos", "ilhankyuchyuk", "ALamassoure", "GreenJeanMEP", "ph_lamberts", "Lambsdorff", "berndlange", "Esther_de_Lange", "langen_werner", "LauristinMarju", "giovannilavia", "jlavrilleux", "Gilles_Lebreton", "clegrip", "PatrickLeHyaric", "jo_leinen", "jeroen_lenaers", "lepenjm", "MLP_officiel", "J_Lewandowski", "ALewerMEP", "BLiberadzki", "peterliese", "ArneLietz", "blochbihler", "ph_loiseau", "Loekkegaard_MEP", "SanderLoones", "fjavilopez", "JFLopezAguilar", "palomalopezB", "TonoEPP", "BerndLucke", "olleludvigsson", "UlrikeLunacek", "KrystynaLybacka", "davidmcallister", "LindaMcAvanMEP", "EmmaMcClarkin", "MaireadMcGMEP", "PetrMachMEP", "anthea_mcintyre", "MonicaMacovei1", "VickyMaeijer", "MaleticIvana", "SvMalinov", "curziomaltesetw", "AndrejsMamikins", "RamonaManescu", "LJManscour", "fmarcellesi", "Notis_Marias", "MarianMarinescu", "marinhoepinto", "davidmartinmep", "DMartinFN", "edouardmartinEU", "fulviomartuscie", "BarbaraMatera", "mmatias_", "GabrielMatoA", "stefanomaullu", "emmanuelmaurel", "alexlmayer", "georgmayermep", "ValentinasMazu1", "gesine_meissner", "JLMelenchon", "JoelleMelinFN", "NunoMeloCDS", "MrMesserschmidt", "MeszericsT", "RobertaMetsola", "LouisMichel", "martina_michels", "miromikolasik", "MatthijsvMilt", "AnneMarieMineur", "MarleneMizzi", "AngelikaMlinar", "GiuliaMoi_M5S", "sorinmoisa", "bernard_monot", "cmonteiroaguiar", "Sophie_Montel", "ClareMoodyMEP", "ClaudeMoraesMEP", "nadine__morano", "luigi_morgano", "emorinchartier", "alessiamosca", "UliMuellerMdEP", "SMuresan", "RenaudMuselier", "Ale_Mussolini_", "NagyJozsefEU", "negrescuvictor", "momchilnekov", "JNicholsonMEP", "Norica_Nicolai", "ANiebler", "LudekNie", "NiedermullerMEP", "CvNieuwenhuizen", "jensni", "LiadhNiRiadaMEP", "LvNistelrooij", "AndreyNovakov", "paulnuttallukip", "franzobermayr", "oflynnmep", "JanOlbrycht", "younousomarjee", "biuroposelskie", "Pabriks", "Urmaspaet", "maitepagaza", "RolandasPaksas", "AntonioPanzeri", "MassimoPaolucc6", "DemPapadakis", "papadimoulis", "gillespargneaux", "MargotLJParker", "ioanmirceapascu", "PatricielloAldo", "evapaunova", "PavelEmilian", "PediciniM5S", "Vincent_Peillon", "lojzepeterle", "mortenhelveg", "marijana_petir", "f_philippot", "pinapic", "TPicula", "markuspieperMEP", "spietikainen", "KatiPiri", "giannipittella", "marek_plura", "pavelpoc", "PocheMEP", "SalvoPogliese", "stanislavpolcak", "mauriceponga", "TomaszPoreba", "Pospisil_Jiri", "SorayaPostFi", "CDPreda", "MarcusPretzell", "GabrielePreuss", "JProcterMEP", "franckproust", "CarolinaPunset", "GQuisthoudt", "Emil_Radev", "jozorados", "libertarofuturo", "Senficon", "VivianeRedingEU", "Evelyn_Regner", "julia_reid", "michelreimon", "TerryReintke", "hreul", "cdallonnes", "SofiaHRibeiro", "Frederiqueries", "DominiqueRiquet", "MicheleRivasi", "robertrochefort", "LilianaMEP", "MJRodriguesEU", "RodriguezPinero", "UlrikeRodust", "rohde_jens", "clauderolin", "BronisRopeLT", "DariuszRosati", "VRoziere", "fernandoruas", "PaulRuebig", "TokiaSaifi", "SofiaSakorafa", "MaxSalini", "matteosalvinimi", "LolaPodemos", "ASanderMEP", "SantAlfred", "DacianaSarbu", "judithineuropa", "petrisarvamaa", "JSaryuszWolski", "DavidSassoli", "SaudargasA", "MarietjeSchaake", "JLSchaffhauser", "SchaldemoseMEP", "ellyesse", "Schmidt_Clau", "HelmutScholzMEP", "schopflinMEP", "AnnieSchreijer", "MartinSchulz", "schulzeeuropa", "Andreas_Schwab", "MollyScottCato", "OlgaSehnalova", "jasenkos", "LidiaSenra", "SernagiottoRemo", "JSeymourUKIP", "CzSiekierski", "PeterSimonMEP", "sionsimon", "BirgitSippelMEP", "BranoSkripek", "DavorSkrlec", "AlynSmithMEP", "SmolkovaMonika", "msojdrova", "jordisolef", "isoltesEP", "MartinSonneborn", "renatosoru", "MariaSpyraki", "BartStaes", "SergeiStanishev", "JStarbatty", "IvanStefanec", "JuttaSteinruck", "StetinaEP", "StevensHelga", "C_Stihler_MEP", "TheodorStolojan", "Beatrix_vStorch", "OlafStuger", "dubravkasuica", "SulikRichard", "PatricijaSulin", "1PavelSvoboda", "KaySwinburneMEP", "sylikiotis", "Synadinos_Eleft", "szanyitibor", "szejnfeld", "Antonio_Tajani", "HTakkula", "tamburrano", "paultang", "CharlesTannock", "ClaudiaTapardel", "marctarabella", "indrektarand", "GreenKeithMEP", "Telicka", "jmterricabras", "THEOCHAROUSE", "EUTheurer", "Isabel_thomasEU", "rozathun", "toiapatrizia", "RuzaTomasic", "RomanaTomc", "YanaToom", "etorrespodemos", "NilsTorvalds", "EvzenTosenovsky", "TrebesiusMdEP", "ramontremosa", "Troszczynski_FN", "HelgaTruepel", "turcanu2014", "ClaudeTurmes", "kmujazdowski", "istvan_ujhelyi", "maritaulvskog", "TraianUngureanu", "MiguelUrban", "ernesturtasun", "urutchev", "ViktorUspaskich", "IneseVaidere", "ivajgl", "ElenaValenciano", "bodilvalero", "MarcoValliM5S", "AngelaVallina", "MonikaVana", "anneleen_vb", "kvanbrempt", "tomvdkendelaere", "derekvaughan", "hildevautmans", "kokokansanpaavo", "MCVergiat", "sabineverheyen", "GuyVerhofstadt", "vilimsky", "danieleviotti", "HennaVirkkunen", "AndersVistisen", "udovoigt", "AxelVossMdEP", "vozemberg", "WalesaMEP", "julie4nw", "ManfredWeber", "renateweber", "Weidenholzer", "MartinaWernerEU", "WestphalKerstin", "LieveWierinck", "CeciliaWikstrom", "GlenisWillmott", "KristinaWinberg", "IuliuWinkler", "j_wisniewska", "Steven_Woolfe", "woelken", "AnnaZaborska", "ZahradilJan", "zalaboris", "Marcozanni86", "flaviozanonato", "Tatjana_Zdanoka", "TomZdechovsky", "BZdrojewski", "joachimzeller", "JanuszZemke", "robertszile", "GabiZimmerMEP", "DamianoZoffoli", "czorrinho", "ZeljanaZovko", "MarcoZullo", "MilanZver", "TadeuszZwiefka"]

parser = argparse.ArgumentParser(description=
    "Simple Twitter Profile Analyzer (https://github.com/x0rz/tweets_analyzer) version %s" % __version__,
                                 usage='%(prog)s -n <screen_name> [options]')
parser.add_argument('-l', '--limit', metavar='N', type=int, default=1000,
                    help='limit the number of tweets to retreive (default=1000)')
parser.add_argument('-n', '--name', required=True, metavar="screen_name",
                    help='target screen_name')

parser.add_argument('-f', '--filter', help='filter by source (ex. -f android will get android tweets only)')

parser.add_argument('--no-timezone', action='store_true',
                    help='removes the timezone auto-adjustment (default is UTC)')

parser.add_argument('--utc-offset', type=int,
                    help='manually apply a timezone offset (in seconds)')

parser.add_argument('--friends', action='store_true',
                    help='will perform quick friends analysis based on lang and timezone (rate limit = 15 requests)')

args = parser.parse_args()


# Here are globals used to store data - I know it's dirty, whatever
start_date = 0
end_date = 0

activity_hourly = {
    ("%2i:00" % i).replace(" ", "0"): 0 for i in range(24)
}

activity_weekly = {
    "%i" % i: 0 for i in range(7)
}

detected_langs = collections.Counter()
detected_sources = collections.Counter()
detected_places = collections.Counter()
geo_enabled_tweets = 0
detected_hashtags = collections.Counter()
detected_domains = collections.Counter()
detected_timezones = collections.Counter()
retweets = 0
retweeted_users = collections.Counter()
mentioned_users = collections.Counter()
id_screen_names = {}
friends_timezone = collections.Counter()
friends_lang = collections.Counter()


def process_tweet(tweet):
    """ Processing a single Tweet and updating our datasets """
    global start_date
    global end_date
    global geo_enabled_tweets
    global retweets

    # Check for filters before processing any further
    if args.filter and tweet.source:
        if not args.filter.lower() in tweet.source.lower():
            return

    tw_date = tweet.created_at

    # Updating most recent tweet
    end_date = end_date or tw_date
    start_date = tw_date

    # Handling retweets
    try:
        # We use id to get unique accounts (screen_name can be changed)
        rt_id_user = tweet.retweeted_status.user.id_str
        retweeted_users[rt_id_user] += 1

        if tweet.retweeted_status.user.screen_name not in id_screen_names:
            id_screen_names[rt_id_user] = "@%s" % tweet.retweeted_status.user.screen_name

        retweets += 1
    except:
        pass

    # Adding timezone from profile offset to set to local hours
    if tweet.user.utc_offset and not args.no_timezone:
        tw_date = (tweet.created_at + datetime.timedelta(seconds=tweet.user.utc_offset))

    if args.utc_offset:
        tw_date = (tweet.created_at + datetime.timedelta(seconds=args.utc_offset))

    # Updating our activity datasets (distribution maps)
    activity_hourly["%s:00" % str(tw_date.hour).zfill(2)] += 1
    activity_weekly[str(tw_date.weekday())] += 1

    # Updating langs
    detected_langs[tweet.lang] += 1

    # Updating sources
    detected_sources[tweet.source] += 1

    # Detecting geolocation
    if tweet.place:
        geo_enabled_tweets += 1
        tweet.place.name = tweet.place.name
        detected_places[tweet.place.name] += 1

    # Updating hashtags list
    if tweet.entities['hashtags']:
        for ht in tweet.entities['hashtags']:
            ht['text'] = "#%s" % ht['text']
            detected_hashtags[ht['text']] += 1

    # Updating domains list
    if tweet.entities['urls']:
        for url in tweet.entities['urls']:
            domain = urlparse(url['expanded_url']).netloc
            if domain != "twitter.com":  # removing twitter.com from domains (not very relevant)
                detected_domains[domain] += 1

    # Updating mentioned users list
    if tweet.entities['user_mentions']:
        for ht in tweet.entities['user_mentions']:
            mentioned_users[ht['id_str']] += 1
            if not ht['screen_name'] in id_screen_names:
                id_screen_names[ht['id_str']] = "@%s" % ht['screen_name']


def process_friend(friend):
    """ Process a single friend """
    friends_lang[friend.lang] += 1 # Getting friend language & timezone
    if friend.time_zone:
        friends_timezone[friend.time_zone] += 1


def get_friends(api, username, limit):
    """ Download friends and process them """
    for friend in tqdm(tweepy.Cursor(api.friends, screen_name=username).items(limit), unit="friends", total=limit):
        process_friend(friend)


def get_tweets(api, username, limit):
    """ Download Tweets from username account """
    for status in tqdm(tweepy.Cursor(api.user_timeline, screen_name=username).items(limit),
                       unit="tw", total=limit):
        process_tweet(status)


def int_to_weekday(day):
    weekdays = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
    return weekdays[int(day) % len(weekdays)]

def get_dictionary_with_percentages(dataset, top=5):
    sum = numpy.sum(list(dataset.values()))
    od_slice = OrderedDict(sorted(dataset.items(), key=lambda x: x[1], reverse=True)[:top])
    od_slice_percentage = od_slice.copy()
    # od_slice_percentage.update((x, int(((float(y) / sum) * 100))) for x, y in od_slice_percentage.items())
    od_slice_percentage.update((x, round(((float(y) / sum) * 100),1)) for x, y in od_slice_percentage.items())

    return od_slice, od_slice_percentage

def print_charts(dataset, title, weekday=False):
    """ Prints nice charts based on a dict {(key, value), ...} """
    chart = []
    keys = sorted(dataset.keys())
    mean = numpy.mean(list(dataset.values()))
    
    for key in keys:
        displayed_key = (int_to_weekday(key) if weekday else key)
        chart.append((displayed_key, dataset[key]))

    D = dict(chart)

    mean = numpy.mean(list(D.values()))

    if weekday==True:
    	keyorder =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    	od= collections.OrderedDict(sorted(D.items(), reverse=True, key=lambda i:keyorder.index(i[0])))
    	filename_to_save = args.name+'_'+"weekly.svg"
        save_path_weekly = "../assets/img/weekly"
        complete_path = os.path.join(save_path_weekly, filename_to_save)
    else:
    	od = collections.OrderedDict(sorted(D.items(), reverse=True))
    	filename_to_save = args.name+'_'+"hourly.svg"
        save_path_hourly = "../assets/img/hourly"
        complete_path = os.path.join(save_path_hourly, filename_to_save)

       

    fig, ax = plt.subplots()
    ax.barh(range(len(od)), od.values(), align='center')

    thr = lambda l, t:  [v if (v <= t) else t for v in l ]

    ax.barh(range(len(od)), thr(od.values(),int(mean * 3)), align='center')
    ax.barh(range(len(od)), thr(od.values(),int(mean * 2)), align='center')

    ax.set_yticks(range(len(od)))
    ax.set_yticklabels(od.keys())
    ax.set_xticks([])

    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(range(len(od)))
    ax2.set_yticklabels(od.values())

    for spine in ax.spines.values():
    	spine.set_visible(False)

    for spine in ax2.spines.values():
    	spine.set_visible(False)

    ax.tick_params(top='off', bottom='off', left='off', right='off', labelleft='on', labelbottom='off')
    ax2.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='off')

    if weekday==True:
    	ax.text(-0.05, 1,'Days', horizontalalignment='center', verticalalignment='top', transform=ax.transAxes, fontweight='bold')
    else:
    	ax.text(-0.05, 1,'HH:MM', horizontalalignment='center', verticalalignment='top', transform=ax.transAxes, fontweight='bold')
    
    ax2.text(0.95, 1,'# Tweets', horizontalalignment='left', verticalalignment='top', transform=ax.transAxes, fontweight='bold')

    plt.savefig(complete_path, bbox_inches='tight')
    plt.clf()
    plt.close()
    gc.collect()

def get_profile_image(profile_img_url, twitter_handle):
    import urlparse
    prof_img_url = str(profile_img_url)
    imgUrl = urlparse.urlparse(prof_img_url)
    extension = imgUrl.path.split('.')[1]
    profile_image_name = args.name+'_'+"prof_img."+extension
    
    save_path = "../assets/img/profiles"
    complete_path = os.path.join(save_path, profile_image_name)

    dimension = (imgUrl.path).replace("normal", "200x200")

    imgUrl = imgUrl._replace(path=dimension)
    fullimgUrl = imgUrl.geturl()
    
    urllib.urlretrieve (fullimgUrl,complete_path)
    return profile_image_name

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth)
    # Getting general account's metadata
    print("[+] Getting @%s account data..." % args.name)
    user_info = twitter_api.get_user(screen_name=args.name)


    curr_profile_image_name = get_profile_image(user_info.profile_image_url, args.name)



    if user_info.utc_offset is None:
        print("[+] Can't get specific timezone for this user")

    if args.utc_offset:
        print("[+] Applying timezone offset %d (--utc-offset)" % args.utc_offset)

    print "[+] statuses_count :", user_info.statuses_count

    # Will retreive all Tweets from account (or max limit)
    num_tweets = numpy.amin([args.limit, user_info.statuses_count])
    print("[+] Retrieving last %d tweets..." % num_tweets)

    # Download tweets
    get_tweets(twitter_api, args.name, limit=num_tweets)
    print("[+] Downloaded %d tweets from %s to %s (%d days)" % (num_tweets, start_date, end_date, (end_date - start_date).days))

    num_dates = (end_date - start_date).days
    if (end_date - start_date).days != 0:
        avg_tweets_per_day = round((num_tweets / float((end_date - start_date).days)), 1)
        

    tweet_RT_perc = round((float(retweets) * 100 / num_tweets),1)

    print "activity_hourly"
    print_charts(activity_hourly, "Daily activity distribution (per hour)")
    print "activity_weekly"
    print_charts(activity_weekly, "Weekly activity distribution (per day)", weekday=True)

    from django.template import Template, Context
    from django.conf import settings
    settings.configure()

    template = """
    <!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8">
					<meta http-equiv="X-UA-Compatible" content="IE=edge">
					<title>{{ name }}</title>
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<meta name="Description" lang="en" content="Haukna Metadata (2): Altwitter - Twitter metadata Profiles of the Members of the European Parliament">
					<meta name="author" content="Sid Rao, Ford-Mozilla Open Web Fellow">
					<meta name="robots" content="index, follow">

					<!-- icons -->
                    <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
					<link rel="shortcut icon" href="../assets/img/ALTwitter.gif">
					

					<!-- Bootstrap Core CSS file -->
					<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

					<!-- Override CSS file - add your own CSS rules -->
					<link rel="stylesheet" href="../assets/css/styles.css">

				</head>

				<body>

				<!-- Navigation -->
				    <nav class="navbar navbar-fixed-top navbar-inverse" role="navigation">
						<div class="container-fluid">
							<div class="navbar-header">
								<a class="navbar-brand" href="../index.html"><span class="glyphicon glyphicon-home"></span> <b>ALT</b>witter</a>
							</div>
						</div>
						<!-- /.container-fluid -->
					</nav>
					<!-- /.navbar -->

				<!-- Page Content -->
					<div class="container-fluid">
						<div class="row">
							<div class="col-sm-8 col-sm-push-4 ">
								<div class="panel panel-default">
									<div class="panel-body" style="background-color:#87CEFA"><p>We analyzed {{ num_tweets_analyzed }} tweets from <span class="glyphicon glyphicon-time"></span> {{ from_timestamp }} to <span class="glyphicon glyphicon-time"></span> {{ to_timestamp }} ({{ num_days }} days). <b>{{ retweets }}</b> out of these <b>{{ num_tweets_analyzed }}</b> tweets by <b>{{ name }}</b> were re-tweets, which is <b>{{ tweet_RT_perc }}</b>%.</p>
                                    <p> Based on the metadata associated with these, we can understand {{ name }}'s Twitter usage patterns on hourly or weekly basis, timezones, geo-location tags, devices that have been used, etc. </p>
									<p class="small text-center" style="font-weight:bold;">Created on <span class="glyphicon glyphicon-time"></span> {{ created_timestamp }}</p>
								    </div>
                                </div>
                                
                                <br>

                                <div class="panel panel-default">
                                        <div class="panel-heading">
                                            <h4 class="panel-title" style="font-weight: bold">Hourly Twitter activities according to the metadata.</h4>
                                        </div>
                                        <div class="panel-body">
            								<figure class="margin-b-2">
            									<img class="img-responsive" style="width:650px" src="../assets/img/hourly/{{ twiiter_handle }}_hourly.svg" alt="Hourly Activities">
            								</figure>
                                </div>
                                </div>

                                <div class="panel panel-default">
                                        <div class="panel-heading">
                                            <h4 class="panel-title" style="font-weight: bold">Weekly Twitter activities according to the metadata.</h4>
                                        </div>
                                    <div class="panel-body">
        								<figure class="margin-b-2">
        									<img class="img-responsive" style="width:650px" src="../assets/img/weekly/{{ twiiter_handle }}_weekly.svg" alt="Weekly Activities">
        								</figure>
                                     </div>
                                </div>
                                <div class="row">

                                <div class="col-md-6">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                                <h4 class="panel-title" style="font-weight: bold">Top 5 most retweeted users</h4>
                                            </div>

                                            <div class="panel-body">
                                            <dl class="dl-horizontal">
                                                        {% for rt_names_key, rt_names_value in rt_names_data.items %}
                                                                {% for rt_names_per_key, rt_names_percentage in rt_names_data_percentage.items %}
                                                                        {% ifequal rt_names_key rt_names_per_key %}
                                                                                <dt> {{ rt_names_key }} </dt> <dd> {{ rt_names_value }} ({{ rt_names_percentage }}%)</dd>
                                                                            {% endifequal %}
                                                                    {% endfor %}
                                                            {% endfor %}
                                                    </dl>
                                        </div>
                                    </div>
                                </div>

                                <div class="col-md-6">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                                <h4 class="panel-title" style="font-weight: bold">Top 5 most mentioned users</h4>
                                            </div>

                                            <div class="panel-body">
                                            <dl class="dl-horizontal">
                                                        {% for mntn_names_key, mntn_names_value in mntn_names_data.items %}
                                                                {% for mntn_names_per_key, mntn_names_percentage in mntn_names_data_percentage.items %}
                                                                        {% ifequal mntn_names_key mntn_names_per_key %}
                                                                                <dt> {{ mntn_names_key }} </dt> <dd> {{ mntn_names_value }} ({{ mntn_names_percentage }}%)</dd>
                                                                            {% endifequal %}
                                                                    {% endfor %}
                                                            {% endfor %}
                                                    </dl>
                                        </div>
                                    </div>
                                </div>


                                <div class="col-md-6">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            <h4 class="panel-title" style="font-weight: bold">Top 10 hashtags</h4>
                                        </div>

                                        <div class="panel-body">
                                            <dl class="dl-horizontal">
                                              {% for hashtag_key, hashtag_value in hashtag_data.items %}
                                                {% for hashtag_per_key, hashtag_percentage in hashtag_data_percentage.items %}
                                                    {% ifequal hashtag_key hashtag_per_key %}
                                                        <dt> {{ hashtag_key }} </dt> <dd> {{ hashtag_value }} ({{ hashtag_percentage }}%)</dd>
                                                    {% endifequal %}
                                                {% endfor %}
                                              {% endfor %}
                                            </dl>
                                        </div>
                                    </div>
                                </div>

                                <div class="col-md-6">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                                <h4 class="panel-title" style="font-weight: bold">Most referenced websites</h4>
                                            </div>

                                            <div class="panel-body">
                                            <dl class="dl-horizontal">
                                                        {% for domains_key, domains_value in domains_data.items %}
                                                                {% for domains_per_key, domains_percentage in domains_data_percentage.items %}
                                                                        {% ifequal domains_key domains_per_key %}
                                                                                <dt> {{ domains_key }} </dt> <dd> {{ domains_value }} ({{ domains_percentage }}%)</dd>
                                                                            {% endifequal %}
                                                                    {% endfor %}
                                                            {% endfor %}
                                                    </dl>
                                        </div>
                                    </div>
                                </div>
                                </div>

								<!-- Pager -->
								<nav>
									<ul class="pager">
										<li class="previous"><a href="{{ prev_mep }}.html"><span class="glyphicon glyphicon-menu-left" aria-hidden="true"></span> Previous</a></li>
										<li class="next"><a href="{{ next_mep }}.html">Next <span class="glyphicon glyphicon-menu-right" aria-hidden="true"></span></a></li>
									</ul>
								</nav>
							</div>

							<div class="col-sm-4 col-sm-pull-8">
								<figure class="margin-b-2">
										<img class="img-responsive" width="300" height="300" src="../assets/img/profiles/{{ profile_image_name }}" alt="Profile Image">
										<figcaption class="margin-t-h"><h4 class="text-capitalize" style="font-weight: bold">{{ name }}</h4> <br>
											<b>@{{ twiiter_handle }}</b>
                                            <br>
                                            Account created on <span class="glyphicon glyphicon-time"></span> {{ created_at }}.
								 		</figcaption>
								</figure>
                                

								<!-- Panel -->
								<div class="panel panel-default">
									<div class="panel-heading">
										<h4 class="panel-title">Profile info</h4>
									</div>
									<div class="panel-body">
										<p>{{ profile_desc }}</p>
                                        <hr>
                                        <dl class="dl-horizontal">
                                            <dt>Location</dt> <dd>{{ location }}</dd>
                                            <dt>Following <span class="glyphicon glyphicon-user" style="color:#337ab7;"></span></dt><dd> {{ Following }}</dd>
                                            <dt>Followers <span class="glyphicon glyphicon-user" style="color:#337ab7;"></span></dt><dd> {{ Followers }}</dd>
                                            <dt>Total Tweets</dt><dd> {{ total_tweets }}</dd>
                                        </dl>                                  
									</div>
								</div>

								<div class="panel panel-default">
									<div class="panel-heading">
										<h4 class="panel-title">Meta info</h4>
									</div>
									<div class="panel-body">
										<dl class="dl-horizontal">
                                            <dt>Language</dt> <dd> {{ languages }}</dd>
                                            <dt>Managed by multiple people?</dt> <dd> {{ Contributors }}</dd>
                                            <dt>Geo Enabled</dt> <dd> {{ geo_enabaled }}</dd>
                                            <dt>Time Zone</dt> <dd> {{ time_zone }}</dd>
                                            <dt>UTC offset</dt> <dd> {{ UTC_offset }}</dd>
                                            <dt>Tweets /Day</dt> <dd> {{ avg_tweets_per_day }}</dd>
										</dl>
									</div>
								</div>

                                <div class="panel panel-default">
                                    <div class="panel-heading">
                                        <h4 class="panel-title" style="font-weight: bold">Detected languages</h4>
                                    </div>

                                    <div class="panel-body">
                                        <dl class="dl-horizontal">
                                            {% for lang_key, lang_value in lang_data.items %}
                                                {% for lang_per_key, lang_percentage in lang_data_percentage.items %}
                                                    {% ifequal lang_key lang_per_key %}
                                                        <dt class="text-uppercase"> {{ lang_key }} </dt> <dd> {{ lang_value }} ({{ lang_percentage }}%)</dd>
                                                    {% endifequal %}
                                                {% endfor %}
                                            {% endfor %}
                                        </dl>
                                    </div>
                                </div>

                                <div class="panel panel-default">
                                    <div class="panel-heading">
                                        <h4 class="panel-title" style="font-weight: bold">Detected Sources</h4>
                                    </div>

                                    <div class="panel-body">
                                        <dl class="dl-horizontal">
                                            {% for source_key, source_value in source_data.items %}
                                                {% for source_per_key, source_percentage in source_data_percentage.items %}
                                                    {% ifequal source_key source_per_key %}
                                                        <dt> {{ source_key }} </dt> <dd> {{ source_value }} ({{ source_percentage }}%)</dd>
                                                    {% endifequal %}
                                                {% endfor %}
                                            {% endfor %}
                                        </dl>
                                    </div>
                                </div>

                                <div class="panel panel-default">
                                    <div class="panel-heading">
                                        <h4 class="panel-title" style="font-weight: bold">Detected places ({{ geo_enabled_tweets }} found)</h4>
                                    </div>

                                    <div class="panel-body">
                                        <dl class="dl-horizontal">
                                            {% for place_key, place_value in place_data.items %}
                                                {% for place_per_key, place_percentage in place_data_percentage.items %}
                                                    {% ifequal place_key place_per_key %}
                                                        <dt> {{ place_key }} </dt> <dd> {{ place_value }} ({{ place_percentage }}%)</dd>
                                                    {% endifequal %}
                                                {% endfor %}
                                            {% endfor %}
                                        </dl>
                                    </div>
                                </div>




							</div>
						</div>
						<!-- /.row -->

						<hr>
						<footer class="margin-tb-3 text-center">
                            <div class="row">
                                <div class="container">
                                    <p>Made with <span class="glyphicon glyphicon-heart" style="color:red"></span> by <a href="https://twitter.com/sidnext2none">Sid Rao</a>
                                    <br>
                                    <a href="https://advocacy.mozilla.org/en-US/open-web-fellows/fellows2016">Ford-Mozilla Open Web Fellow</a> 
                                    <br>
                                    <a href="https://edri.org/"><h4>European Digital Rights (EDRi)</h4></a>
                                    </p>
                                </div>
                            </div>
                        </footer>
					</div>
					<!-- /.container-fluid -->

					<!-- JQuery scripts -->
				    <script src="assets/js/jquery-1.11.2.min.js"></script>

					<!-- Bootstrap Core scripts -->
					<script src="assets/js/bootstrap.min.js"></script>
			  </body>
			</html>
			"""

  

    retweeted_users_names = {}
    for k in retweeted_users.keys():
        retweeted_users_names[id_screen_names[k]] = retweeted_users[k]

    mentioned_users_names = {}
    for k in mentioned_users.keys():
        mentioned_users_names[id_screen_names[k]] = mentioned_users[k]

    (hashtag_slice, hashtag_slice_percentage) = get_dictionary_with_percentages(detected_hashtags, 10)
    (lang_slice, lang_slice_percentage) = get_dictionary_with_percentages(detected_langs)
    (source_slice, source_slice_percentage) = get_dictionary_with_percentages(detected_sources)
    (place_slice, place_slice_percentage) = get_dictionary_with_percentages(detected_places)
    (domains_slice, domains_slice_percentage) = get_dictionary_with_percentages(detected_domains, 10)
    (rt_names_slice, rt_names_slice_percentage) = get_dictionary_with_percentages(retweeted_users_names)
    (mntn_names_slice, mntn_names_slice_percentage) = get_dictionary_with_percentages(mentioned_users_names)

   
    try:
        name_shown = user_info.name.encode('utf-8')
    except UnicodeEncodeError:
        name_shown = user_info.name.encode('ascii', 'ignore').decode('ascii')

    try:
        clean_description = user_info.description.encode('utf-8')
    except UnicodeEncodeError:
        clean_description = user_info.description.encode('ascii', 'ignore').decode('ascii')


    curr_item = args.name
    try:
        curr_index = full_list_mep.index(curr_item) 
        if curr_index == 0:
            prev_v = "index"
        else:
            prev_v = full_list_mep[curr_index -1]

        if curr_index == len(full_list_mep)-1:
            next_v = "index"
        else:
            next_v = full_list_mep[curr_index +1]
    except ValueError:
        prev_v ="null"
        next_v ="null"



    t = Template(template)
    c = Context({"name": name_shown,
    	"num_tweets_analyzed": num_tweets,
    	"from_timestamp": str(start_date),
    	"to_timestamp": str(end_date),
    	"num_days": num_dates, 
    	"twiiter_handle": args.name,
    	"profile_desc": clean_description,
    	"location": user_info.location,
    	"languages": str(user_info.lang).upper(),
    	"geo_enabaled": user_info.geo_enabled,
    	"time_zone": str(user_info.time_zone),
    	"UTC_offset": str(user_info.utc_offset),
        "created_timestamp": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        "Following":user_info.friends_count,
        "Followers": user_info.followers_count,
        "Contributors": user_info.contributors_enabled,
        "total_tweets": user_info.statuses_count,
        "avg_tweets_per_day": avg_tweets_per_day,
        "created_at": str(user_info.created_at.date().strftime("%A %d %B, %Y")),
        "retweets":retweets,
        "tweet_RT_perc": tweet_RT_perc,
        "hashtag_data": hashtag_slice,
        "hashtag_data_percentage": hashtag_slice_percentage,
        "lang_data": lang_slice,
        "lang_data_percentage": lang_slice_percentage,
        "source_data": source_slice,
        "source_data_percentage": source_slice_percentage,
        "place_data": place_slice,
        "place_data_percentage": place_slice_percentage,
        "geo_enabled_tweets": geo_enabled_tweets,
        "domains_data": domains_slice,
        "domains_data_percentage": domains_slice_percentage,
        "rt_names_data": rt_names_slice,
        "rt_names_data_percentage": rt_names_slice_percentage,
        "mntn_names_data": mntn_names_slice,
        "mntn_names_data_percentage": mntn_names_slice_percentage,
        "profile_image_name": curr_profile_image_name,
        "prev_mep": prev_v,
        "next_mep": next_v
        })

    f1=open(args.name+'.html', 'w+')
    try:
        f1.write(t.render(c).encode('utf-8'))
    except UnicodeEncodeError:
        f1.write(t.render(c).encode('ascii', 'ignore').decode('ascii'))

    f1.close()

    print "###################################################################################"
    print "###################################################################################"

   

if __name__ == '__main__':
    main()

    	