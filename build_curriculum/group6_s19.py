# build_curriculum/group6_s19.py
# S19: Sports, Games & International Championships (15 topics across 4 chapters)

DATA = {}

# S19-C03e5a72a Olympic Games, Commonwealth Games & Asian Games (2 topics)
DATA["S19-C03e5a72a"] = [
    {
        "name_en": "Olympic Games: Ancient Olympia, Modern Revival (Pierre de Coubertin) & India's Olympic Odyssey",
        "name_hi": "ओलंपिक खेल: प्राचीन ओलंपिया, आधुनिक पुनरुद्धार (पियरे डी कुबर्तिन) एवं भारत की ओलंपिक यात्रा",
        "concepts_en": ["Ancient Olympics: Began 776 BCE in Olympia, Greece in honor of Zeus; Modern Olympic revival: Baron Pierre de Coubertin founded International Olympic Committee (IOC) in 1894; First modern games held in Athens (1896)", "Olympic Motto: 'Citius, Altius, Fortius - Communiter' (Faster, Higher, Stronger - Together); Five interlocking rings represent 5 continents (Blue, Yellow, Black, Green, Red)", "India at Olympics: First participation in 1900 Paris (Norman Pritchard, 2 silver in athletics); KD Jadhav won India's first individual Olympic medal (Bronze, Wrestling, Helsinki 1952); Abhinav Bindra won India's first individual Gold (10m Air Rifle, Beijing 2008); Neeraj Chopra won India's first Track & Field Gold (Javelin, Tokyo 2020 with 87.58 m throw); Indian Men's Field Hockey team won 8 Gold medals (1928 to 1980)"],
        "concepts_hi": ["प्राचीन ओलंपिक: 776 ईसा पूर्व ओलंपिया (ग्रीस) में भगवान ज़्यूस के सम्मान में प्रारंभ; आधुनिक ओलंपिक: बैरन पियरे डी कुबर्तिन ने 1894 में अंतर्राष्ट्रीय ओलंपिक समिति (IOC) की स्थापना की; पहले आधुनिक खेल 1896 में एथेंस में आयोजित", "ओलंपिक आदर्श वाक्य: 'सिटियस, अल्टियस, फोर्टियस - कम्युनिटर' (तेज, ऊंचा, बलवान - साथ-साथ); 5 आपस में जुड़े छल्ले पांच महाद्वीपों का प्रतिनिधित्व करते हैं", "ओलंपिक में भारत: 1900 पेरिस में प्रथम भागीदारी (नॉर्मन प्रिचर्ड); के.डी. जाधव ने स्वतंत्र भारत का पहला व्यक्तिगत पदक (कांस्य, कुश्ती, हेलसिंकी 1952) जीता; अभिनव बिंद्रा ने पहला व्यक्तिगत स्वर्ण पदक (10 मीटर एयर राइफल, बीजिंग 2008) जीता; नीरज चोपड़ा ने ट्रैक एंड फील्ड में भारत का पहला स्वर्ण पदक (भाला फेंक, टोक्यो 2020 में 87.58 मी.) जीता; भारतीय पुरुष हॉकी टीम ने कुल 8 स्वर्ण पदक जीते"],
        "q_en": "Who scripted history by winning independent India's very FIRST individual Olympic medal (Bronze in freestyle wrestling) at the 1952 Helsinki Summer Games?",
        "q_hi": "1952 के हेलसिंकी ओलंपिक खेलों में फ्रीस्टाइल कुश्ती में कांस्य पदक जीतकर स्वतंत्र भारत का पहला व्यक्तिगत ओलंपिक पदक जीतने का ऐतिहासिक गौरव किसे प्राप्त है?",
        "options_en": ["K.D. Jadhav (के.डी. जाधव / खशाबा दादासाहेब जाधव)", "Milkha Singh", "Karnam Malleswari", "Abhinav Bindra"],
        "options_hi": ["के.डी. जाधव (K.D. Jadhav - हेलसिंकी 1952)", "मिल्खा सिंह (1960 रोम में चौथे स्थान पर रहे)", "कर्णम मल्लेश्वरी (2000 सिडनी में पहली भारतीय महिला पदक विजेता)", "अभिनव बिंद्रा (2008 में पहला व्यक्तिगत स्वर्ण)"],
        "correct_idx": 0,
        "exp_en": "Khashaba Dadasaheb (K.D.) Jadhav won a Bronze medal in the Bantamweight freestyle wrestling category at the 1952 Helsinki Olympics, becoming the first individual medalist of independent India.",
        "exp_hi": "महाराष्ट्र के पहलवान खशाबा दादासाहेब जाधव (के.डी. जाधव) ने 1952 के हेलसिंकी ओलंपिक में कुश्ती में कांस्य पदक जीता था, जो स्वतंत्र भारत का पहला व्यक्तिगत ओलंपिक पदक था।",
        "cue_en": "First individual Olympic medal for independent India = K.D. Jadhav (1952 Helsinki).",
        "cue_hi": "स्वतंत्र भारत का पहला व्यक्तिगत ओलंपिक पदक = के.डी. जाधव (1952 हेलसिंकी)।",
        "wrong_en": ["First independent Indian individual medalist (1952).", "Finished 4th in 400m at 1960 Rome.", "First Indian woman medalist (Sydney 2000).", "First individual Gold medalist (Beijing 2008)."],
        "wrong_hi": ["स्वतंत्र भारत के पहले व्यक्तिगत पदक विजेता।", "1960 रोम में 400 मी. में चौथे स्थान पर।", "पहली भारतीय महिला पदक विजेता (2000 सिडनी)।", "पहले व्यक्तिगत स्वर्ण पदक विजेता (2008)।"]
    },
    {
        "name_en": "Asian Games & Commonwealth Games: Origins, Emblem & India's Historic 100+ Medals Milestone",
        "name_hi": "एशियाई खेल एवं राष्ट्रमंडल खेल: उद्भव, प्रतीक चिह्न एवं भारत का 100+ पदकों का ऐतिहासिक मील का पत्थर",
        "concepts_en": ["Asian Games (Asiad): First Asian Games hosted in New Delhi in 1951, inaugurated by President Dr. Rajendra Prasad; conceptualized by Guru Dutt Sondhi; motto 'Ever Onward' given by Pt. Jawaharlal Nehru; emblem is a bright red Rising Sun with interlocking rings", "19th Asian Games Hangzhou (China, 2023): India achieved historic milestone of crossing 100 medals for the first time, finishing with 107 medals (28 Gold, 38 Silver, 41 Bronze)", "Commonwealth Games (CWG): Began in 1930 in Hamilton (Canada) as British Empire Games; India hosted the 19th CWG in New Delhi in 2010 (finishing second with 101 medals)"],
        "concepts_hi": ["एशियाई खेल (एशियाड): प्रथम एशियाई खेल 1951 में नई दिल्ली में आयोजित हुए; उद्घाटन राष्ट्रपति डॉ. राजेंद्र प्रसाद ने किया; संकल्पना गुरुदत्त सोंधी ने की; 'एवर ऑनवर्ड' (सदा आगे) का आदर्श वाक्य पं. जवाहरलाल नेहरू ने दिया; प्रतीक चिह्न चमकता हुआ लाल सूर्य (Rising Sun) है", "19वें एशियाई खेल हांगझू (चीन, 2023): भारत ने पहली बार 100 पदकों का ऐतिहासिक आंकड़ा पार करते हुए कुल 107 पदक (28 स्वर्ण, 38 रजत, 41 कांस्य) जीते", "राष्ट्रमंडल खेल (CWG): 1930 में हैमिल्टन (कनाडा) में 'ब्रिटिश एंपायर गेम्स' के रूप में प्रारंभ; भारत ने 2010 में नई दिल्ली में 19वें राष्ट्रमंडल खेलों की मेजबानी की थी (101 पदक जीतकर दूसरा स्थान)"],
        "q_en": "In which city were the very first Asian Games inaugurated in March 1951, under the motto 'Ever Onward' coined by Pandit Jawaharlal Nehru?",
        "q_hi": "मार्च 1951 में पंडित जवाहरलाल नेहरू द्वारा दिए गए आदर्श वाक्य 'एवर ऑनवर्ड' (Ever Onward) के साथ प्रथम एशियाई खेलों का उद्घाटन किस शहर में हुआ था?",
        "options_en": ["New Delhi, India (नई दिल्ली, भारत)", "Manila, Philippines", "Tokyo, Japan", "Bangkok, Thailand"],
        "options_hi": ["नई दिल्ली, भारत (New Delhi, India)", "मनीला, फिलीपींस", "टोक्यो, जापान", "बैंकॉक, थाईलैंड"],
        "correct_idx": 0,
        "exp_en": "The inaugural Asian Games were hosted by New Delhi, India from March 4 to 11, 1951 at the Dhyan Chand National Stadium, featuring 489 athletes from 11 Asian nations.",
        "exp_hi": "पहले एशियाई खेलों का आयोजन 1951 में नई दिल्ली के नेशनल स्टेडियम में हुआ था, जिसमें 11 एशियाई देशों के खिलाड़ियों ने भाग लिया था। (1982 में भारत ने दोबारा एशियाई खेलों की मेजबानी की)।",
        "cue_en": "First Asian Games (1951) = New Delhi, India.",
        "cue_hi": "प्रथम एशियाई खेल (1951) = नई दिल्ली, भारत।",
        "wrong_en": ["Host of first Asian Games (1951).", "Host of second Asian Games (1954).", "Host of third Asian Games (1958).", "Host of Asian Games four times."],
        "wrong_hi": ["प्रथम एशियाई खेलों का मेजबान।", "1954 के खेलों का मेजबान।", "1958 के खेलों का मेजबान।", "चार बार का मेजबान शहर।"]
    }
]

