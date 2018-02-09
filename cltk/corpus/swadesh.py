"""Generate Swadesh lists for classical languages"""

__author__ = ['Patrick J. Burns <patrick@diyclassics.org>']
__license__ = 'MIT License. See LICENSE.'

swadesh_la = ['ego', 'tū', 'is, ea, id', 'nōs', 'vōs', 'eī, iī, eae, ea', 'hic, haec, hoc', 'ille, illa, illud', 'hīc', 'illic, ibi', 'quis, quae', 'quid', 'ubi', 'cum', 'quōmodō', 'nōn, nē', 'omnēs, omnia', 'multī, multae, multa', 'aliquī, aliqua, aliquod', 'paucī, paucae, pauca', 'alter, alius', 'ūnus', 'duō', 'trēs', 'quattuor', 'quīnque', 'magnus', 'longus', 'lātus', 'crassus', 'gravis', 'parvus', 'brevis', 'angustus', 'gracilis', 'fēmina', 'vir', 'homō', 'puer', 'uxor, mulier', 'marītus', 'māter', 'pater', 'animal', 'piscis', 'avis', 'canis', 'pēdīculus', 'serpens', 'vermis', 'arbor', 'silva', 'hasta, pālus', 'fructus', 'sēmen', 'folium', 'rādix', 'cortex', 'flōs', 'herba', 'chorda', 'cutis', 'carō', 'sanguis', 'os', 'pinguāmen', 'ōvum', 'cornū', 'cauda', 'penna', 'pilus', 'caput', 'auris', 'oculus', 'nāsus, nāris', 'ōs', 'dens', 'lingua', 'unguis', 'pēs', 'crūs', 'genū', 'manus', 'āla', 'venter, abdōmen', 'viscera', 'cervix', 'dorsum', 'mamma', 'cor', 'iecur', 'bibere', 'edere', 'mordēre', 'sūgere', 'spuere', 'vomere', 'īnflāre', 'respīrāre', 'rīdēre', 'vidēre', 'audīre', 'scīre', 'cōgitāre, putāre, existimāre', 'olfacere', 'timēre', 'dormīre', 'vīvere', 'morī', 'necāre', 'luctārī', 'vēnārī', 'pellere', 'secāre', 'dīvidere', 'pungere', 'scabere', 'fodere', 'nāre, natāre', 'volāre', 'ambulāre', 'venīre', 'cubāre', 'sedēre', 'stāre', 'vertere', 'cadere', 'dare', 'tenēre', 'exprimere', 'fricāre', 'lavāre', 'tergēre', 'trahere', 'pellere', 'iacere', 'ligāre', 'cōnsuere', 'computāre, numerāre', 'dīcere', 'canere', 'ludere', 'fluctuāre', 'fluere', 'gelāre', 'augēre', 'sol', 'lūna', 'stella', 'aqua', 'pluvia', 'flūmen, fluvius, amnis', 'lacus', 'mare', 'sal', 'saxum, lapis, petra', 'harēna', 'pulvis', 'humus, terra, ager', 'nūbēs, nebula', 'cālīgō, nebula, tenebrae', 'caelum', 'ventus', 'nix', 'gelū', 'fūmus', 'ignis', 'cinis', 'ūrere, flammāre', 'via', 'mons', 'ruber, rūfus', 'viridis', 'croceus', 'albus, candidus', 'āter, niger', 'nox', 'dies', 'annus', 'calidus', 'frigidus', 'plēnus', 'novus', 'vetus', 'bonus', 'malus', 'putridus', 'immundus', 'rectus', 'rotundus', 'acūtus', 'hebes', 'suāvis', 'humidus, aqueus', 'siccus', 'rectus', 'propinquus, proximus', 'longus', 'dexter', 'laevus, sinister', 'ad, in', 'in', 'cum', 'et, -que', 'si', 'quod', 'nōmen']

