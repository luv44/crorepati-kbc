# build_curriculum/group6_s18.py
# S18: World & Indian Literature (9 topics across 3 chapters)

DATA = {}

# S18-C2b02f8ee Ancient Sanskrit Classics, Epics & Dramas (Kalidasa, Bhasa) (3 topics)
DATA["S18-C2b02f8ee"] = [
    {
        "name_en": "Epics of Ancient India: Valmiki Ramayana, Vyasa Mahabharata & Bhagavad Gita Philosophy",
        "name_hi": "प्राचीन भारतीय महाकाव्य: वाल्मीकि रामायण, वेदव्यास कृत महाभारत एवं श्रीमद्भगवद्गीता दर्शन",
        "concepts_en": ["Valmiki Ramayana (Adi Kavya): First metrical Sanskrit poem in Anushtubh meter; 24,000 verses across 7 Kandas (Bala, Ayodhya, Aranya, Kishkindha, Sundara, Yuddha, Uttara)", "Vyasa's Mahabharata (Itihasa): World's longest epic poem (~100,000 shlokas, 'Shatasahasri Samhita'); evolved through Jaya (8,800 verses) -> Bharata (24,000 verses) -> Mahabharata across 18 Parvas", "Bhagavad Gita: Embedded in Bhishma Parva of Mahabharata (Chapters 23 to 40, 700 verses across 18 chapters); dialogue between Lord Krishna and Arjuna on the battlefield of Kurukshetra", "Core philosophies of Gita: Nishkama Karma (selfless action without attachment to fruits: 'Karmanye vadikaraste ma phaleshu kadachana'), Jnana Yoga, Bhakti Yoga, and Svadharma"],
        "concepts_hi": ["वाल्मीकि रामायण (आदि काव्य): अनुष्टुप छंद में रचित प्रथम महाकाव्य; 24,000 श्लोक, 7 कांड (बाल, अयोध्या, अरण्य, किष्किंधा, सुंदर, युद्ध एवं उत्तर कांड)", "वेदव्यास कृत महाभारत: विश्व का सबसे बड़ा महाकाव्य ग्रंथ (~1 लाख श्लोक, 'शतसाहस्री संहिता'); तीन चरणों में विकास: जय (8,800 श्लोक) -> भारत (24,000 श्लोक) -> महाभारत (18 पर्व)", "श्रीमद्भगवद्गीता: महाभारत के 'भीष्म पर्व' का अंश (18 अध्याय, 700 श्लोक); कुरुक्षेत्र के युद्धक्षेत्र में श्रीकृष्ण और अर्जुन का दार्शनिक संवाद", "गीता का मूल संदेश: निष्काम कर्मयोग ('कर्मण्येवाधिकारस्ते मा फलेषु कदाचन' - फल की चिंता किए बिना कर्तव्य पालन), ज्ञानयोग और भक्तियोग"],
        "q_en": "In which specific Parva (book/section) of the epic Mahabharata is the philosophical scripture 'Bhagavad Gita' embedded as a dialogue between Krishna and Arjuna?",
        "q_hi": "महाभारत महाकाव्य के किस विशिष्ट 'पर्व' में कुरुक्षेत्र युद्ध के समय श्रीकृष्ण और अर्जुन के बीच हुए संवाद के रूप में 'श्रीमद्भगवद्गीता' समाहित है?",
        "options_en": ["Bhishma Parva (भीष्म पर्व)", "Drona Parva", "Shanti Parva", "Vana Parva"],
        "options_hi": ["भीष्म पर्व (Bhishma Parva)", "द्रोण पर्व (Drona Parva)", "शांति पर्व (Shanti Parva - यह सबसे बड़ा पर्व है)", "वन पर्व (Vana Parva)"],
        "correct_idx": 0,
        "exp_en": "The Bhagavad Gita comprises chapters 23 to 40 of the Bhishma Parva (the 6th book of the Mahabharata), narrated right before the commencement of the great Kurukshetra war.",
        "exp_hi": "श्रीमद्भगवद्गीता महाभारत के छठे पर्व 'भीष्म पर्व' के 23वें से 40वें अध्याय के रूप में संकलित है, जिसमें भगवान कृष्ण ने विषादग्रस्त अर्जुन को निष्काम कर्मयोग का उपदेश दिया था।",
        "cue_en": "Bhagavad Gita is part of Bhishma Parva of Mahabharata.",
        "cue_hi": "भगवद्गीता = महाभारत का भीष्म पर्व।",
        "wrong_en": ["Section containing the Bhagavad Gita.", "War section under Drona's command.", "Post-war philosophical section on statecraft.", "Section covering the forest exile."],
        "wrong_hi": ["गीता का सही पर्व।", "द्रोणाचार्य का युद्ध पर्व।", "राजधर्म उपदेश वाला पर्व।", "पांडवों के वनवास का पर्व।"]
    },
    {
        "name_en": "Kalidasa's Masterpieces: Shakuntalam, Meghaduta, Raghuvamsham & Kumarasambhavam",
        "name_hi": "महाकवि कालिदास की कालजयी रचनाएं: अभिज्ञानशाकुंतलम्, मेघदूतम्, रघुवंशम् एवं कुमारसंभवम्",
        "concepts_en": ["Mahakavi Kalidasa ('Shakespeare of India'): Court poet of Gupta King Chandragupta II Vikramaditya; master of Upama (simile: 'Upama Kalidasasya')", "7 Canonized Works: Two Mahakavyas (Raghuvamsham - dynasty of Sun kings; Kumarasambhavam - birth of war god Kartikeya/Kumara to Shiva and Parvati)", "Two Khandakavyas / Lyric poems: Meghaduta (Cloud Messenger - Yaksha exiled to Ramagiri sends cloud to his beloved in Alaka, Mandakranta meter) and Ritusamhara (Six seasons)", "Three Natakas / Dramas: Abhijnanashakuntalam (masterpiece drama translated to German by Goethe, love of King Dushyanta and Shakuntala, ring of recognition), Malavikagnimitram (love of Shunga King Agnimitra and Malavika), and Vikramorvashiyam (King Pururavas and Apsara Urvashi)"],
        "concepts_hi": ["महाकवि कालिदास: गुप्त सम्राट चंद्रगुप्त द्वितीय 'विक्रमादित्य' के नवरत्नों में प्रमुख; उपमा अलंकार के अद्वितीय सम्राट ('उपमा कालिदासस्य')", "कालिदास की 7 प्रामाणिक रचनाएं:", "दो महाकाव्य: रघुवंशम् (रघु कुल के 29 प्रतापी राजाओं का वर्णन) एवं कुमारसंभवम् (शिव-पार्वती विवाह एवं कार्तिकेय जन्म)", "दो खंडकाव्य: मेघदूतम् (यक्ष द्वारा रामगिरि से अलकापुरी में अपनी प्रेयसी को मेघ के माध्यम से संदेश भेजना, मंदाक्रांता छंद) एवं ऋतुसंहारम् (छह ऋतुओं का वर्णन)", "तीन नाटक: अभिज्ञानशाकुंतलम् (राजा दुष्यंत व शकुंतला की प्रेम कथा; जर्मन विद्वान गेटे द्वारा अत्यधिक प्रशंसित), मालविकाग्निमित्रम् (शुंग राजा अग्निमित्र), विक्रमोर्वशीयम् (पुरूरवा व उर्वशी)"],
        "q_en": "Which famous lyric poem (Khandakavya) by Kalidasa narrates the poignant longing of an exiled Yaksha who dispatches a rain-bearing monsoon cloud as his messenger to his beloved wife in Alaka?",
        "q_hi": "महाकवि कालिदास द्वारा मंदाक्रांता छंद में रचित वह प्रसिद्ध खंडकाव्य कौन सा है, जिसमें रामगिरि पर्वत पर निर्वासित एक विरही यक्ष मेघ (बादल) को दूत बनाकर अलकापुरी में अपनी प्रेमिका के पास भेजता है?",
        "options_en": ["Meghaduta (मेघदूतम् / Cloud Messenger)", "Ritusamhara", "Kumarasambhavam", "Raghuvamsham"],
        "options_hi": ["मेघदूतम् (Meghaduta)", "ऋतुसंहारम् (Ritusamhara)", "कुमारसंभवम् (Kumarasambhavam)", "रघुवंशम् (Raghuvamsham)"],
        "correct_idx": 0,
        "exp_en": "Kalidasa's 'Meghaduta' (The Cloud Messenger) is a lyrical masterpiece consisting of 111 stanzas where an exiled Yaksha instructs a monsoon cloud on the geographic route from Central India to the Himalayan city of Alakapuri.",
        "exp_hi": "'मेघदूतम्' कालिदास का विश्वविख्यात गीतिकाव्य है जिसमें कुबेर द्वारा निष्कासित यक्ष वर्षा ऋतु के पहले मेघ को संदेशवाहक बनाकर हिमालय की अलकापुरी भेजता है।",
        "cue_en": "Cloud messenger poem = Meghaduta by Kalidasa.",
        "cue_hi": "मेघ को दूत बनाने वाला काव्य = मेघदूतम् (कालिदास)।",
        "wrong_en": ["Lyrical poem of cloud messenger.", "Poetic description of six Indian seasons.", "Epic on birth of Kartikeya.", "Epic chronicling the Ikshvaku/Raghu dynasty."],
        "wrong_hi": ["कालिदास का मेघदूतम्।", "छह ऋतुओं का वर्णन।", "कुमारसंभवम् महाकाव्य।", "रघुवंश महाकाव्य।"]
    },
    {
        "name_en": "Classical Sanskrit Playwrights: Bhasa (Svapnavasavadattam), Sudraka (Mrichhakatika) & Vishakhadatta (Mudrarakshasa)",
        "name_hi": "शास्त्रीय संस्कृत नाटककार: भास (स्वप्नवासवदत्तम्), शूद्रक (मृच्छकटिकम्) एवं विशाखदत्त (मुद्राराक्षस)",
        "concepts_en": ["Bhasa: Pre-Kalidasa dramatist discovered by T. Ganapati Sastri in Kerala (13 plays / Nataka-Chakra); famous play Svapnavasavadattam (The Dream of Vasavadatta - King Udayana and Queen Vasavadatta)", "Sudraka: Wrote Mrichhakatika ('The Little Clay Cart') - unique Prakarana realistic social drama set in Ujjayini depicting love between impoverished noble merchant Charudatta and virtuous courtesan Vasantasena, with political rebellion by Aryaka", "Vishakhadatta: Wrote Mudrarakshasa ('The Signet Ring of Rakshasa') - pure political espionage drama without female lead, depicting Chanakya's political scheming to win over Rakshasa, the loyal minister of defeated Nanda dynasty, for Chandragupta Maurya; also wrote Devichandraguptam", "Bhavabhuti: 8th century dramatist; Uttararamacharita (poignant depiction of Karuna rasa in later life of Rama and Sita) and Malatimadhava"],
        "concepts_hi": ["भास: कालिदास से पूर्ववर्ती नाटककार (टी. गणपति शास्त्री द्वारा 1912 में खोजे गए 13 नाटक); प्रसिद्ध नाटक 'स्वप्नवासवदत्तम्' (राजा उदयन और महारानी वासवदत्ता)", "शूद्रक: 'मृच्छकटिकम्' (मिट्टी की गाड़ी) के रचयिता - उज्जैन की पृष्ठभूमि पर आधारित यथार्थवादी सामाजिक नाटक जिसमें निर्धन ब्राह्मण व्यापारी चारुदत्त और गणिका वसंतसेना का प्रेम प्रसंग है", "विशाखदत्त: 'मुद्राराक्षस' के रचयिता - संस्कृत का एकमात्र शुद्ध राजनीतिक जासूसी नाटक (बिना किसी नायिका या विदूषक के), जिसमें चाणक्य द्वारा नंद वंश के निष्ठावान मंत्री राक्षस को चंद्रगुप्त मौर्य के पक्ष में लाने की कूटनीति का वर्णन है", "भवभूति: 8वीं सदी के महान नाटककार; 'उत्तररामचरितम्' (करुण रस की पराकाष्ठा, राम और सीता का विछोह)"],
        "q_en": "Which unique classical Sanskrit drama, written by Vishakhadatta, depicts the intricate political stratagems of Chanakya to win over Minister Rakshasa for Emperor Chandragupta Maurya without including any romance or female lead?",
        "q_hi": "विशाखदत्त द्वारा रचित वह अद्वितीय शास्त्रीय संस्कृत नाटक कौन सा है, जिसमें किसी प्रेम प्रसंग या नायिका के बिना, केवल चाणक्य की कूटनीतिक चालों द्वारा नंद वंश के मंत्री राक्षस को चंद्रगुप्त मौर्य का मंत्री बनाने का वर्णन है?",
        "options_en": ["Mudrarakshasa (मुद्राराक्षस)", "Mrichhakatika", "Svapnavasavadattam", "Uttararamacharita"],
        "options_hi": ["मुद्राराक्षस (Mudrarakshasa)", "मृच्छकटिकम् (Mrichhakatika - शूद्रक कृत)", "स्वप्नवासवदत्तम् (Svapnavasavadattam - भास कृत)", "उत्तररामचरितम् (भवभूति कृत)"],
        "correct_idx": 0,
        "exp_en": "'Mudrarakshasa' by Vishakhadatta is a political thriller devoid of romantic subplots, focusing entirely on statecraft, espionage, and Chanakya's psychological maneuvering.",
        "exp_hi": "विशाखदत्त कृत 'मुद्राराक्षस' संस्कृत साहित्य का अनूठा कूटनीतिक नाटक है, जिसमें कौटिल्य (चाणक्य) अपनी गुप्तचर प्रणाली और बौद्धिक चालों से नंद वंश के निष्ठावान मंत्री राक्षस को चंद्रगुप्त के सामने आत्मसमर्पण कराता है।",
        "cue_en": "Chanakya's political espionage drama = Mudrarakshasa by Vishakhadatta.",
        "cue_hi": "चाणक्य की कूटनीति पर नाटक = मुद्राराक्षस (विशाखदत्त)।",
        "wrong_en": ["Political espionage play by Vishakhadatta.", "Realistic comedy/drama by Sudraka.", "Dream drama by Bhasa.", "Tragedy of later Rama by Bhavabhuti."],
        "wrong_hi": ["विशाखदत्त का राजनीतिक नाटक।", "शूद्रक का सामाजिक नाटक।", "भास का नाटक।", "भवभूति का करुण नाटक।"]
    }
]