# S19-C8da61983 Chess Regulations (FIDE), World Champions & Chess Olympiads (4 topics)
DATA["S19-C8da61983"] = [
    {
        "name_en": "Chess Board Anatomy, Piece Values & Special Rules (Castling, En Passant, Promotion)",
        "name_hi": "शतरंज बोर्ड संरचना, मोहरों के मान एवं विशेष नियम (कैसलिंग, एन पासेंट एवं प्यादे की पदोन्नति)",
        "concepts_en": ["Board geometry: 64 alternating light and dark squares (8 ranks numbered 1 to 8, 8 files lettered a to h); right-hand corner square is always light ('White on right')", "Standard piece values (relative point system): Pawn = 1 point, Knight = 3 points, Bishop = 3 points, Rook = 5 points, Queen = 9 points, King = infinite / invaluable", "Special moves: 1. Castling (simultaneous move of King two squares towards Rook and Rook jumping over King; invalidated if King or Rook has previously moved, or if King is in check or moves through check)", "2. En Passant (in-passing pawn capture: pawn advancing two squares past enemy pawn can be captured diagonally on the very next move)", "3. Pawn Promotion: Pawn reaching 8th rank must immediately promote to Queen, Rook, Bishop, or Knight"],
        "concepts_hi": ["बोर्ड संरचना: 64 खाने (32 सफेद और 32 काले); 8 रैंक (1 से 8) एवं 8 फाइल (a से h); खिलाड़ी के दाईं ओर का कोना हमेशा सफेद होता है ('सफेद दायां')", "मोहरों के मानक अंक मान: प्यादा (Pawn) = 1 अंक, घोड़ा (Knight) = 3 अंक, ऊंट (Bishop) = 3 अंक, हाथी (Rook) = 5 अंक, वजीर (Queen) = 9 अंक, राजा (King) = अमूल्य", "शतरंज के 3 विशेष नियम:", "1. कैसलिंग (Castling / किलाबंदी): राजा और हाथी की संयुक्त चाल; यदि राजा या हाथी पहले चल चुका हो, या राजा शह (Check) में हो तो कैसलिंग नहीं हो सकती", "2. एन पासेंट (En Passant): दो घर आगे बढ़े विरोधी प्यादे को तुरंत अगली चाल में तिरछा काटकर मारना", "3. प्यादे की पदोन्नति (Pawn Promotion): अंतिम 8वें खाने में पहुंचते ही प्यादे का वजीर, हाथी, ऊंट या घोड़ा बन जाना"],
        "q_en": "Under international FIDE chess rules, which special pawn capture move allows a pawn to capture an opponent's pawn that has advanced two squares from its initial square as if it had moved only one square?",
        "q_hi": "अंतर्राष्ट्रीय फिडे (FIDE) शतरंज नियमों के अनुसार वह कौन सा विशेष नियम है, जिसके तहत यदि कोई विरोधी प्यादा अपनी शुरुआती स्थिति से दो घर आगे बढ़ता है, तो उसे तुरंत उसी चाल में तिरछा काटकर मारा जा सकता है?",
        "options_en": ["En Passant (एन पासेंट)", "Castling", "Pawn Promotion", "Stalemate"],
        "options_hi": ["एन पासेंट (En Passant)", "कैसलिंग (Castling)", "प्यादे की पदोन्नति (Promotion)", "स्टेलमेट (Stalemate - गतिरोध)"],
        "correct_idx": 0,
        "exp_en": "'En Passant' (French for 'in passing') is a special pawn capture rule introduced in the 15th century to prevent pawns from using the two-square first advance to bypass an opposing pawn's attack square.",
        "exp_hi": "'एन पासेंट' (En Passant) फ्रेंच भाषा का शब्द है जिसका अर्थ 'गुजरते हुए' है। यह प्यादे की एक विशेष चाल है जो केवल उसी चाल में तुरंत चली जा सकती है जब विरोधी प्यादा दो घर चला हो।",
        "cue_en": "Pawn capture in passing = En Passant.",
        "cue_hi": "प्यादे द्वारा विशेष तिरछी मार = एन पासेंट।",
        "wrong_en": ["Special pawn capture in passing.", "Simultaneous King-Rook defensive move.", "Transforming pawn into Queen/Rook.", "Drawn position with no legal moves."],
        "wrong_hi": ["गुजरते हुए प्यादे को मारने का नियम।", "राजा व हाथी की संयुक्त चाल।", "प्यादे का वजीर बनना।", "ड्रा स्थिति।"]
    },
    {
        "name_en": "FIDE Hierarchy, Grandmaster Title Criteria & Elo Rating System",
        "name_hi": "फिडे (FIDE) पदानुक्रम, ग्रैंडमास्टर (GM) खिताब के मानदंड एवं एलो रेटिंग प्रणाली",
        "concepts_en": ["FIDE (Fédération Internationale des Échecs): Founded in Paris in 1924; headquarters in Lausanne, Switzerland", "Titles awarded for life: Grandmaster (GM - highest title), International Master (IM), FIDE Master (FM), Candidate Master (CM)", "Grandmaster Title Criteria: Player must achieve an official published Elo rating of at least 2500, and earn three Grandmaster Norms in international tournaments with a 2600+ performance rating over at least 27 games", "Elo Rating System: Devised by Hungarian-American physics professor Arpad Elo; statistical method calculating relative skill levels in zero-sum games", "Viswanathan Anand became India's first Grandmaster in 1988 (won Padma Vibhushan, Rajiv Gandhi Khel Ratna inaugural recipient)"],
        "concepts_hi": ["फिडे (FIDE): अंतर्राष्ट्रीय शतरंज महासंघ; स्थापना 1924 पेरिस; मुख्यालय लुसाने (स्विट्जरलैंड)", "आजीवन खिताब: ग्रैंडमास्टर (GM - सर्वोच्च खिताब), इंटरनेशनल मास्टर (IM), फिडे मास्टर (FM)", "ग्रैंडमास्टर (GM) बनने के मानदंड: खिलाड़ी की आधिकारिक FIDE Elo रेटिंग कम से कम 2500 होनी चाहिए और कम से कम 27 अंतरराष्ट्रीय मुकाबलों में 3 ग्रैंडमास्टर नॉर्म (Norms) हासिल होने चाहिए", "एलो रेटिंग प्रणाली (Elo Rating): हंगेरियन-अमेरिकी भौतिक विज्ञानी अरपाद एलो द्वारा विकसित सांख्यिकीय रेटिंग प्रणाली", "विश्वनाथन आनंद 1988 में भारत के पहले ग्रैंडमास्टर बने (प्रथम खेल रत्न पुरस्कार विजेता)"],
        "q_en": "To attain the prestigious, lifelong title of Chess Grandmaster (GM) awarded by FIDE, what minimum official Elo rating threshold must a player cross in addition to securing three GM norms?",
        "q_hi": "फिडे (FIDE) द्वारा प्रदान किया जाने वाला सर्वोच्च आजीवन 'ग्रैंडमास्टर' (GM) खिताब हासिल करने हेतु 3 GM नॉर्म्स के अलावा खिलाड़ी की न्यूनतम आधिकारिक Elo रेटिंग कितनी होनी अनिवार्य है?",
        "options_en": ["2500 Elo rating (2500 एलो रेटिंग)", "2400 Elo rating", "2600 Elo rating", "2700 Elo rating"],
        "options_hi": ["2500 एलो रेटिंग (2500 Elo points)", "2400 एलो रेटिंग (यह इंटरनेशनल मास्टर / IM हेतु है)", "2600 एलो रेटिंग", "2700 एलो रेटिंग (यह सुपर ग्रैंडमास्टर की अनौपचारिक सीमा है)"],
        "correct_idx": 0,
        "exp_en": "To qualify for the Grandmaster title, a chess player must attain a published or live FIDE rating of at least 2500 and achieve 3 Grandmaster norms (tournament performance ratings above 2600).",
        "exp_hi": "शतरंज में ग्रैंडमास्टर (GM) बनने के लिए न्यूनतम 2500 FIDE रेटिंग छूना और 3 GM नॉर्म्स प्राप्त करना अनिवार्य होता है। (2400 रेटिंग इंटरनेशनल मास्टर हेतु होती है)।",
        "cue_en": "Grandmaster (GM) minimum rating = 2500; IM = 2400.",
        "cue_hi": "ग्रैंडमास्टर न्यूनतम रेटिंग = 2500; आईएम = 2400।",
        "wrong_en": ["Minimum rating threshold for GM title.", "Minimum rating threshold for International Master (IM).", "Super GM performance benchmark.", "Elite Super-GM benchmark."],
        "wrong_hi": ["ग्रैंडमास्टर की न्यूनतम रेटिंग।", "इंटरनेशनल मास्टर की न्यूनतम रेटिंग।", "सुपर GM बेंचमार्क।", "अभिजात वर्ग बेंचमार्क।"]
    },
    {
        "name_en": "World Chess Championship Lineage: From Steinitz, Fischer, Kasparov, Anand to Carlsen & Ding Liren",
        "name_hi": "विश्व शतरंज चैंपियनशिप परंपरा: विल्हेम स्टीनिट्ज़, बॉबी फिशर, कास्पारोव, विश्वनाथन आनंद से कार्लसन तक",
        "concepts_en": ["Wilhelm Steinitz became first official World Chess Champion in 1886 defeating Johannes Zukertort", "Iconic Champions: Emanuel Lasker (held title for longest: 27 years, 1894-1921), Jose Raul Capablanca, Alexander Alekhine, Mikhail Botvinnik, Bobby Fischer (Match of the Century 1972 defeating Boris Spassky in Reykjavik), Garry Kasparov (youngest undisputed champion at age 22 in 1985; played Deep Blue)", "Viswanathan Anand: 5-time World Champion (2000 FIDE knockout; 2007 tournament; 2008 vs Kramnik; 2010 vs Topalov; 2012 vs Gelfand)", "Magnus Carlsen (Norway): World Champion 2013-2023 (defeated Anand in 2013; highest Elo rating in history: 2882)", "Ding Liren (China, 2023 Champion defeating Ian Nepomniachtchi); D. Gukesh (India) won Candidates 2024 at age 17, becoming youngest challenger"],
        "concepts_hi": ["विल्हेम स्टीनिट्ज़: 1886 में पहले आधिकारिक विश्व शतरंज चैंपियन बने", "ऐतिहासिक चैंपियन: इमैनुएल लास्कर (सर्वाधिक 27 वर्ष तक चैंपियन, 1894-1921), कैपब्लांका, मिखाइल बोटविनिक, बॉबी फिशर (1972 में रेक्याविक में बोरिस स्पास्की को हराकर 'मैच ऑफ द सेंचुरी' जीता), गैरी कास्पारोव (1985 में 22 वर्ष की उम्र में सबसे युवा निर्विवाद विश्व चैंपियन बने)", "विश्वनाथन आनंद: 5 बार के विश्व चैंपियन (2000, 2007, 2008, 2010, 2012)", "मैग्नस कार्लसन (नॉर्वे): 2013 से 2023 तक विश्व चैंपियन (इतिहास की सर्वोच्च Elo रेटिंग 2882 हासिल की)", "डिंग लिरेन (चीन, 2023 चैंपियन); भारत के डी. गुकेश ने 2024 में 17 वर्ष की उम्र में कैंडिडेट्स टूर्नामेंट जीतकर इतिहास के सबसे युवा चैलेंजर बनने का कीर्तिमान बनाया"],
        "q_en": "At what age did India's chess prodigy Dommaraju Gukesh (D. Gukesh) script history in April 2024 by winning the FIDE Candidates Tournament in Toronto, becoming the youngest-ever challenger for the World Chess Championship?",
        "q_hi": "अप्रैल 2024 में टोरंटो में फिडे (FIDE) कैंडिडेट्स टूर्नामेंट जीतकर विश्व शतरंज चैंपियनशिप के सबसे युवा चैलेंजर बनने का ऐतिहासिक कीर्तिमान भारत के डी. गुकेश (D. Gukesh) ने किस उम्र में स्थापित किया?",
        "options_en": ["17 years old (17 वर्ष की उम्र में)", "19 years old", "21 years old", "15 years old"],
        "options_hi": ["17 वर्ष की उम्र में (17 years old)", "19 वर्ष की उम्र में", "21 वर्ष की उम्र में", "15 वर्ष की उम्र में"],
        "correct_idx": 0,
        "exp_en": "At 17 years and 11 months, Grandmaster D. Gukesh broke Garry Kasparov's 40-year-old record (Kasparov qualified at age 20 in 1984) to become the youngest winner of the Candidates Tournament and world title challenger.",
        "exp_hi": "भारत के 17 वर्षीय ग्रैंडमास्टर डी. गुकेश ने अप्रैल 2024 में कैंडिडेट्स टूर्नामेंट जीतकर गैरी कास्पारोव का 40 साल पुराना रिकॉर्ड तोड़ा और विश्व चैंपियनशिप का मुकाबला करने वाले इतिहास के सबसे युवा खिलाड़ी बने।",
        "cue_en": "Youngest Candidates winner = D. Gukesh (17 years old, 2024).",
        "cue_hi": "सबसे युवा कैंडिडेट्स विजेता = डी. गुकेश (17 वर्ष, 2024)।",
        "wrong_en": ["Record-setting age (17 years).", "Age of earlier young contenders.", "Kasparov's age when he challenged.", "Age at becoming GM."],
        "wrong_hi": ["ऐतिहासिक सबसे युवा आयु (17 वर्ष)।", "गलत आयु।", "कास्पारोव की चुनौती आयु (20-21)।", "ग्रैंडमास्टर बनने की आयु।"]
    },
    {
        "name_en": "Chess Olympiads: History, Hamilton-Russell Cup & India's Historic Double Gold in Budapest 2024",
        "name_hi": "शतरंज ओलंपियाड: इतिहास, हैमिल्टन-रसेल कप एवं बुडापेस्ट 2024 में भारत का ऐतिहासिक दोहरा स्वर्ण",
        "concepts_en": ["Chess Olympiad: Premier biennial team chess championship organized by FIDE since 1927 (Hamilton-Russell Cup for Open category; Vera Menchik Cup for Women's category)", "44th Chess Olympiad held in Chennai (Mamallapuram), India in 2022 (India won bronze in Open and bronze in Women's; mascot Thambi)", "45th Chess Olympiad in Budapest (Hungary, September 2024): Historic landmark where INDIA WON DOUBLE GOLD (winning both Open section and Women's section simultaneously for the first time in history)", "Open Gold team: D. Gukesh (Individual Board 1 Gold), R. Praggnanandhaa, Arjun Erigaisi (Individual Board 3 Gold), Vidit Gujrathi, Pentala Harikrishna", "Women's Gold team: Harika Dronavalli, Vaishali Rameshbabu, Divya Deshmukh (Individual Gold), Vantika Agrawal (Individual Gold), Tania Sachdev"],
        "concepts_hi": ["शतरंज ओलंपियाड: फिडे द्वारा 1927 से आयोजित द्विवार्षिक टीम प्रतियोगिता (ओपन श्रेणी में हैमिल्टन-रसेल कप; महिला श्रेणी में वेरा मेंचिक कप)", "44वां शतरंज ओलंपियाड 2022 में चेन्नई (मामल्लापुरम, भारत) में आयोजित हुआ (शुभंकर 'थम्बी')", "45वां शतरंज ओलंपियाड बुडापेस्ट (हंगरी, सितंबर 2024): भारत ने रचा स्वर्णिम इतिहास - भारत ने पहली बार एक साथ ओपन और महिला दोनों श्रेणियों में स्वर्ण पदक जीतकर 'डबल गोल्ड' अपने नाम किया", "ओपन विजेता टीम: डी. गुकेश, आर. प्रज्ञानानंद, अर्जुन एरिगैसी, विदित गुजराती एवं पेंटाला हरिकृष्णा", "महिला विजेता टीम: हरिका द्रोणावल्ली, आर. वैशाली, दिव्या देशमुख, वंतिका अग्रवाल एवं तानिया सचदेव"],
        "q_en": "In September 2024, at the 45th FIDE Chess Olympiad held in Budapest, Hungary, which country accomplished the unprecedented historic feat of winning GOLD in BOTH the Open and Women's team sections?",
        "q_hi": "सितंबर 2024 में बुडापेस्ट (हंगरी) में आयोजित 45वें फिडे शतरंज ओलंपियाड में किस देश ने ओपन और महिला दोनों वर्गों में ऐतिहासिक दोहरा स्वर्ण पदक (Double Gold) जीतकर नया विश्व कीर्तिमान बनाया?",
        "options_en": ["India (भारत - ऐतिहासिक दोहरा स्वर्ण पदक)", "United States", "China", "Uzbekistan"],
        "options_hi": ["भारत (India - बुडापेस्ट 2024 में ओपन व महिला दोनों में स्वर्ण)", "संयुक्त राज्य अमेरिका (USA)", "चीन (China)", "उज्बेकिस्तान (Uzbekistan)"],
        "correct_idx": 0,
        "exp_en": "At the 45th Chess Olympiad in Budapest (September 2024), India scripted sporting history by sweeping both the Open section (led by Gukesh and Arjun Erigaisi) and the Women's section (led by Divya Deshmukh and Vantika Agrawal) with Gold medals.",
        "exp_hi": "बुडापेस्ट में आयोजित 45वें शतरंज ओलंपियाड (2024) में भारतीय पुरुष (ओपन) और महिला दोनों टीमों ने स्वर्ण पदक जीतकर इतिहास रच दिया; भारत यह ऐतिहासिक उपलब्धि हासिल करने वाला विश्व का तीसरा देश बना।",
        "cue_en": "2024 Budapest Chess Olympiad Double Gold = INDIA.",
        "cue_hi": "2024 शतरंज ओलंपियाड बुडापेस्ट डबल गोल्ड = भारत।",
        "wrong_en": ["Historic double gold champions (India).", "Silver medalists in Open section.", "Silver medalists in Women's section.", "Defending champions from 2022."],
        "wrong_hi": ["दोहरा स्वर्ण पदक विजेता (भारत)।", "रजत पदक विजेता।", "महिला वर्ग में उपविजेता।", "2022 का चैंपियन।"]
    }
]