swadesh_gr = ['ἐγώ', 'σύ', 'αὐτός, οὗ, ὅς, ὁ, οὗτος', 'ἡμεῖς', 'ὑμεῖς', 'αὐτοί', 'ὅδε', 'ἐκεῖνος', 'ἔνθα, ἐνθάδε, ἐνταῦθα', 'ἐκεῖ', 'τίς', 'τί', 'ποῦ, πόθι', 'πότε, πῆμος', 'πῶς', 'οὐ, μή', 'πᾶς, ἅπᾱς', 'πολύς', 'τις', 'ὀλίγος, βαιός, παῦρος', 'ἄλλος, ἕτερος', 'εἷς', 'δύο', 'τρεῖς', 'τέσσαρες', 'πέντε', 'μέγας', 'μακρός', 'εὐρύς', 'πυκνός', 'βαρύς', 'μῑκρός', 'βραχύς', 'στενός', 'μανός', 'γυνή', 'ἀνήρ', 'ἄνθρωπος', 'τέκνον, παῖς, παιδίον', 'γυνή', 'ἀνήρ', 'μήτηρ', 'πατήρ', 'ζῷον', 'ἰχθύς', 'ὄρνις, πετεινόν', 'κύων', 'φθείρ', 'ὄφις', 'ἑρπετόν, σκώληξ, ἕλμινς', 'δένδρον', 'ὕλη', 'βακτηρία, ῥάβδος', 'καρπός', 'σπέρμα', 'φύλλον', 'ῥίζα', 'φλοιός', 'ἄνθος', 'χλόη', 'δεσμός, σχοινίον', 'δέρμα', 'κρέας', 'αἷμα', 'ὀστοῦν', 'δημός', 'ᾠόν', 'κέρας', 'οὐρά, κέρκος', 'πτερόν', 'θρίξ, κόμη', 'κεφαλή', 'οὖς', 'ὀφθαλμός', 'ῥίς', 'στόμα', 'ὀδούς', 'γλῶσσα', 'ὄνυξ', 'πούς', 'κῶλον, σκέλος', 'γόνυ', 'χείρ', 'πτέρυξ', 'γαστήρ, κοιλία', 'ἔντερα, σπλάγχνα', 'αὐχήν, τράχηλος', 'νῶτον', 'μαστός, στῆθος', 'καρδία', 'ἧπαρ', 'πίνω', 'ἐσθίω, ἔφαγον', 'δάκνω', 'σπάω', 'πτύω', 'ἐμέω', 'φυσάω', 'πνέω', 'γελάω', 'βλέπω, ὁράω, εἶδον', 'ἀκούω, ἀΐω', 'οἶδα, γιγνώσκω', 'νομίζω, δοκέω, νοέω, οἴομαι', 'ὀσφραίνομαι', 'φοβέομαι', 'καθεύδω, εὕδω, εὐνάζομαι, κοιμάομαι, ἰαύω', 'ζάω, βιόω, οἰκέω', 'ἀποθνῄσκω, θνῄσκω, τελευτάω, ὄλομαι', 'ἀποκτείνω, ἔπεφνον', 'μάχομαι', 'θηρεύω, θηράω, ἰχνεύω, κυνηγετέω, κυνηγέω, σεύω', 'τύπτω', 'τέμνω', 'σχίζω', 'κεντέω', 'κνάω', 'ὀρύσσω, σκᾰ́πτω', 'νέω, κολυμβάω', 'πέτομαι', 'περιπατέω, πατέω, στείχω, βαίνω, βαδίζω, πεζεύω, πορεύω', 'ἱκνέομαι, ἵκω, ἔρχομαι, εἶμι', 'κεῖμαι', 'καθίζω', 'ἵστημι', 'τρέπω', 'πίπτω', 'παρέχω, δίδωμι', 'ἔχω', 'πιέζω', 'τρίβω', 'λούω, πλύνω, νίπτω', 'ἀπομάσσω', 'ἕλκω', 'ὠθέω', 'ῥίπτω, βάλλω', 'δέω', 'ῥάπτω', 'ἀριθμέω', 'φημί, λέγω, ἐνέπω', 'ἀείδω', 'παίζω', 'νέω', 'ῥέω', 'πήγνυμαι', 'αὐξάνω', 'ἥλιος', 'σελήνη', 'ἀστήρ', 'ὕδωρ', 'ὑετός, βροχή', 'ποταμός', 'λίμνη', 'θάλασσα, πέλαγος, πόντος', 'ἅλς', 'λίθος', 'ἄμμος', 'κόνις', 'γῆ, χθών', 'νέφος', 'ὀμίχλη', 'οὐρανός', 'ἄνεμος', 'χιών', 'κρύσταλλος', 'καπνός', 'πῦρ', 'τέφρα', 'καίω', 'ὁδός', 'ἄκρα, ὄρος, βουνός', 'ἐρυθρός, πυρρός', 'χλωρός', 'ξανθός', 'λευκός', 'μέλας', 'νύξ', 'ἡμέρα, ἦμαρ', 'ἔτος', 'θερμός', 'ψυχρός', 'μεστός, πλήρης', 'νέος', 'παλαιός', 'ἀγαθός', 'κακός', 'σαπρός', 'θολερός', 'εὐθύς, ὀρθός', 'κυκλοτερής', 'τομός, ὀξύς', 'ἀμβλύς, βαρύς', 'λεῖος', 'ὑγρός', 'ξηρός', 'δίκαιος', 'ἐγγύς', 'μακράν', 'δεξιός', 'ἀριστερός, εὐώνυμος', 'ἐν', 'ἐν', 'μετά, σύν', 'καί, τε', 'εἰ', 'ὅτι', 'ὄνομα']