# S18-Cd793f594 Modern Indian Literature: Tagore, Premchand & Regional Maestros (2 topics)
DATA["S18-Cd793f594"] = [
    {
        "name_en": "Rabindranath Tagore: Gitanjali (Nobel Prize 1913), Visva-Bharati & National Anthems",
        "name_hi": "रवींद्रनाथ टैगोर: गीतांजलि (नोबेल पुरस्कार 1913), विश्वभारती एवं राष्ट्रगान रचना",
        "concepts_en": ["Gurudev Rabindranath Tagore (1861-1941): First non-European and first Asian to win the Nobel Prize in Literature in 1913 for his poetry collection 'Gitanjali' (Song Offerings, English translation prefaced by W.B. Yeats)", "Composed National Anthems of two sovereign nations: India ('Jana Gana Mana' from poem Bharoto Bhagyo Bidhata) and Bangladesh ('Amar Shonar Bangla'); inspired Sri Lanka's anthem ('Sri Lanka Matha')", "Founded Visva-Bharati University at Santiniketan (1921), declared UNESCO World Heritage Site in 2023", "Famous novels and stories: Gora, Ghare Baire (The Home and the World), Chokher Bali, Kabuliwala, The Postmaster; renounced British Knighthood in 1919 protesting Jallianwala Bagh massacre"],
        "concepts_hi": ["गुरुदेव रवींद्रनाथ टैगोर (1861-1941): 1913 में अपनी काव्य कृति 'गीतांजलि' (Gitanjali) के लिए साहित्य का नोबेल पुरस्कार प्राप्त करने वाले प्रथम एशियाई एवं गैर-यूरोपीय विभूति (अंग्रेजी संस्करण की भूमिका डब्ल्यू.बी. येट्स ने लिखी)", "विश्व के एकमात्र कवि जिन्होंने दो संप्रभु राष्ट्रों के राष्ट्रगान रचे: भारत ('जन गण मन') एवं बांग्लादेश ('आमार सोनार बाsecret/बांग्ला'); श्रीलंका के राष्ट्रगान को भी प्रेरित किया", "1921 में शांतिनिकेतन में 'विश्वभारती विश्वविद्यालय' की स्थापना (2023 में यूनेस्को विश्व धरोहर घोषित)", "प्रमुख उपन्यास व कहानियां: गोरा, घरे-बाईरे (घर और बाहर), चोखेर बाली, काबुलीवाला, पोस्टमास्टर; 1919 में जलियांवाला बाग हत्याकांड के विरोध में ब्रिटिश 'नाइटहुड' उपाधि लौटा दी"],
        "q_en": "For which immortal lyrical poetry collection was Gurudev Rabindranath Tagore awarded the prestigious Nobel Prize in Literature in 1913, becoming the first Asian laureate?",
        "q_hi": "किस कालजयी काव्य संग्रह के लिए गुरुदेव रवींद्रनाथ टैगोर को 1913 में साहित्य का नोबेल पुरस्कार प्रदान किया गया, जिससे वे यह सम्मान पाने वाले प्रथम एशियाई बने?",
        "options_en": ["Gitanjali (गीतांजलि - Song Offerings)", "Gora", "Ghare Baire", "Chokher Bali"],
        "options_hi": ["गीतांजलि (Gitanjali)", "गोरा (Gora - यह उनका प्रसिद्ध उपन्यास है)", "घरे-बाईरे (The Home and the World)", "चोखेर बाली (Chokher Bali)"],
        "correct_idx": 0,
        "exp_en": "Rabindranath Tagore won the Nobel Prize in Literature in 1913 'because of his profoundly sensitive, fresh and beautiful verse' in 'Gitanjali' (Song Offerings).",
        "exp_hi": "रवींद्रनाथ टैगोर को 1913 में उनकी 157 गीतों के संकलन 'गीतांजलि' के अंग्रेजी अनुवाद के लिए साहित्य के नोबेल पुरस्कार से सम्मानित किया गया था।",
        "cue_en": "Tagore Nobel Prize 1913 = Gitanjali.",
        "cue_hi": "टैगोर को नोबेल पुरस्कार (1913) = गीतांजलि।",
        "wrong_en": ["Nobel-winning poetry collection.", "Tagore's major philosophical novel.", "Tagore's novel on Swadeshi movement.", "Tagore's psychological novel."],
        "wrong_hi": ["नोबेल विजेता काव्य संकलन।", "टैगोर का महाकाव्यात्मक उपन्यास।", "स्वदेशी आंदोलन पर उपन्यास।", "टैगोर का मनोवैज्ञानिक उपन्यास।"]
    },
    {
        "name_en": "Munshi Premchand: Realism in Hindi Literature, Godan, Kafan & Social Reformation",
        "name_hi": "मुंशी प्रेमचंद: हिंदी साहित्य में यथार्थवाद, गोदान, कफन, पंच परमेश्वर एवं सामाजिक सुधार",
        "concepts_en": ["Munshi Premchand (Dhanpat Rai Shrivastava, 1880-1936): Revered as 'Upanyas Samrat' (Emperor of Novels) and 'Katha Samrat'; pioneered critical social realism in Hindi and Urdu literature (wrote under pen-name 'Nawab Rai' initially)", "Masterpiece novel 'Godan' (The Gift of a Cow, 1936): Epic tragedy of Indian peasant life depicted through farmer Hori, his wife Dhania, and cow Punia, exposing feudal exploitation, caste hegemony, rural debt, and colonial bureaucracy", "Other monumental novels: Gaban (ornaments and embezzlement), Sevasadan (prostitution reform), Karmabhumi, Rangbhumi, Nirmala (dowry and mismatched marriage), Pratigya", "Legendary short stories (collected in 8 volumes of Mansarovar): Kafan (stark realism of Ghisu and Madhav), Poos ki Raat (Halku and dog Jabra), Panch Parmeshwar, Idgah (young Hamid's chimta for grandmother Amina), Namak Ka Daroga, Shatranj Ke Khilari"],
        "concepts_hi": ["मुंशी प्रेमचंद (धनपत राय श्रीवास्तव, 1880-1936): 'उपन्यास सम्राट' एवं 'कथा सम्राट'; हिंदी व उर्दू साहित्य में आदर्शोन्मुख यथार्थवाद के प्रवर्तक (प्रारंभ में 'नवाब राय' नाम से लिखा; प्रथम उर्दू संग्रह 'सोज़े-वतन' अंग्रेजों ने जब्त किया)", "कालजयी महाकाव्यात्मक उपन्यास 'गोदान' (1936): भारतीय कृषक जीवन की त्रासदी; मुख्य पात्र होरी महतो, धनिया, गोबर और गाय पुनिया के माध्यम से महाजनी शोषण, जातिवाद व गरीबी का सजीव चित्रण", "अन्य अमर उपन्यास: गबन (आभूषणों की लालसा), सेवासदन, रंगभूमि, कर्मभूमि, निर्मला (अनमेल विवाह व दहेज प्रथा)", "अमर कहानियां ('मानसरोवर' के 8 खंड): कफन (घीसू और माधव की संवेदनहीनता), पूस की रात (हलकू और कुत्ता जबरा), पंच परमेश्वर (अलगू चौधरी व जुम्मन शेख), ईदगाह (हामिद का चिमटा), नमक का दारोगा, शतरंज के खिलाड़ी"],
        "q_en": "Which monumental novel by Munshi Premchand, published in 1936, is celebrated as the epic tragedy of the Indian peasantry through the poignant life and demise of the impoverished farmer Hori?",
        "q_hi": "मुंशी प्रेमचंद द्वारा 1936 में रचित वह कालजयी महाकाव्यात्मक उपन्यास कौन सा है, जिसे निर्धन किसान होरी के जीवन संघर्ष और महाजनी शोषण के माध्यम से 'भारतीय कृषक जीवन का महाकाव्य' कहा जाता है?",
        "options_en": ["Godan (गोदान - 1936)", "Gaban", "Nirmala", "Rangbhumi"],
        "options_hi": ["गोदान (Godan - 1936)", "गबन (Gaban - आभूषण प्रेम की कथा)", "निर्मला (Nirmala - अनमेल विवाह की व्यथा)", "रंगभूमि (Rangbhumi - सूरदास का संघर्ष)"],
        "correct_idx": 0,
        "exp_en": "'Godan' (The Gift of a Cow), completed just before Premchand's death in 1936, is widely acclaimed as the greatest novel in modern Hindi literature, depicting the socio-economic strangulation of rural peasantry.",
        "exp_hi": "'गोदान' मुंशी प्रेमचंद का अंतिम और सर्वोत्कृष्ट उपन्यास है; इसमें किसान होरी की गाय रखने की अंतिम अभिलाषा और महाजनों के कर्ज चक्र में उसके पिसने का हृदयविदारक चित्रण है।",
        "cue_en": "Indian peasant epic = Godan by Munshi Premchand (1936).",
        "cue_hi": "कृषक जीवन का महाकाव्य = गोदान (मुंशी प्रेमचंद, 1936)।",
        "wrong_en": ["Premchand's peasant epic masterpiece.", "Novel on middle-class greed for jewelry.", "Novel criticizing dowry and child marriage.", "Novel featuring blind hero Surdas."],
        "wrong_hi": ["प्रेमचंद का महाकाव्यात्मक उपन्यास।", "गबन उपन्यास।", "निर्मला उपन्यास।", "रंगभूमि उपन्यास।"]
    }
]

