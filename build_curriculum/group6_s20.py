# build_curriculum/group6_s20.py
# S20: Cinema, Theatre & Performing Arts (8 topics across 2 chapters)

DATA = {}

# S20-Ca04b08c0 Origins & Technical Milestones of World & Indian Cinema (3 topics)
DATA["S20-Ca04b08c0"] = [
    {
        "name_en": "Birth of Motion Pictures: Lumiere Brothers, Cinematographe & Silent Film Era",
        "name_hi": "सिनेमा का जन्म: ल्यूमिएर बंधु, सिनेमैटोग्राफ एवं मूक फिल्म (साइलेंट एरा) का विकास",
        "concepts_en": ["Birth of Cinema: Auguste and Louis Lumière patented the Cinématographe (camera and projector combined) and held the first commercial public screening on December 28, 1895 at the Grand Café in Paris ('Workers Leaving the Lumière Factory' and 'The Arrival of a Train at La Ciotat')", "First film screening in India: Lumière brothers screened six short films at Watson's Hotel in Bombay on July 7, 1896 ('Miracle of the Century')", "Georges Méliès: Pioneered science fiction and visual special effects ('A Trip to the Moon', 1902)", "Silent Era Masters: Charlie Chaplin (The Tramp character: 'City Lights', 'Modern Times', 'The Great Dictator'), Buster Keaton (The General), D.W. Griffith"],
        "concepts_hi": ["सिनेमा का जन्म: ऑगस्ट और लुई ल्यूमिएर (Lumière brothers) ने 'सिनेमैटोग्राफ' का आविष्कार किया और 28 दिसंबर 1895 को पेरिस के ग्रैंड कैफे में दुनिया का पहला व्यावसायिक फिल्म प्रदर्शन किया", "भारत में पहली फिल्म स्क्रीनिंग: ल्यूमिएर बंधुओं ने 7 जुलाई 1896 को बॉम्बे के वाटसन होटल में 6 लघु फिल्मों का प्रदर्शन किया (अखबारों ने इसे 'शताब्दी का चमत्कार' कहा)", "जॉर्ज मेलिएस: विज्ञान कथा और सिनेमाई स्पेशल इफेक्ट्स के जनक ('अ ट्रिप टू द मून', 1902)", "मूक युग के महानायक: चार्ली चैपलिन ('द ट्रैम्प' किरदार: 'द किड', 'मॉडर्न टाइम्स', 'द ग्रेट डिक्टेटर'), बस्टर कीटन"],
        "q_en": "On which historic date did Auguste and Louis Lumière host the world's very first commercial public projection of cinematographic motion pictures at the Grand Café in Paris?",
        "q_hi": "ऑगस्ट और लुई ल्यूमिएर बंधुओं ने पेरिस के ग्रैंड कैफे में किस ऐतिहासिक तारीख को दुनिया का पहला व्यावसायिक सार्वजनिक सिनेमा शो प्रदर्शित किया था, जिसे सिनेमा का जन्म माना जाता है?",
        "options_en": ["December 28, 1895 (28 दिसंबर 1895)", "July 7, 1896", "August 15, 1900", "January 1, 1890"],
        "options_hi": ["28 दिसंबर 1895 (December 28, 1895)", "7 जुलाई 1896 (इस दिन भारत/बॉम्बे में पहली स्क्रीनिंग हुई)", "15 अगस्त 1900", "1 जनवरी 1890"],
        "correct_idx": 0,
        "exp_en": "December 28, 1895 is universally marked as the birthdate of cinema, when the Lumière brothers screened 10 short motion picture clips using their Cinématographe to a paying audience in Paris.",
        "exp_hi": "28 दिसंबर 1895 को ल्यूमिएर बंधुओं ने पेरिस में पहली बार टिकट वाले दर्शकों को चलती तस्वीरें दिखाई थीं; इसी दिन को विश्व सिनेमा का जन्मदिवस माना जाता है।",
        "cue_en": "Birth of cinema = December 28, 1895 (Lumière brothers, Paris).",
        "cue_hi": "सिनेमा का जन्म = 28 दिसंबर 1895 (ल्यूमिएर बंधु)।",
        "wrong_en": ["Official birthdate of cinema.", "First screening date in India (Bombay).", "Turn of the century.", "Pre-dates the Cinématographe patent."],
        "wrong_hi": ["सिनेमा का आधिकारिक जन्मदिवस।", "भारत में पहली स्क्रीनिंग (बॉम्बे)।", "गलत तारीख।", "गलत तारीख।"]
    },
    {
        "name_en": "Dawn of Indian Cinema: Dadasaheb Phalke, Raja Harishchandra (1913) & The Silent Era",
        "name_hi": "भारतीय सिनेमा का उदय: दादासाहेब फाल्के, राजा हरिश्चंद्र (1913) एवं मूक फिल्मों का स्वर्णकाल",
        "concepts_en": ["Dundiraj Govind Phalke (Dadasaheb Phalke): Revered as the 'Father of Indian Cinema'", "Raja Harishchandra: Released on May 3, 1913 at Coronation Cinematograph in Bombay; first full-length Indian feature film (silent, 40 minutes, 4 reels); since women were forbidden from acting, female role of Queen Taramati was played by male actor Anna Salunke", "Phalke subsequently made 'Mohini Bhasmasur' (1913, introducing first Indian female actresses Durgabai Kamat and daughter Kamlabai Gokhale), 'Satyavan Savitri', and 'Lanka Dahan' (1917, huge commercial blockbuster)", "Baburao Painter founded Maharashtra Film Company in Kolhapur (1919), introducing realistic sets and movie posters"],
        "concepts_hi": ["धुंडीराज गोविंद फाल्के (दादासाहेब फाल्के): 'भारतीय सिनेमा के जनक' (Father of Indian Cinema)", "राजा हरिश्चंद्र: 3 मई 1913 को बॉम्बे के कोरोनेशन सिनेमा में रिलीज; भारत की पहली पूर्ण-लंबाई वाली मूक फीचर फिल्म (40 मिनट, 4 रील); उस समय महिलाओं के अभिनय पर रोक के कारण रानी तारामती का किरदार एक पुरुष अभिनेता अन्ना सालुंके ने निभाया था", "फाल्के की अन्य फिल्में: 'मोहिनी भस्मासुर' (1913 - पहली महिला अभिनेत्री दुर्गाबाई कामत और उनकी पुत्री कमलाबाई गोखले), 'लंका दहन' (1917 - ऐतिहासिक ब्लॉकबस्टर)", "बाबूराव पेंटर ने 1919 में कोल्हापुर में 'महाराष्ट्र फिल्म कंपनी' स्थापित कर सिनेमा में कलात्मक पोस्टर और यथार्थवादी सेट की शुरुआत की"],
        "q_en": "In Dadasaheb Phalke's landmark 1913 silent film 'Raja Harishchandra' (India's first feature film), who played the female lead role of Queen Taramati due to societal taboos against women acting?",
        "q_hi": "दादासाहेब फाल्के द्वारा निर्देशित भारत की पहली फीचर फिल्म 'राजा हरिश्चंद्र' (1913) में महिलाओं के अभिनय पर सामाजिक निषेध होने के कारण रानी तारामती का मुख्य स्त्री किरदार किसने निभाया था?",
        "options_en": ["Anna Salunke (अन्ना सालुंके - एक पुरुष अभिनेता)", "Durgabai Kamat", "Kamlabai Gokhale", "Zubeida Begum"],
        "options_hi": ["अन्ना सालुंके (Anna Salunke - पुरुष अभिनेता)", "दुर्गाबाई कामत (इन्होंने फाल्के की दूसरी फिल्म 'मोहिनी भस्मासुर' में अभिनय किया)", "कमलाबाई गोखले (बाल कलाकार)", "जुबैदा बेगम (इन्होंने पहली बोलती फिल्म आलम आरा में अभिनय किया)"],
        "correct_idx": 0,
        "exp_en": "Because respectable women were prohibited from acting on screen in 1913, Dadasaheb Phalke cast Anna Salunke, a male cook working at a restaurant, to play Queen Taramati in 'Raja Harishchandra'.",
        "exp_hi": "1913 में महिलाओं के फिल्मों में काम करने को अनुचित माना जाता था, इसलिए दादासाहेब फाल्के ने एक भोजनालय में काम करने वाले युवक 'अन्ना सालुंके' को साड़ी पहनाकर रानी तारामती का किरदार करवाया था।",
        "cue_en": "Queen Taramati in Raja Harishchandra (1913) played by Anna Salunke.",
        "cue_hi": "राजा हरिश्चंद्र (1913) में तारामती का किरदार = अन्ना सालुंके।",
        "wrong_en": ["Male actor who played Queen Taramati.", "First Indian woman to act on screen (in Mohini Bhasmasur).", "First Indian female child star.", "Female lead in the first sound talkie Alam Ara."],
        "wrong_hi": ["तारामती का किरदार निभाने वाले अभिनेता।", "पहली महिला अभिनेत्री (मोहिनी भस्मासुर)।", "पहली बाल अभिनेत्री।", "पहली बोलती फिल्म आलम आरा की नायिका।"]
    },
    {
        "name_en": "Arrival of Sound (Talkies): The Jazz Singer (1927) & Alam Ara (1931 - Ardeshir Irani)",
        "name_hi": "ध्वनि का आगमन (बोलती फिल्में): द जैज़ सिंगर (1927) एवं आलम आरा (1931 - अर्देशिर ईरानी)",
        "concepts_en": ["Global Talkie milestone: 'The Jazz Singer' released on October 6, 1927 by Warner Bros in USA; first feature-length motion picture with synchronized recorded speech and singing (starring Al Jolson: 'You ain't heard nothin' yet!')", "Indian Talkie milestone: 'Alam Ara' (The Light of the World), released on March 14, 1931 at the Majestic Cinema in Bombay; produced and directed by Ardeshir Irani (Imperial Movietone); starred Master Vithal and Zubeida; marketed as 'All Talking, Singing, Dancing'", "First playback song of Indian cinema: 'De De Khuda Ke Naam Pe Pyaare' sung by W.M. Khan in 'Alam Ara' (recorded live on set with hidden microphone)", "First Indian color film: 'Kisan Kanya' (1937), directed by Moti Gidwani and produced by Ardeshir Irani (using Cinecolor process)"],
        "concepts_hi": ["विश्व की पहली बोलती फिल्म: 'द जैज़ सिंगर' (The Jazz Singer), 6 अक्टूबर 1927 को वार्नर ब्रदर्स द्वारा रिलीज; समन्वित ध्वनि और संवाद वाली पहली फिल्म (अल जोल्सन द्वारा अभिनीत)", "भारत की पहली बोलती (सवाक) फिल्म: 'आलम आरा' (Alam Ara), 14 मार्च 1931 को बॉम्बे के मैजेस्टिक सिनेमा में रिलीज; निर्माता-निर्देशक अर्देशिर ईरानी (इंपीरियल मूवीटोन); मुख्य कलाकार मास्टर विट्ठल और जुबैदा", "भारतीय सिनेमा का पहला गाना: 'दे दे खुदा के नाम पे प्यारे ताक़त हो गर देने की', जिसे वजीर मोहम्मद (W.M.) खान ने सेट पर लाइव गाया था", "भारत की पहली स्वदेशी रंगीन (Color) फिल्म: 'किसान कन्या' (1937), निर्माता अर्देशिर ईरानी, निर्देशक मोती गिडवानी"],
        "q_en": "Which historic film, released on March 14, 1931 at Bombay's Majestic Cinema by producer-director Ardeshir Irani, is celebrated as India's very FIRST sound-synchronized talking picture (Talkie)?",
        "q_hi": "14 मार्च 1931 को बॉम्बे के मैजेस्टिक सिनेमा में अर्देशिर ईरानी द्वारा प्रदर्शित वह ऐतिहासिक फिल्म कौन सी है, जो भारत की पहली सवाक (बोलती) फिल्म 'टॉकी' के रूप में विख्यात है?",
        "options_en": ["Alam Ara (आलम आरा - 1931)", "Raja Harishchandra", "Kisan Kanya", "Ayodhyecha Raja"],
        "options_hi": ["आलम आरा (Alam Ara - 1931)", "राजा हरिश्चंद्र (1913 - यह पहली मूक फिल्म थी)", "किसान कन्या (1937 - यह पहली रंगीन फिल्म थी)", "अयोध्याचा राजा (1932 - पहली मराठी बोलती फिल्म)"],
        "correct_idx": 0,
        "exp_en": "'Alam Ara' (1931), directed by Ardeshir Irani, was India's first sound film. It revolutionized Indian cinema with spoken dialogues and 7 songs, ending the silent era.",
        "exp_hi": "अर्देशिर ईरानी द्वारा बनाई गई 'आलम आरा' भारत की पहली बोलती फिल्म थी। इसका प्रदर्शन 14 मार्च 1931 को हुआ था और इसमें सिनेमा का पहला गाना 'दे दे खुदा के नाम पे प्यारे' गाया गया था।",
        "cue_en": "First Indian talkie = Alam Ara (1931, Ardeshir Irani).",
        "cue_hi": "भारत की पहली बोलती फिल्म = आलम आरा (1931, अर्देशिर ईरानी)।",
        "wrong_en": ["India's first sound/talkie film (1931).", "India's first silent feature film (1913).", "India's first indigenously produced color film (1937).", "First Marathi sound film (1932)."],
        "wrong_hi": ["पहली बोलती फिल्म (1931)।", "पहली मूक फिल्म (1913)।", "पहली रंगीन फिल्म (1937)।", "पहली मराठी बोलती फिल्म।"]
    }
]

