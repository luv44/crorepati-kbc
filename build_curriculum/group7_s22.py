# build_curriculum/group7_s22.py
# S22: World Religions, Philosophies & Mythologies (7 topics across 2 chapters)

DATA = {}

# S22-Cbc82f40b Six Schools of Indian Philosophy (Shad-Darshanas) & Heterodox Systems (3 topics)
DATA["S22-Cbc82f40b"] = [
    {
        "name_en": "Six Classical Orthodox Schools (Shad-Darshanas): Samkhya, Yoga, Nyaya, Vaisheshika, Mimamsa & Vedanta",
        "name_hi": "भारतीय षड्-दर्शन (आस्तिक दर्शन): सांख्य, योग, न्याय, वैशेषिक, मीमांसा एवं वेदांत",
        "concepts_en": ["Astika (Orthodox) Schools accept the authority of the Vedas; paired into three coupled systems:", "1. Samkhya (Sage Kapila, Samkhya Sutra): Dualistic realism of Purusha (pure consciousness) and Prakriti (matter/nature with 3 Gunas: Sattva, Rajas, Tamas); oldest philosophical school", "2. Yoga (Sage Patanjali, Yoga Sutra): Practical application of Samkhya; Ashtanga Yoga (8 limbs: Yama, Niyama, Asana, Pranayama, Pratyahara, Dharana, Dhyana, Samadhi)", "3. Nyaya (Sage Gautama, Nyaya Sutra): Epistemology, logical analysis, 4 Pramanas (valid means of knowledge: Pratyaksha, Anumana, Upamana, Shabda)", "4. Vaisheshika (Sage Kanada / Kashyapa): Atomism; universe composed of Paramāṇu (indivisible atoms); 7 Padarthas (categories of reality)", "5. Purva Mimamsa (Sage Jaimini): Vedic ritualism and hermeneutics, Dharma through Vedic injunctions", "6. Uttara Mimamsa / Vedanta (Sage Badarayana, Brahma Sutras): Monism and Upanishadic realization; Advaita (Adi Shankara - non-dualism: 'Brahma Satyam Jagan Mithya'), Vishishtadvaita (Ramanuja - qualified non-dualism), Dvaita (Madhvacharya - dualism)"],
        "concepts_hi": ["आस्तिक दर्शन (वेदों की प्रामाणिकता स्वीकार करने वाले 6 दर्शन):", "1. सांख्य दर्शन (महर्षि कपिल, सांख्य सूत्र): सबसे प्राचीन दर्शन; पुरुष (चेतना) और प्रकृति (त्रिगुणात्मक भौतिक संसार - सत्व, रज, तम) का द्वैतवाद", "2. योग दर्शन (महर्षि पतंजलि, योग सूत्र): चित्तवृत्ति निरोध; अष्टांग योग (यम, नियम, आसन, प्राणायाम, प्रत्याहार, धारणा, ध्यान, समाधि)", "3. न्याय दर्शन (महर्षि गौतम / अक्षपाद गौतम): तर्कशास्त्र व ज्ञानमीमांसा; 4 प्रमाण (प्रत्यक्ष, अनुमान, उपमान, शब्द)", "4. वैशेषिक दर्शन (महर्षि कणाद): प्राचीन परमाणुवाद के जनक; सृष्टि का मूल अविभाज्य 'परमाणु' है", "5. पूर्व मीमांसा (महर्षि जैमिनी): वैदिक कर्मकांड, यज्ञ और धर्म का दार्शनिक विश्लेषण", "6. उत्तर मीमांसा / वेदांत (महर्षि बादरायण): उपनिषदों का सार; अद्वैत वेदांत (आदि शंकराचार्य: 'ब्रह्म सत्यं जगन्मिथ्या जीवो ब्रह्मैव नापरः')"],
        "q_en": "Which ancient Indian sage is celebrated as the founder of the 'Vaisheshika' philosophical school, having proposed an early atomic theory of matter composed of indestructible 'Paramāṇu'?",
        "q_hi": "प्राचीन भारतीय 'वैशेषिक दर्शन' के प्रवर्तक कौन से महर्षि हैं, जिन्होंने यह प्रतिपादित किया था कि यह संपूर्ण भौतिक जगत अविभाज्य 'परमाणुओं' के संघटन से निर्मित है?",
        "options_en": ["Maharishi Kanada / Kashyapa (महर्षि कणाद)", "Sage Kapila", "Sage Gautama", "Sage Patanjali"],
        "options_hi": ["महर्षि कणाद (Maharishi Kanada)", "महर्षि कपिल (यह सांख्य दर्शन के प्रवर्तक हैं)", "महर्षि गौतम (यह न्याय दर्शन के प्रवर्तक हैं)", "महर्षि पतंजलि (यह योग दर्शन के प्रवर्तक हैं)"],
        "correct_idx": 0,
        "exp_en": "Maharishi Kanada (also called Kashyapa) founded the Vaisheshika school around the 6th-2nd century BCE, formulating the atomic concept of Paramāṇu centuries before Greek philosophers like Democritus.",
        "exp_hi": "महर्षि कणाद ने वैशेषिक दर्शन की नींव रखी और बताया कि पदार्थ का सूक्ष्मतम अविभाज्य कण 'परमाणु' है; वे भारतीय परमाणुवाद के जनक माने जाते हैं।",
        "cue_en": "Vaisheshika atomism = Maharishi Kanada; Samkhya = Kapila; Nyaya = Gautama; Yoga = Patanjali.",
        "cue_hi": "वैशेषिक (परमाणु) = कणाद; सांख्य = कपिल; न्याय = गौतम; योग = पतंजलि।",
        "wrong_en": ["Founder of Vaisheshika atomism.", "Founder of Samkhya philosophy.", "Founder of Nyaya logic.", "Codifier of Ashtanga Yoga."],
        "wrong_hi": ["वैशेषिक दर्शन के प्रवर्तक।", "सांख्य दर्शन के प्रवर्तक।", "न्याय दर्शन के प्रवर्तक।", "योग दर्शन के प्रवर्तक।"]
    },
    {
        "name_en": "Advaita Vedanta of Adi Shankaracharya: Non-Dualism, Maya, Nirguna Brahman & Four Amnaya Mutts",
        "name_hi": "आदि शंकराचार्य का अद्वैत वेदांत: मायावाद, निर्गुण ब्रह्म एवं चार दिशाओं के आम्नाय मठ",
        "concepts_en": ["Adi Shankaracharya (788-820 CE, born in Kalady, Kerala): Propounded Advaita (Absolute Non-Dualism); core aphorism: 'Brahma Satyam Jagan Mithya, Jivo Brahmaiva Naparah' (Brahman alone is real, the empirical world is an illusion/Maya, and the individual soul is identical to Brahman)", "Nirguna Brahman: Ultimate attribute-less reality beyond space, time, and form; superimposed by Maya/Avidya", "Commentaries (Prasthanatrayi Bhasya): Authored master commentaries on the 3 canonical foundations of Hindu philosophy: Upanishads, Bhagavad Gita, and Brahma Sutras", "Established Four Cardinal Amnaya Peethams (Mutts) to unify and protect Sanatana Dharma:", "1. Sringeri Sharada Peetham (South, Karnataka - Yajurveda)", "2. Govardhana Mutt (East, Puri, Odisha - Rigveda)", "3. Kalika Mutt / Dwaraka Peetham (West, Gujarat - Samaveda)", "4. Jyotirmath / Badrikashram (North, Uttarakhand - Atharvaveda)"],
        "concepts_hi": ["आदि शंकराचार्य (788-820 ई., जन्म कालड़ी, केरल): 'अद्वैत वेदांत' (पूर्ण अद्वैतवाद) के महान प्रतिपादक; मूल सूत्र: 'ब्रह्म सत्यं जगन्मिथ्या जीवो ब्रह्मैव नापरः' (केवल निर्गुण निराकार ब्रह्म ही सत्य है, संसार माया है और जीवात्मा ब्रह्म से भिन्न नहीं है)", "प्रस्थानत्रयी पर भाष्य: उपनिषद, श्रीमद्भगवद्गीता और ब्रह्मसूत्र पर कालजयी दार्शनिक भाष्य लिखे", "चार आम्नाय मठों की स्थापना (सनातन धर्म की रक्षा हेतु चार दिशाओं में):", "1. शृंगेरी शारदा पीठ (दक्षिण, कर्नाटक - यजुर्वेद)", "2. गोवर्धन पीठ (पूर्व, पुरी, ओडिशा - ऋग्वेद)", "3. द्वारका पीठ / कालिका मठ (पश्चिम, गुजरात - सामवेद)", "4. ज्योतिर्मठ (उत्तर, बद्रीनाथ, उत्तराखंड - अथर्ववेद)"],
        "q_en": "Which cardinal Amnaya Peetham (Mutt) was established by Adi Shankaracharya in Northern India (Uttarakhand) associated with the Atharvaveda?",
        "q_hi": "आदि शंकराचार्य द्वारा सनातन धर्म के संरक्षण हेतु उत्तर भारत (उत्तराखंड) में अथर्ववेद से संबद्ध कौन सा प्रमुख आम्नाय पीठ (मठ) स्थापित किया गया था?",
        "options_en": ["Jyotirmath / Badrikashram (ज्योतिर्मठ, उत्तराखंड)", "Sringeri Sharada Peetham", "Govardhana Mutt, Puri", "Dwaraka Sharada Peetham"],
        "options_hi": ["ज्योतिर्मठ / बदरिकाश्रम (Jyotirmath, Uttarakhand - उत्तर)", "शृंगेरी शारदा पीठ (Sringeri - दक्षिण, कर्नाटक)", "गोवर्धन पीठ (Puri - पूर्व, ओडिशा)", "द्वारका पीठ (Dwaraka - पश्चिम, गुजरात)"],
        "correct_idx": 0,
        "exp_en": "Adi Shankara established four corner mutts: Jyotirmath in the North (Uttarakhand, Atharvaveda), Sringeri in the South (Karnataka, Yajurveda), Govardhana in the East (Puri, Rigveda), and Dwaraka in the West (Gujarat, Samaveda).",
        "exp_hi": "आदि शंकराचार्य ने चार दिशाओं में चार पीठ स्थापित किए: उत्तर में ज्योतिर्मठ (उत्तराखंड), दक्षिण में शृंगेरी (कर्नाटक), पूर्व में गोवर्धन मठ (पुरी, ओडिशा) और पश्चिम में द्वारका पीठ (गुजरात)।",
        "cue_en": "North Mutt = Jyotirmath; South = Sringeri; East = Govardhan Puri; West = Dwaraka.",
        "cue_hi": "उत्तर = ज्योतिर्मठ; दक्षिण = शृंगेरी; पूर्व = गोवर्धन पुरी; पश्चिम = द्वारका।",
        "wrong_en": ["Northern Mutt in Uttarakhand.", "Southern Mutt in Karnataka.", "Eastern Mutt in Puri, Odisha.", "Western Mutt in Gujarat."],
        "wrong_hi": ["उत्तरी मठ (उत्तराखंड)।", "दक्षिणी मठ (कर्नाटक)।", "पूर्वी मठ (ओडिशा)।", "पश्चिमी मठ (गुजरात)।"]
    },
    {
        "name_en": "Heterodox (Nastika) Systems: Charvaka Materialism, Ajivika Fatalism & Jain Anekantavada",
        "name_hi": "नास्तिक दर्शन: चार्वाक (भौतिकवाद / लोकायत), आजीवक (नियतिवाद) एवं जैन अनेकांतवाद",
        "concepts_en": ["Nastika Schools reject the absolute authority of the Vedas:", "1. Charvaka / Lokayata (Sage Brihaspati): Pure philosophical materialism, empiricism, and hedonism; Pratyaksha (direct perception) is the ONLY valid source of knowledge (rejects inference and testimony); rejects soul, afterlife, rebirth, heaven/hell, and God; famous attributed verse: 'Yavaj jivet sukham jivet, rinam kritva ghritam pibet' (as long as you live, live happily, even if you have to borrow money to drink ghee)", "2. Ajivika (Makkhali Gosala, contemporary of Buddha and Mahavira): Absolute fatalism / determinism (Niyati); belief that human effort, karma, and free will are complete illusions, and all destinies are rigidly predetermined across 8.4 million rebirths; Barabar Caves dedicated to Ajivikas by Ashoka", "3. Jain Epistemology: Anekantavada (doctrine of many-sidedness of reality), Syadvada (theory of conditioned predication: seven-fold logic), and Ahimsa (absolute non-violence)"],
        "concepts_hi": ["नास्तिक दर्शन (जो वेदों की प्रामाणिकता को नहीं मानते):", "1. चार्वाक / लोकायत दर्शन (ऋषि बृहस्पति): शुद्ध भौतिकवाद एवं सुखवाद; केवल 'प्रत्यक्ष प्रमाण' को एकमात्र सत्य मानता है (अनुमान व शब्द प्रमाण को खारिज करता है); आत्मा, ईश्वर, पुनर्जन्म व परलोक का खंडन; प्रसिद्ध सूत्र: 'यावज्जीवेत् सुखं जीवेत् ऋणं कृत्वा घृतं पिबेत्' (जब तक जियो सुख से जियो, चाहे ऋण लेकर घी पियो)", "2. आजीवक संप्रदाय (मक्खलि गोशाल): पूर्ण 'नियतिवाद' (Fatalism); मनुष्य के कर्म और पुरुषार्थ को निष्फल मानते हुए सब कुछ पूर्व-निर्धारित (नियति) मानता है; मौर्य सम्राट अशोक ने बराबर की गुफाएं आजीवकों को दान में दी थीं", "3. जैन ज्ञानमीमांसा: 'अनेकांतवाद' (सत्य के बहुआयामी रूप), 'स्याद्वाद' (सप्तभंगी नय) एवं परम अहिंसा"],
        "q_en": "Which heterodox (Nastika) school of ancient Indian philosophy accepted ONLY 'Pratyaksha' (direct empirical perception) as the sole valid means of knowledge (Pramana), rejecting God, soul, and rebirth?",
        "q_hi": "प्राचीन भारतीय दर्शन का वह कौन सा नास्तिक व भौतिकवादी संप्रदाय था, जो ईश्वर, आत्मा व पुनर्जन्म को नकारते हुए केवल 'प्रत्यक्ष' (Direct Perception) को ही ज्ञान का एकमात्र प्रमाण मानता था?",
        "options_en": ["Charvaka / Lokayata (चार्वाक / लोकायत दर्शन)", "Ajivika", "Buddhism", "Jainism"],
        "options_hi": ["चार्वाक / लोकायत दर्शन (Charvaka / Lokayata)", "आजीवक संप्रदाय (Ajivika - मक्खलि गोशाल का नियतिवाद)", "बौद्ध दर्शन (Buddhism - मध्यम मार्ग)", "जैन दर्शन (Jainism - अनेकांतवाद)"],
        "correct_idx": 0,
        "exp_en": "The Charvaka (Lokayata) school was an uncompromising materialist and empiricist philosophy that held direct sense perception (Pratyaksha) as the only valid Pramana, rejecting metaphysics, karma, and the afterlife.",
        "exp_hi": "चार्वाक दर्शन केवल उसी को सत्य मानता था जिसे आंखों से प्रत्यक्ष देखा जा सके; इसने अदृश्य ईश्वर, आत्मा, स्वर्ग-नरक और यज्ञों को केवल धूर्तों की आजीविका का साधन बताया था।",
        "cue_en": "Charvaka = Only Pratyaksha is valid (materialism).",
        "cue_hi": "चार्वाक दर्शन = केवल प्रत्यक्ष प्रमाण ही सत्य।",
        "wrong_en": ["Radical materialist school accepting only perception.", "Fatalist school led by Makkhali Gosala.", "Accepts perception and inference (Pratyaksha & Anumana).", "Accepts perception, inference, and testimony."],
        "wrong_hi": ["केवल प्रत्यक्ष को मानने वाला चार्वाक दर्शन।", "नियतिवादी आजीवक।", "बौद्ध धर्म (मध्यम मार्ग)।", "जैन धर्म।"]
    }
]