# S18-C19aab9fd World Literary Masterpieces & Nobel Laureates in Literature (4 topics)
DATA["S18-C19aab9fd"] = [
    {
        "name_en": "William Shakespeare: Four Great Tragedies (Hamlet, Macbeth, Othello, King Lear) & Sonnets",
        "name_hi": "विलियम शेक्सपियर: चार महान त्रासदियां (हैमलेट, मैकबेथ, ओथेलो, किंग लियर) एवं सॉनेट्स",
        "concepts_en": ["William Shakespeare (1564-1616, 'Bard of Avon'): English Renaissance playwright and poet; wrote 38 plays, 154 sonnets (Shakespearean sonnet form: 3 quatrains + 1 rhyming couplet, ABAB CDCD EFEF GG in iambic pentameter)", "Four Great Tragedies: 1. Hamlet (Prince of Denmark, tragic flaw of procrastination / indecisiveness: 'To be, or not to be', ghost of father, Ophelia)", "2. Macbeth (Tragic flaw of vaulting ambition, Scottish general, Three Witches, Lady Macbeth: 'Out, damned spot')", "3. Othello (Tragic flaw of jealousy stirred by treacherous ancient Iago, Moor of Venice, Desdemona and handkerchief)", "4. King Lear (Tragic flaw of vanity and blindness to flattery, dividing kingdom among daughters Goneril, Regan, Cordelia)"],
        "concepts_hi": ["विलियम शेक्सपियर (1564-1616, 'बार्ड ऑफ एवन'): अंग्रेजी पुनर्जागरण के अमर नाटककार व कवि; 38 नाटक एवं 154 सॉनेट्स (शेक्सपीयरियन सॉनेट: 14 पंक्तियां, ABAB CDCD EFEF GG तुकबंदी)", "चार महान कालजयी त्रासदियां (Four Great Tragedies):", "1. हैमलेट (Hamlet): डेनमार्क का राजकुमार, अनिर्णय की स्थिति ('To be, or not to be' - होना या न होना); ओफीलिया", "2. मैकबेथ (Macbeth): बेलगाम महत्वाकांक्षा की त्रासदी; स्कॉटिश सेनापति, तीन डायनें, लेडी मैकबेथ ('Out, damned spot!')", "3. ओथेलो (Othello): ईर्ष्या और संदेह की त्रासदी; वेनिस का मूर सेनापति, खलनायक इयागो, निर्दोष पत्नी डेसडेमोना", "4. किंग लियर (King Lear): चापलूसी में अंधे पिता की त्रासदी; तीनों पुत्रियों (गोनेरिल, रीगन, कॉर्डेलिया) में राज्य विभाजन"],
        "q_en": "In which famous Shakespearean tragedy does the tormented protagonist deliver the universally quoted soliloquy pondering existence and suicide: 'To be, or not to be, that is the question'?",
        "q_hi": "शेक्सपियर की किस कालजयी त्रासदी में व्यथित नायक जीवन, मृत्यु और अनिर्णय पर विचार करते हुए विश्व प्रसिद्ध स्वगत कथन (Soliloquy) 'To be, or not to be, that is the question' (होना या न होना, यही प्रश्न है) बोलता है?",
        "options_en": ["Hamlet (हैमलेट)", "Macbeth", "Othello", "King Lear"],
        "options_hi": ["हैमलेट (Hamlet)", "मैकबेथ (Macbeth)", "ओथेलो (Othello)", "किंग लियर (King Lear)"],
        "correct_idx": 0,
        "exp_en": "Prince Hamlet utters the famous 'To be, or not to be' soliloquy in Act III, Scene 1 of Shakespeare's 'Hamlet', weighing the pain of living against the unknown dread of death.",
        "exp_hi": "शेक्सपियर के नाटक 'हैमलेट' के तीसरे अंक के पहले दृश्य में डेनमार्क का राजकुमार हैमलेट अपने जीवन का सबसे प्रसिद्ध एकालाप बोलता है, जिसमें वह कर्तव्य, जीवन के कष्ट और मृत्यु के भय के बीच अनिर्णय में फंसा है।",
        "cue_en": "'To be, or not to be' = Hamlet by Shakespeare.",
        "cue_hi": "'To be, or not to be' = हैमलेट (शेक्सपियर)।",
        "wrong_en": ["Hamlet delivers this iconic soliloquy.", "Macbeth speaks 'Tomorrow and tomorrow and tomorrow'.", "Othello speaks about loving not wisely but too well.", "King Lear speaks about ungrateful children."],
        "wrong_hi": ["हैमलेट का अमर स्वगत कथन।", "मैकबेथ का एकालाप।", "ओथेलो का एकालाप।", "किंग लियर का एकालाप।"]
    },
    {
        "name_en": "Russian Realism: Leo Tolstoy (War and Peace, Anna Karenina) & Fyodor Dostoevsky (Crime and Punishment)",
        "name_hi": "रूसी यथार्थवाद: लियो टॉल्स्टॉय (वॉर एंड पीस, अन्ना कैरेनिना) एवं फ्योदोर दोस्तोयेव्स्की (क्राइम एंड पनिशमेंट)",
        "concepts_en": ["Leo Tolstoy (1828-1910): Master of epic realism; 'War and Peace' (1869 - epic chronicling French invasion of Russia in 1812 under Napoleon, following Pierre Bezukhov, Prince Andrei Bolkonsky, Natasha Rostova); 'Anna Karenina' (1877 - 'Happy families are all alike; every unhappy family is unhappy in its own way', tragic love with Count Vronsky); 'The Kingdom of God Is Within You' (advocating Christian pacifism and non-violent resistance, deeply influencing Mahatma Gandhi)", "Fyodor Dostoevsky (1821-1881): Master of psychological existential realism; 'Crime and Punishment' (1866 - impoverished ex-student Rodion Raskolnikov murders pawnbroker Alyona Ivanovna to prove extraordinary man theory, redeemed by Sonya Marmeladov through Siberian exile); 'The Brothers Karamazov' (1880 - Dmitry, Ivan, Alyosha, 'The Grand Inquisitor', problem of evil and free will), 'Notes from Underground'"],
        "concepts_hi": ["लियो टॉल्स्टॉय (1828-1910): महाकाव्यात्मक यथार्थवाद के सम्राट; 'वॉर एंड पीस' (1869 - 1812 में नेपोलियन के रूस पर आक्रमण की पृष्ठभूमि पर रचित विशाल उपन्यास; पात्र: पियरे बेज़ुखोव, नताशा रोस्तोवा); 'अन्ना कैरेनिना' (1877 - 'सभी सुखी परिवार एक जैसे होते हैं, पर दुखी परिवार अपने-अपने ढंग से दुखी'); 'द किंगडम ऑफ गॉड इज विदिन यू' (अहिंसा का दर्शन, जिसने महात्मा गांधी को गहराई से प्रभावित किया)", "फ्योदोर दोस्तोयेव्स्की (1821-1881): मनोवैज्ञानिक यथार्थवाद के शिखर; 'क्राइम एंड पनिशमेंट' (1866 - निर्धन छात्र रास्कोलनिकोव द्वारा एक लालची बुढ़िया की हत्या और उसके बाद अंतरात्मा के तीव्र पश्चाताप व सोन्या द्वारा आध्यात्मिक मुक्ति की कथा); 'द ब्रदर्स करमाज़ोव' (1880 - ईश्वर, पाप और नैतिक स्वतंत्रता पर गहन विमर्श)"],
        "q_en": "In Fyodor Dostoevsky's psychological masterpiece 'Crime and Punishment' (1866), which impoverished former student commits a calculated murder of an old pawnbroker to test his 'Extraordinary Man' theory?",
        "q_hi": "फ्योदोर दोस्तोयेव्स्की के कालजयी मनोवैज्ञानिक उपन्यास 'क्राइम एंड पनिशमेंट' (1866) में वह निर्धन पूर्व छात्र कौन है, जो अपनी 'असाधारण मानव' (नेपोलियन) सिद्धांत की परीक्षा लेने हेतु एक वृद्ध सूदखोर महिला की हत्या कर देता है?",
        "options_en": ["Rodion Raskolnikov (रोडियन रास्कोलनिकोव)", "Pierre Bezukhov", "Ivan Karamazov", "Prince Myshkin"],
        "options_hi": ["रोडियन रास्कोलनिकोव (Rodion Raskolnikov)", "पियरे बेज़ुखोव (यह टॉल्स्टॉय के 'वॉर एंड पीस' का पात्र है)", "इवान करमाज़ोव (द ब्रदर्स करमाज़ोव का पात्र)", "प्रिंस मिश्किन (द इडियट का पात्र)"],
        "correct_idx": 0,
        "exp_en": "Rodion Romanovich Raskolnikov is the conflicted protagonist of 'Crime and Punishment' whose rationalization of murder leads to psychological torment, moral confession, and spiritual redemption in Siberia.",
        "exp_hi": "रास्कोलनिकोव 'क्राइम एंड पनिशमेंट' का केंद्रीय पात्र है, जो मानता है कि असाधारण मनुष्यों को बड़े लक्ष्य के लिए कानून तोड़ने का अधिकार है, किंतु हत्या के बाद अपराधबोध और अंतरात्मा के द्वंद्व से टूट जाता है।",
        "cue_en": "Crime and Punishment protagonist = Rodion Raskolnikov (Dostoevsky).",
        "cue_hi": "क्राइम एंड पनिशमेंट का नायक = रास्कोलनिकोव (दोस्तोयेव्स्की)।",
        "wrong_en": ["Protagonist of Crime and Punishment.", "Protagonist of Tolstoy's War and Peace.", "Intellectual brother in The Brothers Karamazov.", "Title protagonist of Dostoevsky's The Idiot."],
        "wrong_hi": ["क्राइम एंड पनिशमेंट का नायक।", "वॉर एंड पीस का पात्र।", "द ब्रदर्स करमाज़ोव का पात्र।", "द इडियट का पात्र।"]
    },
    {
        "name_en": "Latin American Magical Realism: Gabriel Garcia Marquez (One Hundred Years of Solitude) & Jorge Luis Borges",
        "name_hi": "लैटिन अमेरिकी जादुई यथार्थवाद: गैब्रियल गार्सिया मार्केज़ (वन हंड्रेड इयर्स ऑफ सॉलिट्यूड) एवं जॉर्ज लुइस बोर्गेस",
        "concepts_en": ["Magical Realism (Realismo Mágico): Literary style blending realistic, mundane narrative with fantastical, supernatural elements presented as everyday matter-of-fact reality", "Gabriel Garcia Marquez ('Gabo', Colombia, Nobel Prize 1982): 'One Hundred Years of Solitude' (1967 - 'Cien años de soledad') chronicles 7 generations of the Buendía family in the mythical isolated town of Macondo; opening line: 'Many years later, as he faced the firing squad, Colonel Aureliano Buendía was to remember that distant afternoon when his father took him to discover ice'; 'Love in the Time of Cholera' (Florentino Ariza and Fermina Daza)", "Jorge Luis Borges (Argentina): Labyrinths, mirrors, infinity, fictional encyclopedias ('Ficciones', 'The Aleph')", "Octavio Paz (Mexico, Nobel Prize 1990): 'The Labyrinth of Solitude' (Mexican identity); Mario Vargas Llosa (Peru, Nobel Prize 2010)"],
        "concepts_hi": ["जादुई यथार्थवाद (Magical Realism): ऐसी साहित्यिक शैली जिसमें जादुई, अवास्तविक और अलौकिक घटनाओं को सामान्य दैनिक यथार्थ के रूप में स्वाभाविक ढंग से प्रस्तुत किया जाता है", "गैब्रियल गार्सिया मार्केज़ (कोलंबिया, 1982 का नोबेल पुरस्कार): कालजयी उपन्यास 'वन हंड्रेड इयर्स ऑफ सॉलिट्यूड' (1967 - सौ साल का अकेलापन); काल्पनिक शहर 'मकोंडो' में बुएंडिया परिवार की सात पीढ़ियों की महागाथा; पात्र: कर्नल ऑरेलियानो बुएंडिया, उर्सुला; 'लव इन द टाइम ऑफ कॉलरा'", "जॉर्ज लुइस बोर्गेस (अर्जेंटीना): भूलभुलैया, दर्पण और अनंतता के दार्शनिक कथाकार ('द एलेफ')", "ऑक्टावियो पाज़ (मेक्सिको, 1990 नोबेल पुरस्कार): 'द लैबिरिंथ ऑफ सॉलिट्यूड'; मारियो वर्गास ल्लोसा (पेरू, 2010 नोबेल पुरस्कार)"],
        "q_en": "Which mythical isolated town serves as the vibrant setting for seven generations of the Buendía family in Gabriel García Márquez's magical realist epic 'One Hundred Years of Solitude'?",
        "q_hi": "गैब्रियल गार्सिया मार्केज़ के जादुई यथार्थवादी महाकाव्यात्मक उपन्यास 'वन हंड्रेड इयर्स ऑफ सॉलिट्यूड' (सौ साल का अकेलापन) में बुएंडिया परिवार की सात पीढ़ियों की कथा किस काल्पनिक नगर की पृष्ठभूमि पर घटित होती है?",
        "options_en": ["Macondo (मकोंडो)", "Comala", "Yoknapatawpha", "Malgudi"],
        "options_hi": ["मकोंडो (Macondo)", "कोमाला (Comala - यह जुआन रुल्फो के उपन्यास का नगर है)", "योक्नापाटोफा (यह विलियम फॉकनर का काल्पनिक काउंटी है)", "मालगुडी (Malgudi - यह आर.के. नारायण का काल्पनिक दक्षिण भारतीय शहर है)"],
        "correct_idx": 0,
        "exp_en": "'Macondo' is the famous fictional Colombian town founded by José Arcadio Buendía in 'One Hundred Years of Solitude', reflecting the turbulent history, solitude, and magical essence of Latin America.",
        "exp_hi": "मकोंडो (Macondo) गार्सिया मार्केज़ द्वारा गढ़ा गया काल्पनिक शहर है जहां बुएंडिया परिवार बसता है और अंत में एक बवंडर में सदा के लिए लुप्त हो जाता है। (मालगुडी आर.के. नारायण का शहर है)।",
        "cue_en": "One Hundred Years of Solitude setting = Macondo (García Márquez).",
        "cue_hi": "सौ साल का अकेलापन का नगर = मकोंडो (गार्सिया मार्केज़)।",
        "wrong_en": ["Fictional setting of One Hundred Years of Solitude.", "Ghost town in Juan Rulfo's Pedro Páramo.", "Fictional county in William Faulkner's novels.", "Fictional South Indian town of R.K. Narayan."],
        "wrong_hi": ["मार्केज़ का काल्पनिक नगर (मकोंडो)।", "जुआन रुल्फो का काल्पनिक शहर।", "विलियम फॉकनर का काउंटी।", "आर.के. नारायण का मालगुडी।"]
    },
    {
        "name_en": "Modern Nobel Laureates in Literature: Ernest Hemingway, George Orwell & Post-Colonial Voices",
        "name_hi": "आधुनिक साहित्यकार व नोबेल विजेता: अर्नेस्ट हेमिंग्वे, जॉर्ज ऑरवेल एवं उत्तर-औपनिवेशिक साहित्य",
        "concepts_en": ["Ernest Hemingway (USA, Nobel Prize 1954): Iceberg theory (minimalist journalism style); 'The Old Man and the Sea' (1952 - Cuban fisherman Santiago struggles with giant marlin and sharks: 'Man is not made for defeat; a man can be destroyed but not defeated'); 'A Farewell to Arms', 'For Whom the Bell Tolls'", "George Orwell (Eric Arthur Blair, born in Motihari, Bihar 1903): Dystopian anti-totalitarian classics: 'Animal Farm' (1945 - satirical allegorical novella on Soviet Stalinism, pigs Napoleon and Snowball: 'All animals are equal, but some animals are more equal than others') and 'Nineteen Eighty-Four' (1949 - Big Brother, Thought Police, Newspeak, Room 101, Doublethink)", "Post-Colonial Maestros: Chinua Achebe (Nigeria - 'Things Fall Apart', tragedy of Okonkwo); V.S. Naipaul (Trinidad/Indian diaspora, Nobel 2001 - 'A House for Mr Biswas'); Salman Rushdie (Midnight's Children - Booker of Bookers)"],
        "concepts_hi": ["अर्नेस्ट हेमिंग्वे (अमेरिका, 1954 का नोबेल पुरस्कार): 'आइसबर्ग सिद्धांत' (कम शब्दों में गहरा प्रभाव); 'द ओल्ड मैन एंड द सी' (1952 - बूढ़े क्यूबाई मछुआरे सैंटियागो और विशाल मार्लिन मछली का संघर्ष: 'इंसान पराजय के लिए नहीं बना है; इंसान को नष्ट किया जा सकता है, पर हराया नहीं जा सकता')", "जॉर्ज ऑरवेल (एरिक आर्थर ब्लेयर, जन्म मोतिहारी, बिहार 1903): अधिनायकवाद-विरोधी कालजयी कृतियां: 'एनिमल फार्म' (1945 - सोवियत सर्वसत्तावाद पर व्यंग्य रूपक: 'सभी जानवर बराबर हैं, लेकिन कुछ जानवर दूसरों से अधिक बराबर हैं') एवं 'नाइन्टीन एटी-फोर' (1984 - बिग ब्रदर, थॉट पुलिस)", "उत्तर-औपनिवेशिक साहित्य: चिनुआ अचेबे (नाइजीरिया - 'थिंग्स फॉल अपार्ट', अफ्रीकी समाज का बिखराव); वी.एस. नायपॉल (2001 नोबेल पुरस्कार - 'अ हाउस फॉर मिस्टर बिस्वास'); सलमान रुश्दी ('मिडनाइट्स चिल्ड्रन्स')"],
        "q_en": "In George Orwell's satirical allegorical political novella 'Animal Farm' (1945), which famous corrupt commandment eventually replaces all seven original commandments of Animalism?",
        "q_hi": "जॉर्ज ऑरवेल के प्रसिद्ध राजनीतिक व्यंग्य लघु-उपन्यास 'एनिमल फार्म' (1945) में सभी सात मूल नियमों को हटाकर दीवार पर अंततः कौन सा भ्रष्ट नियम लिख दिया जाता है?",
        "options_en": ["'All animals are equal, but some animals are more equal than others' (सभी जानवर बराबर हैं, लेकिन कुछ जानवर दूसरों से अधिक बराबर हैं)", "'No animal shall drink alcohol to excess'", "'Four legs good, two legs bad forever'", "'Whatever goes upon two legs is an enemy'"],
        "options_hi": ["'सभी जानवर बराबर हैं, लेकिन कुछ जानवर दूसरों से अधिक बराबर हैं' (All animals are equal, but some are more equal)", "'कोई जानवर शराब नहीं पिएगा'", "'चार टांगें अच्छी, दो टांगें बुरी'", "'दो टांगों पर चलने वाला हर कोई दुश्मन है'"],
        "correct_idx": 0,
        "exp_en": "In 'Animal Farm', the ruling pigs rewrite the foundational egalitarian code into the paradoxical slogan: 'All animals are equal, but some animals are more equal than others', satirizing the corruption of revolutionary ideals.",
        "exp_hi": "'एनिमल फार्म' के अंत में सत्तावादी सुअर नेपोलियन के शासन में एकमात्र नियम बचता है: 'सभी जानवर बराबर हैं, लेकिन कुछ जानवर दूसरों से अधिक बराबर हैं', जो तानाशाही विशेषाधिकारों का क्रूर प्रतीक बन जाता है।",
        "cue_en": "Animal Farm final commandment = 'Some animals are more equal than others'.",
        "cue_hi": "एनिमल फार्म का अंतिम नियम = 'कुछ जानवर अधिक बराबर हैं'।",
        "wrong_en": ["Ultimate corrupt commandment in Animal Farm.", "Earlier revised rule on alcohol.", "Earlier sheep chant.", "First original commandment."],
        "wrong_hi": ["एनिमल फार्म का अंतिम भ्रष्ट नियम।", "शराब संबंधी पुराना नियम।", "भेड़ों का प्रारंभिक नारा।", "पहला प्रारंभिक नियम।"]
    }
]

print("Loaded S18 successfully")
