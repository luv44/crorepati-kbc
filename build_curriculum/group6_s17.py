# build_curriculum/group6_s17.py
# S17: Indian Art, Architecture & Cultural Heritage (8 topics across 2 chapters)

DATA = {}

# S17-C0375a3bf Indian Temple Architecture: Nagara, Dravida & Vesara Styles (3 topics)
DATA["S17-C0375a3bf"] = [
    {
        "name_en": "Nagara Style Temple Architecture: Curvilinear Shikhara, Amalaka & Khajuraho/Odisha Schools",
        "name_hi": "नागर शैली मंदिर स्थापत्य: रेखा-प्रसाद शिखर, आमलक एवं खजुराहो व ओडिशा उप-शैलियां",
        "concepts_en": ["Nagara Style (North India): Built on elevated plinth (Jagati); features curvilinear beehive-shaped tower (Shikhara/Rekha-Prasad), crowned by ribbed stone disc (Amalaka) and water pot (Kalasha); no elaborate boundary walls or Gopurams", "Core structural units: Garbhagriha (sanctum sanctorum), Mandapa (pillared assembly hall), Antarala (vestibule), Ardhamandapa (entrance porch)", "Khajuraho School (Chandela dynasty, MP): Kandariya Mahadeva Temple; erotic sculptures, interlocking sandstone, cruciform plan", "Odisha School: Lingaraja Temple (Bhubaneswar), Jagannath Temple (Puri), Sun Temple (Konark - Black Pagoda); classified into Rekha Deula (sanctum), Pidha Deula (mandapa), Khakhara Deula"],
        "concepts_hi": ["नागर शैली (उत्तर भारत): ऊंचे चबूतरे (जगती) पर निर्मित; वक्राकार शिखर (रेखा-प्रसाद), जिसके शीर्ष पर क्षैतिज चक्र जैसी 'आमलक' और उसके ऊपर 'कलश' स्थापित होता है; इसमें विशाल प्रवेश द्वार (गोपुरम) या चारदीवारी नहीं होती", "मूल संरचनात्मक अंग: गर्भगृह (मुख्य देवस्थान), मंडप (सभा भवन), अंतराल (गर्भगृह व मंडप का गलियारा), अर्धमंडप (प्रवेश द्वार)", "खजुराहो शैली (चंदेल शासक, म.प्र.): कंदारिया महादेव मंदिर; पंचायतन शैली, कामुक मूर्तियां, बलुआ पत्थर का प्रयोग", "ओडिशा उप-शैली: लिंगराज मंदिर (भुवनेश्वर), जगन्नाथ मंदिर (पुरी), कोणार्क का सूर्य मंदिर ('ब्लैक पैगोडा'); रेखा देउल (शिखर) और पीढ़ा देउल (मंडप)"],
        "q_en": "Which architectural feature uniquely crowns the soaring curvilinear Shikhara in classical Nagara-style North Indian temples, over which the Kalasha is installed?",
        "q_hi": "शास्त्रीय नागर शैली के उत्तर भारतीय मंदिरों में वक्राकार शिखर के शीर्ष पर स्थापित गोल चपटी पसलियों वाली वह पत्थर की चक्र संरचना क्या कहलाती है, जिसके ऊपर कलश स्थापित होता है?",
        "options_en": ["Amalaka (आमलक)", "Gopuram", "Vimana", "Antarala"],
        "options_hi": ["आमलक (Amalaka)", "गोपुरम (Gopuram - यह दक्षिण भारतीय द्रविड़ मंदिर का प्रवेश द्वार है)", "विमान (Vimana - द्रविड़ मंदिर का शिखर)", "अंतराल (Antarala)"],
        "correct_idx": 0,
        "exp_en": "In Nagara temple architecture, the curvilinear Shikhara is crowned by a large fluted stone disc called the 'Amalaka', symbolizing the sacred Amla fruit or sun, atop which rests the Kalasha.",
        "exp_hi": "नागर शैली के मंदिरों के शिखर के सबसे ऊपरी भाग पर आंवले के आकार का चपटा गोल पत्थर रखा होता है जिसे 'आमलक' कहते हैं; इसी के ऊपर पवित्र कलश स्थापित किया जाता है।",
        "cue_en": "Nagara temple crown stone = Amalaka.",
        "cue_hi": "नागर शिखर का शीर्ष चक्र = आमलक।",
        "wrong_en": ["Fluted stone disc crowning Nagara Shikhara.", "Ornate monumental gateway in Dravidian temples.", "Pyramidal tower in Dravidian temples.", "Vestibule connecting Garbhagriha and Mandapa."],
        "wrong_hi": ["नागर शिखर का शीर्ष भाग।", "द्रविड़ शैली का भव्य प्रवेश द्वार।", "द्रविड़ मंदिर का मीनारनुमा शिखर।", "मंडप और गर्भगृह का गलियारा।"]
    },
    {
        "name_en": "Dravida Style Temple Architecture: Pyramidal Vimana, Monolithic Gopuram & Chola Masterpieces",
        "name_hi": "द्रविड़ शैली मंदिर स्थापत्य: पिरामिडनुमा विमान, भव्य गोपुरम एवं चोल युगीन स्थापत्य (तंजावुर)",
        "concepts_en": ["Dravida Style (South India): Enclosed within high boundary walls (Prakara); towering stepped-pyramidal tower over sanctum called Vimana, crowned by octagonal/domical Shikhara (equivalent to stupika)", "Gopuram: Monumental, multi-tiered ornate entrance gateway (evolved under Pallavas, matured under Cholas, reached colossal heights under Vijayanagara/Nayakas)", "Temple water tank (Kalyani / Pushkarini) inside complex", "Brihadisvara Temple (Thanjavur, Tamil Nadu): Built by Rajaraja Chola I (1010 CE); granite monolithic 80-tonne kumbam dome atop 216-ft Vimana; UNESCO World Heritage site ('Great Living Chola Temples')"],
        "concepts_hi": ["द्रविड़ शैली (दक्षिण भारत): ऊंची चारदीवारी (प्राकार) से घिरा परिसर; गर्भगृह के ऊपर सीढ़ीदार पिरामिड के आकार का ऊंचा 'विमान' (Vimana), जिसके शीर्ष पर अष्टकोणीय स्तूपिका (शिखर) होती है", "गोपुरम (Gopuram): मंदिर परिसर का विशाल, बहुमंजिला और मूर्तियों से सुसज्जित भव्य प्रवेश द्वार (विजयनगर और नायक काल में यह विमान से भी ऊंचा हो गया)", "मंदिर परिसर में पवित्र जलाशय (कल्याणी / पुष्करिणी) अनिवार्य अंग", "बृहदेश्वर मंदिर (तंजावुर, तमिलनाडु): चोल सम्राट राजराज प्रथम (1010 ई.) द्वारा निर्मित; पूर्णतः ग्रेनाइट से निर्मित; 216 फीट ऊंचा विमान जिसके शीर्ष पर 80 टन का एकाश्म गुंबद है; यूनेस्को विश्व धरोहर स्थल"],
        "q_en": "Which majestic UNESCO World Heritage monument, built entirely of granite by Rajaraja Chola I around 1010 CE in Tamil Nadu, represents the pinnacle of Dravidian Vimana architecture?",
        "q_hi": "चोल सम्राट राजराज प्रथम द्वारा 1010 ईस्वी के आसपास तंजावुर (तमिलनाडु) में पूर्णतः ग्रेनाइट पत्थर से निर्मित वह विश्व धरोहर मंदिर कौन सा है, जो द्रविड़ शैली के 'विमान' का सर्वोच्च शिखर माना जाता है?",
        "options_en": ["Brihadisvara Temple, Thanjavur (तंजावुर का बृहदेश्वर / राजराजेश्वर मंदिर)", "Meenakshi Temple, Madurai", "Shore Temple, Mahabalipuram", "Kailasanatha Temple, Kanchipuram"],
        "options_hi": ["बृहदेश्वर मंदिर, तंजावुर (Brihadisvara Temple, Thanjavur)", "मीनाक्षी अम्मन मंदिर, मदुरै", "तट मंदिर (शोर टेंपल), महाबलीपुरम", "कैलाशनाथ मंदिर, कांचीपुरम"],
        "correct_idx": 0,
        "exp_en": "The Brihadisvara (Rajarajeswaram) Temple at Thanjavur, dedicated to Lord Shiva, was commissioned by Rajaraja I of the Chola dynasty. Its 13-tiered granite Vimana reaches a height of 66 meters without binding mortar.",
        "exp_hi": "तंजावुर का बृहदेश्वर मंदिर चोल वास्तुकला की पराकाष्ठा है; इसे राजराज चोल प्रथम ने भगवान शिव को समर्पित करते हुए बनवाया था। इसका 216 फीट ऊंचा विमान द्रविड़ वास्तुकला का बेजोड़ नमूना है।",
        "cue_en": "Brihadisvara Temple Thanjavur = Rajaraja Chola I (Dravida Vimana).",
        "cue_hi": "बृहदेश्वर मंदिर तंजावुर = राजराज प्रथम चोल (द्रविड़ विमान)।",
        "wrong_en": ["Pinnacle Chola Dravidian monument.", "Famous for soaring Nayaka Gopurams.", "Pallava monolithic rock-cut temple.", "Early structural Pallava temple."],
        "wrong_hi": ["द्रविड़ विमान का चोल स्मारक।", "विशाल गोपुरमों हेतु विख्यात।", "पल्लव कालीन तट मंदिर।", "पल्लव कालीन संरचनात्मक मंदिर।"]
    },
    {
        "name_en": "Vesara Hybrid Style: Badami Chalukyas, Hoysala Stellate Temples & Rashtrakuta Monoliths",
        "name_hi": "वेसर मिश्रित शैली: बादामी चालुक्य, होयसल नक्षत्रनुमा (ताराकार) मंदिर एवं राष्ट्रकूट एकाश्म (एलोरा)",
        "concepts_en": ["Vesara Style (Karnataka / Deccan): Hybrid blend combining North Indian Nagara curvilinear profile with South Indian Dravida stepped tiering; pioneered by Badami Chalukyas (Aihole, Pattadakal, Badami)", "Pattadakal (UNESCO): Virupaksha Temple (Dravida) and Papanatha Temple (Nagara) stand side by side", "Hoysala Style (Belur, Halebidu, Somanathapura): Stellate (star-shaped) ground plan; built using soft Chloritic Schist (soapstone) allowing intricate micro-carvings; elevated star-shaped Jagati platform; Hoysala Sacred Ensembles inscribed as UNESCO site in 2023", "Rashtrakuta Monolithic Kailash Temple (Cave 16, Ellora): Carved top-down from a single basalt cliff under King Krishna I (8th century CE)"],
        "concepts_hi": ["वेसर शैली (दक्कन/कर्नाटक): नागर (उत्तरी) और द्रविड़ (दक्षिणी) शैलियों का अनूठा संकर (मिश्रित) रूप; बादामी के चालुक्यों (ऐहोल, बादामी, पट्टदकल) द्वारा प्रारंभ", "पट्टदकल (यूनेस्को): विरुपाक्ष मंदिर (द्रविड़) और पापनाथ मंदिर (नागर) एक ही परिसर में साथ-साथ", "होयसल शैली (बेलूर, हलेबिदु, सोमनाथपुरा): नक्षत्रनुमा (ताराकार / Stellate) योजना पर निर्मित; सोपस्टोन (सैलखड़ी) पर बारीक नक्काशी; 2023 में यूनेस्को विश्व धरोहर घोषित", "राष्ट्रकूट कैलाश मंदिर (गुफा 16, एलोरा): राजा कृष्ण प्रथम द्वारा 8वीं सदी में ऊपर से नीचे की ओर एक ही विशाल बेसाल्ट पहाड़ी को तराशकर बनाया गया विश्व का सबसे बड़ा एकाश्म मंदिर"],
        "q_en": "Which distinctive architectural feature characterizes the Hoysala temples at Belur and Halebidu (inscribed as UNESCO World Heritage sites in 2023)?",
        "q_hi": "बेलूर और हलेबिदु के प्रसिद्ध होयसल मंदिरों (जिन्हें 2023 में यूनेस्को विश्व धरोहर सूची में शामिल किया गया) का आधार तल किस विशिष्ट ज्यामितीय आकार (प्लान) पर निर्मित है?",
        "options_en": ["Stellate (Star-shaped) Ground Plan (ताराकार / नक्षत्रनुमा आधार तल)", "Hexagonal Plan", "Purely Circular Plan", "Triangular Plan"],
        "options_hi": ["ताराकार / नक्षत्रनुमा आधार तल (Stellate / Star-shaped Plan)", "षट्कोणीय आधार", "पूर्णतः वृत्ताकार आधार", "त्रिभुजाकार आधार"],
        "correct_idx": 0,
        "exp_en": "Hoysala temples (Chennakeshava at Belur, Hoysaleswara at Halebidu) feature a unique stellate (star-shaped) platform and sanctum plan, providing numerous recessed wall surfaces for intricate soapstone carvings.",
        "exp_hi": "होयसल वास्तुशिल्प की सबसे प्रमुख विशेषता उसका 'ताराकार' (Star-shaped / Stellate) चबूतरा और आधार तल है, जिससे बाहरी दीवारों पर देवी-देवताओं और नर्तकियों की बारीक नक्काशी हेतु अतिरिक्त स्थान मिलता है।",
        "cue_en": "Hoysala temples = Stellate (star-shaped) plan + Soapstone carvings.",
        "cue_hi": "होयसल मंदिर = ताराकार (नक्षत्रनुमा) आधार + सोपस्टोन नक्काशी।",
        "wrong_en": ["Stellate star plan of Hoysala temples.", "Not used in Hoysala sanctum layout.", "Rarely seen in Deccan sanctums.", "Not a traditional Indian temple layout."],
        "wrong_hi": ["होयसल मंदिरों की ताराकार योजना।", "होयसल योजना में नहीं।", "वृत्ताकार नहीं।", "त्रिभुजाकार नहीं।"]
    }
]