swadesh_txb = ['ñäś', 'tuwe', 'su', 'wes', 'yes', 'cey', 'se', 'su, samp', 'tane', 'tane, omp', 'kᵤse', 'kᵤse', 'ente', 'ente', 'mäkte', 'mā', 'poñc', 'māka', 'ṣemi', 'totka', 'allek', 'ṣe', 'wi', 'trey', 'śtwer', 'piś', 'orotstse', 'pärkare', 'aurtstse', '', 'kramartse', 'lykaśke, totka', '', '', '', 'klyiye, śana', 'eṅkwe', 'śaumo', 'śamaśke', 'śana', 'petso', 'mācer', 'pācer', 'luwo', 'laks', 'salamo luwo', 'ku', 'pärśeriñ', 'arṣāklo, auk', 'yel', 'stām', 'wartto, karāś', 'śakātai', 'oko', 'sārm, śäktālye', 'pilta', 'witsako', 'enmetre', 'pyāpyo', 'atiyai', '', 'ewe, yetse', 'misa', 'yasar', 'āy, āsta pl', 'ṣalype', '', 'krorīyai', 'pako', 'paruwa', 'matsi', 'āśce', 'klautso', 'ek', 'meli', 'koyṃ', 'keme', 'kantwo', '', 'paiyye', 'ckāckai', 'keni', 'ṣar', '', 'kātso', 'kātso', 'kor', 'sark', 'päścane', 'arañce', 'wästarye', 'yokäṃ', 'śuwaṃ', '', '', 'pitke', 'aṅkaiṃ', 'pinaṣṣnäṃ', 'anāṣṣäṃ, satāṣṣäṃ', 'ker-', 'lkāṣṣäṃ', 'klyauṣäṃ', 'aiśtär, kärsanaṃ', 'pälskanaṃ', 'warṣṣäṃ', 'prāskaṃ', 'kläntsaṃ', 'śaiṃ', 'sruketär', 'kauṣäṃ', 'witāre', 'śerītsi', 'karnäṣṣäṃ', 'karsnaṃ, latkanaṃ', 'kautanaṃ', 'tsopäṃ', '', 'rapanaṃ', 'nāṣṣäṃ', 'pluṣäṃ', 'yaṃ', 'känmaṣṣäṃ', 'lyaśäṃ', 'ṣamäṃ, āṣṣäṃ', 'kaltär', 'kluttaṅktär, sporttotär', 'kloyotär', 'aiṣṣäṃ', '', 'klupnātär, nuskaṣṣäṃ', 'lyuwetär, kantanatär', 'laikanatär', 'lyyāstär', 'slaṅktär', 'nätkanaṃ', 'karṣṣäṃ, saläṣṣäṃ', 'śanmästär, kärkaṣṣäṃ', '', 'ṣäṃṣtär', 'weṣṣäṃ', 'piyaṃ', 'kāñmäṃ', 'pluṣäṃ', 'reṣṣäṃ', '', 'staukkanatär', 'kauṃ', 'meñe', 'ścirye', 'war', 'swese', 'cake', 'lyam', 'samudtär', 'salyiye', 'kärweñe', 'warañc', 'tweye, taur', 'keṃ', 'tarkär', '', 'iprer', 'yente', 'śiñcatstse', '', '', 'puwar', 'taur, tweye', 'tsakṣtär,pälketär', 'ytārye', 'ṣale', 'ratre', 'motartstse', 'tute', 'ārkwi', 'erkent-', 'yṣiye', 'kauṃ', 'pikul', 'emalle', 'krośce', 'ite', 'ñuwe', 'ktsaitstse', 'kartse', 'yolo, pakwāre', 'āmpau', 'sal, kraketstse', '', '', 'mātre, akwatse', 'mālle', 'ṣmare', 'karītstse', 'asāre', '', 'akartte, ysape, etsuwai', 'lau, lauke', 'saiwai', 'śwālyai', '-ne', '-ne', 'śle', 'ṣp', 'krui, ente', 'kuce, mäkte', 'ñem']

