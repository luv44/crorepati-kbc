# build_curriculum/group7_s25.py
# S25: Visual & Identification GK (9 topics across 3 chapters)

DATA = {}

# S25-C92a15c80 National Emblems, Official Seals, State Animal/Bird/Floral Symbols (3 topics)
DATA["S25-C92a15c80"] = [
    {
        "name_en": "National Emblem of India: Lion Capital of Ashoka at Sarnath, Abacus Animals & 'Satyameva Jayate'",
        "name_hi": "भारत का राष्ट्रीय प्रतीक: सारनाथ का अशोक सिंह स्तंभ, आधार चक्र के 4 पशु एवं 'सत्यमेव जयते'",
        "concepts_en": ["Adopted on January 26, 1950 by Government of India; modeled after the Mauryan Lion Capital of Ashoka at Sarnath (erected around 250 BCE)", "Visual Structure: Four Asiatic lions standing back to back (only 3 visible in 2D profile view), symbolizing power, courage, pride, and confidence", "Circular Abacus: Supported on a bell-shaped lotus (omitted in official emblem); bordered by high reliefs of 4 ANIMALS separated by intervening Dharmachakras (wheels with 24 spokes):", "1. Galloping Horse (West - energy, speed)", "2. Striding Bull (South - hard work, steadfastness)", "3. Majestic Lion (North - bravery)", "4. Regal Elephant (East - wisdom, Buddha's conception)", "Motto: 'सत्यमेव जयते' (Satyameva Jayate - Truth Alone Triumphs) inscribed below the abacus in Devanagari script, taken from the ancient Mundaka Upanishad"],
        "concepts_hi": ["26 जनवरी 1950 को भारत सरकार द्वारा आधिकारिक रूप से अपनाया गया; सारनाथ (वाराणसी) में सम्राट अशोक द्वारा 250 ई.पू. में स्थापित 'सिंह स्तंभ' के शीर्ष से लिया गया", "संरचना: एक-दूसरे की ओर पीठ किए हुए 4 एशियाई सिंह (सामने से देखने पर केवल 3 दिखाई देते हैं), जो शक्ति, शौर्य, गर्व और आत्मविश्वास के प्रतीक हैं", "गोल आधार (Abacus): घंटीनुमा कमल के ऊपर (आधिकारिक मुहर में कमल को छोड़ दिया गया है); आधार पर 24 तीलियों वाले धर्मचक्रों के बीच 4 पशुओं की आकृतियां उत्कीर्ण हैं:", "1. घोड़ा (पश्चिम - गति व ऊर्जा), 2. बैल/सांड (दक्षिण - दृढ़ता व परिश्रम), 3. सिंह (उत्तर), 4. हाथी (पूर्व - बुद्ध के गर्भधारण का प्रतीक)", "राष्ट्रीय आदर्श वाक्य: आधार के नीचे देवनागरी में 'सत्यमेव जयते' (सत्य की ही विजय होती है) अंकित है, जो प्राचीन 'मुंडक उपनिषद' से लिया गया है"],
        "q_en": "Which sacred ancient Hindu scripture is the source of India's national motto 'सत्यमेव जयते' (Satyameva Jayate - Truth Alone Triumphs), inscribed below the National Emblem?",
        "q_hi": "भारत के राष्ट्रीय प्रतीक के नीचे देवनागरी लिपि में उत्कीर्ण राष्ट्रीय आदर्श वाक्य 'सत्यमेव जयते' (सत्य की ही विजय होती है) किस प्राचीन उपनिषद से लिया गया है?",
        "options_en": ["Mundaka Upanishad (मुंडक उपनिषद)", "Mandukya Upanishad", "Chandogya Upanishad", "Katha Upanishad"],
        "options_hi": ["मुंडक उपनिषद (Mundaka Upanishad)", "मांडूक्य उपनिषद (Mandukya Upanishad - यह सबसे छोटा उपनिषद है)", "छांदोग्य उपनिषद", "कठ उपनिषद (यम-नचिकेता संवाद)"],
        "correct_idx": 0,
        "exp_en": "The national motto 'Satyameva Jayate' is taken from the famous verse in the Mundaka Upanishad (3.1.6): 'सत्यमेव जयते नानृतं' (Truth alone triumphs, not falsehood). (Often confused with Mandukya Upanishad).",
        "exp_hi": "'सत्यमेव जयते' मंत्र मुंडक उपनिषद के तीसरे मुंडक के प्रथम खंड का छठा मंत्र है: 'सत्यमेव जयते नानृतं सत्येन पन्था विततो देवयानः'।",
        "cue_en": "Satyameva Jayate = Mundaka Upanishad (NOT Mandukya).",
        "cue_hi": "सत्यमेव जयते = मुंडक उपनिषद (मांडूक्य नहीं)।",
        "wrong_en": ["Scriptural origin of Satyameva Jayate.", "Shortest Upanishad (12 verses), not the source.", "Known for Tat Tvam Asi, not this motto.", "Known for Nachiketa dialogue on death."],
        "wrong_hi": ["सत्यमेव जयते का मूल स्रोत।", "सबसे छोटा उपनिषद (गलत विकल्प)।", "छांदोग्य उपनिषद।", "यम-नचिकेता संवाद।"]
    },
    {
        "name_en": "National Flag of India: Tricolor Proportions, Pingali Venkayya, 24-Spoke Ashoka Chakra & Flag Code of India",
        "name_hi": "भारत का राष्ट्रीय ध्वज: तिरंगा अनुपात (3:2), पिंगली वेंकैया, 24 तीलियों का अशोक चक्र एवं भारतीय ध्वज संहिता (2002)",
        "concepts_en": ["Designed by freedom fighter Pingali Venkayya of Andhra Pradesh; adopted by the Constituent Assembly on July 22, 1947", "Dimensional Ratio: Aspect ratio of length to height (width) is strictly 3 : 2", "Color Symbolism:", "1. Top Saffron (Kesari): Courage and sacrifice", "2. Middle White: Peace, purity, and truth", "3. Bottom Dark Green: Fertility, growth, and auspiciousness of the land", "Ashoka Chakra: High-relief navy blue wheel with 24 equally spaced spokes in the center of the white band, representing the eternal Wheel of Law (Dharmachakra from Sarnath); symbolizes motion, progress, and 24 hours of virtuous action", "Flag Code of India 2002 (amended in 2021 & 2022 to permit machine-made polyester flags and day/night hoisting under Har Ghar Tiranga)"],
        "concepts_hi": ["आंध्र प्रदेश के स्वतंत्रता सेनानी पिंगली वेंकैया द्वारा डिजाइन किया गया; संविधान सभा द्वारा 22 जुलाई 1947 को राष्ट्रीय ध्वज के रूप में अंगीकृत", "आयाम अनुपात: लंबाई और चौड़ाई (ऊंचाई) का अनुपात अनिवार्य रूप से 3 : 2 होता है", "रंगों का अर्थ:", "1. शीर्ष पर गहरा केसरिया: साहस, पराक्रम और बलिदान का प्रतीक", "2. मध्य में सफेद: शांति, सत्य और पवित्रता का प्रतीक", "3. नीचे गहरा हरा: भूमि की उर्वरता, समृद्धि और विकास का प्रतीक", "अशोक चक्र: सफेद पट्टी के केंद्र में गहरे नीले (Navy Blue) रंग का 24 तीलियों वाला चक्र, जो सारनाथ के अशोक सिंह स्तंभ के धर्मचक्र से लिया गया है; यह निरंतर प्रगति और गतिशीलता का प्रतीक है", "भारतीय ध्वज संहिता 2002 (2021 और 2022 में संशोधित, जिससे पॉलिस्टर और मशीन निर्मित तिरंगे की अनुमति मिली)"],
        "q_en": "What is the mandatory legal dimensional ratio of the LENGTH to the BREADTH (height) of the National Flag of India as codified in the Flag Code of India?",
        "q_hi": "भारतीय ध्वज संहिता (Flag Code of India) के अनुसार भारत के राष्ट्रीय ध्वज की 'लंबाई' और 'चौड़ाई' (ऊंचाई) का अनिवार्य वैधानिक अनुपात क्या निर्धारित है?",
        "options_en": ["3 : 2 (तीन अनुपात दो)", "2 : 3", "4 : 3", "5 : 3"],
        "options_hi": ["3 : 2 (लंबाई 3 : चौड़ाई 2)", "2 : 3 (यह उल्टा अनुपात है)", "4 : 3", "5 : 3"],
        "correct_idx": 0,
        "exp_en": "The Flag Code of India explicitly prescribes that the ratio of the length to the height (breadth) of the National Flag shall be 3:2.",
        "exp_hi": "भारत के राष्ट्रीय ध्वज की लंबाई और चौड़ाई का अनुपात 3:2 होना चाहिए। यदि लंबाई 3 फीट है तो चौड़ाई 2 फीट होगी।",
        "cue_en": "Flag ratio = 3:2 (Length : Breadth).",
        "cue_hi": "तिरंगे का अनुपात = 3:2 (लंबाई : चौड़ाई)।",
        "wrong_en": ["Mandated 3:2 ratio.", "Inverted ratio (Breadth : Length).", "Incorrect geometric ratio.", "Incorrect geometric ratio."],
        "wrong_hi": ["सही वैधानिक अनुपात (3:2)।", "उल्टा अनुपात।", "गलत मान।", "गलत मान।"]
    },
    {
        "name_en": "State Animal, Bird, Tree & Flower Symbols of India: Royal Bengal Tiger, Peacock, Banyan & Lotus",
        "name_hi": "भारत के राष्ट्रीय जीव व वनस्पति प्रतीक: रॉयल बंगाल टाइगर, मयूर (मोर), बरगद, कमल एवं गंगा डॉल्फिन",
        "concepts_en": ["National Animal: Royal Bengal Tiger (Panthera tigris tigris) adopted in April 1973 replacing the Asiatic Lion, marked by the launch of Project Tiger at Corbett National Park", "National Aquatic Animal: South Asian River Dolphin / Gangetic Dolphin (Platanista gangetica, declared in 2009; National Dolphin Day on October 5); blind freshwater cetacean using echolocation", "National Bird: Indian Peacock (Pavo cristatus, declared in 1963; protected under Schedule I of WPA 1972)", "National Tree: Indian Banyan (Ficus benghalensis, 'Vat Vriksha'); symbolizes immortality through its aerial prop roots", "National Flower: Indian Lotus (Nelumbo nucifera); sacred flower of divine beauty and spiritual detachment", "National Heritage Animal: Indian Elephant (Elephas maximus indicus, declared in 2010)", "National Reptile: King Cobra (Ophiophagus hannah)"],
        "concepts_hi": ["राष्ट्रीय पशु: रॉयल बंगाल टाइगर (Panthera tigris tigris); अप्रैल 1973 में एशियाई शेर के स्थान पर अपनाया गया (इसी समय कॉर्बेट पार्क से 'प्रोजेक्ट टाइगर' शुरू हुआ था)", "राष्ट्रीय जलीय जीव: गंगा डॉल्फिन (Platanista gangetica, 2009 में घोषित; प्रतिवर्ष 5 अक्टूबर को 'राष्ट्रीय डॉल्फिन दिवस'); मीठे पानी की अंधी डॉल्फिन जो इकोलोकेशन से रास्ता खोजती है", "राष्ट्रीय पक्षी: भारतीय मयूर / मोर (Pavo cristatus, 1963 में घोषित; वन्यजीव संरक्षण अधिनियम 1972 की अनुसूची I में पूर्ण संरक्षित)", "राष्ट्रीय वृक्ष: बरगद का पेड़ (Ficus benghalensis / वट वृक्ष); अपनी विशालता और हवाई जड़ों के कारण अमरता का प्रतीक", "राष्ट्रीय पुष्प: कमल (Nelumbo nucifera); पवित्रता और अनासक्ति का प्रतीक", "राष्ट्रीय विरासत पशु: भारतीय हाथी (2010 में घोषित)"],
        "q_en": "Which magnificent endangered freshwater mammal, which navigates turbid river waters via echolocation, was declared as India's 'National Aquatic Animal' in 2009?",
        "q_hi": "मीठे पानी का वह कौन सा संकटापन्न स्तनधारी जीव है, जो दृष्टिहीन होने के कारण ध्वनि तरंगों (इकोलोकेशन) से शिकार करता है और जिसे 2009 में भारत का 'राष्ट्रीय जलीय जीव' घोषित किया गया?",
        "options_en": ["Gangetic River Dolphin (गंगा नदी डॉल्फिन / सुंस - Platanista gangetica)", "Gharial (Gavialis gangeticus)", "Olive Ridley Sea Turtle", "Irrawaddy Dolphin"],
        "options_hi": ["गंगा नदी डॉल्फिन (Gangetic River Dolphin - Platanista gangetica)", "घड़ियाल (Gharial)", "ओलिव रिडले समुद्री कछुआ", "इरावदी डॉल्फिन (चिल्का झील की खारे पानी की डॉल्फिन)"],
        "correct_idx": 0,
        "exp_en": "The Gangetic River Dolphin (Platanista gangetica) was officially designated as the National Aquatic Animal of India in October 2009, celebrated annually on National Dolphin Day (October 5).",
        "exp_hi": "गंगा डॉल्फिन को अक्टूबर 2009 में भारत का राष्ट्रीय जलीय जीव घोषित किया गया था; यह केवल शुद्ध व मीठे पानी में ही जीवित रह सकती है, अतः इसे गंगा नदी के स्वास्थ्य का सूचक माना जाता है।",
        "cue_en": "National Aquatic Animal = Gangetic River Dolphin (2009).",
        "cue_hi": "राष्ट्रीय जलीय जीव = गंगा डॉल्फिन (2009)।",
        "wrong_en": ["India's National Aquatic Animal.", "Endangered crocodilian, not a mammal.", "Marine turtle nesting in Odisha.", "Marine/brackish dolphin in Chilika lake."],
        "wrong_hi": ["भारत का राष्ट्रीय जलीय जीव।", "घड़ियाल (सरीसृप)।", "ओलिव रिडले कछुआ।", "इरावदी डॉल्फिन।"]
    }
]

