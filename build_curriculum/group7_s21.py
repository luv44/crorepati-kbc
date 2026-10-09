# build_curriculum/group7_s21.py
# S21: Awards, Honors & National/International Distinctions (8 topics across 3 chapters)

DATA = {}

# S21-C7f420f5a Bharat Ratna, Padma Awards & Wartime/Peacetime Gallantry Awards (4 topics)
DATA["S21-C7f420f5a"] = [
    {
        "name_en": "Bharat Ratna: Institution, Peepal Leaf Design, First Recipients (1954) & Non-Indian Laureates",
        "name_hi": "भारत रत्न: स्थापना, पीपल के पत्ते का पदक, प्रथम प्राप्तकर्ता (1954) एवं गैर-भारतीय विजेता",
        "concepts_en": ["Instituted on January 2, 1954 by President Dr. Rajendra Prasad; highest civilian honor of the Republic of India; no formal monetary grant attached; carries Sanad (certificate signed by President) and bronze medallion in the shape of a Peepal leaf with embossed Sun and 'Bharat Ratna' in Devanagari script", "First Recipients in 1954: C. Rajagopalachari (last Governor-General of India), Dr. Sarvepalli Radhakrishnan (first Vice-President and philosopher), and Dr. C.V. Raman (Nobel laureate in Physics)", "Non-Indian / Foreign Recipients: Khan Abdul Ghaffar Khan ('Frontier Gandhi', Pakistan, 1987) and Nelson Mandela (anti-apartheid leader, South Africa, 1990); Mother Teresa was a naturalized citizen (1980)", "Maximum 3 conferred in a year traditionally; historic exception in 2024 with 5 conferred (Karpoori Thakur, Lal Krishna Advani, P.V. Narasimha Rao, Charan Singh, M.S. Swaminathan)"],
        "concepts_hi": ["2 जनवरी 1954 को राष्ट्रपति डॉ. राजेंद्र प्रसाद द्वारा स्थापित; भारत का सर्वोच्च नागरिक सम्मान; इसके साथ कोई मौद्रिक राशि नहीं मिलती; राष्ट्रपति के हस्ताक्षर वाली 'सनद' और कांसे का पीपल के पत्ते के आकार का पदक मिलता है (जिस पर सूर्य का चित्र और देवनागरी में 'भारत रत्न' अंकित है)", "1954 के प्रथम प्राप्तकर्ता: सी. राजगोपालाचारी (स्वतंत्र भारत के अंतिम गवर्नर जनरल), डॉ. सर्वपल्ली राधाकृष्णन (प्रथम उपराष्ट्रपति व दार्शनिक) एवं डॉ. सी.वी. रमन (भौतिकी में नोबेल पुरस्कार विजेता)", "गैर-भारतीय (विदेशी) प्राप्तकर्ता: खान अब्दुल गफ्फार खान ('सीमांत गांधी', पाकिस्तान, 1987) एवं नेल्सन मंडेला (दक्षिण अफ्रीका, 1990); मदर टेरेसा को 1980 में मिला (वे प्राकृतिक नागरिक थीं)", "परंपरागत रूप से प्रतिवर्ष अधिकतम 3 को दिया जाता है; 2024 में अभूतपूर्व रूप से 5 विभूतियों को दिया गया (कर्पूरी ठाकुर, लालकृष्ण आडवाणी, पी.वी. नरसिम्हा राव, चौधरी चरण सिंह, एम.एस. स्वामीनाथन)"],
        "q_en": "Who among the following was the very FIRST non-Indian citizen to be honored with India's highest civilian decoration, the Bharat Ratna, in 1987?",
        "q_hi": "1987 में भारत के सर्वोच्च नागरिक सम्मान 'भारत रत्न' से सम्मानित होने वाले प्रथम गैर-भारतीय नागरिक (विदेशी विभूति) कौन थे?",
        "options_en": ["Khan Abdul Ghaffar Khan (खान अब्दुल गफ्फार खान / सीमांत गांधी - 1987)", "Nelson Mandela", "Mother Teresa", "Martin Luther King Jr."],
        "options_hi": ["खान अब्दुल गफ्फार खान (Khan Abdul Ghaffar Khan - 1987)", "नेल्सन मंडेला (Nelson Mandela - 1990 में प्राप्तकर्ता)", "मदर टेरेसा (1980 में प्राप्तकर्ता - प्राकृतिक भारतीय नागरिक)", "मार्टिन लूथर किंग जूनियर"],
        "correct_idx": 0,
        "exp_en": "Khan Abdul Ghaffar Khan ('Frontier Gandhi' of the Khudai Khidmatgar movement, a Pakistani citizen) was the first non-Indian awarded the Bharat Ratna in 1987. Nelson Mandela was the second in 1990.",
        "exp_hi": "खुदाई खिदमतगार आंदोलन के संस्थापक और स्वतंत्रता सेनानी खान अब्दुल गफ्फार खान (सीमांत गांधी) 1987 में भारत रत्न पाने वाले पहले विदेशी नागरिक बने। 1990 में दक्षिण अफ्रीका के नेल्सन मंडेला को यह सम्मान मिला।",
        "cue_en": "First non-Indian Bharat Ratna = Khan Abdul Ghaffar Khan (1987).",
        "cue_hi": "प्रथम गैर-भारतीय भारत रत्न = खान अब्दुल गफ्फार खान (1987)।",
        "wrong_en": ["First foreign recipient (1987).", "Second foreign recipient (1990).", "Naturalized Indian citizen awarded in 1980.", "Not a recipient of Bharat Ratna."],
        "wrong_hi": ["प्रथम विदेशी प्राप्तकर्ता (1987)।", "दूसरे विदेशी प्राप्तकर्ता (1990)।", "प्राकृतिक नागरिकता प्राप्त (1980)।", "भारत रत्न नहीं मिला।"]
    },
    {
        "name_en": "Padma Awards Hierarchy: Padma Vibhushan, Padma Bhushan & Padma Shri Regulations",
        "name_hi": "पद्म पुरस्कार पदानुक्रम: पद्म विभूषण (द्वितीय), पद्म भूषण (तृतीय) एवं पद्म श्री (चतुर्थ) नियम",
        "concepts_en": ["Instituted in 1954; announced annually on the eve of Republic Day (January 25); given in three descending categories:", "1. Padma Vibhushan: For 'exceptional and distinguished service' (India's second-highest civilian honor)", "2. Padma Bhushan: For 'distinguished service of high order' (third-highest civilian honor)", "3. Padma Shri: For 'distinguished service in any field' (fourth-highest civilian honor)", "Padma Awards Committee: Headed by Cabinet Secretary, submits recommendations to Prime Minister and President; maximum 120 awards per year (excluding posthumous and foreign/NRI awards); medal features geometric circular pattern with lotus flower and motto in Devanagari"],
        "concepts_hi": ["1954 में स्थापित; प्रतिवर्ष गणतंत्र दिवस की पूर्व संध्या (25 जनवरी) पर घोषित किए जाते हैं; तीन घटते क्रमों में दिए जाते हैं:", "1. पद्म विभूषण: 'असाधारण और विशिष्ट सेवा' के लिए (भारत का दूसरा सर्वोच्च नागरिक सम्मान)", "2. पद्म भूषण: 'उच्च कोटि की विशिष्ट सेवा' के लिए (तीसरा सर्वोच्च नागरिक सम्मान)", "3. पद्म श्री: 'किसी भी क्षेत्र में विशिष्ट सेवा' के लिए (चौथा सर्वोच्च नागरिक सम्मान)", "पद्म पुरस्कार समिति: कैबिनेट सचिव की अध्यक्षता में गठित समिति प्रधानमंत्री और राष्ट्रपति को अनुशंसा भेजती है; एक वर्ष में मरणोपरांत व विदेशियों को छोड़कर अधिकतम 120 पुरस्कार दिए जा सकते हैं; पदक पर कमल का फूल उत्कीर्ण होता है"],
        "q_en": "In the official hierarchy of Indian civilian honors below the Bharat Ratna, which decoration stands as India's SECOND-highest civilian award for 'exceptional and distinguished service'?",
        "q_hi": "भारत रत्न के बाद भारतीय नागरिक सम्मानों के आधिकारिक पदानुक्रम में 'असाधारण और विशिष्ट सेवा' हेतु दिया जाने वाला देश का दूसरा (2nd) सर्वोच्च नागरिक सम्मान कौन सा है?",
        "options_en": ["Padma Vibhushan (पद्म विभूषण)", "Padma Bhushan", "Padma Shri", "Param Vir Chakra"],
        "options_hi": ["पद्म विभूषण (Padma Vibhushan)", "पद्म भूषण (Padma Bhushan - तीसरा सर्वोच्च सम्मान)", "पद्म श्री (Padma Shri - चौथा सर्वोच्च सम्मान)", "परमवीर चक्र (यह सर्वोच्च सैन्य वीरता पुरस्कार है)"],
        "correct_idx": 0,
        "exp_en": "The hierarchy of Indian civilian decorations is: 1. Bharat Ratna, 2. Padma Vibhushan, 3. Padma Bhushan, 4. Padma Shri. Thus, Padma Vibhushan is the second-highest civilian award.",
        "exp_hi": "नागरिक सम्मानों का सही क्रम है: 1. भारत रत्न, 2. पद्म विभूषण, 3. पद्म भूषण, 4. पद्म श्री। अतः दूसरा सर्वोच्च नागरिक सम्मान पद्म विभूषण है।",
        "cue_en": "2nd highest civilian award = Padma Vibhushan.",
        "cue_hi": "दूसरा सर्वोच्च नागरिक सम्मान = पद्म विभूषण।",
        "wrong_en": ["Second-highest civilian decoration.", "Third-highest civilian decoration.", "Fourth-highest civilian decoration.", "Highest military gallantry decoration."],
        "wrong_hi": ["दूसरा सर्वोच्च नागरिक सम्मान।", "तीसरा सर्वोच्च नागरिक सम्मान।", "चौथा सर्वोच्च नागरिक सम्मान।", "सर्वोच्च सैन्य वीरता पुरस्कार।"]
    },
    {
        "name_en": "Wartime Gallantry Awards: Param Vir Chakra (PVC), Maha Vir Chakra & Major Somnath Sharma",
        "name_hi": "युद्धकालीन वीरता पुरस्कार: परमवीर चक्र (PVC), महावीर चक्र, वीर चक्र एवं मेजर सोमनाथ शर्मा",
        "concepts_en": ["Instituted on January 26, 1950 (with retrospective effect from August 15, 1947); awarded for conspicuous bravery or self-sacrifice in the presence of the enemy on land, sea, or air", "Param Vir Chakra (PVC): Highest wartime gallantry medal; designed by Savitri Khanolkar (Eve Yvonne Maday de Maros); circular bronze medal with 4 replicas of Indra's Vajra surrounding the state emblem; ribbon is plain purple", "First PVC recipient: Major Somnath Sharma (4 Kumaon Regiment, posthumously for Battle of Badgam, Kashmir, November 3, 1947)", "Total 21 PVCs awarded to date (14 posthumously); 4 living PVC recipients: Bana Singh (Siachen 1987), Yogendra Singh Yadav, Sanjay Kumar (Kargil 1999); youngest recipient: Arun Khetarpal (Battle of Basantar 1971, age 21)", "Hierarchy: 1. Param Vir Chakra, 2. Maha Vir Chakra, 3. Vir Chakra"],
        "concepts_hi": ["26 जनवरी 1950 को स्थापित (15 अगस्त 1947 से प्रभावी); शत्रु के समक्ष अदम्य साहस, पराक्रम या आत्मबलिदान के लिए", "परमवीर चक्र (PVC): भारत का सर्वोच्च युद्धकालीन सैन्य वीरता पदक; डिजाइन सावित्री खानोलकर द्वारा तैयार किया गया; पदक पर इंद्र के वज्र की 4 प्रतिकृतियां और बीच में अशोक स्तंभ; सादा बैंगनी फीता", "प्रथम परमवीर चक्र विजेता: मेजर सोमनाथ शर्मा (4 कुमाऊं रेजिमेंट, 3 नवंबर 1947 को कश्मीर के बडगाम युद्ध में अदम्य वीरता हेतु मरणोपरांत)", "अब तक कुल 21 जांबाज सैनिकों को परमवीर चक्र दिया गया है (14 मरणोपरांत); सबसे युवा विजेता सेकंड लेफ्टिनेंट अरुण खेत्रपाल (1971 बसंतर युद्ध, उम्र 21 वर्ष)", "क्रम: 1. परमवीर चक्र, 2. महावीर चक्र, 3. वीर चक्र"],
        "q_en": "Who was posthumously awarded independent India's very FIRST Param Vir Chakra (PVC) for supreme gallantry during the Battle of Badgam in Jammu & Kashmir in November 1947?",
        "q_hi": "नवंबर 1947 में जम्मू-कश्मीर के बडगाम के ऐतिहासिक युद्ध में सर्वोच्च बलिदान और अदम्य वीरता हेतु स्वतंत्र भारत के पहले 'परमवीर चक्र' (PVC) से मरणोपरांत किसे सम्मानित किया गया था?",
        "options_en": ["Major Somnath Sharma (मेजर सोमनाथ शर्मा - 4 कुमाऊं रेजिमेंट)", "Captain Vikram Batra", "Second Lieutenant Arun Khetarpal", "Subedar Major Bana Singh"],
        "options_hi": ["मेजर सोमनाथ शर्मा (Major Somnath Sharma - 1947)", "कैप्टन विक्रम बत्रा (1999 कारगिल युद्ध के परमवीर चक्र विजेता)", "सेकंड लेफ्टिनेंट अरुण खेत्रपाल (1971 के सबसे युवा परमवीर चक्र विजेता)", "सूबेदार मेजर बाना सिंह (1987 सियाचिन ऑपरेशन के विजेता)"],
        "correct_idx": 0,
        "exp_en": "Major Somnath Sharma of 4 Kumaon was the inaugural recipient of the Param Vir Chakra, posthumously recognized for holding the Badgam airfield against overwhelming tribal raiders in 1947 despite mortal wounds.",
        "exp_hi": "मेजर सोमनाथ शर्मा ने हाथ में प्लास्टर बंधा होने के बावजूद बडगाम हवाई अड्डे की रक्षा करते हुए अंतिम सांस तक दुश्मन का मुकाबला किया और भारत के पहले परमवीर चक्र से सम्मानित हुए।",
        "cue_en": "First Param Vir Chakra = Major Somnath Sharma (1947 Badgam).",
        "cue_hi": "प्रथम परमवीर चक्र = मेजर सोमनाथ शर्मा (1947 बडगाम)।",
        "wrong_en": ["First Param Vir Chakra recipient (1947).", "Kargil 1999 hero ('Yeh Dil Maange More').", "1971 Battle of Basantar hero (youngest recipient).", "1987 Operation Rajiv hero (Siachen Glacier)."],
        "wrong_hi": ["पहले परमवीर चक्र विजेता।", "1999 कारगिल युद्ध के महानायक।", "1971 के सबसे युवा विजेता।", "1987 सियाचिन के विजेता।"]
    },
    {
        "name_en": "Peacetime Gallantry Awards: Ashoka Chakra, Kirti Chakra & Shaurya Chakra",
        "name_hi": "शांतिकाल के वीरता पुरस्कार: अशोक चक्र (सर्वोच्च), कीर्ति चक्र एवं शौर्य चक्र",
        "concepts_en": ["Instituted on January 4, 1952 (originally called Ashoka Chakra Class I, II, and III; renamed in 1967 as Ashoka Chakra, Kirti Chakra, and Shaurya Chakra)", "Awarded for most conspicuous bravery, daring, or pre-eminent valor / self-sacrifice OTHER THAN in the face of the enemy (e.g., counter-terrorist operations, disaster rescue); open to military personnel and civilians alike", "Ashoka Chakra: Peacetime equivalent of the Param Vir Chakra; circular gold gilt medal with Ashoka's Chakra surrounded by lotus wreath; dark green ribbon with central orange vertical stripe", "First recipients (1952): Flight Lieutenant Suhas Biswas and Havildar Bachittar Singh", "Notable recipients: Neerja Bhanot (youngest recipient and first civilian woman, Pan Am 73 hijack 1986), Major Sandeep Unnikrishnan (26/11 Mumbai terror attacks)"],
        "concepts_hi": ["4 जनवरी 1952 को स्थापित (प्रारंभ में अशोक चक्र वर्ग I, II और III; 1967 में नाम बदलकर अशोक चक्र, कीर्ति चक्र और शौर्य चक्र किया गया)", "शत्रु के सीधे सामने के अलावा (अन्यथा) शांतिकाल में आतंकवाद विरोधी अभियानों, आपदा बचाव आदि में अदम्य साहस व सर्वोच्च बलिदान हेतु; सैनिकों और नागरिकों दोनों को दिया जा सकता है", "अशोक चक्र: शांतिकाल में परमवीर चक्र के समतुल्य सर्वोच्च पदक; पदक पर अशोक चक्र और कमल की माला उत्कीर्ण; गहरे हरे रंग का फीता जिसमें बीच में नारंगी पट्टी होती है", "प्रथम प्राप्तकर्ता (1952): फ्लाइट लेफ्टिनेंट सुहास विश्वास एवं हवलदार बचित्तर सिंह", "प्रमुख विजेता: नीरजा भानोट (1986 पैन एम 73 विमान अपहरण में जान बचाई, सबसे युवा व पहली नागरिक महिला विजेता), मेजर संदीप उन्नीकृष्णन (26/11 मुंबई हमला)"],
        "q_en": "Which decoration serves as India's HIGHEST military/civilian decoration for conspicuous bravery, valor, or self-sacrifice during PEACETIME (away from the face of the enemy)?",
        "q_hi": "शत्रु के सीधे मुकाबले के अलावा शांतिकाल (Peacetime) में आतंकवाद-रोधी अभियानों या असाधारण वीरता हेतु प्रदान किया जाने वाला भारत का सर्वोच्च वीरता पुरस्कार कौन सा है?",
        "options_en": ["Ashoka Chakra (अशोक चक्र - शांतिकालीन सर्वोच्च वीरता पदक)", "Kirti Chakra", "Shaurya Chakra", "Param Vir Chakra"],
        "options_hi": ["अशोक चक्र (Ashoka Chakra)", "कीर्ति चक्र (Kirti Chakra - द्वितीय शांतिकालीन वीरता पुरस्कार)", "शौर्य चक्र (Shaurya Chakra - तृतीय शांतिकालीन वीरता पुरस्कार)", "परमवीर चक्र (यह युद्धकालीन सर्वोच्च पदक है)"],
        "correct_idx": 0,
        "exp_en": "The Ashoka Chakra is India's highest peacetime military decoration awarded for valor, courageous action, or self-sacrifice away from the battlefield, equivalent in status to the wartime Param Vir Chakra.",
        "exp_hi": "शांतिकाल का सर्वोच्च वीरता पदक 'अशोक चक्र' है (जो युद्धकालीन परमवीर चक्र के बराबर दर्जा रखता है)। इसके बाद कीर्ति चक्र और शौर्य चक्र का स्थान आता है।",
        "cue_en": "Highest peacetime gallantry award = Ashoka Chakra.",
        "cue_hi": "सर्वोच्च शांतिकालीन वीरता पुरस्कार = अशोक चक्र।",
        "wrong_en": ["Highest peacetime gallantry award.", "Second-highest peacetime gallantry award.", "Third-highest peacetime gallantry award.", "Highest wartime gallantry award."],
        "wrong_hi": ["सर्वोच्च शांतिकालीन वीरता पदक।", "दूसरा शांतिकालीन वीरता पदक।", "तीसरा शांतिकालीन वीरता पदक।", "सर्वोच्च युद्धकालीन वीरता पदक।"]
    }
]