# S20-C8dd4bb3c National Film Awards, Dadasaheb Phalke & Academy Awards (Oscars) (5 topics)
DATA["S20-C8dd4bb3c"] = [
    {
        "name_en": "Dadasaheb Phalke Award: India's Highest Cinema Honor, Devika Rani & Legendary Recipients",
        "name_hi": "दादासाहेब फाल्के पुरस्कार: भारतीय सिनेमा का सर्वोच्च सम्मान, देविका रानी एवं प्रमुख विजेता",
        "concepts_en": ["Instituted in 1969 by Ministry of Information and Broadcasting to commemorate Dadasaheb Phalke's birth centenary", "India's highest award in the field of cinema, presented annually at the National Film Awards ceremony by the President of India; consists of a Swarna Kamal (Golden Lotus), cash prize of ₹15 lakh (enhanced in 2024), and a shawl", "First recipient (1969): Devika Rani Chaudhuri ('First Lady of Indian Cinema', co-founder of Bombay Talkies studio)", "Other iconic recipients: Satyajit Ray (1984), Raj Kapoor (1987), Lata Mangeshkar (1989), Dilip Kumar (1994), K. Balachander (2010), Amitabh Bachchan (2018), Rajinikanth (2019), Asha Parekh (2020), Waheeda Rehman (2021), Mithun Chakraborty (2022 conferred in 2024)"],
        "concepts_hi": ["सूचना एवं प्रसारण मंत्रालय द्वारा 1969 में दादासाहेब फाल्के के जन्म शताब्दी वर्ष के उपलक्ष्य में स्थापित", "भारतीय सिनेमा के क्षेत्र में देश का सर्वोच्च आधिकारिक सम्मान; राष्ट्रपति द्वारा राष्ट्रीय फिल्म पुरस्कार समारोह में प्रदान किया जाता है; स्वर्ण कमल, ₹15 लाख की नकद राशि (2024 में बढ़ाई गई) और शॉल", "प्रथम प्राप्तकर्ता (1969): देविका रानी चौधुरी ('भारतीय सिनेमा की प्रथम महिला', बॉम्बे टॉकीज की सह-संस्थापक)", "अन्य प्रमुख विजेता: सत्यजीत रे (1984), राज कपूर (1987), लता मंगेशकर (1989), दिलीप कुमार (1994), अमिताभ बच्चन (2018), रजनीकांत (2019), आशा पारेख (2020), वहीदा रहमान (2021), मिथुन चक्रवर्ती (2022 सम्मान, 2024 में प्रदत्त)"],
        "q_en": "Who was conferred the inaugural Dadasaheb Phalke Award in 1969, celebrated in cultural history as the 'First Lady of Indian Cinema'?",
        "q_hi": "1969 में स्थापित पहले दादासाहेब फाल्के पुरस्कार से किसे सम्मानित किया गया था, जिन्हें भारतीय सिनेमा के इतिहास में 'फर्स्ट लेडी ऑफ इंडियन सिनेमा' कहा जाता है?",
        "options_en": ["Devika Rani (देविका रानी चौधुरी - 1969)", "Nargis Dutt", "Lata Mangeshkar", "Kanan Devi"],
        "options_hi": ["देविका रानी (Devika Rani - 1969)", "नरगिस दत्त", "लता मंगेशकर (1989 में प्राप्तकर्ता)", "कानन देवी (1976 में प्राप्तकर्ता)"],
        "correct_idx": 0,
        "exp_en": "Devika Rani, who co-founded the legendary studio Bombay Talkies with Himanshu Rai and starred in classics like 'Achhut Kanya' (1936), was the first-ever recipient of the Dadasaheb Phalke Award in 1969.",
        "exp_hi": "बॉम्बे टॉकीज की सह-संस्थापक और 'अछूत कन्या' की अभिनेत्री देविका रानी को 1969 में भारतीय सिनेमा में उनके आजीवन योगदान के लिए पहला दादासाहेब फाल्के पुरस्कार दिया गया था।",
        "cue_en": "First Dadasaheb Phalke Award (1969) = Devika Rani.",
        "cue_hi": "पहला दादासाहेब फाल्के पुरस्कार (1969) = देविका रानी।",
        "wrong_en": ["Inaugural recipient in 1969.", "First Best Actress National Award winner (1967 for Raat Aur Din).", "Received Phalke Award in 1989.", "Received Phalke Award in 1976."],
        "wrong_hi": ["1969 की प्रथम विजेता।", "पहली सर्वश्रेष्ठ अभिनेत्री राष्ट्रीय पुरस्कार विजेता।", "1989 में पुरस्कार प्राप्त किया।", "1976 में पुरस्कार प्राप्त किया।"]
    },
    {
        "name_en": "National Film Awards: Golden Lotus (Swarna Kamal), Shyamchi Aayi & Feature Film Honours",
        "name_hi": "राष्ट्रीय फिल्म पुरस्कार: स्वर्ण कमल, प्रथम सर्वश्रेष्ठ फीचर फिल्म 'श्यामची आई' एवं प्रमुख श्रेणियां",
        "concepts_en": ["Instituted in 1954 (originally called 'State Awards for Films') by Government of India to honor aesthetic, technical, and cultural excellence in all Indian languages", "First President's Gold Medal for Best Feature Film (1954): Marathi film 'Shyamchi Aayi' (Shyam's Mother), directed by P.K. Atre (Acharya Atre), based on the autobiographical novel by Sane Guruji", "First Silver Medal for Best Hindi Feature Film: Bimal Roy's 'Do Bigha Zamin' (1953)", "Award categories: Swarna Kamal (Best Feature Film, Best Director, Best Debut, Dadasaheb Phalke) and Rajat Kamal (Best Actor, Best Actress, Music, Cinematography)", "First National Film Award for Best Actress: Nargis Dutt in 1967 for 'Raat Aur Din'; Best Actor: Uttam Kumar in 1967 for 'Antony Firingee' and 'Chiriyakhana'"],
        "concepts_hi": ["1954 में भारत सरकार द्वारा 'राजकीय फिल्म पुरस्कार' के रूप में स्थापित, ताकि सभी भारतीय भाषाओं में कलात्मक व सांस्कृतिक उत्कृष्टता को प्रोत्साहित किया जा सके", "सर्वश्रेष्ठ फीचर फिल्म हेतु प्रथम राष्ट्रपति स्वर्ण पदक (1954): मराठी फिल्म 'श्यामची आई' (Shyamchi Aayi), निर्देशक प्रल्हाद केशव (आचार्य) अत्रे, जो साने गुरुजी के आत्मकथात्मक उपन्यास पर आधारित थी", "सर्वश्रेष्ठ हिंदी फिल्म का प्रथम रजत पदक: बिमल रॉय की 'दो बीघा ज़मीन' (1953)", "पुरस्कार श्रेणियां: स्वर्ण कमल (सर्वश्रेष्ठ फिल्म, सर्वश्रेष्ठ निर्देशक) एवं रजत कमल (सर्वश्रेष्ठ अभिनेता, अभिनेत्री, संगीत आदि)", "सर्वश्रेष्ठ अभिनेत्री का पहला पुरस्कार: नरगिस दत्त (1967 में 'रात और दिन' हेतु); सर्वश्रेष्ठ अभिनेता का पहला पुरस्कार: उत्तम कुमार (1967)"],
        "q_en": "Which moving Marathi film directed by Acharya Atre made cinematic history in 1954 by winning the very FIRST President's Gold Medal for Best Feature Film at the National Film Awards?",
        "q_hi": "1954 में आयोजित पहले राष्ट्रीय फिल्म पुरस्कारों में सर्वश्रेष्ठ फीचर फिल्म का पहला राष्ट्रपति स्वर्ण पदक जीतकर इतिहास रचने वाली आचार्य अत्रे द्वारा निर्देशित मराठी फिल्म कौन सी थी?",
        "options_en": ["Shyamchi Aayi (श्यामची आई - 1954)", "Do Bigha Zamin", "Pather Panchali", "Mother India"],
        "options_hi": ["श्यामची आई (Shyamchi Aayi - 1954)", "दो बीघा ज़मीन (Do Bigha Zamin - सर्वश्रेष्ठ हिंदी फिल्म)", "पाथेर पांचाली (Pather Panchali - 1955 में विजेता)", "मदर इंडिया (Mother India - 1957)"],
        "correct_idx": 0,
        "exp_en": "'Shyamchi Aayi' (Shyam's Mother), directed by P.K. Atre based on the autobiography of freedom fighter Sane Guruji, won the inaugural National Film Award for Best Feature Film (President's Gold Medal) in 1954.",
        "exp_hi": "साने गुरुजी के उपन्यास पर आचार्य अत्रे द्वारा निर्देशित मराठी फिल्म 'श्यामची आई' (1953) ने 1954 के पहले राष्ट्रीय फिल्म पुरस्कारों में भारत की सर्वश्रेष्ठ फिल्म का पहला स्वर्ण पदक जीता था।",
        "cue_en": "First National Film Award for Best Feature Film = Shyamchi Aayi (1954, Marathi).",
        "cue_hi": "पहला राष्ट्रीय फिल्म पुरस्कार (सर्वश्रेष्ठ फिल्म) = श्यामची आई (1954, मराठी)।",
        "wrong_en": ["First National Award for Best Feature Film.", "First Silver Medal for Hindi feature film.", "Won Best Feature Film in 1955 (Satyajit Ray).", "All India Certificate of Merit winner (1957)."],
        "wrong_hi": ["प्रथम राष्ट्रीय स्वर्ण पदक विजेता फिल्म।", "पहली सर्वश्रेष्ठ हिंदी फिल्म।", "1955 की विजेता (सत्यजीत रे)।", "1957 की क्लासिक फिल्म।"]
    },
    {
        "name_en": "Satyajit Ray: The Apu Trilogy, Pather Panchali at Cannes & Honorary Lifetime Oscar (1992)",
        "name_hi": "सत्यजीत रे: अपू त्रयी (पाथेर पांचाली, अपराजितो, अपुर संसार), कान्स फिल्म समारोह एवं मानद ऑस्कर (1992)",
        "concepts_en": ["Satyajit Ray (1921-1992): Master filmmaker of world cinema, writer, illustrator, and composer; awarded Bharat Ratna (1992) and Honorary Lifetime Achievement Oscar (Academy Award) in 1992 on his sickbed in Kolkata", "The Apu Trilogy (based on Bibhutibhushan Bandyopadhyay novels): 1. 'Pather Panchali' (Song of the Little Road, 1955 - won 'Best Human Document' at Cannes Film Festival 1956, shot on shoestring budget with Subrata Mitra cinematography and Ravi Shankar sitar score), 2. 'Aparajito' (The Unvanquished, 1956 - won Golden Lion at Venice Film Festival), 3. 'Apur Sansar' (The World of Apu, 1959 - introduced Soumitra Chatterjee and Sharmila Tagore)", "Other masterpieces: Charulata (The Lonely Wife, 1964 - won Silver Bear at Berlin), Nayak, Shatranj Ke Khilari (1977, in Hindi/Urdu starring Sanjeev Kumar, Amjad Khan as Wajid Ali Shah)", "Created beloved detective character Feluda and scientist Professor Shonku in Bengali literature"],
        "concepts_hi": ["सत्यजीत रे (1921-1992): विश्व सिनेमा के महानतम निर्देशकों में से एक; 1992 में भारत का सर्वोच्च नागरिक सम्मान 'भारत रत्न' तथा 1992 में ही ऑस्कर द्वारा लाइफटाइम अचीवमेंट मानद अकादमी पुरस्कार (कोलकाता में अस्पताल के बिस्तर पर प्रदत्त)", "अपू त्रयी (Apu Trilogy - बिभूतिभूषण बंद्योपाध्याय के उपन्यास पर):", "1. 'पाथेर पांचाली' (1955 - 1956 के कान्स फिल्म समारोह में 'बेस्ट ह्यूमन डॉक्यूमेंट' पुरस्कार; संगीत पंडित रविशंकर; अपू और दुर्गा की कथा)", "2. 'अपराजितो' (1956 - वेनिस फिल्म समारोह में सर्वोच्च 'गोल्डन लायन' पुरस्कार जीतने वाली पहली भारतीय फिल्म)", "3. 'अपुर संसार' (1959 - सौमित्र चटर्जी और शर्मिला टैगोर का पदार्पण)", "अन्य कालजयी कृतियां: चारुलता (1964), नायक, जलसाघर, शतरंज के खिलाड़ी (1977 - मुंशी प्रेमचंद की कहानी पर संजीव कुमार और अमजद खान [वाजिद अली शाह])"],
        "q_en": "Which internationally acclaimed film marked the cinematic debut of Satyajit Ray in 1955, winning the prestigious 'Best Human Document' award at the 1956 Cannes Film Festival?",
        "q_hi": "1955 में निर्देशक के रूप में सत्यजीत रे की पहली ही फिल्म कौन सी थी, जिसने 1956 के कान्स फिल्म समारोह में 'बेस्ट ह्यूमन डॉक्यूमेंट' का प्रतिष्ठित वैश्विक पुरस्कार जीतकर भारतीय सिनेमा को विश्व पटल पर स्थापित किया?",
        "options_en": ["Pather Panchali (पाथेर पांचाली - 1955)", "Aparajito", "Apur Sansar", "Charulata"],
        "options_hi": ["पाथेर पांचाली (Pather Panchali - 1955)", "अपराजितो (Aparajito - 1956)", "अपुर संसार (Apur Sansar - 1959)", "चारुलता (Charulata - 1964)"],
        "correct_idx": 0,
        "exp_en": "'Pather Panchali' (1955), the first installment of the Apu Trilogy, made Satyajit Ray a global cinematic icon when it won the 'Best Human Document' award at Cannes in 1956.",
        "exp_hi": "सत्यजीत रे की पहली फिल्म 'पाथेर पांचाली' ने 1956 के कान्स फिल्म फेस्टिवल में 'बेस्ट ह्यूमन डॉक्यूमेंट' का पुरस्कार जीता था, जिससे भारतीय सिनेमा को पहली बार अंतरराष्ट्रीय स्तर पर व्यापक पहचान मिली।",
        "cue_en": "Satyajit Ray debut Cannes award = Pather Panchali (1955).",
        "cue_hi": "सत्यजीत रे की पहली कान्स विजेता फिल्म = पाथेर पांचाली (1955)।",
        "wrong_en": ["Won Best Human Document at Cannes 1956.", "Won Golden Lion at Venice 1957.", "Third film of the Apu trilogy (1959).", "Won Silver Bear at Berlin 1965."],
        "wrong_hi": ["कान्स 1956 की विजेता फिल्म।", "वेनिस 1957 की विजेता।", "अपू त्रयी की तीसरी फिल्म।", "बर्लिन 1965 की विजेता।"]
    },
    {
        "name_en": "Academy Awards (Oscars): Bhanu Athaiya, AR Rahman, Resul Pookutty & Historic Wins for 'Naatu Naatu' and 'The Elephant Whisperers'",
        "name_hi": "अकादमी पुरस्कार (ऑस्कर): भानु अथैया (प्रथम भारतीय विजेता), ए.आर. रहमान, 'नाटू नाटू' एवं 'द एलिफेंट व्हिस्परर्स'",
        "concepts_en": ["Academy of Motion Picture Arts and Sciences (AMPAS): Awards the Oscar statuette since 1929", "First Indian Oscar winner: Bhanu Athaiya won Best Costume Design in 1983 for Richard Attenborough's biopic 'Gandhi'", "Satyajit Ray received Honorary Academy Award for Lifetime Achievement in 1992", "Slumdog Millionaire (81st Oscars, 2009): A.R. Rahman won 2 Oscars (Best Original Score and Best Original Song for 'Jai Ho' with lyricist Gulzar); Resul Pookutty won Best Sound Mixing", "95th Academy Awards (March 2023): Historic double triumph for India: 1. 'Naatu Naatu' from S.S. Rajamouli's 'RRR' won Best Original Song (composed by M.M. Keeravani, lyrics by Chandrabose, first song from an Indian production to win), 2. 'The Elephant Whisperers' directed by Kartiki Gonsalves and produced by Guneet Monga won Best Documentary Short Film"],
        "concepts_hi": ["अकादमी पुरस्कार (ऑस्कर / Oscars): 1929 से प्रतिवर्ष लॉस एंजिल्स में आयोजित विश्व का सबसे प्रतिष्ठित सिनेमाई पुरस्कार", "ऑस्कर जीतने वाले प्रथम भारतीय: भानु अथैया ने 1983 में रिचर्ड एटनबरो की फिल्म 'गांधी' हेतु सर्वश्रेष्ठ कॉस्ट्यूम डिजाइन का ऑस्कर जीता", "सत्यजीत रे को 1992 में लाइफटाइम अचीवमेंट हेतु मानद ऑस्कर प्रदान किया गया", "स्लमडॉग मिलेनियर (2009): संगीतकार ए.आर. रहमान ने दो ऑस्कर (सर्वश्रेष्ठ मूल स्कोर एवं 'जय हो' गीत हेतु गुलजार के साथ) जीते; रसूल पूकुट्टी ने सर्वश्रेष्ठ साउंड मिक्सिंग का ऑस्कर जीता", "95वें ऑस्कर पुरस्कार (मार्च 2023): भारत की ऐतिहासिक दोहरी विजय: 1. एस.एस. राजामौली की फिल्म 'RRR' के ऊर्जावान गीत 'नाटू नाटू' ने सर्वश्रेष्ठ मूल गीत का ऑस्कर जीता (संगीत: एम.एम. कीरावानी, गीतकार: चंद्रबोस); 2. कार्तिकी गोंजाल्विस व गुनीत मोंगा की 'द एलिफेंट व्हिस्परर्स' ने सर्वश्रेष्ठ डॉक्यूमेंट्री शॉर्ट फिल्म का ऑस्कर जीता"],
        "q_en": "Who holds the monumental distinction of being the very FIRST Indian to win an Academy Award (Oscar), winning Best Costume Design in 1983 for the biographical epic 'Gandhi'?",
        "q_hi": "1983 में रिचर्ड एटनबरो की जीवनी फिल्म 'गांधी' के लिए सर्वश्रेष्ठ कॉस्ट्यूम डिजाइन का पुरस्कार जीतकर ऑस्कर (अकादमी पुरस्कार) जीतने वाले प्रथम भारतीय बनने का गौरव किसे प्राप्त है?",
        "options_en": ["Bhanu Athaiya (भानु अथैया - 1983)", "Satyajit Ray", "A.R. Rahman", "Resul Pookutty"],
        "options_hi": ["भानु अथैया (Bhanu Athaiya - 1983)", "सत्यजीत रे (1992 में मानद ऑस्कर)", "ए.आर. रहमान (2009 में ऑस्कर विजेता)", "रसूल पूकुट्टी (2009 में साउंड मिक्सिंग ऑस्कर)"],
        "correct_idx": 0,
        "exp_en": "Costume designer Bhanu Athaiya became the first Indian Oscar laureate at the 55th Academy Awards in 1983, sharing the Best Costume Design Oscar with John Mollo for 'Gandhi'.",
        "exp_hi": "भानु अथैया ने 1983 में फिल्म 'गांधी' में प्रामाणिक भारतीय परिधानों की डिजाइन के लिए जॉन मोलो के साथ संयुक्त रूप से ऑस्कर जीता था, जिससे वे ऑस्कर जीतने वाली पहली भारतीय बनीं।",
        "cue_en": "First Indian Oscar winner = Bhanu Athaiya (1983, Gandhi).",
        "cue_hi": "प्रथम भारतीय ऑस्कर विजेता = भानु अथैया (1983, गांधी)।",
        "wrong_en": ["First Indian Oscar laureate in 1983.", "Won Lifetime Achievement Oscar in 1992.", "Won two Oscars in 2009 for Slumdog Millionaire.", "Won Sound Mixing Oscar in 2009."],
        "wrong_hi": ["1983 में प्रथम भारतीय विजेता।", "1992 में मानद ऑस्कर विजेता।", "2009 में दो ऑस्कर विजेता।", "2009 में साउंड ऑस्कर विजेता।"]
    },
    {
        "name_en": "Indian Submissions to Academy Awards: Mother India (1957), Salaam Bombay! & Lagaan (Top 5 Nominations)",
        "name_hi": "ऑस्कर में भारत की आधिकारिक प्रविष्टियां: मदर इंडिया (1957), सलाम बॉम्बे! एवं लगान (अंतिम 5 नामांकन)",
        "concepts_en": ["Best International Feature Film (formerly Best Foreign Language Film): Film Federation of India (FFI) selects India's official annual submission", "Only THREE Indian films have ever achieved the final nomination (Top 5) in Oscar history:", "1. 'Mother India' (1957): Directed by Mehboob Khan, starring Nargis as Radha, Sunil Dutt, and Rajendra Kumar; lost by a single vote to Federico Fellini's Italian masterpiece 'Nights of Cabiria'", "2. 'Salaam Bombay!' (1988): Directed by Mira Nair, depicting street children of Mumbai (Shafiq Syed as Chaipau); lost to Denmark's 'Pelle the Conqueror'", "3. 'Lagaan' (2001): Directed by Ashutosh Gowariker, starring Aamir Khan as Bhuvan; colonial cricket match for tax abolition; lost to Bosnia's 'No Man's Land'"],
        "concepts_hi": ["सर्वश्रेष्ठ अंतर्राष्ट्रीय फीचर फिल्म (पूर्व नाम: सर्वश्रेष्ठ विदेशी भाषा फिल्म): फिल्म फेडरेशन ऑफ इंडिया (FFI) द्वारा भारत की आधिकारिक प्रविष्टि का चयन", "ऑस्कर के 95+ वर्षों के इतिहास में केवल तीन (3) भारतीय फिल्में अंतिम 5 नामांकनों (Top 5 Nominees) में जगह बनाने में सफल रही हैं:", "1. 'मदर इंडिया' (Mother India, 1957): निर्देशक महबूब खान; नरगिस (राधा), सुनील दत्त (बिरजू), राजेंद्र कुमार; यह ऑस्कर में नामांकित होने वाली पहली भारतीय फिल्म थी (मात्र 1 वोट से इटली की फिल्म से हारी)", "2. 'सलाम बॉम्बे!' (Salaam Bombay!, 1988): निर्देशक मीरा नायर; मुंबई के बाल मजदूरों व बेसहारा बच्चों का यथार्थवादी चित्रण", "3. 'लगान' (Lagaan, 2001): निर्देशक आशुतोष गोवारिकर; आमिर खान (भुवन); लगान माफी हेतु अंग्रेजों के विरुद्ध क्रिकेट मैच; बोस्निया की 'नो मैन्स लैंड' से हारी"],
        "q_en": "Which 1957 cinematic masterpiece directed by Mehboob Khan and starring Nargis made history as India's very FIRST film nominated for the Academy Award (Oscar) for Best Foreign Language Film?",
        "q_hi": "महबूब खान द्वारा निर्देशित तथा नरगिस द्वारा अभिनीत 1957 की वह कालजयी फिल्म कौन सी थी, जिसने सर्वश्रेष्ठ विदेशी भाषा फिल्म श्रेणी में ऑस्कर (Academy Award) के अंतिम 5 में नामांकित होने वाली भारत की पहली फिल्म बनने का गौरव प्राप्त किया?",
        "options_en": ["Mother India (मदर इंडिया - 1957)", "Salaam Bombay!", "Lagaan", "Pather Panchali"],
        "options_hi": ["मदर इंडिया (Mother India - 1957)", "सलाम बॉम्बे! (Salaam Bombay! - 1988 में दूसरी नामांकित)", "लगान (Lagaan - 2001 में तीसरी नामांकित)", "पाथेर पांचाली (Pather Panchali)"],
        "correct_idx": 0,
        "exp_en": "Mehboob Khan's epic 'Mother India' (1957), a remake of his 1940 film 'Aurat', was India's first official submission to reach the final five Oscar nominations, narrowly missing the award by just one vote.",
        "exp_hi": "महबूब खान की फिल्म 'मदर इंडिया' (1957) ऑस्कर के अंतिम 5 में नामांकित होने वाली भारत की पहली फिल्म थी। बाद में केवल 'सलाम बॉम्बे' (1988) और 'लगान' (2001) ही यह मुकाम हासिल कर सकीं।",
        "cue_en": "First Indian film nominated for Oscar = Mother India (1957).",
        "cue_hi": "ऑस्कर में नामांकित पहली भारतीय फिल्म = मदर इंडिया (1957)।",
        "wrong_en": ["First Indian Oscar nominee (1957).", "Second Indian Oscar nominee (1988).", "Third Indian Oscar nominee (2001).", "Not officially nominated in Foreign Language category."],
        "wrong_hi": ["पहली नामांकित फिल्म (1957)।", "दूसरी नामांकित फिल्म (1988)।", "तीसरी नामांकित फिल्म (2001)।", "ऑस्कर में नामांकित नहीं।"]
    }
]

print("Loaded S20 successfully")
