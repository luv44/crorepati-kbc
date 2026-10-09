# build_curriculum/group1.py
# S01: India Basics & Physical Geography (13 topics)
# S02: Current Affairs & Contemporary Events (11 topics)
# S03: Ancient Indian History & Archaeology (30 topics)

DATA = {}

# S01
DATA["S01-C8994e811"] = [
    {
        "name_en": "Geographical Coordinates, Latitudinal & Longitudinal Extent of India",
        "name_hi": "भारत का भौगोलिक विस्तार, अक्षांशीय एवं देशांतरीय स्थिति",
        "concepts_en": ["Mainland latitude 8°4'N to 37°6'N", "Longitudinal extent 68°7'E to 97°25'E", "Total area 3.287 million sq km", "Seventh largest country globally"],
        "concepts_hi": ["मुख्य भूमि अक्षांश 8°4' उत्तर से 37°6' उत्तर", "देशांतरीय विस्तार 68°7' पूर्व से 97°25' पूर्व", "कुल क्षेत्रफल 32.87 लाख वर्ग किमी", "विश्व का सातवां सबसे बड़ा देश"],
        "q_en": "Between which latitudes does the mainland of India extend from South to North?",
        "q_hi": "भारत की मुख्य भूमि दक्षिण से उत्तर की ओर किन अक्षांशों के मध्य विस्तृत है?",
        "options_en": ["8°4' N and 37°6' N", "6°45' N and 35°8' N", "7°5' N and 36°4' N", "9°2' N and 38°1' N"],
        "options_hi": ["8°4' उत्तर और 37°6' उत्तर", "6°45' उत्तर और 35°8' उत्तर", "7°5' उत्तर और 36°4' उत्तर", "9°2' उत्तर और 38°1' उत्तर"],
        "correct_idx": 0,
        "exp_en": "According to the Survey of India, the mainland of India extends between latitudes 8°4'N and 37°6'N, and longitudes 68°7'E and 97°25'E.",
        "exp_hi": "सर्वे ऑफ इंडिया के अनुसार, भारत की मुख्य भूमि 8°4' उत्तरी अक्षांश से 37°6' उत्तरी अक्षांश तथा 68°7' पूर्वी देशांतर से 97°25' पूर्वी देशांतर के मध्य विस्तृत है।",
        "cue_en": "Remember: 8-4 south to 37-6 north.",
        "cue_hi": "याद रखें: 8°4' दक्षिण से 37°6' उत्तर।",
        "wrong_en": ["Matches mainland coordinates.", "6°45' N is Indira Point.", "Incorrect latitudinal span.", "Incorrect northern coordinate."],
        "wrong_hi": ["मुख्य भूमि का सही अक्षांशीय विस्तार है।", "6°45' उत्तर इंदिरा पॉइंट की स्थिति है, मुख्य भूमि नहीं।", "गलत अक्षांशीय मान।", "गलत उत्तरी अक्षांश।"]
    },
    {
        "name_en": "Indian Standard Time (IST) & 82°30' E Meridian",
        "name_hi": "भारतीय मानक समय (IST) एवं 82°30' पूर्वी याम्योत्तर",
        "concepts_en": ["Standard Meridian 82°30' E passes through Mirzapur (UP)", "Time offset UTC+05:30", "Disseminated by CSIR-NPL New Delhi", "Crosses 5 Indian states"],
        "concepts_hi": ["मानक याम्योत्तर 82°30' पूर्व मिर्जापुर (यूपी) से गुजरती है", "समय अंतराल UTC+05:30", "सीएसआईआर-एनपीएल नई दिल्ली द्वारा प्रसारित", "5 भारतीय राज्यों से होकर गुजरती है"],
        "q_en": "The Standard Meridian of India (82°30' E) passes through how many Indian states?",
        "q_hi": "भारतीय मानक समय (IST) की 82°30' पूर्वी याम्योत्तर रेखा भारत के कितने राज्यों से होकर गुजरती है?",
        "options_en": ["5 states (UP, MP, Chhattisgarh, Odisha, AP)", "4 states", "6 states", "7 states"],
        "options_hi": ["5 राज्य (उत्तर प्रदेश, मध्य प्रदेश, छत्तीसगढ़, ओडिशा, आंध्र प्रदेश)", "4 राज्य", "6 राज्य", "7 राज्य"],
        "correct_idx": 0,
        "exp_en": "The 82°30' E meridian passes through five states: Uttar Pradesh, Madhya Pradesh, Chhattisgarh, Odisha, and Andhra Pradesh.",
        "exp_hi": "82°30' पूर्वी देशांतर रेखा 5 राज्यों (उत्तर प्रदेश, मध्य प्रदेश, छत्तीसगढ़, ओडिशा और आंध्र प्रदेश) से होकर गुजरती है।",
        "cue_en": "UP, MP, CG, OD, AP = 5 states.",
        "cue_hi": "यूपी, एमपी, छत्तीसगढ़, ओडिशा, आंध्र प्रदेश = 5 राज्य।",
        "wrong_en": ["Covers all five states.", "Omits one state.", "Overcounts states.", "Exceeds actual count."],
        "wrong_hi": ["पांचों राज्यों को सही दर्शाता है।", "एक राज्य छूट गया है।", "अधिक संख्या है।", "वास्तविक संख्या से अधिक है।"]
    },
    {
        "name_en": "Geographical Extremities: Indira Col, Indira Point, Kibithu & Ghuar Moti",
        "name_hi": "भारत के सुदूरतम बिंदु: इंदिरा कोल, इंदिरा पॉइंट, किबिथू एवं घुआर मोती",
        "concepts_en": ["Northernmost: Indira Col (Ladakh)", "Southernmost point: Indira Point (Great Nicobar)", "Easternmost: Kibithu (Arunachal Pradesh)", "Westernmost: Ghuar Moti (Gujarat)"],
        "concepts_hi": ["उत्तरी बिंदु: इंदिरा कोल (लद्दाख)", "दक्षिणी बिंदु: इंदिरा पॉइंट (ग्रेट निकोबार)", "पूर्वी बिंदु: किबिथू (अरुणाचल प्रदेश)", "पश्चिमी बिंदु: घुआर मोती (गुजरात)"],
        "q_en": "Which of the following represents the easternmost point of India?",
        "q_hi": "निम्नलिखित में से कौन सा स्थान भारत का सुदूर पूर्वी बिंदु (Easternmost Point) है?",
        "options_en": ["Kibithu (Arunachal Pradesh)", "Ghuar Moti (Gujarat)", "Indira Col (Ladakh)", "Kanyakumari (Tamil Nadu)"],
        "options_hi": ["किबिथू (अरुणाचल प्रदेश)", "घुआर मोती (गुजरात)", "इंदिरा कोल (लद्दाख)", "कन्याकुमारी (तमिलनाडु)"],
        "correct_idx": 0,
        "exp_en": "Kibithu in Anjaw district of Arunachal Pradesh is the easternmost inhabited point of India at roughly 97°25' E.",
        "exp_hi": "अरुणाचल प्रदेश के अंजाव जिले में स्थित किबिथू (लगभग 97°25' पूर्वी देशांतर) भारत का सबसे पूर्वी बिंदु है।",
        "cue_en": "Kibithu = East, Ghuar Moti = West.",
        "cue_hi": "किबिथू = पूर्व, घुआर मोती = पश्चिम।",
        "wrong_en": ["Easternmost point.", "Westernmost point in Gujarat.", "Northernmost point in Ladakh.", "Southernmost mainland tip."],
        "wrong_hi": ["सही पूर्वी बिंदु है।", "गुजरात में पश्चिमी बिंदु है।", "लद्दाख में उत्तरी बिंदु है।", "मुख्य भूमि का दक्षिणी छोर है।"]
    },
    {
        "name_en": "Tropic of Cancer in India: States & Alignment",
        "name_hi": "कर्क रेखा का भारतीय राज्यों से होकर गुजरना",
        "concepts_en": ["Tropic of Cancer 23°26' N", "Passes through 8 Indian states", "Divides India into subtropical and tropical zones", "Mahi river cuts it twice"],
        "concepts_hi": ["कर्क रेखा 23°26' उत्तर", "8 भारतीय राज्यों से गुजरती है", "भारत को उपोष्ण और उष्णकटिबंधीय भागों में बांटती है", "माही नदी इसे दो बार काटती है"],
        "q_en": "Through which of the following groups of states does the Tropic of Cancer pass?",
        "q_hi": "कर्क रेखा (23°30' N) भारत के किस राज्य समूह से होकर गुजरती है?",
        "options_en": ["Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, Mizoram", "Gujarat, Maharashtra, MP, Odisha, Bengal", "Rajasthan, UP, Bihar, Jharkhand, Assam", "MP, UP, Bihar, West Bengal, Meghalaya"],
        "options_hi": ["गुजरात, राजस्थान, मध्य प्रदेश, छत्तीसगढ़, झारखंड, पश्चिम बंगाल, त्रिपुरा, मिजोरम", "गुजरात, महाराष्ट्र, मध्य प्रदेश, ओडिशा, पश्चिम बंगाल", "राजस्थान, उत्तर प्रदेश, बिहार, झारखंड, असम", "मध्य प्रदेश, उत्तर प्रदेश, बिहार, पश्चिम बंगाल, मेघालय"],
        "correct_idx": 0,
        "exp_en": "The Tropic of Cancer passes through 8 states: Gujarat, Rajasthan, MP, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram.",
        "exp_hi": "कर्क रेखा भारत के 8 राज्यों से गुजरती है: गुजरात, राजस्थान, मध्य प्रदेश, छत्तीसगढ़, झारखंड, पश्चिम बंगाल, त्रिपुरा और मिजोरम।",
        "cue_en": "8 states: 'Mitra par Gamcha Jhar' mnemonic.",
        "cue_hi": "'मित्र पर गमछा झार' सूत्र: मिजोरम, त्रिपुरा, पश्चिम बंगाल, राजस्थान, गुजरात, मध्य प्रदेश, छत्तीसगढ़, झारखंड।",
        "wrong_en": ["Accurate list of 8 states.", "Maharashtra and Odisha not crossed.", "UP and Bihar not crossed.", "UP and Meghalaya not crossed."],
        "wrong_hi": ["सभी 8 राज्य सही हैं।", "महाराष्ट्र और ओडिशा से नहीं गुजरती।", "यूपी और बिहार से नहीं गुजरती।", "यूपी और मेघालय से नहीं गुजरती।"]
    },
    {
        "name_en": "Coastal Boundaries, Island Territories & Maritime Zones",
        "name_hi": "तटीय सीमाएं, द्वीपीय क्षेत्र एवं समुद्री क्षेत्र",
        "concepts_en": ["Mainland coastline 5,422.6 km", "Total coastline with islands 7,516.6 km", "Exclusive Economic Zone (EEZ) 200 nautical miles", "Territorial sea 12 nautical miles"],
        "concepts_hi": ["मुख्य भूमि तटरेखा 5,422.6 किमी", "द्वीपों सहित कुल तटरेखा 7,516.6 किमी", "अनन्य आर्थिक क्षेत्र (EEZ) 200 समुद्री मील", "प्रादेशिक समुद्री सीमा 12 समुद्री मील"],
        "q_en": "What is the total length of the coastline of India, including its island territories?",
        "q_hi": "द्वीपीय क्षेत्रों सहित भारत की कुल समुद्री तटरेखा की लंबाई कितनी है?",
        "options_en": ["7,516.6 km", "6,100 km", "5,422.6 km", "15,200 km"],
        "options_hi": ["7,516.6 किमी", "6,100 किमी", "5,422.6 किमी", "15,200 किमी"],
        "correct_idx": 0,
        "exp_en": "The total coastline of India including Andaman & Nicobar and Lakshadweep islands measures 7,516.6 km. The mainland coastline alone is 5,422.6 km.",
        "exp_hi": "अंडमान-निकोबार और लक्षद्वीप सहित भारत की कुल तटरेखा 7,516.6 किमी है, जबकि मुख्य भूमि की तटरेखा 5,422.6 किमी है।",
        "cue_en": "7516.6 km total; 15200 km land border.",
        "cue_hi": "7,516.6 किमी कुल तटरेखा; 15,200 किमी स्थलीय सीमा।",
        "wrong_en": ["Accurate total coastline.", "Traditional round figure for mainland.", "Exact mainland coastline.", "Total terrestrial land frontier."],
        "wrong_hi": ["द्वीप समूहों सहित सही कुल तटरेखा।", "मुख्य भूमि का अनुमानित पुराना आंकड़ा।", "केवल मुख्य भूमि की तटरेखा।", "भारत की कुल स्थलीय सीमा की लंबाई।"]
    }
]

