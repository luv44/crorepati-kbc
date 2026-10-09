# build_curriculum/group3_s09.py
# S09: Environment, Ecology & Biodiversity (13 topics across 3 chapters)

DATA = {}

# S09-C3ee11016 Ecosystem Concepts, Food Webs & Ecological Pyramids (3 topics)
DATA["S09-C3ee11016"] = [
    {
        "name_en": "Ecosystem Structure: Biotic, Abiotic Components, Food Chains & Webs",
        "name_hi": "पारिस्थितिकी तंत्र की संरचना: जैविक व अजैविक घटक, खाद्य श्रृंखला एवं खाद्य जाल",
        "concepts_en": ["Term 'Ecosystem' coined by A.G. Tansley in 1935; 'Ecology' coined by Ernst Haeckel (1866)", "Abiotic components: Sunlight, temperature, precipitation, soil, nutrients", "Biotic components: Producers (autotrophs), Consumers (herbivores, carnivores, omnivores), Decomposers (saprotrophs/detritivores)", "Grazing food chain (starts with green plants) vs Detritus food chain (starts with dead organic matter)"],
        "concepts_hi": ["'पारिस्थितिकी तंत्र' (Ecosystem) शब्द 1935 में ए.जी. टांसले द्वारा दिया गया; 'पारिस्थितिकी' (Ecology) शब्द 1866 में अर्नस्ट हेकेल द्वारा दिया गया", "अजैविक घटक: सूर्य का प्रकाश, तापमान, वर्षा, मृदा, अकार्बनिक पोषक तत्व", "जैविक घटक: उत्पादक (स्वपोषी पौधे), उपभोक्ता (शाकाहारी, मांसाहारी, सर्वाहारी), अपघटक (मृतोपजीवी कवक व जीवाणु)", "चारण खाद्य श्रृंखला (जीवित पौधों से शुरू) बनाम अपरद खाद्य श्रृंखला (मृत कार्बनिक पदार्थों से शुरू)"],
        "q_en": "Who coined the scientific term 'Ecosystem' in 1935 to define the integrated community of living organisms interacting with their physical environment?",
        "q_hi": "1935 में भौतिक पर्यावरण के साथ अंतःक्रिया करने वाले जीवों के समुदाय को परिभाषित करने के लिए 'पारिस्थितिकी तंत्र' (Ecosystem) शब्द का सर्वप्रथम प्रयोग किसने किया था?",
        "options_en": ["Arthur G. Tansley (आर्थर जी. टांसले)", "Ernst Haeckel", "Eugene P. Odum", "Charles Elton"],
        "options_hi": ["आर्थर जी. टांसले (Arthur G. Tansley)", "अर्नस्ट हेकेल (Ernst Haeckel)", "यूजीन पी. ओडम (Eugene Odum)", "चार्ल्स एल्टन (Charles Elton)"],
        "correct_idx": 0,
        "exp_en": "British ecologist Arthur G. Tansley introduced the term 'ecosystem' in 1935 in his classic paper in the journal Ecology.",
        "exp_hi": "ब्रिटिश पारिस्थितिकीविद् आर्थर जी. टांसले ने 1935 में पहली बार 'इकोसिस्टम' शब्द दिया था। (अर्नस्ट हेकेल ने 1866 में 'इकोलॉजी' शब्द दिया था)।",
        "cue_en": "Ecosystem = A.G. Tansley (1935); Ecology = Ernst Haeckel (1866).",
        "cue_hi": "इकोसिस्टम = टांसले (1935); इकोलॉजी = हेकेल (1866)।",
        "wrong_en": ["Coined 'Ecosystem' (1935).", "Coined 'Ecology' (1866).", "Father of Modern Ecosystem Ecology.", "Pioneered Ecological Pyramids (1927)."],
        "wrong_hi": ["इकोसिस्टम शब्द दिया (1935)।", "इकोलॉजी शब्द दिया (1866)।", "पारिस्थितिकी तंत्र के आधुनिक जनक।", "पारिस्थितिक पिरामिड के जनक।"]
    },
    {
        "name_en": "Trophic Levels & Lindeman's 10% Energy Transfer Law",
        "name_hi": "पोषण स्तर (Trophic Levels) एवं लिंडमैन का 10% ऊर्जा स्थानांतरण नियम",
        "concepts_en": ["Trophic levels: T1 Producers -> T2 Primary Consumers -> T3 Secondary Consumers -> T4 Tertiary Consumers", "Raymond Lindeman (1942) formulated the Ten Percent Law of trophic efficiency", "Only ~10% of energy entering a trophic level is stored as biomass and transferred to next level; 90% lost as metabolic respiration, heat, and waste", "Limits food chains to generally 4 to 5 trophic levels"],
        "concepts_hi": ["पोषण स्तर: T1 प्राथमिक उत्पादक -> T2 प्राथमिक उपभोक्ता (शाकाहारी) -> T3 द्वितीयक उपभोक्ता -> T4 शीर्ष मांसाहारी", "रेमंड लिंडमैन ने 1942 में ऊर्जा दक्षता का '10 प्रतिशत का नियम' (Ten Percent Law) प्रतिपादित किया", "एक पोषण स्तर से अगले पोषण स्तर में केवल 10% ऊर्जा ही स्थानांतरित होती है; शेष 90% ऊर्जा श्वसन व उपापचय में ऊष्मा के रूप में नष्ट हो जाती है", "यही कारण है कि खाद्य श्रृंखला में सामान्यतः 4 या 5 से अधिक पोषण स्तर नहीं होते"],
        "q_en": "According to Raymond Lindeman's Ten Percent Law of energy transfer in an ecosystem, approximately what percentage of energy is passed from one trophic level to the next?",
        "q_hi": "पारिस्थितिकी तंत्र में रेमंड लिंडमैन के 'दस प्रतिशत के नियम' (10% Law) के अनुसार एक पोषण स्तर से अगले पोषण स्तर में लगभग कितने प्रतिशत ऊर्जा स्थानांतरित होती है?",
        "options_en": ["10% (दस प्रतिशत)", "1%", "50%", "90%"],
        "options_hi": ["10% (Ten Percent)", "1%", "50%", "90%"],
        "correct_idx": 0,
        "exp_en": "Lindeman's 10% Law states that during the transfer of organic energy from one trophic level to the next, only about 10% is incorporated into new biomass.",
        "exp_hi": "लिंडमैन के नियम के अनुसार प्रत्येक चरण पर 90% ऊर्जा का क्षय हो जाता है और केवल 10% ऊर्जा ही अगले पोषण स्तर के जीवों को प्राप्त होती है।",
        "cue_en": "Energy transfer across trophic levels = 10%.",
        "cue_hi": "ऊर्जा स्थानांतरण दक्षता = 10%।",
        "wrong_en": ["Correct fraction transferred.", "Fraction of sunlight captured by plants.", "Gross efficiency under laboratory cultures.", "Fraction lost as metabolic heat."],
        "wrong_hi": ["स्थानांतरित होने वाला सही प्रतिशत।", "सूर्य के प्रकाश का पौधों द्वारा अवशोषण।", "गलत मान।", "ऊष्मा के रूप में नष्ट होने वाला भाग (90%)।"]
    },
    {
        "name_en": "Ecological Pyramids: Numbers, Biomass & Always-Upright Pyramid of Energy",
        "name_hi": "पारिस्थितिक पिरामिड: संख्या, जैवभार एवं ऊर्जा का सदैव सीधा पिरामिड",
        "concepts_en": ["Pioneered by Charles Elton (Eltonian Pyramids, 1927)", "Pyramid of Numbers: Can be upright (grassland), inverted (single tree supporting birds/parasites), or spindle-shaped", "Pyramid of Biomass: Upright in terrestrial ecosystems; INVERTED in marine/aquatic ecosystems (standing crop of phytoplankton is small with rapid turnover, supporting large zooplankton/fish biomass)", "Pyramid of Energy: ALWAYS upright according to second law of thermodynamics (energy diminishes at each successive level)"],
        "concepts_hi": ["चार्ल्स एल्टन द्वारा 1927 में प्रतिपादित (एल्टोनियन पिरामिड)", "संख्या का पिरामिड: सीधा (घास का मैदान), उल्टा (एक वृक्ष पर कई पक्षी व परजीवी) या तुर्कुरूपी हो सकता है", "जैवभार का पिरामिड (Biomass): स्थलीय तंत्र में सीधा; लेकिन जलीय/महासागरीय तंत्र में 'उल्टा' होता है (पादप प्लवकों का तात्कालिक जैवभार कम और मछलियों का अधिक होता है)", "ऊर्जा का पिरामिड: ऊष्मागतिकी के दूसरे नियम के अनुसार 'सदैव सीधा' (Always Upright) रहता है क्योंकि ऊर्जा का प्रवाह एकदिशीय होता है"],
        "q_en": "Which ecological pyramid is strictly and ALWAYS upright in all natural ecosystems without any exception?",
        "q_hi": "सभी प्राकृतिक पारिस्थितिकी तंत्रों में बिना किसी अपवाद के कौन सा पारिस्थितिक पिरामिड 'सदैव सीधा' (Always Upright) रहता है?",
        "options_en": ["Pyramid of Energy (ऊर्जा का पिरामिड)", "Pyramid of Biomass in an ocean", "Pyramid of Numbers in a forest", "Pyramid of Numbers in a parasitic food chain"],
        "options_hi": ["ऊर्जा का पिरामिड (Pyramid of Energy)", "महासागर में जैवभार का पिरामिड", "वन में संख्या का पिरामिड", "परजीवी खाद्य श्रृंखला में संख्या का पिरामिड"],
        "correct_idx": 0,
        "exp_en": "The Pyramid of Energy is always upright because energy is lost as heat at each trophic transfer following the laws of thermodynamics; it can never be inverted.",
        "exp_hi": "ऊर्जा का पिरामिड सदैव सीधा होता है क्योंकि ऊर्जा एक पोषण स्तर से दूसरे में जाते समय हमेशा घटती है और इसका प्रवाह केवल एक दिशा में होता है।",
        "cue_en": "Always upright pyramid = Pyramid of Energy.",
        "cue_hi": "सदैव सीधा पिरामिड = ऊर्जा का पिरामिड।",
        "wrong_en": ["Always upright without exception.", "Inverted in aquatic systems.", "Spindle-shaped or upright.", "Inverted pyramid of numbers."],
        "wrong_hi": ["हमेशा सीधा रहता है।", "जलीय तंत्र में उल्टा होता है।", "तुर्कुरूपी या सीधा।", "उल्टा संख्या पिरामिड।"]
    }
]