# S21-Ce927e9b3 Nobel Prizes: Will, Physics, Chemistry, Medicine, Peace & Economics (2 topics)
DATA["S21-Ce927e9b3"] = [
    {
        "name_en": "The Nobel Foundation: Alfred Nobel's Will (1895), Six Prize Domains & Awarding Bodies",
        "name_hi": "नोबेल फाउंडेशन: अल्फ्रेड नोबेल की वसीयत (1895), 6 पुरस्कार श्रेणियां एवं चयन संस्थाएं",
        "concepts_en": ["Alfred Bernhard Nobel (Swedish chemist and inventor of Dynamite, 1867): Bequeathed 94% of his fortune in his 1895 will to establish annual international prizes 'to those who, during the preceding year, have conferred the greatest benefit to humankind'", "First awarded in 1901 in five domains: Physics, Chemistry, Physiology or Medicine, Literature (presented in Stockholm, Sweden) and Peace (presented in Oslo, Norway)", "Sixth Prize: Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel (instituted 1968 by Sweden's central bank, first awarded in 1969 to Ragnar Frisch and Jan Tinbergen)", "Awarding bodies: Royal Swedish Academy of Sciences (Physics, Chemistry, Economics); Nobel Assembly at Karolinska Institute (Physiology or Medicine); Swedish Academy (Literature); Norwegian Nobel Committee appointed by Norwegian Parliament (Peace)", "Presented annually on December 10 (death anniversary of Alfred Nobel)"],
        "concepts_hi": ["अल्फ्रेड बर्नहार्ड नोबेल (स्वीडिश रसायनशास्त्री एवं डायनामाइट के आविष्कारक, 1867): 1895 की अपनी वसीयत में अपनी 94% संपत्ति मानवता के कल्याण हेतु अंतरराष्ट्रीय पुरस्कारों के लिए दान की", "प्रथम पुरस्कार 1901 में 5 क्षेत्रों में दिए गए: भौतिकी, रसायन, चिकित्सा, साहित्य (स्टॉकहोम, स्वीडन में प्रदत्त) एवं शांति (ओस्लो, नॉर्वे में प्रदत्त)", "छठी श्रेणी: अल्फ्रेड नोबेल की स्मृति में स्वेरिजेस रिक्सबैंक आर्थिक विज्ञान पुरस्कार (1968 में स्वीडन के केंद्रीय बैंक द्वारा स्थापित, 1969 में पहली बार रैग्नर फ्रिस्क और जन टिनबर्गेन को दिया गया)", "चयन संस्थाएं: रॉयल स्वीडिश एकेडमी ऑफ साइंसेज (भौतिकी, रसायन, अर्थशास्त्र); कारोलिंस्का इंस्टीट्यूट (चिकित्सा); स्वीडिश एकेडमी (साहित्य); नार्वेजियन नोबेल समिति (शांति)", "प्रतिवर्ष 10 दिसंबर (अल्फ्रेड नोबेल की पुण्यतिथि) को प्रदान किए जाते हैं"],
        "q_en": "Unlike the other five Nobel Prizes which are presented in Stockholm, Sweden, in which Nordic capital city is the prestigious Nobel Peace Prize presented each year?",
        "q_hi": "स्टॉकहोम (स्वीडन) में दिए जाने वाले अन्य पांच नोबेल पुरस्कारों के विपरीत, प्रतिष्ठित 'नोबेल शांति पुरस्कार' प्रतिवर्ष किस नॉर्डिक देश की राजधानी में प्रदान किया जाता है?",
        "options_en": ["Oslo, Norway (ओस्लो, नॉर्वे)", "Helsinki, Finland", "Copenhagen, Denmark", "Reykjavik, Iceland"],
        "options_hi": ["ओस्लो, नॉर्वे (Oslo, Norway)", "हेलसिंकी, फिनलैंड", "कोपेनहेगन, डेनमार्क", "रेक्याविक, आइसलैंड"],
        "correct_idx": 0,
        "exp_en": "Per Alfred Nobel's explicit will, the Nobel Peace Prize is selected by the Norwegian Nobel Committee and presented annually at the Oslo City Hall in Oslo, Norway, whereas all other prizes are awarded in Stockholm.",
        "exp_hi": "अल्फ्रेड नोबेल की वसीयत के अनुसार नोबेल शांति पुरस्कार नॉर्वे की संसद द्वारा चुनी गई समिति द्वारा दिया जाता है और इसका समारोह ओस्लो (नॉर्वे) में होता है; बाकी सभी पुरस्कार स्टॉकहोम (स्वीडन) में दिए जाते हैं।",
        "cue_en": "Nobel Peace Prize is presented in Oslo, Norway.",
        "cue_hi": "नोबेल शांति पुरस्कार = ओस्लो, नॉर्वे।",
        "wrong_en": ["Venue for Nobel Peace Prize.", "Capital of Finland.", "Capital of Denmark.", "Capital of Iceland."],
        "wrong_hi": ["शांति पुरस्कार का आयोजन स्थल।", "फिनलैंड की राजधानी।", "डेनमार्क की राजधानी।", "आइसलैंड की राजधानी।"]
    },
    {
        "name_en": "Indian & Indian-Origin Nobel Laureates: Tagore, Raman, Khurana, Mother Teresa, Chandrasekhar, Sen & Banerjee",
        "name_hi": "भारतीय एवं भारतीय मूल के नोबेल पुरस्कार विजेता: टैगोर, रमन, खुराना, टेरेसा, चंद्रशेखर, अमर्त्य सेन एवं अभिजीत बनर्जी",
        "concepts_en": ["Indian Citizens at time of award:", "1. Rabindranath Tagore (Literature, 1913 - Gitanjali, first Asian laureate)", "2. C.V. Raman (Physics, 1930 - Raman Effect of light scattering, first Asian scientist laureate)", "3. Mother Teresa (Peace, 1979 - Missionaries of Charity)", "4. Amartya Sen (Economics, 1998 - Welfare economics and famine studies)", "5. Kailash Satyarthi (Peace, 2014 - Bachpan Bachao Andolan, shared with Malala Yousafzai)", "Foreign citizens of Indian origin / birth:", "Har Gobind Khorana (Medicine 1968 - genetic code interpretation, US citizen); Subrahmanyan Chandrasekhar (Physics 1983 - Chandrasekhar Limit 1.44 M☉, US citizen); Venkatraman Ramakrishnan (Chemistry 2009 - ribosome structure, UK/US citizen); Abhijit Banerjee (Economics 2019 - experimental poverty alleviation, US citizen, shared with Esther Duflo and Michael Kremer)"],
        "concepts_hi": ["पुरस्कार के समय भारतीय नागरिक:", "1. रवींद्रनाथ टैगोर (साहित्य, 1913 - गीतांजलि, प्रथम एशियाई विजेता)", "2. सी.वी. रमन (भौतिकी, 1930 - रमन प्रभाव, प्रकाश का प्रकीर्णन, पहले एशियाई वैज्ञानिक)", "3. मदर टेरेसा (शांति, 1979 - मिशनरीज ऑफ चैरिटी)", "4. अमर्त्य सेन (अर्थशास्त्र, 1998 - कल्याणकारी अर्थशास्त्र व अकाल का विश्लेषण)", "5. कैलाश सत्यार्थी (शांति, 2014 - 'बचपन बचाओ आंदोलन', मलाला यूसुफजई के साथ साझा)", "भारतीय मूल के विदेशी नागरिक विजेता:", "हरगोविंद खुराना (चिकित्सा 1968 - आनुवंशिक कोड); सुब्रह्मण्यम चंद्रशेखर (भौतिकी 1983 - चंद्रशेखर सीमा 1.44 सौर द्रव्यमान); वेंकटरमन रामकृष्णन (रसायन 2009 - राइबोसोम संरचना); अभिजीत बनर्जी (अर्थशास्त्र 2019 - गरीबी उन्मूलन के प्रायोगिक दृष्टिकोण, एस्तेर डुफ्लो के साथ साझा)"],
        "q_en": "For which groundbreaking scientific discovery regarding the inelastic scattering of photons by matter was Sir C.V. Raman awarded the Nobel Prize in Physics in 1930, commemorated as National Science Day on February 28?",
        "q_hi": "पदार्थ द्वारा प्रकाश के प्रकीर्णन से संबंधित किस युगांतरकारी खोज के लिए सर सी.वी. रमन को 1930 में भौतिकी का नोबेल पुरस्कार दिया गया, जिसकी याद में प्रतिवर्ष 28 फरवरी को 'राष्ट्रीय विज्ञान दिवस' मनाया जाता है?",
        "options_en": ["Raman Effect (रमन प्रभाव / रमन प्रकीर्णन)", "Chandrasekhar Limit", "Compton Scattering", "Photoelectric Effect"],
        "options_hi": ["रमन प्रभाव (Raman Effect - 28 फरवरी 1928 को खोजा गया)", "चंद्रशेखर सीमा (Chandrasekhar Limit - यह एस. चंद्रशेखर ने खोजी)", "कॉम्पटन प्रकीर्णन (Compton Scattering)", "प्रकाश विद्युत प्रभाव (Photoelectric Effect - आइंस्टीन को नोबेल मिला)"],
        "correct_idx": 0,
        "exp_en": "Sir C.V. Raman announced the discovery of the 'Raman Effect' (inelastic scattering of light where scattered photons change wavelength due to molecular vibrational energy shifts) on February 28, 1928, earning him the 1930 Nobel Prize in Physics.",
        "exp_hi": "28 फरवरी 1928 को सर सी.वी. रमन ने 'रमन प्रभाव' की खोज की थी, जिसके लिए उन्हें 1930 का भौतिकी नोबेल पुरस्कार मिला। इसी उपलक्ष्य में हर साल 28 फरवरी को भारत में राष्ट्रीय विज्ञान दिवस मनाया जाता है।",
        "cue_en": "C.V. Raman Nobel 1930 = Raman Effect (National Science Day, Feb 28).",
        "cue_hi": "सी.वी. रमन नोबेल 1930 = रमन प्रभाव (राष्ट्रीय विज्ञान दिवस, 28 फरवरी)।",
        "wrong_en": ["Discovery of inelastic light scattering.", "Discovered by S. Chandrasekhar.", "X-ray scattering by Arthur Compton.", "Explained by Albert Einstein (Nobel 1921)."],
        "wrong_hi": ["रमन प्रभाव की खोज।", "चंद्रशेखर सीमा।", "कॉम्पटन प्रकीर्णन।", "आइंस्टीन का प्रकाश विद्युत प्रभाव।"]
    }
]