DATA["S01-Cac567568"] = [
    {
        "name_en": "Himalayan Mountain System: Trans, Greater, Lesser Himalayas & Shiwaliks",
        "name_hi": "हिमालय पर्वत प्रणाली: ट्रांस, वृहद, मध्य हिमालय एवं शिवालिक",
        "concepts_en": ["Young fold mountains formed by Indo-Eurasian collision", "Himadri (Greater Himalayas) average height 6,000 m", "Himachal (Lesser Himalayas)", "Shiwaliks outer range"],
        "concepts_hi": ["भारत-यूरेशियाई प्लेटों के टकराव से निर्मित नवीन वलित पर्वत", "हिमाद्रि (वृहद हिमालय) औसत ऊंचाई 6,000 मी", "हिमाचल (लघु हिमालय)", "शिवालिक बाह्य श्रृंखला"],
        "q_en": "Which is the highest mountain peak situated entirely within India's internationally recognized territory?",
        "q_hi": "भारत की राजनीतिक सीमाओं के भीतर स्थित सबसे ऊंची पर्वत चोटी कौन सी है?",
        "options_en": ["Kangchenjunga (8,586 m)", "Nanda Devi (7,816 m)", "Kamet (7,756 m)", "Saltoro Kangri (7,742 m)"],
        "options_hi": ["कंचनजंघा (8,586 मी)", "नंदा देवी (7,816 मी)", "कामेत (7,756 मी)", "साल्तोरो कांगड़ी (7,742 मी)"],
        "correct_idx": 0,
        "exp_en": "Kangchenjunga in Sikkim (8,586 m) is the highest peak administered by India. Nanda Devi is the highest peak located entirely within India without sharing an international border.",
        "exp_hi": "सिक्किम में स्थित कंचनजंघा (8,586 मीटर) भारत द्वारा प्रशासित सबसे ऊंची चोटी है। नंदा देवी पूरी तरह से बिना किसी अंतरराष्ट्रीय सीमा साझा किए भारत के भीतर स्थित सबसे ऊंची चोटी है।",
        "cue_en": "Kangchenjunga = Sikkim, 8586 m.",
        "cue_hi": "कंचनजंघा = सिक्किम, 8,586 मीटर।",
        "wrong_en": ["Highest peak administered by India.", "Highest completely within India's interior.", "Second highest in Garhwal.", "Peak in Karakoram range."],
        "wrong_hi": ["भारत द्वारा प्रशासित सबसे ऊंची चोटी।", "पूरी तरह से भारतीय भूभाग के भीतर स्थित सबसे ऊंची चोटी।", "गढ़वाल की दूसरी सबसे ऊंची चोटी।", "काराकोरम श्रेणी की चोटी।"]
    },
    {
        "name_en": "Major Himalayan Mountain Passes: Strategic & Geographical Routes",
        "name_hi": "प्रमुख हिमालयी दर्रे: रणनीतिक एवं भौगोलिक मार्ग",
        "concepts_en": ["Zoji La connects Srinagar to Leh", "Shipki La in Himachal Pradesh", "Nathu La in Sikkim", "Bomdi La in Arunachal Pradesh"],
        "concepts_hi": ["ज़ोजिला श्रीनगर को लेह से जोड़ता है", "शिपकी ला हिमाचल प्रदेश में", "नाथू ला सिक्किम में", "बोमडिला अरुणाचल प्रदेश में"],
        "q_en": "Which Himalayan mountain pass connects the Kashmir Valley with Ladakh (Srinagar to Leh)?",
        "q_hi": "निम्नलिखित में से कौन सा हिमालयी दर्रा श्रीनगर को लेह (लद्दाख) से जोड़ता है?",
        "options_en": ["Zoji La", "Shipki La", "Nathu La", "Rohtang Pass"],
        "options_hi": ["ज़ोजिला (Zoji La)", "शिपकी ला", "नाथू ला", "रोहतांग दर्रा"],
        "correct_idx": 0,
        "exp_en": "Zoji La at an altitude of 3,528 m on NH-1 connects the Kashmir Valley with Ladakh.",
        "exp_hi": "राष्ट्रीय राजमार्ग-1 पर 3,528 मीटर की ऊंचाई पर स्थित ज़ोजिला दर्रा कश्मीर घाटी को लद्दाख (लेह) से जोड़ता है।",
        "cue_en": "Zoji La: Srinagar to Leh.",
        "cue_hi": "ज़ोजिला: श्रीनगर से लेह।",
        "wrong_en": ["Connects Srinagar to Leh.", "Connects Himachal with Tibet.", "Connects Sikkim with Tibet.", "Connects Kullu with Lahaul-Spiti."],
        "wrong_hi": ["श्रीनगर को लेह से जोड़ता है।", "हिमाचल प्रदेश को तिब्बत से जोड़ता है।", "सिक्किम को तिब्बत से जोड़ता है।", "कुल्लू को लाहौल-स्पीति से जोड़ता है।"]
    },
    {
        "name_en": "Peninsular Plateau, Western Ghats & Eastern Ghats",
        "name_hi": "प्रायद्वीपीय पठार, पश्चिमी घाट एवं पूर्वी घाट",
        "concepts_en": ["Ancient Gondwana landmass", "Western Ghats continuous, higher elevation", "Anamudi (2,695 m) highest peak in South India", "Eastern Ghats discontinuous"],
        "concepts_hi": ["प्राचीन गोंडवाना भूभाग का हिस्सा", "पश्चिमी घाट सतत और अधिक ऊंचे हैं", "अनाईमुडी (2,695 मी) दक्षिण भारत की सबसे ऊंची चोटी", "पूर्वी घाट खंडित और कम ऊंचे"],
        "q_en": "Which is the highest peak in Peninsular India and the Western Ghats?",
        "q_hi": "प्रायद्वीपीय भारत एवं पश्चिमी घाट की सबसे ऊंची पर्वत चोटी कौन सी है?",
        "options_en": ["Anamudi (2,695 m)", "Doddabetta (2,637 m)", "Arma Konda (1,680 m)", "Kalsubai (1,646 m)"],
        "options_hi": ["अनाईमुडी (2,695 मी)", "दोड्डाबेट्टा (2,637 मी)", "अरमा कोंडा (1,680 मी)", "कलसुबाई (1,646 मी)"],
        "correct_idx": 0,
        "exp_en": "Anamudi in the Anaimalai Hills of Kerala (2,695 m) is the highest peak in Peninsular India.",
        "exp_hi": "केरल की अन्नामलाई पहाड़ियों में स्थित अनाईमुडी (2,695 मीटर) प्रायद्वीपीय भारत एवं पश्चिमी घाट की सर्वोच्च चोटी है।",
        "cue_en": "Anamudi = 2,695 m in Kerala.",
        "cue_hi": "अनाईमुडी = 2,695 मीटर, केरल।",
        "wrong_en": ["Highest in South India.", "Highest peak in Nilgiri Hills.", "Highest in Eastern Ghats.", "Highest peak in Maharashtra."],
        "wrong_hi": ["दक्षिण भारत की सर्वोच्च चोटी।", "नीलगिरि पहाड़ियों की सबसे ऊंची चोटी।", "पूर्वी घाट की सर्वोच्च चोटी।", "महाराष्ट्र की सबसे ऊंची चोटी।"]
    },
    {
        "name_en": "Indus River Basin & Tributaries (Panchnad)",
        "name_hi": "सिंधु नदी तंत्र एवं पंचनद सहायक नदियां",
        "concepts_en": ["Origin near Lake Mansarovar (Bokhar Chu glacier)", "Panchnad: Jhelum, Chenab, Ravi, Beas, Sutlej", "Indus Waters Treaty (1960)", "Chenab largest tributary"],
        "concepts_hi": ["मानसरोवर झील के निकट बोखार चू हिमनद से उद्गम", "पंचनद: झेलम, चेनाब, रावी, ब्यास, सतलुज", "सिंधु जल संधि (1960)", "चेनाब सबसे बड़ी सहायक नदी"],
        "q_en": "Which tributary of the Indus originates from the Rohtang Pass and flows entirely within India before joining the Sutlej?",
        "q_hi": "सिंधु की कौन सी सहायक नदी रोहतांग दर्रे से निकलती है और पूरी तरह भारत के भीतर बहते हुए सतलुज में मिलती है?",
        "options_en": ["Beas (ब्यास)", "Chenab (चेनाब)", "Ravi (रावी)", "Jhelum (झेलम)"],
        "options_hi": ["ब्यास (Beas)", "चेनाब (Chenab)", "रावी (Ravi)", "झेलम (Jhelum)"],
        "correct_idx": 0,
        "exp_en": "The Beas originates near Rohtang Pass in Himachal Pradesh and merges with the Sutlej at Harike in Punjab, flowing entirely in India.",
        "exp_hi": "ब्यास नदी हिमाचल प्रदेश के रोहतांग दर्रे के पास व्यास कुंड से निकलती है और पंजाब के हरिके में सतलुज से मिलती है; यह पूरी तरह भारत में बहती है।",
        "cue_en": "Beas flows entirely in India.",
        "cue_hi": "ब्यास पूरी तरह से भारत में प्रवाहित होती है।",
        "wrong_en": ["Flows entirely within India.", "Largest tributary, flows into Pakistan.", "Ravi flows into Pakistan.", "Jhelum originates at Verinag."],
        "wrong_hi": ["पूर्णतः भारतीय क्षेत्र में प्रवाहित होती है।", "सबसे बड़ी सहायक, पाकिस्तान जाती है।", "रावी पाकिस्तान में बहती है।", "झेलम वेरीनाग से निकलती है।"]
    }
]