# S25-Cebd32d28 Famous World & Indian Heritage Monuments, Architectural Icons (4 topics)
DATA["S25-Cebd32d28"] = [
    {
        "name_en": "Mughal Architectural Wonders: Taj Mahal, Agra Fort, Fatehpur Sikri & Buland Darwaza",
        "name_hi": "मुगल स्थापत्य के चमत्कार: ताजमहल, आगरा का किला, फतेहपुर सीकरी एवं बुलंद दरवाजा",
        "concepts_en": ["Taj Mahal (Agra, Uttar Pradesh): Commissioned by 5th Mughal Emperor Shah Jahan in 1632 in memory of his favorite wife Mumtaz Mahal (Arjumand Banu Begum); completed in 1648 on southern bank of Yamuna; chief architect was Ustad Ahmad Lahori; built using pristine white Makrana marble from Rajasthan, decorated with Pietra Dura (Parchin Kari stone inlay) with floral calligraphic inlays; declared UNESCO World Heritage site in 1983 and one of the New 7 Wonders of the World in 2007", "Buland Darwaza (Fatehpur Sikri): Built by Akbar in 1601 to commemorate his historic military conquest of Gujarat; 54 meters (176 feet) high; world's highest gateway; inscribed with famous Jesus inscription: 'The world is a bridge, pass over it, but build no house upon it'", "Agra Fort: Red sandstone fortress built by Akbar (1565); Jahangiri Mahal, Diwan-i-Aam, Diwan-i-Khas, Khas Mahal"],
        "concepts_hi": ["ताजमहल (आगरा, उत्तर प्रदेश): 5वें मुगल सम्राट शाहजहां द्वारा अपनी बेगम मुमताज महल (अर्जुमंद बानो बेगम) की स्मृति में 1632 में प्रारंभ और 1648 में पूर्ण; यमुना नदी के तट पर स्थित; मुख्य वास्तुकार उस्ताद अहमद लाहौरी; राजस्थान के मकराना संगमरमर से निर्मित; पिएत्रा ड्यूरा (पच्चीकारी) पद्धति से रत्नों की जड़ाई; 1983 में यूनेस्को विश्व धरोहर स्थल एवं 2007 में 'विश्व के नए 7 अजूबों' में शामिल", "बुलंद दरवाजा (फतेहपुर सीकरी): सम्राट अकबर द्वारा 1601 में अपनी 'गुजरात विजय' के उपलक्ष्य में निर्मित; 54 मीटर (176 फीट) ऊंचा विश्व का सबसे ऊंचा प्रवेश द्वार; इस पर प्रसिद्ध ईसा मसीह का कथन अंकित है: 'यह संसार एक पुल है, इस पर से गुजरो, लेकिन इस पर घर मत बनाओ'", "आगरा का लाल किला: अकबर द्वारा 1565 में लाल बलुआ पत्थर से निर्मित; जहांगीरी महल, दीवान-ए-आम, दीवान-ए-खास"],
        "q_en": "Who served as the chief master architect and engineer responsible for designing the world-renowned white marble mausoleum, the Taj Mahal, for Emperor Shah Jahan?",
        "q_hi": "मुगल सम्राट शाहजहां के लिए सफेद मकराना संगमरमर से बने विश्व प्रसिद्ध मकबरे 'ताजमहल' का नक्शा तैयार करने वाले मुख्य वास्तुकार (Master Architect) कौन थे?",
        "options_en": ["Ustad Ahmad Lahori (उस्ताद अहमद लाहौरी)", "Mirak Mirza Ghiyas", "Inayat Khan", "Abu al-Fazl"],
        "options_hi": ["उस्ताद अहमद लाहौरी (Ustad Ahmad Lahori)", "मीरक मिर्जा गियास (यह हुमायूं के मकबरे के वास्तुकार थे)", "इनायत खान", "अबुल फजल (अकबरनामा के लेखक)"],
        "correct_idx": 0,
        "exp_en": "Historical records credit Ustad Ahmad Lahori, an architect of Persian origin settled in Lahore, as the chief architect of both the Taj Mahal in Agra and the Red Fort in Delhi.",
        "exp_hi": "ताजमहल और दिल्ली के लाल किले के मुख्य वास्तुकार उस्ताद अहमद लाहौरी थे; शाहजहां ने उनके असाधारण काम से प्रसन्न होकर उन्हें 'नादिर-उल-असर' की उपाधि दी थी।",
        "cue_en": "Chief architect of Taj Mahal = Ustad Ahmad Lahori.",
        "cue_hi": "ताजमहल के मुख्य वास्तुकार = उस्ताद अहमद लाहौरी।",
        "wrong_en": ["Chief architect of Taj Mahal.", "Architect of Humayun's Tomb.", "Court historian who wrote Shahjahannama.", "Grand Vizier and author of Akbarnama."],
        "wrong_hi": ["ताजमहल के मुख्य वास्तुकार।", "हुमायूं के मकबरे के वास्तुकार।", "दरबारी इतिहासकार।", "अकबरनामा के लेखक।"]
    },
    {
        "name_en": "Ancient Rock-Cut Architecture: Ajanta Caves, Ellora Kailash Temple & Elephanta Trimurti",
        "name_hi": "प्राचीन शैलकृत (रॉक-कट) वास्तुकला: अजंता की गुफाएं, एलोरा का कैलाश मंदिर एवं एलिफेंटा की त्रिमूर्ति",
        "concepts_en": ["Ajanta Caves (Aurangabad/Chhatrapati Sambhajinagar, Maharashtra): 30 rock-cut Buddhist cave monuments excavated into a horseshoe-shaped basalt gorge along the Waghora river; 2 phases (Satavahana 2nd BCE and Vakataka 5th CE under Harishena); world-renowned for Fresco/Tempera murals depicting Jataka tales, Bodhisattva Padmapani and Vajrapani; Chaitya halls and Viharas", "Ellora Caves (Verul, Maharashtra): 34 caves representing three religions: Buddhist (Caves 1-12), Hindu (Caves 13-29), and Jain (Caves 30-34, Indra Sabha); Cave 16 is the monolithic KAILASH TEMPLE carved top-to-bottom from a single cliff under Rashtrakuta King Krishna I (8th century CE)", "Elephanta Caves (Gharapuri island off Mumbai harbor): Dedicated to Lord Shiva; features the colossal 6-meter-high rock-cut sculpture of Sadashiva / TRIMURTI (depicting Shiva as Creator/Aghora, Preserver/Tatpurusha, and Destroyer/Vamadeva)"],
        "concepts_hi": ["अजंता की गुफाएं (छत्रपति संभाजीनगर, महाराष्ट्र): वाघोरा नदी के किनारे घोड़े की नाल के आकार की घाटी में बेसाल्ट चट्टानों को काटकर बनाई गई 30 बौद्ध गुफाएं; दो चरण (सातवाहन काल एवं वाकाटक काल); जातक कथाओं के सजीव भित्ति चित्र (पद्मपाणि व वज्रपाणि बोधिसत्व); चैत्य (पूजा स्थल) व विहार (निवास स्थल)", "एलोरा की गुफाएं (महाराष्ट्र): 34 गुफाएं जो तीन धर्मों के संगम का प्रतीक हैं: बौद्ध (गुफा 1-12), हिंदू (गुफा 13-29) एवं जैन (गुफा 30-34, इंद्र सभा); गुफा संख्या 16 विश्व प्रसिद्ध एकाश्म 'कैलाश मंदिर' है जिसे राष्ट्रकूट राजा कृष्ण प्रथम ने ऊपर से नीचे की ओर तराशा था", "एलिफेंटा की गुफाएं (मुंबई के पास धारापुरी द्वीप): भगवान शिव को समर्पित; इसमें 6 मीटर ऊंची चट्टान में तराशी गई 'सदाशिव / त्रिमूर्ति' की प्रतिमा है (जिसमें शिव के संहारक, पालक और निर्माता तीनों रूपों का संगम है)"],
        "q_en": "Which magnificent monolithic rock-cut monument at Ellora (Cave 16), carved entirely top-down from a single basalt mountain cliff, was commissioned by Rashtrakuta King Krishna I in the 8th century CE?",
        "q_hi": "एलोरा की गुफा संख्या 16 में स्थित वह कौन सा भव्य एकाश्म (Monolithic) मंदिर है, जिसे 8वीं सदी में राष्ट्रकूट सम्राट कृष्ण प्रथम द्वारा एक ही विशाल चट्टान को ऊपर से नीचे तराशकर बनाया गया था?",
        "options_en": ["Kailash Temple (कैलाश मंदिर - गुफा 16, एलोरा)", "Brihadisvara Temple", "Shore Temple", "Sun Temple, Konark"],
        "options_hi": ["कैलाश मंदिर, एलोरा (Kailash Temple - Cave 16)", "बृहदेश्वर मंदिर, तंजावुर", "तट मंदिर (शोर टेंपल), महाबलीपुरम", "सूर्य मंदिर, कोणार्क"],
        "correct_idx": 0,
        "exp_en": "Cave 16 at Ellora is the monolithic Kailash Temple, an engineering marvel executed by carving approximately 200,000 tonnes of basalt rock top-down under the Rashtrakuta dynasty.",
        "exp_hi": "एलोरा का कैलाश मंदिर (गुफा 16) दुनिया का सबसे बड़ा एकाश्म शैलकृत स्मारक है, जिसे ऊपर से नीचे की ओर काटकर भगवान शिव के कैलाश पर्वत के रूप में राष्ट्रकूटों ने निर्मित किया था।",
        "cue_en": "Ellora Cave 16 monolithic rock-cut temple = Kailash Temple (Rashtrakutas).",
        "cue_hi": "एलोरा गुफा 16 = कैलाश मंदिर (राष्ट्रकूट शासक)।",
        "wrong_en": ["Monolithic wonder of Ellora Cave 16.", "Structural granite temple by Cholas.", "Pallava structural shore temple.", "Ganga dynasty chariot temple."],
        "wrong_hi": ["एलोरा का एकाश्म कैलाश मंदिर।", "चोलों का बृहदेश्वर मंदिर।", "पल्लवों का तट मंदिर।", "कोणार्क का सूर्य मंदिर।"]
    },
    {
        "name_en": "New Seven Wonders of the World: Great Wall of China, Petra, Colosseum, Chichen Itza, Machu Picchu, Christ the Redeemer & Taj Mahal",
        "name_hi": "विश्व के नए 7 आश्चर्य (New 7 Wonders of the World): पेट्रा, कोलोसियम, माचू पिच्चू, क्राइस्ट द रिडीमर, चीचेन इत्ज़ा, चीन की दीवार एवं ताजमहल",
        "concepts_en": ["Announced on July 7, 2007 (07/07/07) in Lisbon, Portugal by the New7Wonders Foundation following global voting by 100 million people (Great Pyramid of Giza granted Honorary Wonder status as only surviving ancient wonder):", "1. Great Wall of China (China - defensive fortification spanning 21,000 km, built primarily by Ming Dynasty)", "2. Petra (Jordan - 'Rose-Red City' half as old as time, rock-cut treasury Al-Khazneh by Nabataeans)", "3. Colosseum (Rome, Italy - Flavian Amphitheatre for gladiatorial contests, built 80 CE)", "4. Chichen Itza (Yucatan, Mexico - Maya step-pyramid temple of El Castillo / Kukulkan)", "5. Machu Picchu (Cusco, Peru - Incan 15th-century mountain citadel perched at 2,430 meters)", "6. Christ the Redeemer (Rio de Janeiro, Brazil - 30-meter Art Deco statue of Jesus atop Mount Corcovado)", "7. Taj Mahal (Agra, India - white marble Mughal mausoleum)"],
        "concepts_hi": ["7 जुलाई 2007 (07/07/07) को पुर्तगाल के लिस्बन में वैश्विक मतदान के आधार पर 'विश्व के नए 7 अजूबों' की घोषणा (गीज़ा के पिरामिड को प्राचीन अजूबों में से एकमात्र जीवित होने के कारण मानद दर्जा दिया गया):", "1. चीन की महान दीवार (चीन - 21,000 किमी लंबी रक्षात्मक प्राचीर, मुख्य रूप से मिंग वंश)", "2. पेट्रा (जॉर्डन - गुलाबी चट्टानों को काटकर बनाया गया नाबातियों का प्राचीन नगर, 'अल-खज़नेह')", "3. कोलोसियम (रोम, इटली - फ्लेवियन अखाड़ा जहां 50,000 दर्शक ग्लेडिएटर युद्ध देखते थे, 80 ईस्वी)", "4. चीचेन इत्ज़ा (युकाटन, मेक्सिको - माया सभ्यता का सीढ़ीदार पिरामिड 'एल कैस्टिलो')", "5. माचू पिच्चू (पेरू - एंडीज पर्वतों पर 2,430 मीटर की ऊंचाई पर स्थित 15वीं सदी का इंका साम्राज्य का रहस्यमयी शहर)", "6. क्राइस्ट द रिडीमर (रियो डी जनेरियो, ब्राजील - कोरकोवाडो पर्वत पर ईसा मसीह की 30 मीटर ऊंची भव्य प्रतिमा)", "7. ताजमहल (आगरा, भारत - सफेद संगमरमर का मकबरा)"],
        "q_en": "In which Latin American country, nestled in the Andes Mountains high above the Urubamba River valley, is the 15th-century Incan citadel of 'Machu Picchu' situated?",
        "q_hi": "एंडीज पर्वतमाला में उरुबाम्बा नदी घाटी के ऊपर 2,430 मीटर की ऊंचाई पर स्थित 15वीं शताब्दी का प्रसिद्ध इंका सभ्यता का रहस्यमयी शहर 'माचू पिच्चू' किस लैटिन अमेरिकी देश में स्थित है?",
        "options_en": ["Peru (पेरू - माचू पिच्चू)", "Mexico", "Brazil", "Chile"],
        "options_hi": ["पेरू (Peru - इंका साम्राज्य का गढ़)", "मेक्सिको (Mexico - यहां माया पिरामिड चीचेन इत्ज़ा है)", "ब्राजील (Brazil - यहां क्राइस्ट द रिडीमर प्रतिमा है)", "चिली (Chile)"],
        "correct_idx": 0,
        "exp_en": "Machu Picchu is an iconic 15th-century Inca citadel built under Emperor Pachacuti, located in the Cusco Region of Peru above the Sacred Valley, designated as a UNESCO World Heritage site and New 7 Wonder.",
        "exp_hi": "माचू पिच्चू पेरू के एंडीज पर्वतों में स्थित इंका सभ्यता का सबसे प्रसिद्ध ऐतिहासिक स्थल है, जिसे 'इंकाओं का खोया हुआ शहर' भी कहा जाता है।",
        "cue_en": "Machu Picchu = Peru (Inca Citadel).",
        "cue_hi": "माचू पिच्चू = पेरू (इंका सभ्यता)।",
        "wrong_en": ["Home country of Machu Picchu.", "Home of Chichen Itza.", "Home of Christ the Redeemer.", "Long South American nation bordering Peru."],
        "wrong_hi": ["माचू पिच्चू का देश (पेरू)।", "चीचेन इत्ज़ा का देश (मेक्सिको)।", "क्राइस्ट प्रतिमा का देश (ब्राजील)।", "चिली।"]
    },
    {
        "name_en": "Statue of Unity: World's Tallest Statue, Sardar Patel, Ram V. Sutar & Engineering Marvel",
        "name_hi": "स्टैच्यू ऑफ यूनिटी: विश्व की सबसे ऊंची प्रतिमा (182 मी.), सरदार वल्लभभाई पटेल एवं मूर्तिकार राम वी. सुतार",
        "concepts_en": ["World's Tallest Statue: Standing at a colossal height of 182 meters (597 feet), exactly twice the height of the Statue of Liberty (93 m with pedestal); the height 182 m specifically matches the 182 legislative constituencies of the Gujarat Legislative Assembly", "Dedicated to: Sardar Vallabhbhai Patel ('Iron Man of India' / Bismarck of India), who unified 562 princely states into the Indian Union", "Location: Sadhu Bet island on the Narmada River facing the Sardar Sarovar Dam near Kevadiya (renamed Ekta Nagar), Gujarat", "Inauguration: October 31, 2018 (143rd birth anniversary of Patel, celebrated as Rashtriya Ekta Diwas / National Unity Day) by Prime Minister Narendra Modi", "Sculptor: Renowned Padma Bhushan sculptor Ram V. Sutar (studied over 2,000 archival photographs to achieve facial expression)", "Engineered and constructed by Larsen & Toubro (L&T) using structural steel framework, reinforced concrete, and 1,700 tonnes of bronze cladding plates"],
        "concepts_hi": ["विश्व की सबसे ऊंची प्रतिमा: 182 मीटर (597 फीट) की गगनचुंबी ऊंचाई, जो न्यूयॉर्क की स्टैच्यू ऑफ लिबर्टी (93 मी.) से लगभग दोगुनी ऊंची है; 182 मीटर की ऊंचाई गुजरात विधानसभा की कुल 182 सीटों का प्रतीक है", "समर्पित: सरदार वल्लभभाई पटेल ('भारत के लौह पुरुष' एवं भारत के बिस्मार्क), जिन्होंने 562 रियासतों का भारत संघ में ऐतिहासिक एकीकरण किया", "स्थान: गुजरात के केवडिया (वर्तमान नाम एकता नगर) में सरदार सरोवर बांध के सामने नर्मदा नदी के 'साधु बेट' द्वीप पर", "लोकार्पण: 31 अक्टूबर 2018 को सरदार पटेल की 143वीं जयंती ('राष्ट्रीय एकता दिवस') पर प्रधानमंत्री नरेंद्र मोदी द्वारा", "मूर्तिकार: प्रख्यात 93 वर्षीय मूर्तिकार पद्म भूषण राम वी. सुतार (जिन्होंने चेहरे के भावों के लिए पटेल की 2,000 पुरानी तस्वीरों का अध्ययन किया)", "लार्सन एंड टुब्रो (L&T) द्वारा निर्मित; 1,700 टन कांसे (Bronze) की चादरों का आवरण"],
        "q_en": "Who is the legendary Indian sculptor who designed and sculpted the Statue of Unity, the world's tallest statue (182 meters) dedicated to Sardar Vallabhbhai Patel in Gujarat?",
        "q_hi": "गुजरात में नर्मदा नदी के तट पर स्थित सरदार वल्लभभाई पटेल की विश्व की सबसे ऊंची 182 मीटर की प्रतिमा 'स्टैच्यू ऑफ यूनिटी' के मुख्य मूर्तिकार (Sculptor) कौन हैं?",
        "options_en": ["Ram V. Sutar (राम वी. सुतार)", "B.V. Doshi", "Charles Correa", "Anish Kapoor"],
        "options_hi": ["राम वी. सुतार (Ram V. Sutar)", "बी.वी. दोशी (प्रित्जकर पुरस्कार विजेता वास्तुकार)", "चार्ल्स कोरिया", "अनीश कपूर (शिल्पकार)"],
        "correct_idx": 0,
        "exp_en": "Master sculptor Ram Vanji Sutar (Padma Bhushan and Tagore Award recipient) created the design and 3D facial likeness of Sardar Patel for the 182-meter Statue of Unity.",
        "exp_hi": "स्टैच्यू ऑफ यूनिटी की भव्य कांस्य मूर्ति का डिजाइन प्रख्यात भारतीय मूर्तिकार राम वी. सुतार ने अपने पुत्र अनिल सुतार के साथ मिलकर तैयार किया था।",
        "cue_en": "Statue of Unity sculptor = Ram V. Sutar (182 meters).",
        "cue_hi": "स्टैच्यू ऑफ यूनिटी के मूर्तिकार = राम वी. सुतार (182 मीटर)।",
        "wrong_en": ["Sculptor of the Statue of Unity.", "Pritzker Prize winning Indian architect.", "Renowned Indian modernist architect.", "Contemporary British-Indian sculptor."],
        "wrong_hi": ["स्टैच्यू ऑफ यूनिटी के मूर्तिकार।", "प्रित्जकर विजेता वास्तुकार।", "प्रसिद्ध वास्तुकार।", "ब्रिटिश-भारतीय मूर्तिकार।"]
    }
]