# S21-C1ef02426 Literary & Scientific Honors: Jnanpith, Booker, Fields Medal, Abel (2 topics)
DATA["S21-C1ef02426"] = [
    {
        "name_en": "Jnanpith Award & Sahitya Akademi: India's Premier Literary Honors & G. Sankara Kurup",
        "name_hi": "ज्ञानपीठ पुरस्कार एवं साहित्य अकादमी: भारत का सर्वोच्च साहित्यिक सम्मान एवं जी. शंकर कुरुप",
        "concepts_en": ["Jnanpith Award (instituted 1961 by Bharatiya Jnanpith, Sahu Shanti Prasad Jain family): Highest literary award in India; presented for outstanding lifetime contribution to Indian literature in any of the 22 languages recognized in the 8th Schedule of Constitution + English (added in 2013); carries ₹11 lakh cash prize, citation, and a bronze replica of Goddess Saraswati (Vagdevi of Dhar's Bhojshala)", "First Jnanpith Award (1965): Malayalam poet G. Sankara Kurup for his poetry collection 'Odakkuzhal' (The Bamboo Flute)", "First Woman Recipient (1976): Ashapoorna Devi for Bengali novel 'Pratham Pratishruti'", "First English Recipient (2018): Amitav Ghosh", "58th Jnanpith Award (2023, conferred 2024): Awarded jointly to Sanskrit scholar Jagadguru Rambhadracharya and legendary Urdu poet/lyricist Gulzar (Sampooran Singh Kalra)", "Sahitya Akademi Award (instituted 1954): Awarded annually in 24 languages (22 8th Schedule + English and Rajasthani)"],
        "concepts_hi": ["ज्ञानपीठ पुरस्कार: 1961 में भारतीय ज्ञानपीठ (साहू शांति प्रसाद जैन) द्वारा स्थापित; भारतीय साहित्य का सर्वोच्च साहित्यिक सम्मान; संविधान की 8वीं अनुसूची की 22 भाषाओं और अंग्रेजी (2013 में जोड़ी गई) में उत्कृष्ट योगदान हेतु; ₹11 लाख की राशि, प्रशस्ति पत्र एवं वाग्देवी (सरस्वती) की कांस्य प्रतिमा", "प्रथम ज्ञानपीठ पुरस्कार (1965): मलयालम कवि जी. शंकर कुरुप को उनकी काव्य कृति 'ओडक्कुझल' (बांसुरी) के लिए प्रदान किया गया", "प्रथम महिला प्राप्तकर्ता (1976): आशापूर्णा देवी (बांग्ला उपन्यास 'प्रथम प्रतिश्रुति')", "अंग्रेजी के पहले प्राप्तकर्ता (2018): अमिताव घोष", "58वां ज्ञानपीठ पुरस्कार (2023, 2024 में प्रदत्त): संस्कृत विद्वान जगद्गुरु रामभद्राचार्य एवं प्रसिद्ध उर्दू शायर/गीतकार गुलजार को संयुक्त रूप से", "साहित्य अकादमी पुरस्कार (1954): प्रतिवर्ष 24 भाषाओं (22 संविधान की + अंग्रेजी और राजस्थानी) की उत्कृष्ट कृतियों को प्रदान किया जाता है"],
        "q_en": "Who was the legendary Malayalam poet to receive the very FIRST Jnanpith Award in 1965 for his celebrated poetic work 'Odakkuzhal' (The Bamboo Flute)?",
        "q_hi": "1965 में अपनी प्रसिद्ध काव्य कृति 'ओडक्कुझल' (बांसुरी) के लिए पहला ज्ञानपीठ पुरस्कार प्राप्त करने वाले प्रख्यात मलयालम कवि कौन थे?",
        "options_en": ["G. Sankara Kurup (जी. शंकर कुरुप - 1965)", "Kuppali Venkatappa Puttappa (Kuvempu)", "Sumitranandan Pant", "Ramdhari Singh Dinkar"],
        "options_hi": ["जी. शंकर कुरुप (G. Sankara Kurup - 1965)", "कुवेम्पू (Kuvempu - 1967 में कन्नड़ हेतु विजेता)", "सुमित्रानंदन पंत (1968 में 'चिदंबरा' हेतु हिंदी के प्रथम विजेता)", "रामधारी सिंह दिनकर (1972 में 'उर्वशी' हेतु विजेता)"],
        "correct_idx": 0,
        "exp_en": "Mahakavi G. Sankara Kurup was honored with the inaugural Jnanpith Award in 1965 for his anthology of Malayalam poems 'Odakkuzhal' (The Bamboo Flute). Sumitranandan Pant was the first Hindi winner in 1968.",
        "exp_hi": "मलयालम के महाकवि जी. शंकर कुरुप को 1965 में पहला ज्ञानपीठ पुरस्कार मिला। हिंदी भाषा में पहला ज्ञानपीठ 1968 में सुमित्रानंदन पंत को 'चिदंबरा' के लिए मिला था।",
        "cue_en": "First Jnanpith Award (1965) = G. Sankara Kurup (Malayalam).",
        "cue_hi": "पहला ज्ञानपीठ पुरस्कार (1965) = जी. शंकर कुरुप (मलयालम)।",
        "wrong_en": ["First Jnanpith laureate in 1965.", "First Kannada Jnanpith winner (1967).", "First Hindi Jnanpith winner (1968 for Chidambara).", "Hindi Jnanpith winner in 1972 (Urvashi)."],
        "wrong_hi": ["1965 के प्रथम ज्ञानपीठ विजेता।", "कन्नड़ के पहले विजेता (1967)।", "हिंदी के पहले विजेता (1968)।", "1972 के विजेता (उर्वशी)।"]
    },
    {
        "name_en": "International Honours: Booker Prize, International Booker, Fields Medal & Abel Prize in Mathematics",
        "name_hi": "अंतर्राष्ट्रीय विशिष्ट पुरस्कार: बुकर पुरस्कार, अंतर्राष्ट्रीय बुकर, गणित का फील्ड्स मेडल एवं एबेल पुरस्कार",
        "concepts_en": ["Booker Prize (instituted 1969): Leading literary award for best original novel written in English and published in the UK/Ireland (£50,000 prize); Indian/Indian-origin winners: V.S. Naipaul (1971 - 'In a Free State'), Salman Rushdie (1981 - 'Midnight's Children'), Arundhati Roy (1997 - 'The God of Small Things', first Indian citizen woman), Kiran Desai (2006 - 'The Inheritance of Loss'), Aravind Adiga (2008 - 'The White Tiger')", "International Booker Prize: For fiction translated into English; won in 2022 by Indian author Geetanjali Shree for 'Tomb of Sand' (Ret Samadhi, translated by Daisy Rockwell - first Hindi novel to win)", "Mathematics Highest Honours (no Nobel in Math):", "1. Fields Medal: Instituted 1936 by Canadian mathematician John Charles Fields; awarded every 4 years by International Mathematical Union (IMU) to mathematicians under 40 years of age (Indian-origin winners: Manjul Bhargava in 2014, Akshay Venkatesh in 2018)", "2. Abel Prize: Instituted 2001 by Government of Norway; annual lifetime achievement award (Indian-American S.R. Srinivasa Varadhan won in 2007 for probability/large deviations)"],
        "concepts_hi": ["बुकर पुरस्कार (Booker Prize, 1969): अंग्रेजी भाषा के सर्वश्रेष्ठ उपन्यास हेतु (£50,000 पाउंड); भारतीय मूल के विजेता: वी.एस. नायपॉल (1971), सलमान रुश्दी (1981), अरुंधति रॉय (1997 - 'द गॉड ऑफ स्मॉल थिंग्स', पहली भारतीय महिला नागरिक विजेता), किरण देसाई (2006), अरविंद अडिगा (2008 - 'द व्हाइट टाइगर')", "अंतर्राष्ट्रीय बुकर पुरस्कार (International Booker Prize): अंग्रेजी में अनूदित उपन्यास हेतु; 2022 में गीतांजलि श्री ने 'रेत समाधि' ('Tomb of Sand', अनुवादक डेज़ी रॉकवेल) के लिए जीतकर इतिहास रचा (यह जीतने वाला पहला हिंदी उपन्यास)", "गणित के सर्वोच्च सम्मान (गणित में नोबेल नहीं होता):", "1. फील्ड्स मेडल (Fields Medal): 1936 से प्रति 4 वर्ष में 40 वर्ष से कम आयु के गणितज्ञों को दिया जाता है (भारतीय मूल के विजेता: मंजुल भार्गव 2014, अक्षय वेंकटेश 2018)", "2. एबेल पुरस्कार (Abel Prize): 2001 में नॉर्वे सरकार द्वारा स्थापित; गणित का वार्षिक लाइफटाइम सम्मान (भारतीय-अमेरिकी एस.आर. श्रीनिवास वर्धन ने 2007 में जीता)"],
        "q_en": "Who became the first Indian citizen woman to win the prestigious Booker Prize in 1997 for her debut semi-autobiographical novel 'The God of Small Things' set in Ayemenem, Kerala?",
        "q_hi": "केरल के अय्यमनम की पृष्ठभूमि पर रचित अपने पहले अर्ध-आत्मकथात्मक उपन्यास 'द गॉड ऑफ स्मॉल थिंग्स' (The God of Small Things) के लिए 1997 में प्रतिष्ठित बुकर पुरस्कार जीतने वाली पहली भारतीय महिला नागरिक कौन बनीं?",
        "options_en": ["Arundhati Roy (अरुंधति रॉय - 1997)", "Kiran Desai", "Jhumpa Lahiri", "Anita Desai"],
        "options_hi": ["अरुंधति रॉय (Arundhati Roy - 1997)", "किरण देसाई (Kiran Desai - 2006 में विजेता)", "झुम्पा लाहिड़ी (पुलित्जर पुरस्कार विजेता)", "अनीता देसाई (तीन बार बुकर की अंतिम सूची में नामांकित)"],
        "correct_idx": 0,
        "exp_en": "Arundhati Roy was awarded the 1997 Booker Prize for 'The God of Small Things', becoming the first Indian woman citizen to win the prize. (Kiran Desai won later in 2006).",
        "exp_hi": "अरुंधति रॉय ने 1997 में 'द गॉड ऑफ स्मॉल थिंग्स' के लिए बुकर पुरस्कार जीता था; वे यह उपलब्धि हासिल करने वाली पहली भारतीय महिला नागरिक बनीं।",
        "cue_en": "Booker Prize 1997 = Arundhati Roy (The God of Small Things).",
        "cue_hi": "बुकर पुरस्कार 1997 = अरुंधति रॉय (द गॉड ऑफ स्मॉल थिंग्स)।",
        "wrong_en": ["First Indian woman Booker winner (1997).", "Won Booker Prize in 2006 for The Inheritance of Loss.", "Won Pulitzer Prize for Fiction in 2000.", "Shortlisted three times for Booker Prize."],
        "wrong_hi": ["1997 की पहली भारतीय महिला बुकर विजेता।", "2006 की विजेता।", "पुलित्जर पुरस्कार विजेता।", "तीन बार नामांकित।"]
    }
]

print("Loaded S21 successfully")