# S17-C47d03ca3 Classical Dances, Folk Forms, Music & UNESCO Heritage Sites (5 topics)
DATA["S17-C47d03ca3"] = [
    {
        "name_en": "Indian Classical Dances: 8 Sangeet Natak Akademi Recognitions & Natya Shastra Roots",
        "name_hi": "भारतीय शास्त्रीय नृत्य: संगीत नाटक अकादमी द्वारा मान्य 8 नृत्य एवं नाट्यशास्त्र के मूल सिद्धांत",
        "concepts_en": ["Bharata Muni's Natya Shastra ('Fifth Veda'): Codifies Nritta (pure rhythmic movement), Nritya (expressive facial mime / Abhinaya), and Natya (dramatic storytelling); 9 Rasas (Navarasa)", "8 Classical Dances recognized by Sangeet Natak Akademi: 1. Bharatanatyam (Tamil Nadu - Ekaharya, fire dance), 2. Kathakali (Kerala - vibrant facial makeup, heroic mudras, Ramayana/Mahabharata drama), 3. Kathak (UP/North India - footwork/Tatkar, spins/Chakkars, Lucknow/Jaipur gharanas), 4. Odissi (Odisha - Tribhanga posture, Mahari/Gotipua traditions), 5. Kuchipudi (Andhra Pradesh - brass plate dance Tarangam), 6. Manipuri (Manipur - Raslila of Radha-Krishna, Pung Cholom), 7. Mohiniyattam (Kerala - Lasya feminine grace, white/gold Kasavu saree), 8. Sattriya (Assam - introduced by 15th-century Vaishnavite saint Srimanta Sankardev)", "(Ministry of Culture also includes Chhau as 9th)"],
        "concepts_hi": ["भरत मुनि का नाट्यशास्त्र: नृत्त (ताल-लयबद्ध शारीरिक गति), नृत्य (भाव-भंगिमा व अभिनय) एवं नाट्य (कथा-नाटक); नवरस", "संगीत नाटक अकादमी द्वारा मान्य 8 शास्त्रीय नृत्य: 1. भरतनाट्यम (तमिलनाडु - एकल स्त्री नृत्य, अग्नि नृत्य), 2. कथकली (केरल - विशाल मुखौटे/रंग, कथानक अभिनय), 3. कथक (उत्तर प्रदेश - घुंघरू की थाप/तत्कार, चक्कर, लखनऊ व जयपुर घराना), 4. ओडिसी (ओडिशा - त्रिभंग मुद्रा, जगन्नाथ संस्कृति), 5. कुचिपुड़ी (आंध्र प्रदेश - पीतल की थाली पर नृत्य 'तरंगम'), 6. मणिपुरी (मणिपुर - रासलीला, पुंग चोलोम ढोल), 7. मोहिनीअट्टम (केरल - लास्य भाव, सफेद-सुनहरी जरी की कसावु साड़ी), 8. सत्रिया (असम - 15वीं सदी में वैष्णव संत श्रीमंत शंकरदेव द्वारा सत्रों में विकसित)"],
        "q_en": "Which Indian classical dance form, rooted in the Vaishnavite monasteries (Satras) of Assam, was founded and propagated by the revered 15th-century Bhakti saint Srimanta Sankardev?",
        "q_hi": "असम के वैष्णव मठों (सत्रों) में 15वीं शताब्दी के महान भक्ति संत श्रीमंत शंकरदेव द्वारा विकसित और प्रचारित शास्त्रीय नृत्य कौन सा है?",
        "options_en": ["Sattriya (सत्रिया नृत्य - असम)", "Kathakali", "Mohiniyattam", "Odissi"],
        "options_hi": ["सत्रिया नृत्य (Sattriya - असम)", "कथकली (केरल)", "मोहिनीअट्टम (केरल)", "ओडिसी (ओडिशा)"],
        "correct_idx": 0,
        "exp_en": "Sattriya dance was created by Mahapurush Srimanta Sankardev in the 15th century as an accompaniment to the Ankia Naat (one-act plays) in Vaishnavite monasteries (Satras) of Assam, recognized by SNA in 2000.",
        "exp_hi": "सत्रिया नृत्य असम के वैष्णव मठों (सत्रों) से निकला है; इसे 15वीं सदी में महापुरुष श्रीमंत शंकरदेव ने भक्ति आंदोलन के प्रचार हेतु विकसित किया था। संगीत नाटक अकादमी ने वर्ष 2000 में इसे शास्त्रीय नृत्य का दर्जा दिया।",
        "cue_en": "Sattriya = Srimanta Sankardev (Assam Satras).",
        "cue_hi": "सत्रिया नृत्य = श्रीमंत शंकरदेव (असम के सत्र)।",
        "wrong_en": ["Classical dance from Assam Satras.", "Classical dance-drama from Kerala.", "Classical dance from Kerala.", "Classical dance from Odisha."],
        "wrong_hi": ["असम का शास्त्रीय नृत्य।", "केरल का शास्त्रीय नृत्य।", "केरल का लास्य नृत्य।", "ओडिशा का शास्त्रीय नृत्य।"]
    },
    {
        "name_en": "Hindustani vs Carnatic Music: Ragas, Talas, Gharanas & Trinity of Carnatic Music",
        "name_hi": "हिंदुस्तानी बनाम कर्नाटक शास्त्रीय संगीत: राग, ताल, घराना परंपरा एवं कर्नाटक संगीत के त्रिमूर्ति",
        "concepts_en": ["Two major traditions: Hindustani (North India - Persian/Central Asian Islamic influence) vs Carnatic (South India - indigenous, Kriti-centric)", "Raga (melodic framework based on 10 Thaats classified by V.N. Bhatkhande) and Tala (rhythmic cycle, e.g., Teental of 16 beats)", "Hindustani vocal forms: Dhrupad (ancient, spiritual, Gwalior/Darbhanga), Khayal (improvisational, Amir Khusrau roots), Thumri, Dadra, Ghazal", "Hindustani Gharanas: Gwalior (oldest), Agra, Kirana (Bhimsen Joshi), Patiala (Bade Ghulam Ali Khan), Jaipur-Atrauli", "Carnatic Music Trinity (Tiruvarur, 18th century): Tyagaraja, Muthuswami Dikshitar, and Syama Sastri; Purandara Dasa is revered as 'Pitamaha of Carnatic Music'"],
        "concepts_hi": ["भारतीय संगीत की दो मुख्य धाराएं: हिंदुस्तानी (उत्तर भारत - फारसी व मध्य एशियाई प्रभाव) बनाम कर्नाटक संगीत (दक्षिण भारत - मूल देशीय, कृति-प्रधान)", "राग (विष्णु नारायण भातखंडे द्वारा 10 ठाठों में वर्गीकृत) एवं ताल (लय चक्र, जैसे 16 मात्राओं का तीनताल)", "हिंदुस्तानी गायन शैलियां: ध्रुपद (प्राचीनतम, गंभीर व आध्यात्मिक), ख्याल (अमीर खुसरो द्वारा प्रेरित, तान-अलाप प्रधान), ठुमरी, टप्पा", "हिंदुस्तानी घराने: ग्वालियर (सबसे प्राचीन), किराना (पं. भीमसेन जोशी), पटियाला (बड़े गुलाम अली खां), आगरा, जयपुर", "कर्नाटक संगीत की त्रिमूर्ति (तिरुवारूर): संत त्यागराज, मुथुस्वामी दीक्षितर एवं श्यामा शास्त्री; पुरंदर दास को 'कर्नाटक संगीत का पितामह' कहा जाता है"],
        "q_en": "Who among the following 15th-16th century Haridasa saint-composers is universally venerated as the 'Pitamaha' (Father/Grandfather) of Carnatic Music for standardizing its foundational pedagogy?",
        "q_hi": "कर्नाटक संगीत की बुनियादी शिक्षा पद्धति (स्वर ज्ञान, अलंकार व गीत) को संहिताबद्ध करने के कारण 15वीं-16वीं सदी के किस हरिदास संत-संगीतकार को 'कर्नाटक संगीत का पितामह' कहा जाता है?",
        "options_en": ["Purandara Dasa (पुरंदर दास)", "Tyagaraja", "Muthuswami Dikshitar", "Syama Sastri"],
        "options_hi": ["पुरंदर दास (Purandara Dasa)", "संत त्यागराज (यह कर्नाटक संगीत त्रिमूर्ति के अंग हैं)", "मुथुस्वामी दीक्षितर", "श्यामा शास्त्री"],
        "correct_idx": 0,
        "exp_en": "Purandara Dasa (1484–1564), a prominent saint of the Haridasa movement in Vijayanagara, is revered as 'Karnataka Sangeeta Pitamaha' for establishing the foundational teaching syllabus (Mayamalavagowla raga exercises) still followed today.",
        "exp_hi": "विजयनगर साम्राज्य के समकालीन संत पुरंदर दास को 'कर्नाटक संगीत का पितामह' कहा जाता है, क्योंकि उन्होंने कर्नाटक संगीत सीखने के प्रारंभिक नियम, अभ्यास और अलंकार तैयार किए जो आज भी मान्य हैं।",
        "cue_en": "Pitamaha of Carnatic Music = Purandara Dasa.",
        "cue_hi": "कर्नाटक संगीत का पितामह = पुरंदर दास।",
        "wrong_en": ["Father of Carnatic music pedagogy.", "Foremost of the 18th-century Carnatic Trinity.", "Member of the Carnatic Trinity.", "Member of the Carnatic Trinity."],
        "wrong_hi": ["कर्नाटक संगीत के पितामह।", "कर्नाटक त्रिमूर्ति के प्रमुख संत।", "कर्नाटक त्रिमूर्ति के सदस्य।", "कर्नाटक त्रिमूर्ति के सदस्य।"]
    },
    {
        "name_en": "Folk Dance & Theatre Traditions of India: Yakshagana, Nautanki, Bihu, Garba & Kalbelia",
        "name_hi": "भारत की लोक नृत्य एवं लोक नाट्य परंपराएं: यक्षगान, नौटंकी, बिहू, गरबा एवं कालबेलिया",
        "concepts_en": ["Traditional Folk Theatres: Yakshagana (Karnataka - coastal dance-drama, elaborate headgear, Bhagavata narrator), Nautanki (Uttar Pradesh - musical operatic theatre, Nagada drum, Hathras/Kanpur styles), Tamasha (Maharashtra - Lavani dance), Bhavai (Gujarat/Rajasthan), Jatra (Bengal), Bhand Pather (Kashmir), Koodiyattam (Kerala - Sanskrit temple theatre, UNESCO Intangible Heritage)", "Folk Dances: Garba and Dandiya Raas (Gujarat - Navratri celebrations, inscribed on UNESCO Intangible Heritage in 2023), Bihu (Assam - Bohag/Rongali agricultural spring dance), Kalbelia (Rajasthan - snake-charmer community dance, UNESCO 2010), Ghoomar (Rajasthan - Bhil tribe roots), Bhangra and Giddha (Punjab), Chhau (tribal martial dance in Purulia, Seraikella, Mayurbhanj)"],
        "concepts_hi": ["पारंपरिक लोक नाट्य: यक्षगान (कर्नाटक - तटीय नृत्य-नाटिका, विशाल पगड़ी, भागवत गायक), नौटंकी (उत्तर प्रदेश - संगीतबद्ध स्वांग, नगाड़ा वाद्य), तमाशा (महाराष्ट्र - लावणी नृत्य आधारित), भवई (गुजरात), जात्रा (पश्चिम बंगाल), भांड पाथेर (कश्मीर), कूडियाट्टम (केरल - संस्कृत नाट्य, यूनेस्को अमूर्त धरोहर)", "प्रमुख लोक नृत्य: गरबा (गुजरात - नवरात्रि में घट-दीप के चारों ओर नृत्य, 2023 में यूनेस्को अमूर्त सांस्कृतिक धरोहर सूची में शामिल), बिहू (असम - रोंगाली बिहू कृषि पर्व), कालबेलिया (राजस्थान - सपेरा समुदाय का नागिन नृत्य, यूनेस्को 2010), घूमर (राजस्थान), भांगड़ा व गिद्दा (पंजाब), छऊ (झारखंड, ओडिशा, प. बंगाल का मुखौटा युद्ध नृत्य)"],
        "q_en": "In December 2023, which famous traditional community folk dance of Gujarat, performed during the nine nights of the Navratri festival, was officially inscribed on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity?",
        "q_hi": "दिसंबर 2023 में गुजरात के किस प्रसिद्ध पारंपरिक लोक नृत्य को, जो नवरात्रि के पावन पर्व पर मां दुर्गा की आराधना हेतु किया जाता है, यूनेस्को की मानवता की अमूर्त सांस्कृतिक धरोहर सूची में शामिल किया गया?",
        "options_en": ["Garba of Gujarat (गुजरात का गरबा नृत्य)", "Ghoomar of Rajasthan", "Bihu of Assam", "Lavani of Maharashtra"],
        "options_hi": ["गुजरात का गरबा नृत्य (Garba of Gujarat)", "राजस्थान का घूमर नृत्य", "असम का बिहू नृत्य", "महाराष्ट्र की लावणी"],
        "correct_idx": 0,
        "exp_en": "During the 18th session of the Intergovernmental Committee in Botswana in December 2023, UNESCO inscribed 'Garba of Gujarat' as India's 15th element on the Intangible Cultural Heritage list.",
        "exp_hi": "दिसंबर 2023 में यूनेस्को की अमूर्त सांस्कृतिक धरोहर समिति ने गुजरात के 'गरबा' नृत्य को मानवता की अमूर्त सांस्कृतिक धरोहर के रूप में मान्यता प्रदान की (यह भारत की 15वीं ऐसी अमूर्त धरोहर बनी)।",
        "cue_en": "Garba inscribed on UNESCO Intangible Heritage in 2023.",
        "cue_hi": "गरबा नृत्य = 2023 में यूनेस्को अमूर्त धरोहर घोषित।",
        "wrong_en": ["Inscribed on UNESCO list in 2023.", "Traditional Rajasthani dance.", "Assamese harvest folk dance.", "Maharashtrian rhythmic folk dance."],
        "wrong_hi": ["2023 में यूनेस्को अमूर्त सूची में शामिल।", "राजस्थान का लोक नृत्य।", "असम का लोक नृत्य।", "महाराष्ट्र का लोक नृत्य।"]
    },
    {
        "name_en": "Indian Painting Traditions: Mural Caves (Ajanta, Bagh, Lepakshi) & Miniature Schools",
        "name_hi": "भारतीय चित्रकला परंपराएं: प्राचीन भित्ति चित्र (अजंता, बाघ, लेपाक्षी) एवं लघु चित्रकला शैलियां (मुगल, राजस्थानी, पहाड़ी)",
        "concepts_en": ["Mural Paintings (Wall frescoes): Ajanta Caves (Maharashtra, 2nd BCE - 5th CE; Jataka tales, Bodhisattva Padmapani and Vajrapani using tempera on plaster), Bagh Caves (MP, Buddhist), Sittanavasal (Tamil Nadu, Jain murals), Lepakshi Veerabhadra Temple (Andhra Pradesh, Vijayanagara ceiling frescoes)", "Miniature Painting Schools: Manuscript illustrations on palm leaf (Pala Buddhist in East, Apabhramsha/Jain in Western India)", "Mughal Miniature School: Synthesized Persian elegance with Indian vibrancy; Akbar established Tasvir Khana (Hamzanama illustrations); Jahangir was master connoisseur of naturalism, birds, animals, portraiture (Ustad Mansur); Shah Jahan introduced jewel-like finish and borders", "Rajasthani Schools: Mewar, Marwar, Bundi, Kota (hunting scenes), Kishangarh (Nihal Chand's 'Bani Thani' - Indian Mona Lisa)", "Pahari Schools: Basohli (bold fiery colors) and Kangra (delicate lyricism, Nayika-Bheda)"],
        "concepts_hi": ["प्राचीन भित्ति चित्रकला (Murals): अजंता की गुफाएं (महाराष्ट्र - जातक कथाएं, पद्मपाणि व वज्रपाणि बोधिसत्व, टेम्परा पद्धति), बाघ की गुफाएं (म.प्र.), सित्तनवासल (तमिलनाडु - जैन भित्ति चित्र), लेपाक्षी (आंध्र प्रदेश - विजयनगर कालीन छत चित्र)", "लघु चित्रकला (Miniatures): ताड़पत्रों पर पाल (बौद्ध) व अपभ्रंश (जैन) पांडुलिपि चित्र", "मुगल चित्रकला: अकबर ने 'तस्वीर खाना' खोला (हम्जानामा); जहांगीर का काल मुगल चित्रकला का 'स्वर्ण युग' माना जाता है (प्रकृति, पक्षी व व्यक्ति चित्रकार उस्ताद मंसूर); शाहजहां काल में महीन बॉर्डर", "राजस्थानी शैलियां: मेवाड़, बूंदी, कोटा (शिकार दृश्य), किशनगढ़ शैली (निहाल चंद द्वारा चित्रित 'बणी-ठणी' - 'भारत की मोनालिसा')", "पहाड़ी शैलियां: बसोहली (तीव्र चटक रंग) एवं कांगड़ा शैली (गीतगोविंद व नायिका-भेद पर आधारित कोमल रेखाएं)"],
        "q_en": "The world-famous painting 'Bani Thani', celebrated as the 'Mona Lisa of India' and painted by master artist Nihal Chand, belongs to which distinct school of Rajasthani miniature painting?",
        "q_hi": "मास्टर चित्रकार निहाल चंद द्वारा चित्रित और 'भारत की मोनालिसा' कही जाने वाली विश्व प्रसिद्ध लघु चित्रकला 'बणी-ठणी' राजस्थानी चित्रकला की किस उप-शैली से संबंधित है?",
        "options_en": ["Kishangarh School (किशनगढ़ शैली / राजस्थान)", "Mewar School", "Bundi School", "Kangra School"],
        "options_hi": ["किशनगढ़ शैली (Kishangarh School)", "मेवाड़ शैली (Mewar School)", "बूंदी शैली (Bundi School)", "कांगड़ा शैली (Kangra School)"],
        "correct_idx": 0,
        "exp_en": "'Bani Thani', depicting the poet-singer mistress of King Sawant Singh (Nagari Das), was created by Nihal Chand in the Kishangarh court, renowned for arched eyes, sharp noses, and graceful demeanor.",
        "exp_hi": "किशनगढ़ के राजा सावंत सिंह (नागरीदास) के समय चित्रकार निहाल चंद ने 'बणी-ठणी' का कालजयी चित्र बनाया, जिसे कला मर्मज्ञ एरिक डिकिंसन ने 'भारत की मोनालिसा' की संज्ञा दी थी।",
        "cue_en": "Bani Thani (Indian Mona Lisa) = Kishangarh School (Nihal Chand).",
        "cue_hi": "बणी-ठणी = किशनगढ़ शैली (चित्रकार निहाल चंद)।",
        "wrong_en": ["Kishangarh miniature depicting Bani Thani.", "Known for Ragamala series.", "Known for lush vegetation and water bodies.", "Pahari lyricism school, not Rajasthani."],
        "wrong_hi": ["किशनगढ़ शैली की कृति।", "मेवाड़ शैली।", "बूंदी की चित्रकला।", "पहाड़ी शैली।"]
    },
    {
        "name_en": "UNESCO World Heritage Sites in India: Cultural, Natural & Mixed Sites (Khangchendzonga)",
        "name_hi": "भारत में यूनेस्को विश्व धरोहर स्थल: सांस्कृतिक, प्राकृतिक एवं एकमात्र मिश्रित स्थल (कंचनजंगा)",
        "concepts_en": ["UNESCO World Heritage Convention (1972); India currently has 42 World Heritage Sites (as of 2024: 34 Cultural, 7 Natural, and 1 Mixed Site)", "First sites inscribed in India (1983): Ajanta Caves, Ellora Caves, Agra Fort, Taj Mahal", "Recent Cultural Inscriptions: Dholavira (Harappan city, Gujarat, 2021), Kakatiya Rudreshwara / Ramappa Temple (Telangana, 2021), Santiniketan (West Bengal, 2023 - founded by Rabindranath Tagore), Sacred Ensembles of the Hoysalas (Karnataka, 2023), Moidams of the Ahom Dynasty (Assam, 2024)", "Sole Mixed World Heritage Site of India: Khangchendzonga National Park (Sikkim, inscribed in 2016 for outstanding biodiversity, sacred Mount Khangchendzonga, and Lepcha cultural lore)", "7 Natural Sites: Kaziranga, Keoladeo, Manas, Sundarbans, Nanda Devi & Valley of Flowers, Western Ghats, Great Himalayan National Park"],
        "concepts_hi": ["यूनेस्को विश्व धरोहर संधि (1972); भारत में कुल 42 विश्व धरोहर स्थल (34 सांस्कृतिक, 7 प्राकृतिक एवं 1 मिश्रित धरोहर स्थल)", "भारत के प्रथम स्थल (1983 में शामिल): अजंता गुफाएं, एलोरा गुफाएं, आगरा का किला और ताजमहल", "हालिया सांस्कृतिक धरोहरें: धोलावीरा (2021), रामप्पा मंदिर (2021), शांतिनिकेतन (2023 - रवींद्रनाथ टैगोर), होयसल के पवित्र मंदिर (2023), अहोम राजवंश के मोइदाम (असम, 2024)", "भारत का एकमात्र 'मिश्रित' (Mixed) विश्व धरोहर स्थल: कंचनजंगा राष्ट्रीय उद्यान (सिक्किम, 2016 में घोषित - अद्वितीय जैव विविधता एवं लेप्चा संस्कृति व पवित्र पर्वत हेतु)", "7 प्राकृतिक स्थल: काजीरंगा, मानस, केवलादेव, सुंदरबन, नंदा देवी व फूलों की घाटी, पश्चिमी घाट, ग्रेट हिमालयन राष्ट्रीय उद्यान"],
        "q_en": "Which national park in Sikkim holds the unique distinction of being India's ONLY 'Mixed' (both Cultural and Natural criteria) UNESCO World Heritage Site, inscribed in 2016?",
        "q_hi": "सिक्किम में स्थित वह राष्ट्रीय उद्यान कौन सा है, जिसे प्राकृतिक एवं सांस्कृतिक दोनों महत्वों के आधार पर भारत के एकमात्र 'मिश्रित' (Mixed) यूनेस्को विश्व धरोहर स्थल के रूप में 2016 में मान्यता दी गई थी?",
        "options_en": ["Khangchendzonga National Park, Sikkim (कंचनजंगा राष्ट्रीय उद्यान)", "Kaziranga National Park", "Sundarbans National Park", "Nanda Devi National Park"],
        "options_hi": ["कंचनजंगा राष्ट्रीय उद्यान (Khangchendzonga National Park, Sikkim)", "काजीरंगा राष्ट्रीय उद्यान (यह केवल प्राकृतिक स्थल है)", "सुंदरबन राष्ट्रीय उद्यान (यह केवल प्राकृतिक स्थल है)", "नंदा देवी राष्ट्रीय उद्यान (यह केवल प्राकृतिक स्थल है)"],
        "correct_idx": 0,
        "exp_en": "Khangchendzonga National Park in Sikkim was inscribed in 2016 as India's first and only 'Mixed' World Heritage site, recognized both for its spectacular alpine ecosystem/wildlife and the sacred mythological traditions of Tibetan Buddhists and Lepchas.",
        "exp_hi": "सिक्किम का कंचनजंगा राष्ट्रीय उद्यान भारत का एकमात्र मिश्रित विश्व धरोहर स्थल है; यह विश्व की तीसरी सबसे ऊंची चोटी, दुर्लभ वन्यजीवों (हिम तेंदुआ) और बौद्ध व लेप्चा जनजातियों की सांस्कृतिक मान्यताओं का संगम है।",
        "cue_en": "India's sole Mixed UNESCO site = Khangchendzonga National Park (Sikkim).",
        "cue_hi": "भारत का एकमात्र मिश्रित यूनेस्को स्थल = कंचनजंगा राष्ट्रीय उद्यान (सिक्किम)।",
        "wrong_en": ["India's only Mixed World Heritage Site.", "Natural site in Assam (one-horned rhinos).", "Natural mangrove site in West Bengal.", "Natural site in Uttarakhand."],
        "wrong_hi": ["भारत का एकमात्र मिश्रित धरोहर स्थल।", "असम का प्राकृतिक स्थल।", "प. बंगाल का मैंग्रोव स्थल।", "उत्तराखंड का प्राकृतिक स्थल।"]
    }
]

print("Loaded S17 successfully")