# S25-Ce3c66b9e Flags, Logos of Multilateral Agencies & Banknote Obverse/Reverse Motifs (2 topics)
DATA["S25-Ce3c66b9e"] = [
    {
        "name_en": "United Nations Emblem & Flags of Specialized Agencies: Olive Branches & World Map",
        "name_hi": "संयुक्त राष्ट्र (UN) का आधिकारिक प्रतीक चिह्न एवं विशिष्ट एजेंसियों के ध्वज: जैतून की शाखाएं व विश्व मानचित्र",
        "concepts_en": ["United Nations Emblem: Adopted on December 7, 1946; designed by a team led by Oliver Lincoln Lundquist during the 1945 San Francisco Conference", "Visual Elements: An azimuthal equidistant projection of the world map centered on the North Pole (depicting all inhabited continents), embraced and encircled by two stylized olive branches; symbol of peace and global unity; color palette is UN Blue (#5B92E5) and white", "Specialized Agency Emblems derived from UN core:", "1. World Health Organization (WHO): UN olive branches and map overlaid by the Rod of Asclepius (a staff entwined by a single serpent, classical Greek symbol of healing and medicine)", "2. UNESCO: Temple portico with stylized pillars formed by letters 'UNESCO'", "3. International Atomic Energy Agency (IAEA): Atom with electron orbits inside olive wreath ('Atoms for Peace')", "4. UNICEF: Mother holding child framed by olive branches"],
        "concepts_hi": ["संयुक्त राष्ट्र (UN) का आधिकारिक प्रतीक: 7 दिसंबर 1946 को अंगीकृत; 1945 के सैन फ्रांसिस्को सम्मेलन में ओलिवर लिंकन लुंडक्विस्ट के नेतृत्व में डिजाइन किया गया", "दृश्य संरचना: उत्तरी ध्रुव पर केंद्रित विश्व के सभी आबाद महाद्वीपों का अज़ीमुथल समदूरस्थ मानचित्र, जिसे दो घुमावदार जैतून (Olive) की शाखाओं ने दोनों ओर से घेर रखा है; जैतून की शाखाएं विश्व शांति का प्रतीक हैं; रंग: यूएन नीला और सफेद", "विशिष्ट एजेंसियों के प्रतीक चिह्न:", "1. विश्व स्वास्थ्य संगठन (WHO): यूएन प्रतीक के बीच में 'एस्क्लेपियस का दंड' (Rod of Asclepius - एक छड़ी पर लिपटा हुआ सांप, जो चिकित्सा और स्वास्थ्य का प्राचीन ग्रीक प्रतीक है)", "2. यूनेस्को (UNESCO): एक मंदिर का प्रवेश द्वार जिसके खंभे 'UNESCO' अक्षरों से बने हैं", "3. अंतर्राष्ट्रीय परमाणु ऊर्जा एजेंसी (IAEA): जैतून के छल्लों के बीच परमाणु और इलेक्ट्रॉनों की कक्षाएं ('शांति हेतु परमाणु')", "4. यूनिसेफ (UNICEF): जैतून की शाखाओं के बीच बच्चे को गोद में लिए मां की आकृति"],
        "q_en": "In the official emblem of the World Health Organization (WHO), which ancient classical mythological symbol of medicine and healing is superimposed over the United Nations globe and olive branches?",
        "q_hi": "विश्व स्वास्थ्य संगठन (WHO) के आधिकारिक प्रतीक चिह्न में संयुक्त राष्ट्र के विश्व मानचित्र और जैतून की शाखाओं के ऊपर प्राचीन काल से चिकित्सा व उपचार का प्रतीक कौन सा चिह्न अंकित है?",
        "options_en": ["Rod of Asclepius / Staff with single coiled snake (एस्क्लेपियस का दंड / सर्प लिपटी छड़ी)", "Caduceus with two winged snakes", "Red Cross on white field", "Mortar and Pestle"],
        "options_hi": ["एस्क्लेपियस का दंड (Rod of Asclepius - छड़ी पर एक सर्प लिपटा हुआ)", "कैड्यूसियस (Caduceus - दो पंखों वाला दोहरा सर्प दंड, यह व्यापार का प्रतीक है)", "रेड क्रॉस (यह रेड क्रॉस संस्था का प्रतीक है)", "खरल और मूसल (फार्मेसी का प्रतीक)"],
        "correct_idx": 0,
        "exp_en": "The WHO emblem features the Rod of Asclepius, a staff entwined by a single serpent belonging to the ancient Greek god of healing Asclepius, universally recognized as the true symbol of medical practice.",
        "exp_hi": "डब्ल्यूएचओ (WHO) के प्रतीक में ग्रीक चिकित्सा देवता एस्क्लेपियस की छड़ी बनी है जिस पर एक सांप लिपटा हुआ है। (दो सांपों वाला कैड्यूसियस वाणिज्य/व्यापार का प्रतीक होता है)।",
        "cue_en": "WHO emblem symbol = Rod of Asclepius (staff with single snake).",
        "cue_hi": "WHO का प्रतीक = एस्क्लेपियस का दंड (एक सर्प लिपटी लाठी)।",
        "wrong_en": ["True classical symbol of medicine on WHO emblem.", "Hermes' staff of commerce with two snakes and wings.", "Emblem of the ICRC.", "Traditional pharmaceutical symbol."],
        "wrong_hi": ["चिकित्सा का सही प्रतीक (एस्क्लेपियस)।", "व्यापार का कैड्यूसियस प्रतीक।", "रेड क्रॉस।", "फार्मेसी प्रतीक।"]
    },
    {
        "name_en": "International Organization Logos & Visual Identities: Olympic Rings, Red Cross, WWF Panda & Interpol",
        "name_hi": "अंतर्राष्ट्रीय संगठनों के लोगो एवं दृश्य पहचान: ओलंपिक छल्ले, रेड क्रॉस, डब्ल्यूडब्ल्यूएफ का पांडा एवं इंटरपोल",
        "concepts_en": ["Olympic Rings: Designed in 1913 by Pierre de Coubertin; five interlaced rings of equal dimensions on a white field (Blue, Yellow, Black, Green, Red); every national flag in the world contains at least one of these six colors (including white background); represents the union of the 5 inhabited continents", "WWF (World Wide Fund for Nature): Giant Panda logo created in 1961 by Sir Peter Scott inspired by Chi-Chi the panda at London Zoo; universal symbol for wildlife conservation", "International Committee of the Red Cross (ICRC): Red Cross on white background (inversion of Swiss flag honoring Swiss founder Henry Dunant); alongside Red Crescent (Islamic nations) and Red Crystal (neutral third protocol 2005)", "INTERPOL (International Criminal Police Organization): Globe, sword (police action), olive branches (peace), and scales of justice"],
        "concepts_hi": ["ओलंपिक के पांच छल्ले (Olympic Rings): 1913 में पियरे डी कुबर्तिन द्वारा डिजाइन; 5 आपस में जुड़े छल्ले (नीला, पीला, काला, हरा, लाल); दुनिया के हर देश के झंडे में इन 6 रंगों (सफेद पृष्ठभूमि सहित) में से कम से कम एक रंग अवश्य मौजूद होता है; यह पांच महाद्वीपों की एकजुटता का प्रतीक है", "डब्ल्यूडब्ल्यूएफ (WWF): विशालकाय पांडा (Giant Panda) का प्रसिद्ध लोगो; 1961 में सर पीटर स्कॉट द्वारा लंदन चिड़ियाघर की 'ची-ची' पांडा से प्रेरित होकर बनाया गया; वन्यजीव संरक्षण का वैश्विक प्रतीक", "रेड क्रॉस (ICRC): सफेद पृष्ठभूमि पर लाल क्रॉस; इसके स्विस संस्थापक हेनरी ड्यूनेंट के सम्मान में स्विट्जरलैंड के झंडे के रंगों को उल्टा करके बनाया गया; मुस्लिम देशों में रेड क्रेसेंट (लाल अर्धचंद्र) और तीसरा प्रतीक रेड क्रिस्टल (2005)", "इंटरपोल (INTERPOL): ग्लोब, तलवार (पुलिस कार्रवाई), जैतून शाखाएं एवं तराजू (न्याय)"],
        "q_en": "Which endangered mammal serves as the globally recognized black-and-white mascot and corporate logo of the World Wide Fund for Nature (WWF) since its inception in 1961?",
        "q_hi": "1961 में अपनी स्थापना के समय से ही विश्व वन्यजीव कोष (WWF) के आधिकारिक काले और सफेद कॉर्पोरेट लोगो के रूप में किस संकटापन्न स्तनधारी जीव का चित्र अंकित है?",
        "options_en": ["Giant Panda (विशाल पांडा - Chi-Chi)", "Snow Leopard", "Bengal Tiger", "Polar Bear"],
        "options_hi": ["विशाल पांडा (Giant Panda - ची-ची पांडा से प्रेरित)", "हिम तेंदुआ (Snow Leopard)", "बंगाल टाइगर", "ध्रुवीय भालू (Polar Bear)"],
        "correct_idx": 0,
        "exp_en": "The iconic Giant Panda logo of the WWF was sketched by founder Sir Peter Scott in 1961 based on Chi-Chi, a beloved giant panda that had recently arrived at the London Zoo.",
        "exp_hi": "डब्ल्यूडब्ल्यूएफ (WWF) का विश्व विख्यात लोगो 'विशाल पांडा' (Giant Panda) है; इसे 1961 में सर पीटर स्कॉट ने डिजाइन किया था क्योंकि यह आसानी से पहचाना जाने वाला और छपाई में सरल काला-सफेद जानवर था।",
        "cue_en": "WWF logo = Giant Panda.",
        "cue_hi": "WWF का लोगो = विशाल पांडा (Giant Panda)।",
        "wrong_en": ["Official WWF mascot and logo.", "High-altitude predator.", "India's national animal.", "Arctic marine mammal."],
        "wrong_hi": ["WWF का आधिकारिक लोगो।", "हिम तेंदुआ।", "बाघ।", "ध्रुवीय भालू।"]
    }
]

print("Loaded S25 successfully")