swadesh_pt_old = ['eu', 'tu', 'ele', 'nos', 'vos', 'eles', 'esto, aquesto', 'aquelo', 'aqui', 'ali', 'quen', 'que', 'u', 'quando', 'como', 'non', 'todo', 'muito', 'algũus', 'pouco', 'outro', 'un, ũu', 'dous', 'tres', 'quatro', 'cinco', 'grande, gran', 'longo', 'ancho', 'grosso', 'pesado', 'pequeno', 'curto', 'estreito', 'magro', 'moller, dona', 'ome', 'ome, pessõa', 'infante, meninno, creatura', 'moller', 'marido', 'madre, mãi', 'padre, pai', 'besta, bestia, bescha', 'peixe', 'ave', 'can', 'peollo', 'coobra', 'vermen', 'arvor', 'furesta, mata, monte', 'baston, pao', 'fruita, fruito', 'semente', 'folla', 'raiz', 'cortiça', 'fror, flor', 'erva', 'corda', 'pele', 'carne', 'sangui, sangue', 'osso', 'gordura', 'ovo', 'corno', 'rabo', 'pena', 'cabelo', 'cabeça', 'orella', 'ollo', 'nariz', 'boca', 'dente', 'lingua', 'unna, unlla', 'pee, pe', 'perna', 'gẽollo', 'mão', 'aa', 'ventre', 'tripas', 'colo', 'costas', 'peito, sẽo', 'coraçon', 'figado', 'bever', 'comer', 'morder', 'mamar', 'cospir', '', 'soprar', '', 'riir', 'veer', 'ouvir, oir, ascuitar', 'saber', 'pensar', 'cheirar', 'temer', 'dormir', 'viver', 'morrer', 'matar', 'pelejar', 'caçar', 'bater', 'cortar, partir', '', 'acuitelar', 'rascar', 'cavar', 'nadar', 'voar', 'andar', 'vĩir', 'jazer, deitar', 'sentar', 'levantar', '', 'caer', 'dar', 'tẽer', 'apertar', '', 'lavar', 'terger, enxugar', 'puxar', 'empuxar', 'lançar', 'atar', 'coser', 'contar', 'contar, dizer, falar', 'cantar', 'jogar', 'boiar', 'correr', 'gelar, *gear', 'inchar', 'sol', 'lũa', 'estrela', 'agua', 'chuvia', 'rio', 'lago', 'mar', 'sal', 'pedra', 'arẽa', 'poo', 'terra', 'nuve', 'nevoeiro', 'ceo', 'vento', 'neve', 'geo', 'fumo, fumaz', 'fogo', 'cĩisa', 'queimar, arder', 'caminno, via', 'montanna, monte', 'vermello', 'verde', 'amarelo', 'branco', 'negro', 'noite', 'dia', 'ano', 'caente', 'frio', 'chẽo', 'novo', 'vello, antigo', 'bon, bõo', 'mal, mao', 'podre', 'lixoso', 'estreito', 'redondo', 'amoado', 'romo', 'chão', 'mollado', 'seco', 'reito, dereito', 'preto', 'longe', 'dereita', 'sẽestra', 'a', 'en', 'con', 'e', 'se', 'porque', 'nome']