# S09-C327a7380 Biodiversity, National Parks, Wildlife Sanctuaries & Ramsar Sites (4 topics)
DATA["S09-C327a7380"] = [
    {
        "name_en": "Biodiversity Levels, Megadiverse Countries & Global Biodiversity Hotspots",
        "name_hi": "जैव विविधता के स्तर, महाविविध देश एवं वैश्विक जैव विविधता हॉटस्पॉट",
        "concepts_en": ["Three levels: Genetic diversity, Species diversity, Ecological/Ecosystem diversity", "Term 'Biodiversity' coined by Walter G. Rosen (1985); popularized by E.O. Wilson", "India is one of 17 Megadiverse countries, harboring 7-8% of recorded global species", "Biodiversity Hotspot concept introduced by Norman Myers (1988); two criteria: >=1,500 endemic vascular plant species and lost >=70% primary habitat", "Four hotspots in India: Western Ghats, Eastern Himalayas, Indo-Burma, and Sundaland (Nicobar)"],
        "concepts_hi": ["तीन स्तर: आनुवंशिक विविधता, प्रजाति विविधता, पारिस्थितिक विविधता", "'बायोडाइवर्सिटी' शब्द 1985 में वाल्टर जी. रोसेन द्वारा दिया गया; ई.ओ. विल्सन द्वारा लोकप्रिय बनाया गया", "भारत विश्व के 17 'महाविविध देशों' में शामिल है, जहां वैश्विक प्रजातियों का 7-8% पाया जाता है", "नॉर्मन मायर्स (1988) द्वारा 'जैव विविधता हॉटस्पॉट' की संकल्पना; दो शर्तें: कम से कम 1500 स्थानिक संवहनी पौधे हों और 70% से अधिक मूल पर्यावास नष्ट हो चुका हो", "भारत में चार हॉटस्पॉट: पश्चिमी घाट, पूर्वी हिमालय, इंडो-बर्मा क्षेत्र एवं सुंडालैंड (निकोबार द्वीप)"],
        "q_en": "How many global Biodiversity Hotspots are represented partially or fully within the geographic territory of India?",
        "q_hi": "विश्व के कुल 36 जैव विविधता हॉटस्पॉट्स में से कितने हॉटस्पॉट भारत के भौगोलिक क्षेत्र में पूर्ण या आंशिक रूप से फैले हैं?",
        "options_en": ["4 Hotspots (Western Ghats, Himalayas, Indo-Burma, Sundaland)", "2 Hotspots", "6 Hotspots", "8 Hotspots"],
        "options_hi": ["4 हॉटस्पॉट (पश्चिमी घाट, हिमालय, इंडो-बर्मा, सुंडालैंड)", "2 हॉटस्पॉट", "6 हॉटस्पॉट", "8 हॉटस्पॉट"],
        "correct_idx": 0,
        "exp_en": "India is home to four designated global biodiversity hotspots: the Himalayas, the Western Ghats (and Sri Lanka), Indo-Burma, and Sundaland (including Nicobar Islands).",
        "exp_hi": "भारत में 4 प्रमुख जैव विविधता हॉटस्पॉट हैं: (1) हिमालय क्षेत्र, (2) पश्चिमी घाट, (3) भारत-म्यांमार (इंडो-बर्मा) सीमा, और (4) सुंडालैंड (अंडमान-निकोबार का निकोबार भाग)।",
        "cue_en": "4 Biodiversity Hotspots in India.",
        "cue_hi": "भारत में 4 जैव विविधता हॉटस्पॉट।",
        "wrong_en": ["Four recognized Indian hotspots.", "Understates Indian hotspots.", "Overstates Indian hotspots.", "Overstates Indian hotspots."],
        "wrong_hi": ["भारत के 4 प्रमुख हॉटस्पॉट।", "कम संख्या।", "अधिक संख्या।", "अधिक संख्या।"]
    },
    {
        "name_en": "In-situ vs Ex-situ Conservation: National Parks, Wildlife Sanctuaries & Biosphere Reserves",
        "name_hi": "स्व-स्थाने (In-situ) बनाम बाह्य-स्थाने (Ex-situ) संरक्षण: राष्ट्रीय उद्यान, वन्यजीव अभयारण्य एवं बायोस्फीयर रिजर्व",
        "concepts_en": ["In-situ Conservation (on-site in natural habitat): National Parks (highest protection, no grazing/private rights, declared under WPA 1972), Wildlife Sanctuaries (limited human activities/grazing allowed), Biosphere Reserves (Core, Buffer, Transition zones under UNESCO MAB), Sacred Groves", "Ex-situ Conservation (off-site): Botanical gardens, Zoological parks, Seed banks, Cryopreservation, Gene banks", "India's first National Park: Hailey National Park (1936, now Jim Corbett National Park in Uttarakhand)", "Nilgiri Biosphere Reserve (1986) first Biosphere Reserve in India"],
        "concepts_hi": ["स्व-स्थाने संरक्षण (In-situ / प्राकृतिक पर्यावास में): राष्ट्रीय उद्यान (सर्वोच्च संरक्षण, शिकार/पशु चराई पूर्ण प्रतिबंधित), वन्यजीव अभयारण्य (सीमित मानवीय गतिविधियों की अनुमति), बायोस्फीयर रिजर्व (कोर, बफर व संक्रमण क्षेत्र), पवित्र उपवन (Sacred Groves)", "बाह्य-स्थाने संरक्षण (Ex-situ / कृत्रिम पर्यावास में): चिड़ियाघर (प्राणी उद्यान), वनस्पति उद्यान (Botanical Gardens), बीज बैंक, जीन बैंक, क्रायोप्रिजर्वेशन", "भारत का पहला राष्ट्रीय उद्यान: हैली नेशनल पार्क (1936, वर्तमान जिम कॉर्बेट / रामगंगा नेशनल पार्क, उत्तराखंड)", "नीलगिरि बायोस्फीयर रिजर्व (1986) भारत का पहला बायोस्फीयर रिजर्व"],
        "q_en": "Which was the very first National Park established in India in 1936, originally named Hailey National Park?",
        "q_hi": "1936 में स्थापित भारत का सबसे पहला राष्ट्रीय उद्यान कौन सा था, जिसे मूल रूप से 'हैली नेशनल पार्क' के नाम से जाना जाता था?",
        "options_en": ["Jim Corbett National Park (जिम कॉर्बेट, उत्तराखंड)", "Kaziranga National Park", "Kanha National Park", "Gir National Park"],
        "options_hi": ["जिम कॉर्बेट राष्ट्रीय उद्यान (Jim Corbett / Hailey NP)", "काजीरंगा राष्ट्रीय उद्यान", "कान्हा राष्ट्रीय उद्यान", "गिर राष्ट्रीय उद्यान"],
        "correct_idx": 0,
        "exp_en": "Jim Corbett National Park, established in 1936 in Nainital/Pauri Garhwal districts of Uttarakhand to protect the endangered Bengal tiger, was India's first national park.",
        "exp_hi": "1936 में उत्तराखंड में स्थापित हैली नेशनल पार्क (बाद में रामगंगा, फिर जिम कॉर्बेट) भारत का पहला राष्ट्रीय उद्यान था; 1973 में यहीं से प्रोजेक्ट टाइगर की शुरुआत हुई थी।",
        "cue_en": "First National Park in India = Hailey / Jim Corbett (1936).",
        "cue_hi": "भारत का पहला राष्ट्रीय उद्यान = जिम कॉर्बेट / हैली (1936)।",
        "wrong_en": ["First national park in India.", "Famous for one-horned rhino in Assam.", "Famous tiger reserve in MP.", "Famous for Asiatic lions in Gujarat."],
        "wrong_hi": ["पहला राष्ट्रीय उद्यान।", "असम में एक सींग वाले गैंडे का पार्क।", "मध्य प्रदेश का प्रसिद्ध राष्ट्रीय उद्यान।", "गुजरात में एशियाई शेरों का पार्क।"]
    },
    {
        "name_en": "Wildlife Conservation Projects: Project Tiger (1973), Project Elephant (1992) & Cheetah Reintroduction",
        "name_hi": "वन्यजीव संरक्षण परियोजनाएं: प्रोजेक्ट टाइगर (1973), प्रोजेक्ट हाथी (1992) एवं चीता पुनर्वास परियोजना",
        "concepts_en": ["Project Tiger launched on 1 April 1973 from Corbett National Park (Kailash Sankhala first director); National Tiger Conservation Authority (NTCA) statutory body under WPA 1972 (amended 2006); India hosts >75% of world's wild tigers", "Project Elephant launched in 1992 (Centrally Sponsored Scheme) for protecting Asian elephants and corridors (Mike program)", "Project Rhino (1987) at Kaziranga", "Cheetah Reintroduction Project: African cheetahs (Acinonyx jubatus) translocated from Namibia and South Africa to Kuno National Park, Madhya Pradesh (Sept 2022)"],
        "concepts_hi": ["प्रोजेक्ट टाइगर: 1 अप्रैल 1973 को कॉर्बेट से शुरू (कैलाश सांखला पहले निदेशक / 'टाइगर मैन ऑफ इंडिया'); राष्ट्रीय बाघ संरक्षण प्राधिकरण (NTCA) 2006 में सांविधिक निकाय बना; विश्व के 75% जंगली बाघ भारत में हैं", "प्रोजेक्ट एलीफेंट: 1992 में हाथियों के संरक्षण, पर्यावास व गलियारों की सुरक्षा हेतु शुरू", "एक सींग वाले गैंडे हेतु प्रोजेक्ट राइनो (1987)", "प्रोजेक्ट चीता: 1952 में भारत से विलुप्त घोषित एशियाई चीते के स्थान पर नामीबिया और दक्षिण अफ्रीका से अफ्रीकी चीतों को कूनो राष्ट्रीय उद्यान (मध्य प्रदेश) में छोड़ा गया (सितंबर 2022)"],
        "q_en": "In which National Park of Madhya Pradesh were African cheetahs from Namibia and South Africa released in September 2022 under the historic Cheetah Reintroduction Project?",
        "q_hi": "सितंबर 2022 में भारत के ऐतिहासिक चीता पुनर्वास प्रोजेक्ट के तहत नामीबिया और दक्षिण अफ्रीका से लाए गए चीतों को मध्य प्रदेश के किस राष्ट्रीय उद्यान में छोड़ा गया?",
        "options_en": ["Kuno National Park (कूनो राष्ट्रीय उद्यान)", "Bandhavgarh National Park", "Panna National Park", "Madhav National Park"],
        "options_hi": ["कूनो राष्ट्रीय उद्यान (Kuno National Park)", "बांधवगढ़ राष्ट्रीय उद्यान", "पन्ना राष्ट्रीय उद्यान", "माधव राष्ट्रीय उद्यान"],
        "correct_idx": 0,
        "exp_en": "Eight Namibian cheetahs were released into Kuno National Park in Sheopur district of Madhya Pradesh on 17 September 2022, marking the world's first intercontinental large carnivore translocation.",
        "exp_hi": "मध्य प्रदेश के श्योपुर जिले में स्थित कूनो राष्ट्रीय उद्यान को चीतों के लिए आदर्श पर्यावास मानते हुए नामीबिया और दक्षिण अफ्रीका से लाए गए चीतों का नया घर बनाया गया।",
        "cue_en": "Cheetah reintroduction = Kuno National Park (MP).",
        "cue_hi": "चीता पुनर्वास = कूनो नेशनल पार्क (मध्य प्रदेश)।",
        "wrong_en": ["Site of cheetah reintroduction.", "Highest tiger density park in MP.", "Known for diamond mines and Ken-Betwa link.", "Shivpuri park in MP."],
        "wrong_hi": ["चीतों का पुनर्वास स्थल।", "बाघ घनत्व हेतु प्रसिद्ध।", "पन्ना बायोस्फीयर रिजर्व।", "शिवपुरी का राष्ट्रीय उद्यान।"]
    },
    {
        "name_en": "Ramsar Convention on Wetlands (1971) & Montreux Record",
        "name_hi": "रामसर आर्द्रभूमि अभिसमय (1971), रामसर स्थल एवं मॉन्ट्रो रिकॉर्ड",
        "concepts_en": ["Adopted in Ramsar, Iran on 2 February 1971 (World Wetlands Day); came into force 1975; India signed in 1982", "Chilika Lake (Odisha) and Keoladeo National Park (Rajasthan) were India's first two Ramsar sites (1981)", "Sundarbans is the largest Ramsar site in India; Renuka Lake (HP) is the smallest", "Montreux Record: Register of wetland sites on List of Ramsar wetlands where changes in ecological character have occurred, are occurring, or are likely to occur (Currently India has 2 sites: Keoladeo NP and Loktak Lake; Chilika was removed after successful restoration)"],
        "concepts_hi": ["2 फरवरी 1971 को ईरान के रामसर शहर में हस्ताक्षरित (2 फरवरी को विश्व आर्द्रभूमि दिवस); 1975 से लागू; भारत 1982 में शामिल हुआ", "ओडिशा की चिल्का झील और राजस्थान का केवलादेव राष्ट्रीय उद्यान 1981 में भारत के पहले रामसर स्थल बने", "सुंदरबन भारत का सबसे बड़ा रामसर स्थल है; रेणुका झील (हिमाचल प्रदेश) सबसे छोटा स्थल है", "मॉन्ट्रो रिकॉर्ड (Montreux Record): उन संकटग्रस्त रामसर स्थलों का रजिस्टर जहां पारिस्थितिक संकट पैदा हो गया है (भारत के 2 स्थल शामिल: केवलादेव एवं मणिपुर की लोकटक झील; चिल्का को सुधार के बाद इससे बाहर कर दिया गया)"],
        "q_en": "Which two Indian wetland sites are currently included in the 'Montreux Record' of wetlands of international importance facing ecological degradation?",
        "q_hi": "मानवीय हस्तक्षेप और पारिस्थितिक क्षरण के कारण वर्तमान में भारत के कौन से दो आर्द्रभूमि स्थल अंतरराष्ट्रीय 'मॉन्ट्रो रिकॉर्ड' (Montreux Record) में सूचीबद्ध हैं?",
        "options_en": ["Keoladeo National Park (Rajasthan) and Loktak Lake (Manipur)", "Chilika Lake (Odisha) and Wular Lake (J&K)", "Sundarbans (WB) and Vembanad Lake (Kerala)", "Sambhar Lake (Rajasthan) and Harike Wetland (Punjab)"],
        "options_hi": ["केवलादेव राष्ट्रीय उद्यान (राजस्थान) एवं लोकटक झील (मणिपुर)", "चिल्का झील (ओडिशा) एवं वुलर झील (जम्मू-कश्मीर)", "सुंदरबन (पश्चिम बंगाल) एवं वेम्बनाड झील (केरल)", "सांभर झील (राजस्थान) एवं हरिके वेटलैंड (पंजाब)"],
        "correct_idx": 0,
        "exp_en": "Currently, only Keoladeo National Park (Rajasthan) and Loktak Lake (Manipur) remain in the Montreux Record from India. Chilika Lake was placed on it in 1993 but removed in 2002 after successful ecological restoration.",
        "exp_hi": "वर्तमान में भारत के केवल दो स्थल - केवलादेव (राजस्थान) और लोकटक झील (मणिपुर, जहां फुमडी पाई जाती हैं) मॉन्ट्रो रिकॉर्ड में हैं। चिल्का झील को सफल संरक्षण के बाद 2002 में इससे हटा दिया गया था।",
        "cue_en": "Montreux Record (India) = Keoladeo NP + Loktak Lake.",
        "cue_hi": "मॉन्ट्रो रिकॉर्ड (भारत) = केवलादेव + लोकटक झील।",
        "wrong_en": ["The two current Indian Montreux sites.", "Chilika was removed in 2002.", "Ramsar sites not on Montreux Record.", "Ramsar sites not on Montreux Record."],
        "wrong_hi": ["भारत के दोनों वर्तमान स्थल।", "चिल्का को 2002 में बाहर कर दिया गया।", "सामान्य रामसर स्थल।", "सामान्य रामसर स्थल।"]
    }
]