DATA["S01-C4d19bee9"] = [
    {
        "name_en": "Ganga-Brahmaputra River System & Water Divides",
        "name_hi": "गंगा-ब्रह्मपुत्र नदी तंत्र एवं जल विभाजक",
        "concepts_en": ["Ganga forms at Devprayag (Bhagirathi + Alaknanda)", "Length 2,525 km", "Brahmaputra originates as Tsangpo", "Sundarbans delta largest globally"],
        "concepts_hi": ["देवप्रयाग में भागीरथी और अलकनंदा के संगम से गंगा का निर्माण", "लंबाई 2,525 किमी", "ब्रह्मपुत्र का उद्गम तिब्बत में सांगपो के रूप में", "सुंदरबन डेल्टा विश्व का सबसे बड़ा डेल्टा"],
        "q_en": "At which confluence do the Bhagirathi and Alaknanda rivers meet to form the Ganga?",
        "q_hi": "भागीरथी और अलकनंदा नदियों का संगम किस स्थान पर होता है, जहां से इसे 'गंगा' कहा जाता है?",
        "options_en": ["Devprayag (देवप्रयाग)", "Rudraprayag (रुद्रप्रयाग)", "Karnaprayag (कर्णप्रयाग)", "Vishnuprayag (विष्णुप्रयाग)"],
        "options_hi": ["देवप्रयाग (Devprayag)", "रुद्रप्रयाग (Rudraprayag)", "कर्णप्रयाग (Karnaprayag)", "विष्णुप्रयाग (Vishnuprayag)"],
        "correct_idx": 0,
        "exp_en": "At Devprayag in Uttarakhand, the Bhagirathi and Alaknanda rivers meet; down from this point the river is known as the Ganga.",
        "exp_hi": "उत्तराखंड के देवप्रयाग में भागीरथी और अलकनंदा का संगम होता है, जिसके आगे इसे पवित्र नदी 'गंगा' के नाम से जाना जाता है।",
        "cue_en": "Devprayag = Bhagirathi + Alaknanda.",
        "cue_hi": "देवप्रयाग = भागीरथी + अलकनंदा।",
        "wrong_en": ["Confluence forming the Ganga.", "Alaknanda meets Mandakini.", "Alaknanda meets Pindar.", "Alaknanda meets Dhauliganga."],
        "wrong_hi": ["गंगा नदी का निर्माण स्थल।", "अलकनंदा और मंदाकिनी का संगम।", "अलकनंदा और पिंडर का संगम।", "अलकनंदा और धौलीगंगा का संगम।"]
    },
    {
        "name_en": "Peninsular River Systems: Godavari, Krishna & Cauvery",
        "name_hi": "प्रायद्वीपीय नदी प्रणालियां: गोदावरी, कृष्णा एवं कावेरी",
        "concepts_en": ["Godavari longest peninsular river (1,465 km, Dakshin Ganga)", "Krishna originates at Mahabaleshwar", "Cauvery originates at Talakaveri", "East-flowing into Bay of Bengal"],
        "concepts_hi": ["गोदावरी प्रायद्वीपीय भारत की सबसे लंबी नदी (1,465 किमी, दक्षिण गंगा)", "कृष्णा नदी महाबलेश्वर से निकलती है", "कावेरी तालकावेरी से निकलती है", "बंगाल की खाड़ी में गिरने वाली पूर्व वाहिनी नदियां"],
        "q_en": "Which river is known as 'Dakshin Ganga' (Ganges of the South) owing to its length and basin size?",
        "q_hi": "अपनी लंबाई एवं विशाल बेसिन के कारण किस नदी को 'दक्षिण गंगा' कहा जाता है?",
        "options_en": ["Godavari (गोदावरी)", "Krishna (कृष्णा)", "Cauvery (कावेरी)", "Mahanadi (महानदी)"],
        "options_hi": ["गोदावरी (Godavari)", "कृष्णा (Krishna)", "कावेरी (Cauvery)", "महानदी (Mahanadi)"],
        "correct_idx": 0,
        "exp_en": "Godavari with a length of 1,465 km is the longest river in peninsular India, originating at Trimbakeshwar in Maharashtra.",
        "exp_hi": "महाराष्ट्र के त्र्यंबकेश्वर से निकलने वाली गोदावरी नदी (1,465 किमी) प्रायद्वीपीय भारत की सबसे लंबी नदी है, जिसे दक्षिण गंगा कहा जाता है।",
        "cue_en": "Godavari = Dakshin Ganga (1,465 km).",
        "cue_hi": "गोदावरी = दक्षिण गंगा (1,465 किमी)।",
        "wrong_en": ["Longest peninsular river.", "Second longest peninsular river.", "Called Ganga of South India for sacredness.", "Major river of Odisha."],
        "wrong_hi": ["प्रायद्वीपीय भारत की सबसे लंबी नदी।", "दूसरी सबसे लंबी प्रायद्वीपीय नदी।", "पवित्रता की दृष्टि से दक्षिण की गंगा।", "ओडिशा की प्रमुख नदी।"]
    },
    {
        "name_en": "West Flowing Rivers: Narmada, Tapti & Rift Valley Drainage",
        "name_hi": "पश्चिम वाहिनी नदियां: नर्मदा, ताप्ती एवं भ्रंश घाटी अपवाह",
        "concepts_en": ["Narmada originates at Amarkantak", "Flows through rift valley between Vindhyas and Satpuras", "Forms Dhuandhar Falls", "Tapti originates at Multai"],
        "concepts_hi": ["नर्मदा का उद्गम अमरकंटक से", "विंध्य और सतपुड़ा के बीच भ्रंश घाटी (Rift Valley) से प्रवाह", "धुआंधार जलप्रपात का निर्माण", "ताप्ती मुलताई से निकलती है"],
        "q_en": "The Narmada river flows westwards through a rift valley situated between which two mountain ranges?",
        "q_hi": "नर्मदा नदी किन दो पर्वत श्रेणियों के मध्य स्थित भ्रंश घाटी (Rift Valley) से होकर पश्चिम की ओर बहती है?",
        "options_en": ["Vindhya and Satpura ranges", "Satpura and Ajanta ranges", "Aravalli and Vindhya ranges", "Western Ghats and Eastern Ghats"],
        "options_hi": ["विंध्याचल और सतपुड़ा पर्वत श्रेणियां", "सतपुड़ा और अजंता पर्वत श्रेणियां", "अरावली और विंध्याचल श्रेणियां", "पश्चिमी घाट और पूर्वी घाट"],
        "correct_idx": 0,
        "exp_en": "The Narmada river originates at Amarkantak and flows through a rift valley between the Vindhyan range to the north and the Satpura range to the south.",
        "exp_hi": "नर्मदा नदी उत्तर में विंध्याचल और दक्षिण में सतपुड़ा पर्वत श्रृंखलाओं के मध्य स्थित एक भ्रंश घाटी (Rift Valley) से होकर बहती है।",
        "cue_en": "Narmada = between Vindhyas (N) and Satpuras (S).",
        "cue_hi": "नर्मदा = उत्तर में विंध्य और दक्षिण में सतपुड़ा के बीच।",
        "wrong_en": ["Flanked by Vindhyas and Satpuras.", "Tapti flows south of Satpura.", "Aravalli is further northwest.", "Enclose the Deccan plateau."],
        "wrong_hi": ["उत्तर में विंध्य और दक्षिण में सतपुड़ा।", "ताप्ती सतपुड़ा के दक्षिण में बहती है।", "अरावली उत्तर-पश्चिम में है।", "दक्कन के पठार को घेरते हैं।"]
    },
    {
        "name_en": "Indian Climate, Monsoons & Western Disturbances",
        "name_hi": "भारतीय जलवायु, मानसून एवं पश्चिमी विक्षोभ",
        "concepts_en": ["Southwest Monsoon (June to Sept)", "Retreating/Northeast Monsoon brings rain to Tamil Nadu", "Western Disturbances bring winter rain to northwest", "ITCZ shift"],
        "concepts_hi": ["दक्षिण-पश्चिम मानसून (जून से सितंबर)", "उत्तर-पूर्वी (लौटता) मानसून तमिलनाडु में वर्षा करता है", "पश्चिमी विक्षोभ उत्तर-पश्चिम में शीतकालीन वर्षा लाते हैं", "आईटीसीजेड का स्थानांतरण"],
        "q_en": "Which atmospheric phenomenon brings winter rainfall to northwestern India, benefiting Rabi crops like wheat?",
        "q_hi": "भारत के उत्तर-पश्चिमी भागों में शीतकाल में वर्षा किस मौसमी परिघटना (Atmospheric Phenomenon) के कारण होती है?",
        "options_en": ["Western Disturbances (पश्चिमी विक्षोभ)", "Southwest Monsoon", "Tropical Cyclones", "Retreating Monsoon"],
        "options_hi": ["पश्चिमी विक्षोभ (Western Disturbances)", "दक्षिण-पश्चिम मानसून", "उष्णकटिबंधीय चक्रवात", "लौटता हुआ मानसून"],
        "correct_idx": 0,
        "exp_en": "Western Disturbances originating in the Mediterranean Sea travel with the subtropical westerly jet stream, bringing crucial winter rains to northwestern India.",
        "exp_hi": "भूमध्य सागर से उत्पन्न होने वाले पश्चिमी विक्षोभ पछुआ जेट धाराओं के साथ भारत के उत्तर-पश्चिम में पहुंचते हैं और रबी फसलों (गेहूं आदि) के लिए लाभकारी शीतकालीन वर्षा करते हैं।",
        "cue_en": "Western Disturbances = winter rain in NW India.",
        "cue_hi": "पश्चिमी विक्षोभ = उत्तर-पश्चिम भारत में शीतकालीन वर्षा।",
        "wrong_en": ["Brings NW winter rain.", "Operates during summer.", "Hits eastern coast in autumn.", "Brings rain to Tamil Nadu coast."],
        "wrong_hi": ["उत्तर-पश्चिम में शीतकालीन वर्षा का कारण।", "ग्रीष्मकालीन मुख्य मानसून।", "शरद ऋतु में पूर्वी तट पर आते हैं।", "तमिलनाडु तट पर वर्षा कराता है।"]
    }
]

print("Loaded S01 successfully")