swadesh_eng_old = ['ic, iċċ, ih', 'þū', 'hē', 'wē', 'ġē', 'hīe', 'þēs, þēos, þis', 'sē, sēo, þæt', 'hēr', 'þār, þāra, þǣr, þēr', 'hwā','hwā, hwæt', 'hwǣr', 'hwanne, hwænne, hwenne', 'hū', 'ne', 'eall', 'maniġ, feola, fela', 'sum', 'fēaw, lyt', 'ōþer', 'ān', 'twēġen, twā, tū', 'þrīe, þrēo', 'fēower', 'fīf', 'grēat, stōr', 'lang, long', 'wīd, brād', 'þicce', 'hefiġ', 'smæl', 'scort, sceort', 'eng, nearu', 'þynn', 'ides, cwēn, wīfmann', 'wer, guma', 'mann', 'ċild, bearn, umbor', 'wīf', 'bunda, banda, hūsbonda', 'mōdor', 'fæder', 'dēor', 'fisc', 'fugol', 'hund', 'lūs', 'snaca', 'wyrm', 'trēo, bēam', 'weald, fyrhþ', 'sticca', 'wæstm, blǣd, ofett', 'sǣd', 'blæd, lēaf', 'wyrt', 'rind', 'blǣd, blōstma', 'græs, gærs', 'rāp, līne, sāl', 'hȳd', 'flǣsc', 'blōd', 'bān', 'fǣtt', 'ǣġ','horn', 'steort, tæġl', 'feþer', 'hǣr, hēr', 'hēafod, hafola', 'ēare', 'ēaġe', 'nosu', 'mūþ', 'tōþ', 'tunge', 'fingernæġel', 'fōt', 'scanca', 'cnēo', 'hand', 'feþera', 'būc', 'þearm', 'heals, hnecca', 'hryċġ, bæc', 'brēost', 'heorte', 'lifer', 'drincan', 'etan', 'bītan', 'sūgan, sūcan', 'spittan, hrǣċan', 'spīwan', 'blāwan', 'ōþian, ēþian', 'hliehhan', 'sēon', 'hīeran', 'witan, cnāwan', 'þenċan', 'ēþian, stincan', 'andrǣdan', 'slǣpan', 'libban, lifian', 'steorfan', 'cwellan', 'feohtan', 'huntian', 'hittan, slēan', 'snīþan', 'splātan, clēofan', 'snǣsan, stingan, stician', 'screpan, clifrian, pliċġan, clāwian', 'grafan', 'swimman, flēotan', 'flēoġan', 'gangan, onsteppan', 'cuman', 'liċġan', 'sittan', 'standan', 'ċierran, hwierfan', 'feallan', 'ġiefan', 'healdan', 'þringan, cwȳsan', 'gnīdan', 'wascan', 'wīpian', 'dragan, pullian', 'scūfan, þyddan, hrindan, potian', 'weorpan', 'bindan, tīeġan', 'sīwian, sēowian', 'tellan', 'cweþan, seċġan', 'singan', 'lācan, pleġan', 'flēotan, flotian, floterian', 'flōwan', 'frēosan', 'swellan', 'sōl, sunne', 'mōna', 'steorra, tungol', 'wæter', 'reġn', 'ēa, flōd, strēam', 'mere, lacu', 'sǣ', 'sealt', 'stān', 'sand', 'dūst, dust', 'eorþe', 'wolcen', 'mist', 'rodor, lyft', 'wind', 'snāw', 'īs', 'rēc, smoca', 'fȳr', 'æsc', 'beornan, biernan, bærnan, ǣlan', 'weġ, pæþ', 'beorg', 'rēad', 'grēne', 'ġeolu', 'hwīt', 'sweart, blæc', 'neaht, niht', 'dōgor, dæġ', 'ġēar', 'wearm', 'ceald','full', 'nēowe, nīwe', 'gamol, eald', 'gōd', 'yfel', 'fūl', 'ādeliht, sol', 'ġerād, ġereclīc', 'hwyrflede, seonuwealt', 'scearp', 'dol, dwæs','slīc, slieht, smēþe, smōþ','wǣt','sēar, drȳġe', 'riht','nēah','wīd, feor','reht, riht','winstre','on, æt','in', 'mid', 'and', 'ġif', 'forþon', 'nama']