# S19-C73a11e71 Cricket, Football World Cups, Tennis Grand Slams & Athletics (6 topics)
DATA["S19-C73a11e71"] = [
    {
        "name_en": "Cricket World Cups: ICC ODI (1975-2023) & T20 World Cups (2007 & 2024 India Triumphs)",
        "name_hi": "क्रिकेट विश्व कप: आईसीसी वनडे (1983 व 2011 भारत) एवं टी20 विश्व कप (2007 व 2024 भारत विजय)",
        "concepts_en": ["ICC Men's Cricket World Cup (ODI, 50 overs): Began in 1975 in England (West Indies won first two under Clive Lloyd); Australia holds record 6 titles (1987, 1999, 2003, 2007, 2015, 2023)", "India's ODI victories: 1983 at Lord's under Kapil Dev defeating West Indies; 2011 at Wankhede under MS Dhoni defeating Sri Lanka", "2023 ICC World Cup: Hosted entirely in India; Australia defeated India in Ahmedabad final; Virat Kohli named Player of the Tournament (765 runs)", "ICC Men's T20 World Cup: Inaugural 2007 in South Africa won by India under MS Dhoni (defeating Pakistan at Johannesburg); 2024 T20 World Cup in USA/West Indies won by India under Rohit Sharma defeating South Africa in Barbados final"],
        "concepts_hi": ["आईसीसी पुरुष एकदिवसीय क्रिकेट विश्व कप: 1975 में इंग्लैंड में प्रारंभ (क्लाइव लॉयड के नेतृत्व में वेस्टइंडीज ने पहले दो जीते); ऑस्ट्रेलिया ने सर्वाधिक 6 बार खिताब जीता है", "भारत की एकदिवसीय विश्व कप विजय: 1983 लॉर्ड्स में कपिल देव के नेतृत्व में वेस्टइंडीज को हराया; 2011 वानखेड़े में महेंद्र सिंह धोनी के नेतृत्व में श्रीलंका को हराया", "2023 विश्व कप: भारत में आयोजित; अहमदाबाद फाइनल में ऑस्ट्रेलिया ने भारत को हराया; विराट कोहली प्लेयर ऑफ द टूर्नामेंट (765 रन)", "आईसीसी पुरुष टी20 विश्व कप: पहला 2007 (दक्षिण अफ्रीका) भारत ने एमएस धोनी के नेतृत्व में पाकिस्तान को हराकर जीता; 2024 (वेस्टइंडीज/अमेरिका) भारत ने रोहित शर्मा के नेतृत्व में दक्षिण अफ्रीका को हराकर जीता"],
        "q_en": "Under whose captaincy did the Indian cricket team defeat South Africa in the thrilling final at Bridgetown, Barbados to lift the ICC Men's T20 World Cup in June 2024?",
        "q_hi": "जून 2024 में बारबाडोस के ब्रिजटाउन में दक्षिण अफ्रीका को रोमांचक फाइनल में हराकर आईसीसी पुरुष टी20 विश्व कप का खिताब किस भारतीय कप्तान के नेतृत्व में जीता गया?",
        "options_en": ["Rohit Sharma (रोहित शर्मा)", "Virat Kohli", "Hardik Pandya", "MS Dhoni"],
        "options_hi": ["रोहित शर्मा (Rohit Sharma - कप्तान 2024)", "विराट कोहली (फाइनल के प्लेयर ऑफ द मैच)", "हार्दिक पांड्या (अंतिम ओवर गेंदबाज)", "महेंद्र सिंह धोनी (2007 के विजेता कप्तान)"],
        "correct_idx": 0,
        "exp_en": "Rohit Sharma captained India to an undefeated championship run at the 2024 ICC Men's T20 World Cup, securing a 7-run victory over South Africa in the Kensington Oval final.",
        "exp_hi": "रोहित शर्मा के नेतृत्व में भारत ने जून 2024 में पूरे टूर्नामेंट में अजेय रहते हुए दक्षिण अफ्रीका को 7 रन से हराकर दूसरी बार आईसीसी टी20 विश्व कप जीता।",
        "cue_en": "2024 T20 World Cup winning captain = Rohit Sharma.",
        "cue_hi": "2024 टी20 विश्व कप विजेता कप्तान = रोहित शर्मा।",
        "wrong_en": ["Winning captain of 2024 T20 World Cup.", "Player of the Match in the 2024 final (76 runs).", "Bowled dramatic final over.", "Winning captain of 2007 T20 World Cup."],
        "wrong_hi": ["2024 विजेता कप्तान।", "फाइनल के मैन ऑफ द मैच।", "अंतिम ओवर के गेंदबाज।", "2007 के विजेता कप्तान।"]
    },
    {
        "name_en": "FIFA World Cup: History, Jules Rimet / FIFA Trophy, Brazil's 5 Titles & Qatar 2022",
        "name_hi": "फीफा विश्व कप: इतिहास, जूल्स रिमेट ट्रॉफी, ब्राजील के 5 खिताब एवं कतर 2022 (अर्जेंटीना विजय)",
        "concepts_en": ["FIFA (Fédération Internationale de Football Association): Founded 1904 in Paris; headquarters Zurich, Switzerland", "First FIFA World Cup in 1930 hosted and won by Uruguay (defeating Argentina in Montevideo)", "Trophies: Original Jules Rimet Trophy awarded permanently to Brazil in 1970 after winning 3 titles (Pele in 1958, 1962, 1970); current FIFA World Cup Trophy introduced in 1974 (sculpted by Silvio Gazzaniga in 18k gold)", "Most titles: Brazil (5: 1958, 1962, 1970, 1994, 2002); Germany (4); Italy (4); Argentina (3: 1978, 1986 under Maradona, 2022 under Messi)", "FIFA World Cup Qatar 2022: Argentina defeated France on penalties (3-3 aet, 4-2 pens); Lionel Messi won Golden Ball; Kylian Mbappe won Golden Boot (hat-trick in final)"],
        "concepts_hi": ["फीफा (FIFA): स्थापना 1904 पेरिस; मुख्यालय ज्यूरिख (स्विट्जरलैंड)", "पहला फीफा विश्व कप 1930 में उरुग्वे में आयोजित हुआ और उरुग्वे ने ही जीता", "ट्रॉफी: मूल जूल्स रिमेट ट्रॉफी 1970 में तीन बार जीतने पर ब्राजील को स्थायी रूप से दे दी गई (पेले 1958, 1962, 1970); वर्तमान फीफा ट्रॉफी 18 कैरेट सोने से बनी है", "सर्वाधिक खिताब: ब्राजील (5 बार), जर्मनी (4 बार), इटली (4 बार), अर्जेंटीना (3 बार: 1978, 1986 में माराडोना, 2022 में लियोनेल मेसी)", "कतर 2022 विश्व कप: लुसैल स्टेडियम में अर्जेंटीना ने फ्रांस को पेनल्टी शूटआउट में 4-2 से हराया; मेसी को गोल्डन बॉल, एमबापे को गोल्डन बूट मिला"],
        "q_en": "Which country has won the prestigious FIFA Men's Football World Cup trophy a record FIVE times in tournament history?",
        "q_hi": "फीफा पुरुष फुटबॉल विश्व कप के इतिहास में सर्वाधिक पांच (5) बार विश्व चैंपियन बनने का विश्व रिकॉर्ड किस देश के नाम दर्ज है?",
        "options_en": ["Brazil (ब्राजील - 1958, 1962, 1970, 1994, 2002)", "Germany", "Italy", "Argentina"],
        "options_hi": ["ब्राजील (Brazil - 5 बार चैंपियन)", "जर्मनी (4 बार चैंपियन)", "इटली (4 बार चैंपियन)", "अर्जेंटीना (3 बार चैंपियन)"],
        "correct_idx": 0,
        "exp_en": "Brazil ('A Seleção') has won five FIFA World Cups (1958, 1962, 1970, 1994, 2002) and is the only nation to have participated in every single World Cup edition.",
        "exp_hi": "ब्राजील ने 1958, 1962, 1970, 1994 और 2002 में कुल 5 बार फीफा विश्व कप जीता है और वह हर विश्व कप में भाग लेने वाला एकमात्र देश है।",
        "cue_en": "Most FIFA World Cups = Brazil (5 titles).",
        "cue_hi": "सर्वाधिक फीफा विश्व कप = ब्राजील (5 खिताब)।",
        "wrong_en": ["Record 5-time champion.", "4-time champion (1954, 1974, 1990, 2014).", "4-time champion (1934, 1938, 1982, 2006).", "3-time champion (1978, 1986, 2022)."],
        "wrong_hi": ["5 बार का रिकॉर्ड विजेता।", "4 बार का विजेता (जर्मनी)।", "4 बार का विजेता (इटली)।", "3 बार का विजेता (अर्जेंटीना)।"]
    },
    {
        "name_en": "Tennis Grand Slams: The Four Majors (Australian Open, Roland Garros, Wimbledon, US Open) & Court Surfaces",
        "name_hi": "टेनिस ग्रैंड स्लैम: चार प्रमुख मेजर्स (ऑस्ट्रेलियन ओपन, फ्रेंच ओपन, विंबलडन, यूएस ओपन) एवं कोर्ट की सतहें",
        "concepts_en": ["Chronological order of the 4 annual Grand Slam tournaments:", "1. Australian Open (Melbourne, mid-January, Hard Court - Plexicushion/GreenSet)", "2. French Open / Roland Garros (Paris, late May/June, Red Clay Court - slower, high bounce; Rafael Nadal won record 14 titles: 'King of Clay')", "3. Wimbledon Championships (London, June/July, Natural Grass Court - fastest surface, low skid bounce, traditional all-white dress code; oldest tournament founded 1877)", "4. US Open (Flushing Meadows, New York, late August/September, Hard Court - Laykold)", "Grand Slam / Calendar Slam: Winning all 4 majors in single calendar year (achieved by Don Budge 1938, Rod Laver 1962 & 1969; Steffi Graf 1988 'Golden Slam' including Olympic Gold)", "Men's singles record: Novak Djokovic (24 Grand Slam titles), Rafael Nadal (22), Roger Federer (20)"],
        "concepts_hi": ["चार ग्रैंड स्लैम टूर्नामेंटों का वार्षिक कालानुक्रम:", "1. ऑस्ट्रेलियन ओपन (मेलबर्न, जनवरी, हार्ड कोर्ट)", "2. फ्रेंच ओपन / रोलां गैरो (पेरिस, मई-जून, लाल बजरी / क्ले कोर्ट - राफेल नडाल ने सर्वाधिक 14 बार जीता, 'क्ले कोर्ट का बादशाह')", "3. विंबलडन (लंदन, जून-जुलाई, प्राकृतिक घास / ग्रास कोर्ट - सबसे पुराना टूर्नामेंट [1877], सफेद पोशाक का नियम)", "4. यूएस ओपन (न्यूयॉर्क, अगस्त-सितंबर, हार्ड कोर्ट)", "कैलेंडर ग्रैंड स्लैम: एक ही वर्ष में चारों ग्रैंड स्लैम जीतना (रॉड लेवर; स्टेफी ग्राफ ने 1988 में ओलंपिक स्वर्ण सहित 'गोल्डन स्लैम' जीता)", "पुरुष एकल में सर्वाधिक ग्रैंड स्लैम: नोवाक जोकोविच (24 खिताब), राफेल नडाल (22), रोजर फेडरर (20)"],
        "q_en": "Which of the four prestigious annual Tennis Grand Slam tournaments is played specifically on natural Grass courts, adhering to a strict all-white attire tradition?",
        "q_hi": "टेनिस के चार प्रमुख वार्षिक ग्रैंड स्लैम टूर्नामेंटों में से वह कौन सा सबसे पुराना टूर्नामेंट है, जो प्राकृतिक घास (Grass Court) पर खेला जाता है और जिसमें केवल सफेद पोशाक पहनने की परंपरा है?",
        "options_en": ["Wimbledon Championships, London (विंबलडन, लंदन - ग्रास कोर्ट)", "Roland Garros (French Open)", "Australian Open", "US Open"],
        "options_hi": ["विंबलडन चैंपियनशिप, लंदन (Wimbledon - ग्रास कोर्ट)", "रोलां गैरो / फ्रेंच ओपन (यह लाल मिट्टी/क्ले पर खेला जाता है)", "ऑस्ट्रेलियन ओपन (हार्ड कोर्ट)", "यूएस ओपन (हार्ड कोर्ट)"],
        "correct_idx": 0,
        "exp_en": "Wimbledon, founded in 1877 at the All England Club in London, is the oldest tennis tournament in the world and the only Grand Slam still contested on traditional outdoor grass courts.",
        "exp_hi": "विंबलडन (स्थापना 1877) विश्व का सबसे प्रतिष्ठित व प्राचीन टेनिस टूर्नामेंट है, जो लंदन में प्राकृतिक घास के कोर्ट पर खेला जाता है और खिलाड़ी केवल सफेद कपड़े पहनते हैं।",
        "cue_en": "Grass court Grand Slam = Wimbledon (London).",
        "cue_hi": "घास के कोर्ट का ग्रैंड स्लैम = विंबलडन (लंदन)।",
        "wrong_en": ["Only grass court Grand Slam.", "Played on red clay courts in Paris.", "Played on blue hard courts in Melbourne.", "Played on hard courts in New York."],
        "wrong_hi": ["घास के कोर्ट पर विंबलडन।", "लाल बजरी (क्ले कोर्ट)।", "हार्ड कोर्ट (मेलबर्न)।", "हार्ड कोर्ट (न्यूयॉर्क)।"]
    },
    {
        "name_en": "Athletics Track and Field: Sprints, Relays, Javelin Throw & Decathlon",
        "name_hi": "एथलेटिक्स ट्रैक एंड फील्ड: स्प्रिंट्स (100 मी.), रिले दौड़, भाला फेंक (जैवलिन) एवं डेकाथलॉन",
        "concepts_en": ["Track events: 100m, 200m, 400m (sprints); 800m, 1500m (middle distance); 5000m, 10000m, Marathon (42.195 km / 26.2 miles, inspired by soldier Pheidippides running from Marathon to Athens in 490 BCE)", "Usain Bolt (Jamaica): World record holder in 100m (9.58s) and 200m (19.19s) set at 2009 Berlin World Championships", "Field throwing events: Javelin throw (men 800g, women 600g; center of gravity modified in 1986 to prevent throws exceeding stadium limits), Shot put, Discus throw, Hammer throw", "Combined events: Decathlon (men - 10 track and field events over 2 days, winner termed 'World's Greatest Athlete') and Heptathlon (women - 7 events)"],
        "concepts_hi": ["ट्रैक स्पर्धाएं: 100 मी., 200 मी., 400 मी. (स्प्रिंट); मैराथन दौड़ की मानक दूरी 42.195 किमी (26 मील 385 गज) होती है (490 ईसा पूर्व मैराथन के मैदान से एथेंस तक सैनिक फिदिपिडेस की दौड़ की याद में)", "उसेन बोल्ट (जमैका): 100 मीटर (9.58 सेकंड) और 200 मीटर (19.19 सेकंड) के विश्व रिकॉर्डधारी", "थ्रोइंग स्पर्धाएं: भाला फेंक / जैवलिन (पुरुष 800 ग्राम, महिला 600 ग्राम), गोला फेंक (शॉट पुट), चक्का फेंक (डिस्कस), तारगोला (हैमर)", "संयुक्त स्पर्धाएं: डेकाथलॉन (Decathlon - पुरुषों की 10 स्पर्धाएं 2 दिनों में, विजेता को 'विश्व का सर्वश्रेष्ठ एथलीट' कहा जाता है) एवं हेप्टाथलॉन (महिलाओं की 7 स्पर्धाएं)"],
        "q_en": "What is the official standardized race distance of an Olympic Marathon event, codified in 1921 after the 1908 London Olympic route from Windsor Castle?",
        "q_hi": "ओलंपिक मैराथन दौड़ की आधिकारिक मानक दूरी कितनी तय की गई है (जो 1908 के लंदन ओलंपिक के बाद से अंतरराष्ट्रीय मानक बनी)?",
        "options_en": ["42.195 kilometers (42.195 किमी / 26 मील 385 गज)", "40.000 kilometers", "45.500 kilometers", "38.250 kilometers"],
        "options_hi": ["42.195 किलोमीटर (42.195 km / 26.2 miles)", "40.000 किलोमीटर", "45.500 किलोमीटर", "38.250 किलोमीटर"],
        "correct_idx": 0,
        "exp_en": "The International Amateur Athletic Federation (IAAF) officially standardized the marathon distance at 42.195 km (26 miles 385 yards) in May 1921, matching the 1908 London Olympics course.",
        "exp_hi": "ओलंपिक मैराथन की मानक दूरी 42.195 किमी (42 किलोमीटर और 195 मीटर) निर्धारित है।",
        "cue_en": "Marathon distance = 42.195 km (26 miles 385 yards).",
        "cue_hi": "मैराथन की दूरी = 42.195 किमी।",
        "wrong_en": ["Official IAAF standardized marathon distance.", "Arbitrary rounded distance.", "Excessive distance.", "Underestimated distance."],
        "wrong_hi": ["मैराथन की सही मानक दूरी।", "पूर्णांकित गलत मान।", "अधिक दूरी।", "कम दूरी।"]
    },
    {
        "name_en": "Badminton & Table Tennis: Thomas & Uber Cups, BWF Tour & India's Historic 2022 Thomas Cup Triumph",
        "name_hi": "बैडमिंटन एवं टेबल टेनिस: थॉमस कप, उबेर कप, बीडब्ल्यूएफ टूर एवं भारत की ऐतिहासिक थॉमस कप विजय (2022)",
        "concepts_en": ["Badminton World Federation (BWF): Headquarters in Kuala Lumpur, Malaysia; scoring system (rally point to 21, best of 3 games)", "Major team championships: Thomas Cup (Men's World Team Championship, founded 1949 by Sir George Thomas) and Uber Cup (Women's World Team Championship, founded 1957 by Betty Uber); Sudirman Cup (World Mixed Team)", "India's Historic Thomas Cup Triumph (Bangkok, May 2022): India defeated 14-time champions Indonesia 3-0 in the final to lift the Thomas Cup for the first time in 73 years of tournament history (Lakshya Sen, Satwiksairaj Rankireddy & Chirag Shetty, Kidambi Srikanth)", "Table Tennis (ITTF): Ping-pong diplomacy; China's global dominance; Sharath Kamal and Manika Batra leading Indian table tennis"],
        "concepts_hi": ["बैडमिंटन वर्ल्ड फेडरेशन (BWF): मुख्यालय कुआलालंपुर (मलेशिया); 21 अंकों का रैली पॉइंट सिस्टम", "प्रमुख टीम चैंपियनशिप: थॉमस कप (पुरुष विश्व टीम बैडमिंटन चैंपियनशिप, 1949 में प्रारंभ) एवं उबेर कप (महिला विश्व टीम बैडमिंटन चैंपियनशिप, 1957 में प्रारंभ); सुदीरमन कप (मिश्रित टीम)", "भारत की ऐतिहासिक थॉमस कप विजय (मई 2022, बैंकॉक): भारत ने 14 बार की चैंपियन इंडोनेशिया को फाइनल में 3-0 से हराकर 73 वर्षों के इतिहास में पहली बार थॉमस कप जीतकर विश्व खेल जगत को चकित कर दिया (लक्ष्य सेन, सात्विकसाईराज-चिराग शेट्टी, किदांबी श्रीकांत)", "टेबल टेनिस (ITTF): पिंग-पॉन्ग कूटनीति; भारत के अचंत शरत कमल एवं मनिका बत्रा"],
        "q_en": "In May 2022, which 14-time defending champion superpower did the Indian men's badminton team stun 3-0 in Bangkok to win the prestigious Thomas Cup for the first time in history?",
        "q_hi": "मई 2022 में बैंकॉक में भारतीय पुरुष बैडमिंटन टीम ने 73 वर्षों में पहली बार प्रतिष्ठित 'थॉमस कप' जीतने हेतु फाइनल में 14 बार की किस विश्व विजेता टीम को 3-0 से पराजित किया था?",
        "options_en": ["Indonesia (इंडोनेशिया - 14 बार की चैंपियन)", "China", "Denmark", "Japan"],
        "options_hi": ["इंडोनेशिया (Indonesia)", "चीन (China)", "डेनमार्क (Denmark)", "जापान (Japan)"],
        "correct_idx": 0,
        "exp_en": "India created sporting history by defeating badminton powerhouse and 14-time champions Indonesia 3-0 in the 2022 Thomas Cup final with wins by Lakshya Sen, Satwik/Chirag, and Kidambi Srikanth.",
        "exp_hi": "भारतीय पुरुष टीम ने बैंकॉक में 14 बार के विजेता इंडोनेशिया को 3-0 से हराकर 2022 में पहली बार थॉमस कप जीतकर बैडमिंटन में नया इतिहास रचा था।",
        "cue_en": "Thomas Cup 2022 final = India defeated Indonesia 3-0.",
        "cue_hi": "2022 थॉमस कप फाइनल = भारत ने इंडोनेशिया को 3-0 से हराया।",
        "wrong_en": ["Defeated by India 3-0 in 2022 final.", "10-time Thomas Cup champion.", "Only European nation to win Thomas Cup (2016).", "2014 champion."],
        "wrong_hi": ["भारत से पराजित 14 बार का विजेता।", "10 बार का विजेता।", "एकमात्र यूरोपीय विजेता।", "2014 का विजेता।"]
    },
    {
        "name_en": "Formula One Racing, Grand Prix Circuits, FIA Regulations & Constructors Champions",
        "name_hi": "फॉर्मूला वन (F1) मोटर रेसिंग: ग्रैंड प्रिक्स सर्किट, एफआईए नियम, ड्राइवर्स एवं कंस्ट्रक्टर्स चैंपियनशिप",
        "concepts_en": ["FIA (Fédération Internationale de l'Automobile): Governs Formula 1 World Championship since 1950 (first race at Silverstone, UK, won by Giuseppe Farina in Alfa Romeo)", "Championship titles awarded annually: World Drivers' Championship (WDC) and World Constructors' Championship (WCC)", "Most Driver Championships (7 titles each): Michael Schumacher (Germany - 1994, 1995, 2000-2004 with Benetton & Ferrari) and Lewis Hamilton (UK - 2008, 2014-2015, 2017-2020 with McLaren & Mercedes); Max Verstappen dominant with Red Bull Racing", "Legendary circuits: Monaco GP (Monte Carlo street circuit, tight corners like Fairmont Hairpin), Monza (Temple of Speed, Italy), Spa-Francorchamps (Belgium, Eau Rouge corner), Silverstone (UK)"],
        "concepts_hi": ["एफआईए (FIA): 1950 से फॉर्मूला 1 विश्व चैंपियनशिप का संचालन; पहली रेस 1950 में सिल्वरस्टोन (ब्रिटेन) में हुई", "वार्षिक खिताब: विश्व ड्राइवर्स चैंपियनशिप (WDC) एवं विश्व कंस्ट्रक्टर्स चैंपियनशिप (कार निर्माता)", "सर्वाधिक विश्व खिताब (7-7 बार): माइकल शूमाकर (जर्मनी - फेरारी व बेनेटन) एवं लुईस हैमिल्टन (ब्रिटेन - मर्सिडीज व मैकलारेन); मैक्स वर्स्टापेन (रेड बुल)", "प्रसिद्ध सर्किट: मोनाको ग्रैंड प्रिक्स (मोंटे कार्लो की संकरी सड़कें, फेयरमोंट हेयरपिन मोड़), मोंज़ा (इटली - गति का मंदिर), स्पा-फ्रैंकोरचैम्प्स (बेल्जियम - ओ रूज मोड़), सिल्वरस्टोन"],
        "q_en": "Which two legendary drivers share the all-time record for the most Formula One World Drivers' Championship titles, with SEVEN world championships each?",
        "q_hi": "फॉर्मूला वन (F1) मोटर रेसिंग के इतिहास में सर्वाधिक सात-सात (7-7) बार विश्व ड्राइवर्स चैंपियनशिप जीतने का संयुक्त सर्वकालिक रिकॉर्ड किन दो महान ड्राइवरों के नाम दर्ज है?",
        "options_en": ["Michael Schumacher and Lewis Hamilton (माइकल शूमाकर एवं लुईस हैमिल्टन)", "Ayrton Senna and Alain Prost", "Sebastian Vettel and Max Verstappen", "Juan Manuel Fangio and Fernando Alonso"],
        "options_hi": ["माइकल शूमाकर एवं लुईस हैमिल्टन (Michael Schumacher & Lewis Hamilton - 7-7 खिताब)", "आयर्टन सेना एवं एलेन प्रोस्ट", "सेबेस्टियन वेटेल एवं मैक्स वर्स्टापेन", "जुआन मैनुअल फैंगियो एवं फर्नांडो अलोंसो"],
        "correct_idx": 0,
        "exp_en": "Michael Schumacher (won in 1994, 1995, 2000-2004) and Sir Lewis Hamilton (won in 2008, 2014, 2015, 2017-2020) each hold seven F1 World Drivers' Championships.",
        "exp_hi": "माइकल शूमाकर (जर्मनी) और लुईस हैमिल्टन (ब्रिटेन) दोनों ने 7-7 बार F1 विश्व खिताब जीतकर इतिहास रचा है। जुआन मैनुअल फैंगियो ने 5 खिताब जीते थे।",
        "cue_en": "7 F1 World Championships = Michael Schumacher & Lewis Hamilton.",
        "cue_hi": "7 बार F1 विश्व चैंपियन = शूमाकर एवं लुईस हैमिल्टन।",
        "wrong_en": ["Co-record holders with 7 titles each.", "Senna won 3, Prost won 4.", "Vettel won 4, Verstappen won 3+.", "Fangio won 5, Alonso won 2."],
        "wrong_hi": ["7-7 खिताब के रिकॉर्डधारी।", "सेना 3, प्रोस्ट 4।", "वेटेल 4 खिताब।", "फैंगियो 5 खिताब।"]
    }
]