# S22-C8e2684ea World Religions (Buddhism, Christianity, Islam) & Classical Myths (4 topics)
DATA["S22-C8e2684ea"] = [
    {
        "name_en": "Buddhism: Four Noble Truths, Eightfold Path, Buddhist Councils & Mahayana vs Theravada",
        "name_hi": "बौद्ध धर्म: चार आर्य सत्य, अष्टांगिक मार्ग, बौद्ध संगीतियां एवं महायान बनाम हीनयान/थेरवाद",
        "concepts_en": ["Siddhartha Gautama (The Buddha, 563-483 BCE): Born in Lumbini (Nepal); Great Renunciation (Mahabhinishkramana) at age 29; Enlightenment (Nirvana) under Bodhi Tree at Bodh Gaya; First Sermon (Dhammacakkappavattana) at Sarnath; Mahaparinirvana at Kushinagar", "Four Noble Truths (Chatvari Arya Satyani): 1. Dukkha (suffering exists), 2. Samudaya (origin of suffering is Trishna/craving), 3. Nirodha (cessation of suffering is Nirvana), 4. Magga (path leading to cessation is Eightfold Path)", "Noble Eightfold Path (Ashtangika Marga): Right View, Right Resolve, Right Speech, Right Action, Right Livelihood, Right Effort, Right Mindfulness, Right Concentration", "Four Buddhist Councils: 1st at Rajgriha (483 BCE, King Ajatashatru), 2nd at Vaishali (383 BCE, King Kalashoka), 3rd at Pataliputra (250 BCE, Emperor Ashoka), 4th at Kundalvana, Kashmir (72 CE, King Kanishka - where Buddhism formally split into Hinayana/Theravada and Mahayana)"],
        "concepts_hi": ["गौतम बुद्ध (563-483 ईसा पूर्व): जन्म लुंबिनी (नेपाल); 29 वर्ष की उम्र में महाभिनिष्क्रमण (गृहत्याग); बोधगया में बोधिवृक्ष के नीचे संबोधि (ज्ञान प्राप्ति); सारनाथ में प्रथम उपदेश (धर्मचक्रप्रवर्तन); कुशीनगर में महापरिनिर्वाण", "चार आर्य सत्य: 1. दुःख (संसार दुःखमय है), 2. दुःख समुदाय (तृष्णा दुःख का कारण है), 3. दुःख निरोध (तृष्णा त्याग से निर्वाण संभव है), 4. दुःख निरोध गामिनी प्रतिपदा (अष्टांगिक मार्ग)", "अष्टांगिक मार्ग: सम्यक दृष्टि, सम्यक संकल्प, सम्यक वाक, सम्यक कर्म, सम्यक आजीव, सम्यक व्यायाम, सम्यक स्मृति, सम्यक समाधि", "चार प्रमुख बौद्ध संगीतियां: 1. राजगृह (483 ई.पू., अजातशत्रु), 2. वैशाली (383 ई.पू., कालाशोक), 3. पाटलिपुत्र (250 ई.पू., सम्राट अशोक), 4. कुंडलवन, कश्मीर (72 ई., कनिष्क - जहां बौद्ध धर्म हीनयान और महायान में विभाजित हुआ)"],
        "q_en": "At which Fourth Buddhist Council, convened during the reign of Kushan Emperor Kanishka around 72 CE in Kundalvana, Kashmir, did Buddhism formally split into Mahayana and Hinayana?",
        "q_hi": "72 ईस्वी में कुषाण सम्राट कनिष्क के शासनकाल में कश्मीर के कुंडलवन में आयोजित किस बौद्ध संगीति में बौद्ध धर्म औपचारिक रूप से 'हीनयान' और 'महायान' दो संप्रदायों में विभाजित हो गया?",
        "options_en": ["Fourth Buddhist Council (चतुर्थ बौद्ध संगीति - कनिष्क के काल में)", "Third Buddhist Council", "First Buddhist Council", "Second Buddhist Council"],
        "options_hi": ["चतुर्थ बौद्ध संगीति (Fourth Buddhist Council - कश्मीर)", "तृतीय बौद्ध संगीति (पाटलिपुत्र - अशोक के काल में)", "प्रथम बौद्ध संगीति (राजगृह - अजातशत्रु के काल में)", "द्वितीय बौद्ध संगीति (वैशाली - कालाशोक के काल में)"],
        "correct_idx": 0,
        "exp_en": "The Fourth Buddhist Council was held in Kundalvana, Kashmir under the patronage of King Kanishka (presided over by Vasumitra and Ashvaghosha), where the historic division into Hinayana and Mahayana was formalized.",
        "exp_hi": "चतुर्थ बौद्ध संगीति कनिष्क के समय कश्मीर के कुंडलवन में वसुमित्र की अध्यक्षता में हुई थी, जहां महायान संप्रदाय ने बुद्ध को भगवान मानकर मूर्ति पूजा प्रारंभ की।",
        "cue_en": "4th Buddhist Council = Kanishka (Kashmir) -> split into Hinayana and Mahayana.",
        "cue_hi": "चतुर्थ संगीति = कनिष्क (कश्मीर) -> हीनयान व महायान विभाजन।",
        "wrong_en": ["Fourth Council under Kanishka.", "Third Council under Ashoka.", "First Council under Ajatashatru.", "Second Council under Kalashoka."],
        "wrong_hi": ["चतुर्थ संगीति (कश्मीर)।", "तृतीय संगीति (पाटलिपुत्र)।", "प्रथम संगीति (राजगृह)।", "द्वितीय संगीति (वैशाली)।"]
    },
    {
        "name_en": "Christianity: Jesus of Nazareth, Apostles, The Holy Bible & Nicene Creed",
        "name_hi": "ईसाई धर्म: ईसा मसीह (यीशु), 12 प्रेरित, पवित्र बाइबिल एवं प्रमुख संप्रदाय (कैथोलिक, प्रोटेस्टेंट)",
        "concepts_en": ["Origins: Life and teachings of Jesus of Nazareth (born in Bethlehem, Judea; raised in Nazareth; crucified under Roman prefect Pontius Pilate in Jerusalem, resurrected on Easter Sunday)", "The Holy Bible: Two testaments - Old Testament (39 books, Hebrew scriptures/Tanakh) and New Testament (27 books in Koine Greek, including 4 canonical Gospels: Matthew, Mark, Luke, John; Acts of the Apostles; Epistles of Paul; Revelation)", "Twelve Apostles: St. Peter (first Bishop of Rome / Pope; Keys of the Kingdom) and St. Paul (apostle to the Gentiles); St. Thomas the Apostle arrived in Kerala, India in 52 CE establishing Malankara Church", "Ecumenical Councils: Council of Nicaea (325 CE convened by Roman Emperor Constantine the Great, formulated Nicene Creed defining the Holy Trinity: Father, Son, and Holy Spirit)", "Great Schism (1054 CE: Western Catholic vs Eastern Orthodox); Protestant Reformation (1517: Martin Luther nailed 95 Theses in Wittenberg)"],
        "concepts_hi": ["उद्भव: ईसा मसीह (यीशु / Jesus Christ) का जीवन व उपदेश (जन्म बेथलेहम, यहूदिया; रोमन गवर्नर पोंटियस पिलातुस द्वारा यरुशलम में क्रूस पर चढ़ाया जाना, ईस्टर पर पुनरुत्थान)", "पवित्र बाइबिल: दो भाग - पुराना नियम (Old Testament - 39 पुस्तकें) एवं नया नियम (New Testament - 27 पुस्तकें, जिसमें 4 मुख्य सुसमाचार/गॉस्पेल: मैथ्यू, मार्क, ल्यूक, जॉन शामिल हैं)", "बारह प्रेरित (Twelve Apostles): सेंट पीटर (प्रथम पोप) एवं सेंट थॉमस (52 ईस्वी में केरल आकर भारत में ईसाई धर्म का प्रचार करने वाले पहले संत)", "नाइसिया की परिषद (325 ईस्वी, रोमन सम्राट कॉन्सटेंटाइन): 'पवित्र त्रित्व' (Holy Trinity - परमपिता, पुत्र यीशु एवं पवित्र आत्मा) के सिद्धांत को औपचारिक मान्यता", "महान विभाजन (1054: रोमन कैथोलिक बनाम ईस्टर्न ऑर्थोडॉक्स); प्रोटेस्टेंट सुधार (1517: मार्टिन लूथर द्वारा 95 थीसिस)"],
        "q_en": "Which Apostle of Jesus Christ is historically recorded as having arrived on the Malabar Coast of Kerala, India in 52 CE to preach the Gospel and establish the Seven Churches?",
        "q_hi": "ईसा मसीह के 12 प्रेरितों (Apostles) में से वह कौन से संत थे, जो 52 ईस्वी में भारत के केरल (मालाबार तट) पहुंचे और उन्होंने भारत में ईसाई धर्म का पहला बीज बोया?",
        "options_en": ["St. Thomas the Apostle (सेंट थॉमस / सेंट थॉमस ईसाई)", "St. Peter", "St. Paul", "St. Francis Xavier"],
        "options_hi": ["सेंट थॉमस (St. Thomas the Apostle - 52 ईस्वी)", "सेंट पीटर (रोम के प्रथम बिशप)", "सेंट पॉल (पत्रों के रचयिता)", "सेंट फ्रांसिस जेवियर (1542 में गोवा आए जेसुइट मिशनरी)"],
        "correct_idx": 0,
        "exp_en": "Tradition holds that Saint Thomas the Apostle landed at Kodungallur (Muziris) in Kerala in 52 CE, founding seven churches (Ezharappallikal) among local communities before his martyrdom in Mylapore, Chennai.",
        "exp_hi": "सेंट थॉमस 52 ईस्वी में केरल के कोडुंगल्लूर पहुंचे थे और उन्होंने भारत में 7 प्राचीन चर्च स्थापित किए; आज भी केरल के प्राचीन ईसाई समुदाय को 'सेंट थॉमस ईसाई' (सीरियन क्रिश्चियन) कहा जाता है।",
        "cue_en": "First Christian apostle to India (52 CE) = St. Thomas.",
        "cue_hi": "भारत आने वाले पहले ईसाई संत (52 ईस्वी) = सेंट थॉमस।",
        "wrong_en": ["Apostle who landed in Kerala in 52 CE.", "First Pope and Bishop of Rome.", "Apostle who wrote epistles to Gentiles.", "Jesuit missionary who arrived in Goa in 1542."],
        "wrong_hi": ["52 ईस्वी में केरल आने वाले संत।", "रोम के पहले पोप।", "पत्रों के लेखक प्रेरित।", "1542 में गोवा आए जेसुइट संत।"]
    },
    {
        "name_en": "Islam: Prophet Muhammad, The Holy Quran, Five Pillars & The Hijrah Calendar",
        "name_hi": "इस्लाम धर्म: पैगंबर हज़रत मुहम्मद, पवित्र कुरआन, पांच स्तंभ (अर्कान) एवं हिजरी संवत (622 ई.)",
        "concepts_en": ["Prophet Muhammad (570-632 CE): Born in Mecca (Quraysh tribe); received first revelation of the Quran from Archangel Jibril (Gabriel) at Cave Hira on Mount Jabal al-Nour in 610 CE (Laylat al-Qadr); established the first Islamic state in Medina", "The Hijrah (622 CE): Migration from Mecca to Medina to escape persecution, marking Year 1 of the Islamic lunar calendar (Hijri Calendar: AH 1)", "The Holy Quran: Literal word of Allah, revealed in Arabic; divided into 114 Surahs (chapters) and 6,236 Ayahs (verses)", "Five Pillars of Islam (Arkan al-Islam):", "1. Shahada (Declaration of faith: 'There is no God but Allah, and Muhammad is His messenger')", "2. Salah (Ritual prayers performed 5 times daily facing the Kaaba in Mecca / Qibla)", "3. Zakat (Mandatory annual alms-giving of 2.5% of accumulated surplus wealth to the poor)", "4. Sawm (Fasting from dawn to dusk during the holy month of Ramadan)", "5. Hajj (Pilgrimage to Mecca required once in a lifetime for every able-bodied and financially capable Muslim)"],
        "concepts_hi": ["पैगंबर हज़रत मुहम्मद (570-632 ई.): मक्का में जन्म (कुरैश कबीला); 610 ईस्वी में जबल-ए-नूर की हीरा गुफा में देवदूत जिब्रील के माध्यम से पहला ईश्वरीय संदेश प्राप्त हुआ; मदीना में पहले इस्लामी राज्य की स्थापना", "हिजरत (622 ईस्वी): मक्का से मदीना का ऐतिहासिक प्रस्थान; इसी वर्ष से इस्लामी चंद्र कैलेंडर 'हिजरी संवत' (Hijri Calendar) की शुरुआत हुई", "पवित्र कुरआन: अरबी भाषा में अवतरित पवित्र ग्रंथ; इसमें 114 सूरह (अध्याय) और 6,236 आयतें हैं", "इस्लाम के पांच बुनियादी स्तंभ (अर्कान-ए-इस्लाम):", "1. कलिमा / शहादा (एकेश्वरवाद का विश्वास: 'अल्लाह के सिवा कोई पूज्य नहीं और मुहम्मद उनके रसूल हैं')", "2. नमाज़ / सलात (प्रतिदिन मक्का की काबा की ओर मुंह करके 5 समय की नमाज)", "3. ज़कात (वार्षिक बचत का 2.5% भाग निर्धनों और जरूरतमंदों को दान देना)", "4. रोज़ा / सौम (रमजान के पवित्र माह में सूर्योदय से सूर्यास्त तक उपवास)", "5. हज (सक्षम व्यक्ति हेतु जीवन में कम से कम एक बार पवित्र मक्का की तीर्थयात्रा)"],
        "q_en": "Which historic event in 622 CE, marking the migration of Prophet Muhammad and his early followers from Mecca to Medina, defines the starting epoch (Year 1) of the Islamic Hijri calendar?",
        "q_hi": "622 ईस्वी में मक्का से मदीना के लिए पैगंबर हज़रत मुहम्मद के ऐतिहासिक प्रस्थान को क्या कहा जाता है, जिससे इस्लामी 'हिजरी संवत' (कैलेंडर) का पहला वर्ष प्रारंभ हुआ?",
        "options_en": ["The Hijrah (हिजरत - 622 ईस्वी)", "Laylat al-Qadr", "The Hajj", "The Miraj"],
        "options_hi": ["हिजरत (The Hijrah - 622 ई.)", "लैलतुल कद्र (शब-ए-कद्र - पहली आयत उतरने की रात)", "हज (तीर्थयात्रा)", "मेराज (स्वर्गारोहण की रात)"],
        "correct_idx": 0,
        "exp_en": "The Hijrah occurred in 622 CE when Prophet Muhammad migrated from Mecca to Yathrib (renamed Medina al-Nabi). Caliph Umar later designated this event as Year 1 of the Islamic lunar Hijri calendar.",
        "exp_hi": "622 ईस्वी में पैगंबर मुहम्मद के मक्का से मदीना जाने की घटना को 'हिजरत' कहा जाता है; खलीफा हज़रत उमर ने इसी वर्ष से हिजरी संवत (1 AH) की शुरुआत की।",
        "cue_en": "Islamic calendar starts from Hijrah (622 CE).",
        "cue_hi": "हिजरी कैलेंडर की शुरुआत = हिजरत (622 ईस्वी)।",
        "wrong_en": ["Migration from Mecca to Medina in 622 CE.", "Night of Power when Quran was revealed.", "Annual pilgrimage to Mecca.", "Prophet's night journey to the heavens."],
        "wrong_hi": ["मक्का से मदीना प्रस्थान (हिजरत)।", "कुरआन अवतरण की पवित्र रात।", "मक्का की वार्षिक तीर्थयात्रा।", "आसमानी यात्रा (मेराज)।"]
    },
    {
        "name_en": "Greek, Roman & Norse Mythologies: Olympians, Norse Pantheon (Odin, Thor) & Mythic Archetypes",
        "name_hi": "ग्रीक, रोमन एवं नोर्स पौराणिक कथाएं: 12 ओलंपियन देवता, नोर्स देवमंडल (ओडिन, थोर) एवं मिथक",
        "concepts_en": ["Greek Twelve Olympians (Mount Olympus): Zeus (King of Gods, thunderbolt), Hera (Queen, marriage), Poseidon (god of sea and earthquakes, trident), Hades (underworld, not on Olympus), Athena (wisdom and warfare, born from Zeus's head, owl), Apollo (sun, music, archery), Artemis (hunt, moon), Ares (war), Aphrodite (love and beauty, born of sea foam), Hephaestus (blacksmith, fire), Hermes (messenger, winged sandals), Dionysus (wine, theatre)", "Roman Equivalents: Zeus = Jupiter, Hera = Juno, Poseidon = Neptune, Hades = Pluto, Athena = Minerva, Ares = Mars, Aphrodite = Venus, Hermes = Mercury, Artemis = Diana", "Norse Mythology (Scandinavia): Nine Realms connected by world tree Yggdrasil (Asgard, Midgard - human realm, Helheim); Odin (Allfather, ravens Huginn & Muninn, lost an eye for wisdom), Thor (god of thunder, hammer Mjölnir), Loki (trickster god), Valhalla (hall of fallen warriors in Asgard); Ragnarok (apocalyptic twilight of the gods)"],
        "concepts_hi": ["ग्रीक 12 ओलंपियन देवता (माउंट ओलंपस): ज़्यूस (देवताओं का राजा, वज्र), हेरा (विवाह की देवी), पोसीडॉन (समुद्र का देवता, त्रिशूल), हेडीस (पाताल लोक का स्वामी), एथेना (ज्ञान व युद्धनीति की देवी, उल्लू), अपोलो (सूर्य व संगीत), आर्टेमिस (चंद्रमा व शिकार), एरेस (युद्ध), एफ्रोडाइट (प्रेम व सौंदर्य की देवी), हेफेस्टस (लोहार देवता), हर्मीस (दूत देवता), डायोनिसस (मदिरा व रंगमंच)", "रोमन समतुल्य नाम: ज़्यूस = ज्यूपिटर, पोसीडॉन = नेप्च्यून, एरेस = मार्स, एफ्रोडाइट = वीनस, हर्मीस = मर्करी, हेडीस = प्लूटो", "नोर्स पौराणिक कथाएं (स्कैंडिनेविया): 9 लोक और विश्व वृक्ष 'इग्ड्रासिल'; ओडिन (सर्वपिता, ज्ञान हेतु एक आंख दान की), थोर (तड़ित देवता, जादुई हथौड़ा म्योलनिर), लोकी (छली देवता), वालहाला (स्वर्गिक सभागार); रैग्नारोक (देवताओं का प्रलयकारी महायुद्ध)"],
        "q_en": "In classical Norse mythology, which supreme deity is venerated as the 'Allfather', ruler of Asgard, who sacrificed one of his eyes at the well of Mimir to gain cosmic wisdom?",
        "q_hi": "शास्त्रीय नोर्स (स्कैंडिनेवियाई) पौराणिक कथाओं में असगार्ड के अधिपति तथा 'सर्वपिता' (Allfather) के रूप में किस सर्वोच्च देवता को पूजा जाता है, जिन्होंने असीम ज्ञान प्राप्त करने हेतु अपनी एक आंख का बलिदान कर दिया था?",
        "options_en": ["Odin (ओडिन - सर्वपिता)", "Thor", "Loki", "Freyr"],
        "options_hi": ["ओडिन (Odin - Allfather)", "थोर (Thor - वज्र और हथौड़े 'म्योलनिर' का देवता)", "लोकी (Loki - चालबाज और छलिया देवता)", "फ्रेयर (Freyr - उर्वरता का देवता)"],
        "correct_idx": 0,
        "exp_en": "Odin is the chief god of Norse mythology, presiding over Valhalla and Asgard; he sacrificed his eye to drink from the well of wisdom and is accompanied by ravens Huginn (Thought) and Muninn (Memory).",
        "exp_hi": "नोर्स गाथाओं में ओडिन को समस्त देवताओं का राजा और पिता माना जाता है; उन्होंने ज्ञान के कुएं से जल पीने हेतु अपनी एक आंख मीमिर को दान कर दी थी। उनके पुत्र थोर हैं।",
        "cue_en": "Norse Allfather who sacrificed an eye = Odin.",
        "cue_hi": "नोर्स सर्वोच्च देवता (सर्वपिता) = ओडिन।",
        "wrong_en": ["Supreme Norse deity (Allfather).", "Son of Odin, god of thunder wielding Mjölnir.", "Norse shapeshifting trickster god.", "Norse god of prosperity and sunshine."],
        "wrong_hi": ["सर्वोच्च नोर्स देवता (ओडिन)।", "तड़ित देवता (थोर)।", "छलिया देवता (लोकी)।", "समृद्धि का देवता।"]
    }
]

print("Loaded S22 successfully")