swadesh_old_norse = ["ek", "þú", "hann", "vér", "þér", "þeir", "sjá, þessi", "sá", "hér", "þar", "hvar", "hvat", "hvar", "hvenær", "hvé", "eigi", "allr", "margr", "nǫkkurr", "fár", "annarr", "einn", "tveir", "þrír", "fjórir", "fimm", "stórr", "langr", "breiðr", "þykkr", "þungr", "lítill", "stuttr", "mjór", "þunnr", "kona", "karl", "maðr", "barn", "kona", "bóndi", 'móðir', "faðir", "dýrr", "fiskr", "fugl", "hundr", "lús", "snókr", "ormr", "tré", "skógr", "stafr", "ávǫxtr", "fræ", "lauf", "rót", "bǫrkr", "blóm", "gras", "reip", "húð", "kjǫt", "blóð", "bein", "fita", "egg", "horn", "hali", "fjǫðr", "hár", "hǫfuð", "eyra", "auga", "nef", "munnr", "tǫnn", "tunga", "nagl", "fótr", "leggr", "kné", "hǫnd", "vængr", "magi", "iinyfli", "hals" , "bak", "brjóst", "hjarta", "lifr", "drekka", "eta", "bíta", "súga", "spýta", ", hrækja", None, "blása", "anda", "hlæja", "sjá", "heyra", "vita", "þýkkja", "þefa", "ugga", "sofa", "lifa", "deyja", "drepa", "hals", "bak", "berja", "skera", "kljúfa""stinga", "klóra", "grafa", "synda", "fljúga", "ganga", "koma", "liggja", "sitja", "standa", "snúa", "falla", "gefa", "halda", "kreista", "gnúa","þvá", "þurka", "draga", "ýta", "kasta", "kasta", "binda", "sauma", "telja", "segja", "syngja", "leika", "flóta", "streyma", "frjósa", "þrútna", "sól", "tungl", "stjarna", "vatn", "regn", "á", "vatn", "hav", "salt", "steinn", "sandr", "ryk", "jörð", "ský", "þoka", "himinn", "vindr", "snjór", "íss", "reykr", "ild", "eldr", "aska", "brenna", "vegr", "fjall", "rauðr", "grœnn", "gulr", "hvítr", "svartr", "nótt", "dagr", "ár", "heitr", "kaldr", "fullr", "nýr", "gamall", "góðr", "illr", "rottin", "skitinn", "beinn", "kringlóttr", "beittr", None, "sleipr", "blautr", "	þurr", "réttr", "nálægr", "langr", "hœgr", "vinstri", "hjá","í", "með", "ok", "ef", "því at", "nafn"]  # pylint: disable=line-too-long


class Swadesh():
    def __init__(self, language):
        self.language = language

    def words(self):
        if self.language == 'la':
            return swadesh_la
        elif self.language == 'gr':
            return swadesh_gr
        elif self.language == 'txb':
            return swadesh_txb
        elif self.language == 'pt_old':
            return swadesh_pt_old
        elif self.language == 'eng_old':
            return swadesh_eng_old
        elif self.language == 'old_norse':
            return swadesh_old_norse