# S09-Cba335bae Climate Change, Global Treaties & Environmental Legislation (6 topics)
DATA["S09-Cba335bae"] = [
    {
        "name_en": "Greenhouse Effect, Global Warming Potential (GWP) & Major Greenhouse Gases",
        "name_hi": "ग्रीनहाउस प्रभाव, वैश्विक तापन क्षमता (GWP) एवं प्रमुख ग्रीनहाउस गैसें",
        "concepts_en": ["Natural greenhouse effect keeps Earth average temperature at habitable ~15°C (without it, Earth would be -18°C); Joseph Fourier discovered it (1824)", "Water vapor (H2O) is most abundant natural GHG; Carbon dioxide (CO2) is primary anthropogenic contributor", "Methane (CH4) GWP ~28-36 times CO2 over 100 years; Nitrous oxide (N2O) GWP ~273 times; Fluorinated gases (SF6, HFCs, PFCs, NF3) have highest GWPs (SF6 ~23,500)", "Keeling Curve (Mauna Loa Observatory) measures atmospheric CO2 concentrations"],
        "concepts_hi": ["प्राकृतिक ग्रीनहाउस प्रभाव पृथ्वी का औसत तापमान 15°C पर जीवन योग्य बनाए रखता है (इसके अभाव में -18°C होता); जोसेफ फूरियर ने 1824 में खोज की", "जलवाष्प (H2O) सबसे प्रचुर प्राकृतिक ग्रीनहाउस गैस है; कार्बन डाइऑक्साइड (CO2) मानव-जनित मुख्य गैस है", "मीथेन (CH4) की ग्लोबल वार्मिंग क्षमता (GWP) 100 वर्षों में CO2 से 28-36 गुना है; नाइट्रस ऑक्साइड (N2O) 273 गुना; सल्फर हेक्साफ्लोराइड (SF6) की 23,500 गुना है", "कीलिंग वक्र (Keeling Curve): वायुमंडल में CO2 सांद्रता का ऐतिहासिक ग्राफ"],
        "q_en": "Which synthetic greenhouse gas, widely used as an electrical insulator in high-voltage circuit breakers, possesses the highest Global Warming Potential (GWP) of approximately 23,500 over a 100-year timescale?",
        "q_hi": "उच्च-वोल्टेज सर्किट ब्रेकरों में विद्युत कुचालक के रूप में प्रयुक्त होने वाली किस मानव-निर्मित गैस की 100 वर्षों में वैश्विक तापन क्षमता (GWP) सर्वाधिक (लगभग 23,500 गुना) है?",
        "options_en": ["Sulfur Hexafluoride (SF6 / सल्फर हेक्साफ्लोराइड)", "Methane (CH4)", "Nitrous Oxide (N2O)", "Carbon Dioxide (CO2)"],
        "options_hi": ["सल्फर हेक्साफ्लोराइड (SF6)", "मीथेन (CH4)", "नाइट्रस ऑक्साइड (N2O)", "कार्बन डाइऑक्साइड (CO2)"],
        "correct_idx": 0,
        "exp_en": "Sulfur Hexafluoride (SF6) is the most potent greenhouse gas evaluated by the IPCC, having a Global Warming Potential roughly 23,500 times that of CO2 and an atmospheric lifetime of 3,200 years.",
        "exp_hi": "सल्फर हेक्साफ्लोराइड (SF6) का जीडब्ल्यूपी मान लगभग 23,500 है, जो क्योटो प्रोटोकॉल के तहत नियंत्रित छह ग्रीनहाउस गैसों में सबसे अधिक शक्तिशाली और दीर्घकालिक प्रभाव वाली गैस है।",
        "cue_en": "Highest GWP gas = Sulfur Hexafluoride (SF6 ~23,500).",
        "cue_hi": "सर्वाधिक GWP वाली गैस = SF6 (सल्फर हेक्साफ्लोराइड)।",
        "wrong_en": ["Highest GWP gas (~23,500).", "GWP of ~28-36.", "GWP of ~273.", "Baseline reference gas (GWP = 1)."],
        "wrong_hi": ["सर्वाधिक शक्तिशाली ग्रीनहाउस गैस।", "GWP लगभग 28-36।", "GWP लगभग 273।", "आधारभूत संदर्भ गैस (GWP = 1)।"]
    },
    {
        "name_en": "UNFCCC, Kyoto Protocol (1997) & Paris Agreement (2015)",
        "name_hi": "यूएनएफसीसीसी (UNFCCC), क्योटो प्रोटोकॉल (1997) एवं पेरिस जलवायु समझौता (2015)",
        "concepts_en": ["UNFCCC adopted at Rio Earth Summit 1992; principle of Common But Differentiated Responsibilities and Respective Capabilities (CBDR-RC)", "Kyoto Protocol (1997, entered force 2005): Legally binding emission reduction targets on Annex I developed countries; Market mechanisms: Clean Development Mechanism (CDM), Joint Implementation, Emissions Trading", "Paris Agreement (COP21, 2015): Legally binding treaty aiming to limit global temperature rise well below 2°C, preferably to 1.5°C above pre-industrial levels", "Nationally Determined Contributions (NDCs); India pledged 50% non-fossil electric capacity by 2030 and Net Zero carbon emissions by 2070 (Panchamrit)"],
        "concepts_hi": ["रियो पृथ्वी सम्मेलन 1992 में यूएनएफसीसीसी का गठन; 'साझा लेकिन विभेदित जिम्मेदारियां' (CBDR-RC) का मूल सिद्धांत", "क्योटो प्रोटोकॉल (1997, लागू 2005): विकसित (अनुलग्नक-1) देशों पर कानूनी रूप से बाध्यकारी उत्सर्जन कटौती लक्ष्य; कार्बन ट्रेडिंग व स्वच्छ विकास तंत्र (CDM)", "पेरिस समझौता (COP21, 2015): वैश्विक औसत तापमान वृद्धि को पूर्व-औद्योगिक स्तर से 2°C से नीचे और संभव हो तो 1.5°C तक सीमित रखने का ऐतिहासिक वैश्विक संकल्प", "राष्ट्रीय स्तर पर निर्धारित योगदान (NDCs); भारत ने 2030 तक 50% गैर-जीवाश्म बिजली क्षमता और 2070 तक 'नेट ज़ीरो' (शुद्ध शून्य उत्सर्जन) का पंचामृत लक्ष्य रखा"],
        "q_en": "Under the landmark 2015 Paris Agreement (COP21), the international community committed to holding the increase in global average temperature to well below:",
        "q_hi": "2015 के ऐतिहासिक पेरिस जलवायु समझौते (COP21) के तहत वैश्विक औसत तापमान वृद्धि को पूर्व-औद्योगिक स्तर से कितने डिग्री सेल्सियस से नीचे रखने का कानूनी रूप से बाध्यकारी लक्ष्य तय किया गया है?",
        "options_en": ["Well below 2.0°C, pursuing efforts to limit it to 1.5°C", "Below 3.0°C", "Below 0.5°C", "Below 2.5°C with no aspirational limit"],
        "options_hi": ["2.0°C से काफी नीचे, और 1.5°C तक सीमित करने का प्रयास", "3.0°C से नीचे", "0.5°C से नीचे", "2.5°C से नीचे"],
        "correct_idx": 0,
        "exp_en": "Article 2 of the Paris Agreement commits nations to holding warming well below 2°C above pre-industrial levels and pursuing efforts to limit the increase to 1.5°C.",
        "exp_hi": "पेरिस समझौते का मुख्य लक्ष्य वैश्विक तापमान वृद्धि को 2 डिग्री सेल्सियस से काफी नीचे रखना और इसे 1.5 डिग्री सेल्सियस तक सीमित रखने के लिए हर संभव प्रयास करना है।",
        "cue_en": "Paris Agreement goal = Well below 2°C, aim for 1.5°C.",
        "cue_hi": "पेरिस समझौता लक्ष्य = 2°C से नीचे, 1.5°C का प्रयास।",
        "wrong_en": ["Official treaty goal.", "Too high, dangerous threshold.", "Unachievable current target.", "Incorrect threshold."],
        "wrong_hi": ["संधि का आधिकारिक लक्ष्य।", "अत्यधिक खतरनाक स्तर।", "अव्यावहारिक।", "गलत सीमा।"]
    },
    {
        "name_en": "Ozone Layer Depletion: Vienna Convention, Montreal Protocol (1987) & Kigali Amendment",
        "name_hi": "ओजोन परत का क्षरण: विएना कन्वेंशन, मॉन्ट्रियल प्रोटोकॉल (1987) एवं किगाली संशोधन",
        "concepts_en": ["Ozone hole discovered over Antarctica in 1985 by British Antarctic Survey (Farman, Gardiner, Shanklin); measured in Dobson Units (DU, 1 DU = 0.01 mm thickness at STP)", "Chlorofluorocarbons (CFCs) and halons release free chlorine/bromine radicals that catalytically destroy O3 molecules", "Vienna Convention (1985) and Montreal Protocol on Substances that Deplete the Ozone Layer (16 Sept 1987, World Ozone Day)", "Universal ratification; Montreal Protocol successfully phased out CFCs and HCFCs", "Kigali Amendment (2016): Mandates phase-down of Hydrofluorocarbons (HFCs - potent GHGs replacing CFCs)"],
        "concepts_hi": ["1985 में अंटार्कटिका के ऊपर जोसेफ फारमैन और ब्रिटिश अंटार्कटिक दल द्वारा ओजोन छिद्र की खोज; ओजोन परत की मोटाई डॉबसन यूनिट (DU) में मापी जाती है", "क्लोरोफ्लोरोकार्बन (CFCs) और हैलॉन से मुक्त क्लोरीन और ब्रोमीन परमाणु ओजोन अणुओं का निरंतर विनाश करते हैं", "विएना कन्वेंशन (1985) और ओजोन क्षरणकारी पदार्थों पर 'मॉन्ट्रियल प्रोटोकॉल' (16 सितंबर 1987; 16 सितंबर को विश्व ओजोन दिवस)", "विश्व का सबसे सफल पर्यावरण समझौता; सीएफसी को पूरी तरह समाप्त किया", "किगाली संशोधन (2016): हाइड्रोफ्लोरोकार्बन (HFCs - जो शक्तिशाली ग्रीनहाउस गैसें हैं) के उत्पादन व उपभोग को कम करने का कानूनी लक्ष्य"],
        "q_en": "In which unit of measurement is the total column thickness of stratospheric ozone conventionally quantified, where 1 unit corresponds to a layer 0.01 mm thick at STP?",
        "q_hi": "समतापमंडलीय ओजोन परत की कुल मोटाई को पारंपरिक रूप से किस इकाई में मापा जाता है, जहां 1 इकाई मानक तापमान और दाब पर 0.01 मिमी मोटाई के बराबर होती है?",
        "options_en": ["Dobson Unit (DU / डॉबसन यूनिट)", "Becquerel", "Decibel", "Lux"],
        "options_hi": ["डॉबसन यूनिट (Dobson Unit - DU)", "बेकेरल (Becquerel)", "डेसिबल (Decibel)", "लक्स (Lux)"],
        "correct_idx": 0,
        "exp_en": "The Dobson Unit (DU) is the standard unit for measuring atmospheric ozone. A normal baseline column ozone level is around 300 to 350 DU, with values under 220 DU defining an 'ozone hole'.",
        "exp_hi": "ओजोन परत की सघनता और मोटाई 'डॉबसन यूनिट' (DU) में मापी जाती है; 220 DU से कम मान को 'ओजोन छिद्र' की स्थिति माना जाता है।",
        "cue_en": "Ozone layer thickness unit = Dobson Unit (DU).",
        "cue_hi": "ओजोन परत की मोटाई = डॉबसन यूनिट (DU)।",
        "wrong_en": ["Standard ozone measurement unit.", "Unit of radioactivity.", "Unit of sound loudness.", "Unit of illuminance."],
        "wrong_hi": ["ओजोन की मानक इकाई।", "रेडियोधर्मिता की इकाई।", "ध्वनि तीव्रता की इकाई।", "प्रकाश प्रदीप्ति की इकाई।"]
    },
    {
        "name_en": "Wildlife (Protection) Act, 1972 & 2022 Amendment: Schedules and CITES Compliance",
        "name_hi": "वन्यजीव (संरक्षण) अधिनियम 1972 एवं 2022 संशोधन: अनुसूचियां एवं साइट्स (CITES) अनुपालन",
        "concepts_en": ["Enacted in 1972 (Article 48A and 51A(g) constitutional mandate); provides legal protection to wild animals, birds, and plants", "Established National Board for Wildlife (NBWL, chaired by Prime Minister), Central Zoo Authority, and Wildlife Crime Control Bureau (WCCB)", "Wildlife (Protection) Amendment Act 2022 (effective April 2023): Rationalized schedules from 6 down to 4 schedules", "Schedule I: Highest level of protection for endangered animal species (Tigers, Lions, Elephants, Great Indian Bustard); Schedule II: Protected animal species; Schedule III: Protected plant species; Schedule IV: CITES scheduled specimens"],
        "concepts_hi": ["1972 में पारित (अनुच्छेद 48A एवं 51A(g) का संवैधानिक आधार); जंगली जानवरों, पक्षियों और पादपों को व्यापक कानूनी संरक्षण", "राष्ट्रीय वन्यजीव बोर्ड (NBWL, अध्यक्ष प्रधानमंत्री), केंद्रीय चिड़ियाघर प्राधिकरण (CZA) एवं वन्यजीव अपराध नियंत्रण ब्यूरो (WCCB) की स्थापना", "वन्यजीव संरक्षण (संशोधन) अधिनियम 2022 (1 अप्रैल 2023 से लागू): अनुसूचियों की संख्या 6 से घटाकर केवल 4 कर दी गई", "अनुसूची I: संकटापन्न पशुओं को सर्वोच्च कानूनी संरक्षण (बाघ, शेर, हाथी, गोडावण); अनुसूची II: संरक्षित पशु; अनुसूची III: संरक्षित पौधे; अनुसूची IV: साइट्स (CITES) के अंतर्गत अंतर्राष्ट्रीय व्यापार वाले नमूने"],
        "q_en": "Under the Wildlife (Protection) Amendment Act 2022, which came into force in April 2023, the total number of protective Schedules in the principal Act was consolidated from six down to how many?",
        "q_hi": "अप्रैल 2023 से प्रभावी 'वन्यजीव (संरक्षण) संशोधन अधिनियम 2022' द्वारा मूल 1972 के अधिनियम की अनुसूचियों की संख्या 6 से घटाकर कितनी कर दी गई है?",
        "options_en": ["4 Schedules (4 अनुसूचियां)", "3 Schedules", "5 Schedules", "2 Schedules"],
        "options_hi": ["4 अनुसूचियां (Four Schedules)", "3 अनुसूचियां", "5 अनुसूचियां", "2 अनुसूचियां"],
        "correct_idx": 0,
        "exp_en": "The 2022 Amendment rationalized the earlier 6 schedules into 4: Schedule I (highest protection animals), Schedule II (lesser protection animals), Schedule III (protected plants), and Schedule IV (CITES species). Vermin schedule was removed.",
        "exp_hi": "2022 के संशोधन द्वारा अनुसूचियों को युक्तिसंगत बनाकर 4 कर दिया गया है और 'वर्मिन' (पीड़क जंतु) की पुरानी अनुसूची V को पूरी तरह समाप्त कर दिया गया है।",
        "cue_en": "Wildlife Act 2022 amendment = 4 Schedules (reduced from 6).",
        "cue_hi": "वन्यजीव संशोधन अधिनियम 2022 = 4 अनुसूचियां (6 से घटाकर)।",
        "wrong_en": ["Current consolidated schedule count.", "Incorrect count.", "Incorrect count.", "Incorrect count."],
        "wrong_hi": ["वर्तमान में अनुसूचियों की संख्या।", "गलत संख्या।", "गलत संख्या।", "गलत संख्या।"]
    },
    {
        "name_en": "Environment (Protection) Act, 1986 (Umbrella Legislation) & Forest Conservation Acts",
        "name_hi": "पर्यावरण (संरक्षण) अधिनियम 1986 (छाता विधान) एवं वन संरक्षण अधिनियम",
        "concepts_en": ["Enacted under Article 253 of the Constitution to implement decisions of UN Stockholm Conference (1972); triggered by Bhopal Gas Tragedy (Dec 1984, Methyl Isocyanate leak)", "Known as 'Umbrella Act' because it coordinates regulatory bodies created under Water Act 1974 and Air Act 1981", "Empowers Central Government to establish environmental quality standards, inspect industrial units, and issue closure orders", "Forest (Conservation) Act 1980 regulates diversion of forest land for non-forest purposes (amended as Van Sanrakshan Evam Samvardhan Adhiniyam 2023)"],
        "concepts_hi": ["स्टॉकहोम सम्मेलन (1972) के निर्णयों को लागू करने हेतु संविधान के अनुच्छेद 253 के तहत पारित; भोपाल गैस त्रासदी (दिसंबर 1984, मिथाइल आइसोसाइनेट गैस रिसाव) के बाद त्वरित रूप से लाया गया", "इसे 'छाता विधान' (Umbrella Legislation) कहा जाता है क्योंकि यह जल अधिनियम 1974 व वायु अधिनियम 1981 के मध्य समन्वय स्थापित करता है", "केंद्र सरकार को औद्योगिक इकाइयों के प्रदूषण मानक तय करने, निरीक्षण करने और बंदी का आदेश देने की असीमित शक्तियां", "वन (संरक्षण) अधिनियम 1980 गैर-वानिकी कार्यों हेतु वनों के उपयोग को नियंत्रित करता है (2023 में संशोधित)"],
        "q_en": "The comprehensive Environment (Protection) Act of 1986 was enacted by the Indian Parliament under Article 253 in the immediate aftermath of which tragic industrial disaster?",
        "q_hi": "1986 का व्यापक पर्यावरण (संरक्षण) अधिनियम भारतीय संसद द्वारा किस भयानक औद्योगिक त्रासदी की सीधी पृष्ठभूमि में पारित किया गया था?",
        "options_en": ["Bhopal Gas Tragedy (भोपाल गैस त्रासदी - दिसंबर 1984)", "Chasnala Mining Disaster", "Vizag Polymer Gas Leak", "Jaipur IOCL Oil Depot Fire"],
        "options_hi": ["भोपाल गैस त्रासदी (Bhopal Gas Tragedy - 1984)", "चासनाला खान दुर्घटना", "विशाखापट्टनम गैस रिसाव", "जयपुर तेल डिपो अग्निकांड"],
        "correct_idx": 0,
        "exp_en": "The catastrophic release of Methyl Isocyanate (MIC) gas at the Union Carbide pesticide plant in Bhopal in December 1984 catalyzed the enactment of the Environment (Protection) Act in May 1986.",
        "exp_hi": "दिसंबर 1984 में भोपाल में यूनियन कार्बाइड कारखाने से मिथाइल आइसोसाइनेट (MIC) गैस के जानलेवा रिसाव के बाद पर्यावरण संबंधी समग्र कानून की आवश्यकता महसूस हुई, जिसके परिणामस्वरूप 1986 का अधिनियम बना।",
        "cue_en": "Environment Protection Act 1986 = Bhopal Gas Tragedy (1984) catalyst.",
        "cue_hi": "पर्यावरण संरक्षण अधिनियम 1986 = भोपाल गैस त्रासदी (1984) की पृष्ठभूमि।",
        "wrong_en": ["Catalyzed the 1986 EPA enactment.", "Coal mine tragedy in 1975.", "Styrene leak in 2020.", "Fire disaster in 2009."],
        "wrong_hi": ["1986 अधिनियम का तात्कालिक कारण।", "1975 की कोयला खान त्रासदी।", "2020 की स्टाइरीन गैस घटना।", "2009 का अग्निकांड।"]
    },
    {
        "name_en": "National Green Tribunal (NGT) Act 2010 & Environmental Impact Assessment (EIA)",
        "name_hi": "राष्ट्रीय हरित अधिकरण (NGT) अधिनियम 2010 एवं पर्यावरण प्रभाव आकलन (EIA)",
        "concepts_en": ["Established on 18 October 2010 under NGT Act 2010 under Article 21 (Right to healthy environment); India is 3rd country globally after Australia and New Zealand with dedicated environmental tribunal", "Principal Bench in New Delhi; regional benches in Pune, Bhopal, Kolkata, Chennai", "Chaired by retired Supreme Court Judge or High Court Chief Justice (Justice Lokeshwar Singh Panta first Chairperson); mandates disposal of cases within 6 months", "Environmental Impact Assessment (EIA): Statutory process under EPA 1986 to evaluate potential environmental consequences of developmental projects prior to environmental clearance (Public Hearing, Scoping, Screening)"],
        "concepts_hi": ["संविधान के अनुच्छेद 21 (स्वच्छ पर्यावरण का अधिकार) के तहत NGT अधिनियम 2010 के जरिए 18 अक्टूबर 2010 को स्थापना; भारत ऑस्ट्रेलिया और न्यूजीलैंड के बाद पर्यावरण अदालत बनाने वाला विश्व का तीसरा देश बना", "प्रधान पीठ नई दिल्ली में; चार क्षेत्रीय पीठें: पुणे, भोपाल, कोलकाता और चेन्नई", "अध्यक्ष सुप्रीम कोर्ट के सेवानिवृत्त न्यायाधीश या हाईकोर्ट के मुख्य न्यायाधीश होते हैं (न्यायमूर्ति लोकेश्वर सिंह पंटा पहले अध्यक्ष); 6 माह के भीतर मामलों का त्वरित निपटारा अनिवार्य", "पर्यावरण प्रभाव आकलन (EIA): किसी भी बड़ी विकास परियोजना को मंजूरी देने से पहले उसके पर्यावरणीय प्रभावों का पूर्व मूल्यांकन करने की वैधानिक प्रक्रिया"],
        "q_en": "Under the National Green Tribunal (NGT) Act 2010, within what maximum statutory timeframe is the Tribunal mandated to endeavor to dispose of environmental applications and appeals?",
        "q_hi": "राष्ट्रीय हरित अधिकरण (NGT) अधिनियम 2010 के अनुसार अधिकरण के समक्ष दायर पर्यावरणीय आवेदनों और अपीलों का अंतिम निपटारा कितने समय के भीतर करने का वैधानिक निर्देश है?",
        "options_en": ["Within 6 months of filing (6 माह के भीतर)", "Within 3 months", "Within 12 months", "Within 30 days"],
        "options_hi": ["6 माह के भीतर (Within 6 months)", "3 माह के भीतर", "12 माह (1 वर्ष) के भीतर", "30 दिन के भीतर"],
        "correct_idx": 0,
        "exp_en": "Section 18(3) of the NGT Act 2010 specifies that the Tribunal shall deal with applications and appeals as expeditiously as possible and endeavor to dispose of them finally within six months of filing.",
        "exp_hi": "एनजीटी अधिनियम 2010 की धारा 18(3) के अनुसार अधिकरण को पर्यावरण संबंधी मुकदमों की सुनवाई पूरी कर उनका अंतिम फैसला 6 महीने के भीतर सुनाने का लक्ष्य दिया गया है।",
        "cue_en": "NGT disposal timeframe = Within 6 months.",
        "cue_hi": "एनजीटी मामलों का निपटारा = 6 माह के भीतर।",
        "wrong_en": ["Statutory disposal goal under Section 18(3).", "Appellate filing limitation period.", "Standard civil court timeframe.", "Urgent stay application timeframe."],
        "wrong_hi": ["धारा 18(3) के तहत समय सीमा।", "अपील दाखिल करने की अवधि।", "सामान्य सिविल अदालती समय।", "अंतरिम स्थगन समय।"]
    }
]

print("Loaded S09 successfully")