# S19-Cb1b9a7ce National Sports Awards (Khel Ratna, Arjuna) & Traditional Sports (3 topics)
DATA["S19-Cb1b9a7ce"] = [
    {
        "name_en": "National Sports Awards of India: Major Dhyan Chand Khel Ratna, Arjuna & Dronacharya Awards",
        "name_hi": "भारत के राष्ट्रीय खेल पुरस्कार: मेजर ध्यानचंद खेल रत्न, अर्जुन पुरस्कार एवं द्रोणाचार्य पुरस्कार",
        "concepts_en": ["Conferred annually by President of India on National Sports Day (August 29, birth anniversary of hockey wizard Major Dhyan Chand)", "Major Dhyan Chand Khel Ratna Award: Highest sporting honour in India (renamed from Rajiv Gandhi Khel Ratna in 2021); carries ₹25 lakh cash prize, medallion, and citation; first awarded in 1991-92 to chess Grandmaster Viswanathan Anand", "Arjuna Award: Instituted in 1961 for consistent outstanding performance over four years at international level; ₹15 lakh cash prize and bronze statuette of Arjuna with bow", "Dronacharya Award: Instituted in 1985 for eminent sports coaches (Regular and Lifetime categories; ₹15 lakh prize)", "Major Dhyan Chand Lifetime Achievement Award in Sports and Games (instituted 2002)"],
        "concepts_hi": ["प्रतिवर्ष 29 अगस्त को 'राष्ट्रीय खेल दिवस' (हॉकी के जादूगर मेजर ध्यानचंद की जयंती) पर राष्ट्रपति द्वारा प्रदान किए जाते हैं", "मेजर ध्यानचंद खेल रत्न पुरस्कार: भारत का सर्वोच्च खेल सम्मान (2021 में राजीव गांधी खेल रत्न से नाम बदला गया); ₹25 लाख नकद पुरस्कार, पदक और प्रशस्ति पत्र; 1991-92 में प्रथम पुरस्कार शतरंज ग्रैंडमास्टर विश्वनाथन आनंद को दिया गया था", "अर्जुन पुरस्कार: 1961 में प्रारंभ; पिछले 4 वर्षों में अंतरराष्ट्रीय स्तर पर उत्कृष्ट प्रदर्शन हेतु; ₹15 लाख नकद एवं धनुष लिए हुए अर्जुन की कांस्य प्रतिमा", "द्रोणाचार्य पुरस्कार: 1985 में प्रारंभ; उत्कृष्ट खेल प्रशिक्षकों (कोचों) को दिया जाने वाला सर्वोच्च सम्मान (नियमित व लाइफटाइम श्रेणी)", "ध्यानचंद लाइफटाइम अचीवमेंट पुरस्कार: खेलों में जीवनपर्यंत योगदान हेतु"],
        "q_en": "Who was the very FIRST recipient of India's highest sporting honor, the Khel Ratna Award (originally Rajiv Gandhi Khel Ratna, now Major Dhyan Chand Khel Ratna), in 1991-92?",
        "q_hi": "1991-92 में भारत के सर्वोच्च खेल सम्मान 'खेल रत्न पुरस्कार' (वर्तमान नाम मेजर ध्यानचंद खेल रत्न पुरस्कार) के प्रथम प्राप्तकर्ता कौन थे?",
        "options_en": ["Viswanathan Anand (विश्वनाथन आनंद - शतरंज)", "Sachin Tendulkar", "Geet Sethi", "Karnam Malleswari"],
        "options_hi": ["विश्वनाथन आनंद (Viswanathan Anand - 1991-92)", "सचिन तेंदुलकर (1997-98 में प्राप्तकर्ता)", "गीत सेठी (1992-93 में बिलियर्ड्स हेतु)", "कर्णम मल्लेश्वरी (1994-95 में भारोत्तोलन हेतु)"],
        "correct_idx": 0,
        "exp_en": "Grandmaster Viswanathan Anand was named the inaugural recipient of the Rajiv Gandhi Khel Ratna Award in 1991-92 for his extraordinary international achievements in chess.",
        "exp_hi": "भारत के पहले शतरंज ग्रैंडमास्टर विश्वनाथन आनंद को 1991-92 में देश का पहला खेल रत्न पुरस्कार प्रदान किया गया था। (सचिन तेंदुलकर को 1997-98 में मिला)।",
        "cue_en": "First Khel Ratna recipient = Viswanathan Anand (1991-92).",
        "cue_hi": "प्रथम खेल रत्न पुरस्कार = विश्वनाथन आनंद (1991-92)।",
        "wrong_en": ["First recipient in 1991-92.", "Received award in 1997-98.", "Second recipient in 1992-93.", "First woman recipient in 1994-95."],
        "wrong_hi": ["1991-92 के पहले प्राप्तकर्ता।", "1997-98 में प्राप्तकर्ता।", "दूसरे प्राप्तकर्ता।", "पहली महिला प्राप्तकर्ता।"]
    },
    {
        "name_en": "Traditional Indian Martial Arts & Indigenous Games: Kalaripayattu, Gatka, Mallakhamb & Kabaddi",
        "name_hi": "पारंपरिक भारतीय युद्ध कलाएं एवं देशी खेल: कलारिपयट्टू, गतका, मल्लखंब, थांग-ता एवं कबड्डी",
        "concepts_en": ["Kalaripayattu (Kerala): One of the world's oldest surviving martial arts; taught in 'Kalari' arenas; incorporates strikes, weapon combat (Urumi flexible whip-sword), Marmam pressure points", "Gatka (Punjab): Traditional Sikh martial art involving wooden sticks (Soti) and leather shields (Phari) associated with the Khalsa Panth and Guru Hargobind", "Thang-Ta (Huyen Langlon, Manipur): Ancient armed martial art with Thang (sword) and Ta (spear)", "Mallakhamb (Madhya Pradesh & Maharashtra): Ancient gymnastic sport performing aerial yoga and acrobatic postures on a vertical wooden pole; declared State Sport of Madhya Pradesh in 2013", "Kabaddi (indigenous contact sport, 7 players per team, canting 'Kabaddi', bonus line, super tackle; India has won all Asian Games men's golds except 2018) and Kho-Kho"],
        "concepts_hi": ["कलारिपयट्टू (केरल): विश्व की प्राचीनतम जीवित युद्ध कलाओं में से एक; 'कलारी' अखाड़े में प्रशिक्षण; उरुमी (लचीली तलवार) व मर्मम (नाड़ी बिंदु) तकनीक", "गतका (पंजाब): सिखों की पारंपरिक युद्ध कला जिसमें लकड़ी की सोंटी और ढाल का उपयोग होता है; गुरु हरगोविंद साहिब की 'मीरी-पीरी' परंपरा से संबंधित", "थांग-ता (मणिपुर): 'हुएन लंगलान' युद्ध कला का सशस्त्र रूप; थांग (तलवार) और ता (भाला)", "मल्लखंब (मध्य प्रदेश व महाराष्ट्र): एक ऊर्ध्वाधर सागौन के लकड़ी के खंभे पर योग और कलाबाजियां दिखाने वाला पारंपरिक खेल; 2013 में मध्य प्रदेश का 'राज्य खेल' घोषित", "कबड्डी: 7 खिलाड़ियों की टीम, रेडर का 'कबड्डी' बोलना; एशियाई खेलों में भारत का ऐतिहासिक दबदबा; खो-खो"],
        "q_en": "Which traditional martial art, originating in Kerala and incorporating the use of the deadly flexible whip-sword 'Urumi', is celebrated as one of the world's oldest surviving combat systems?",
        "q_hi": "केरल में उत्पन्न होने वाली तथा लचीली चाबुक जैसी तलवार 'उरुमी' (Urumi) के प्रयोग हेतु प्रसिद्ध वह पारंपरिक युद्ध कला कौन सी है, जिसे विश्व की सबसे प्राचीन जीवित युद्ध कलाओं में गिना जाता है?",
        "options_en": ["Kalaripayattu (कलारिपयट्टू - केरल)", "Gatka", "Thang-Ta", "Silambam"],
        "options_hi": ["कलारिपयट्टू (Kalaripayattu - केरल)", "गतका (Gatka - पंजाब)", "थांग-ता (Thang-Ta - मणिपुर)", "सिलंबम (Silambam - तमिलनाडु की लाठी कला)"],
        "correct_idx": 0,
        "exp_en": "Kalaripayattu originated in southwestern India (Kerala) dating back over 3,000 years, featuring ritual combat, body conditioning (Meypayattu), and flexible steel whip-swords (Urumi).",
        "exp_hi": "कलारिपयट्टू केरल की पारंपरिक मार्शल आर्ट है जिसे भगवान परशुराम से जोड़ा जाता है; इसमें शरीर की नाड़ियों (मर्मम) और लचीली तलवार 'उरुमी' के दांव-पेंच सिखाए जाते हैं।",
        "cue_en": "Ancient martial art of Kerala with Urumi = Kalaripayattu.",
        "cue_hi": "केरल की प्राचीन युद्ध कला = कलारिपयट्टू।",
        "wrong_en": ["Ancient martial art from Kerala.", "Martial art from Punjab.", "Martial art from Manipur.", "Staff-fighting art from Tamil Nadu."],
        "wrong_hi": ["केरल की प्राचीन युद्ध कला।", "पंजाब की युद्ध कला।", "मणिपुर की युद्ध कला।", "तमिलनाडु की लाठी कला।"]
    },
    {
        "name_en": "Khelo India Initiative, Target Olympic Podium Scheme (TOPS) & Sports Governance in India",
        "name_hi": "खेलो इंडिया पहल, टारगेट ओलंपिक पोडियम स्कीम (TOPS) एवं भारतीय खेल शासन संरचना",
        "concepts_en": ["Khelo India Programme: Launched in 2017-18 by Ministry of Youth Affairs and Sports to revive sports culture at grassroots level; verticals include Khelo India Youth Games (KIYG), Khelo India University Games (KIUG), and Khelo India Winter Games; provides financial assistance of ₹5 lakh per annum for 8 years to talented athletes", "Target Olympic Podium Scheme (TOPS): Flagship program launched in 2014 to identify, groom, and finance prospective Olympic and Paralympic medal winners with customized elite training, foreign coaching, physiotherapy, and ₹50,000 monthly out-of-pocket allowance", "Sports Authority of India (SAI, established 1984) and Indian Olympic Association (IOA, founded 1927 by Sir Dorabji Tata; P.T. Usha elected first female president in 2022)"],
        "concepts_hi": ["खेलो इंडिया कार्यक्रम: युवा मामले और खेल मंत्रालय द्वारा 2017-18 में जमीनी स्तर पर खेल संस्कृति को पुनर्जीवित करने हेतु प्रारंभ; खेलो इंडिया यूथ गेम्स, यूनिवर्सिटी गेम्स एवं विंटर गेम्स; चयनित खिलाड़ियों को 8 वर्षों तक प्रतिवर्ष ₹5 लाख की वित्तीय सहायता", "टारगेट ओलंपिक पोडियम स्कीम (TOPS): 2014 में शुरू की गई महत्वाकांक्षी योजना, जिसका उद्देश्य ओलंपिक व पैरालंपिक में पदक जीतने की संभावना वाले खिलाड़ियों को विश्वस्तरीय विदेशी कोचिंग, उपकरण और ₹50,000 मासिक भत्ता देना है", "भारतीय खेल प्राधिकरण (SAI, स्थापना 1984) एवं भारतीय ओलंपिक संघ (IOA, 1927 में दोराबजी टाटा द्वारा स्थापित; 2022 में पी.टी. उषा पहली महिला अध्यक्ष बनीं)"],
        "q_en": "Which flagship sports scheme was launched by the Government of India in 2014 to identify, finance, and prepare elite athletes specifically for podium finishes at the Olympic and Paralympic Games?",
        "q_hi": "ओलंपिक और पैरालंपिक खेलों में पदक (पोडियम फिनिश) हासिल करने के उद्देश्य से शीर्ष भारतीय एथलीटों को विश्वस्तरीय प्रशिक्षण व वित्तीय सहायता देने हेतु 2014 में कौन सी प्रमुख योजना शुरू की गई थी?",
        "options_en": ["Target Olympic Podium Scheme (TOPS / टारगेट ओलंपिक पोडियम स्कीम)", "Khelo India Youth Mission", "Fit India Movement", "Rashtriya Khel Protsahan Puraskar"],
        "options_hi": ["टारगेट ओलंपिक पोडियम स्कीम (TOPS - Target Olympic Podium Scheme)", "खेलो इंडिया यूथ मिशन", "फिट इंडिया मूवमेंट", "राष्ट्रीय खेल प्रोत्साहन पुरस्कार"],
        "correct_idx": 0,
        "exp_en": "The Target Olympic Podium Scheme (TOPS), operating under the Ministry of Youth Affairs and Sports, identifies elite medal prospects and covers all expenses for international training, coaches, and medical care.",
        "exp_hi": "टारगेट ओलंपिक पोडियम स्कीम (TOPS) 2014 में शुरू की गई थी, जिसके तहत अभिनव बिंद्रा, नीरज चोपड़ा, पी.वी. सिंधु जैसे शीर्ष एथलीटों को ओलंपिक पदक जीतने के लिए विदेश में ट्रेनिंग और वित्तीय सहायता दी जाती है।",
        "cue_en": "Elite Olympic medal training scheme = TOPS (Target Olympic Podium Scheme).",
        "cue_hi": "ओलंपिक पदक विजेता प्रशिक्षण योजना = TOPS।",
        "wrong_en": ["Elite athlete Olympic preparation scheme.", "Grassroots school/college sports program.", "Mass physical fitness awareness campaign.", "Corporate sports sponsorship award."],
        "wrong_hi": ["ओलंपिक पदक प्रशिक्षण योजना।", "जमीनी स्तर की खेल प्रतियोगिता।", "शारीरिक फिटनेस अभियान।", "खेल प्रोत्साहन पुरस्कार।"]
    }
]

print("Loaded S19 successfully")
