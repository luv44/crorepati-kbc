# build_curriculum/group1_s02.py
# S02: Current Affairs & Contemporary Events (11 topics across 3 chapters)

DATA = {}

# S02-Cda5068db (3 topics)
DATA["S02-Cda5068db"] = [
    {
        "name_en": "PM Gati Shakti National Master Plan & Multimodal Connectivity",
        "name_hi": "पीएम गति शक्ति राष्ट्रीय मास्टर प्लान एवं मल्टीमॉडल कनेक्टिविटी",
        "concepts_en": ["7 engines of economic growth", "Integrated multimodal infrastructure planning", "BISAG-N digital platform with GIS mapping", "Reduction of logistics costs"],
        "concepts_hi": ["आर्थिक विकास के 7 इंजन", "एकीकृत मल्टीमॉडल बुनियादी ढांचा योजना", "जीआईएस मैपिंग युक्त बीआईएसएजी-एन डिजिटल प्लेटफॉर्म", "लॉजिस्टिक्स लागत में कमी"],
        "q_en": "Under the PM Gati Shakti National Master Plan, how many 'engines' of economic transformation have been identified?",
        "q_hi": "पीएम गति शक्ति राष्ट्रीय मास्टर प्लान के तहत आर्थिक परिवर्तन के कितने 'इंजनों' की पहचान की गई है?",
        "options_en": ["7 engines (Roads, Railways, Airports, Ports, Mass Transport, Waterways, Logistics)", "5 engines", "10 engines", "12 engines"],
        "options_hi": ["7 इंजन (सड़क, रेलवे, हवाई अड्डे, बंदरगाह, सार्वजनिक परिवहन, जलमार्ग, लॉजिस्टिक्स)", "5 इंजन", "10 इंजन", "12 इंजन"],
        "correct_idx": 0,
        "exp_en": "PM Gati Shakti is driven by 7 engines: Roads, Railways, Airports, Ports, Mass Transport, Waterways, and Logistics Infrastructure.",
        "exp_hi": "पीएम गति शक्ति 7 इंजनों द्वारा संचालित है: सड़क, रेलवे, हवाई अड्डे, बंदरगाह, सार्वजनिक परिवहन, जलमार्ग और रसद अवसंरचना।",
        "cue_en": "PM Gati Shakti = 7 infrastructure engines.",
        "cue_hi": "पीएम गति शक्ति = 7 बुनियादी ढांचागत इंजन।",
        "wrong_en": ["Seven engines defined by the plan.", "Panchamrit targets are five, not Gati Shakti.", "Too high.", "Too high."],
        "wrong_hi": ["योजना के अनुसार कुल 7 इंजन हैं।", "पंचामृत लक्ष्य 5 हैं, गति शक्ति नहीं।", "गलत अधिक संख्या।", "गलत अधिक संख्या।"]
    },
    {
        "name_en": "G20 New Delhi Leaders' Declaration & African Union Induction",
        "name_hi": "जी20 नई दिल्ली घोषणापत्र एवं अफ्रीकी संघ का स्थायी प्रवेश",
        "concepts_en": ["Consensus on 100% paragraphs at New Delhi Summit 2023", "African Union admitted as 21st permanent member", "Global Biofuels Alliance launch", "Vasudhaiva Kutumbakam theme"],
        "concepts_hi": ["नई दिल्ली शिखर सम्मेलन 2023 में 100% पैराग्राफ पर आम सहमति", "अफ्रीकी संघ 21वें स्थायी सदस्य के रूप में शामिल", "वैश्विक जैव ईंधन गठबंधन की शुरुआत", "वसुधैव कुटुम्बकम् विषय (Theme)"],
        "q_en": "Which regional organization was admitted as a permanent member of the G20 during India's Presidency in 2023?",
        "q_hi": "2023 में भारत की जी20 अध्यक्षता के दौरान किस क्षेत्रीय संगठन को जी20 का स्थायी सदस्य बनाया गया?",
        "options_en": ["African Union (55 member states)", "ASEAN", "Arab League", "SAARC"],
        "options_hi": ["अफ्रीकी संघ (African Union - 55 सदस्य देश)", "आसियान (ASEAN)", "अरब लीग (Arab League)", "दक्षेस (SAARC)"],
        "correct_idx": 0,
        "exp_en": "During the 18th G20 Summit in New Delhi (September 2023), the 55-member African Union was formally inducted as a permanent member of the G20.",
        "exp_hi": "सितंबर 2023 में नई दिल्ली में 18वें जी20 शिखर सम्मेलन के दौरान 55 सदस्य देशों वाले अफ्रीकी संघ (AU) को स्थायी सदस्य का दर्जा दिया गया।",
        "cue_en": "African Union = Newest G20 permanent member.",
        "cue_hi": "अफ्रीकी संघ = जी20 का नया स्थायी सदस्य।",
        "wrong_en": ["Inducted under India's presidency.", "ASEAN attends as guest, not full G20 member.", "Arab League is not a member.", "SAARC is regional south asian bloc."],
        "wrong_hi": ["भारत की अध्यक्षता में शामिल किया गया।", "आसियान अतिथि के रूप में भाग लेता है।", "अरब लीग सदस्य नहीं है।", "दक्षेस केवल दक्षिण एशियाई समूह है।"]
    },
    {
        "name_en": "Chandrayaan-3 Mission: Lunar South Pole Soft Landing & Pragyan Rover",
        "name_hi": "चंद्रयान-3 मिशन: चंद्रमा के दक्षिणी ध्रुव पर सॉफ्ट लैंडिंग एवं प्रज्ञान रोवर",
        "concepts_en": ["Soft landing on 23 August 2023 near Lunar South Pole (Shiv Shakti Point)", "Vikram Lander & Pragyan Rover", "India 4th country to soft land, 1st near South Pole", "National Space Day (23 August)"],
        "concepts_hi": ["23 अगस्त 2023 को दक्षिणी ध्रुव के निकट सॉफ्ट लैंडिंग (शिव शक्ति पॉइंट)", "विक्रम लैंडर एवं प्रज्ञान रोवर", "सॉफ्ट लैंडिंग करने वाला चौथा और दक्षिणी ध्रुव पर पहुंचने वाला पहला देश", "राष्ट्रीय अंतरिक्ष दिवस (23 अगस्त)"],
        "q_en": "What name was officially assigned to the touchdown site of Chandrayaan-3's Vikram lander on the Moon?",
        "q_hi": "चंद्रमा पर चंद्रयान-3 के विक्रम लैंडर के उतरने वाले स्थान को आधिकारिक तौर पर क्या नाम दिया गया है?",
        "options_en": ["Shiv Shakti Point (शिव शक्ति पॉइंट)", "Tiranga Point", "Jawahar Point", "Atal Point"],
        "options_hi": ["शिव शक्ति पॉइंट (Shiv Shakti Point)", "तिरंगा पॉइंट", "जवाहर पॉइंट", "अटल पॉइंट"],
        "correct_idx": 0,
        "exp_en": "Prime Minister Narendra Modi announced that the Chandrayaan-3 landing site is named 'Shiv Shakti Point', while the Chandrayaan-2 impact site is 'Tiranga Point'.",
        "exp_hi": "चंद्रयान-3 की सॉफ्ट लैंडिंग के स्थल को 'शिव शक्ति पॉइंट' नाम दिया गया, जबकि चंद्रयान-2 के क्रैश स्थल को 'तिरंगा पॉइंट' नाम दिया गया था।",
        "cue_en": "Chandrayaan-3 landing = Shiv Shakti Point.",
        "cue_hi": "चंद्रयान-3 लैंडिंग स्थल = शिव शक्ति पॉइंट।",
        "wrong_en": ["Touchdown site of Chandrayaan-3.", "Chandrayaan-2 impact site.", "Chandrayaan-1 impact point (2008).", "Not an official lunar feature."],
        "wrong_hi": ["चंद्रयान-3 का आधिकारिक लैंडिंग स्थल।", "चंद्रयान-2 का क्रैश स्थल।", "चंद्रयान-1 का मून इम्पैक्ट प्रोब स्थल (2008)।", "अनधिकृत नाम।"]
    }
]

# S02-Cd08481ed (3 topics)
DATA["S02-Cd08481ed"] = [
    {
        "name_en": "India-Middle East-Europe Economic Corridor (IMEC)",
        "name_hi": "भारत-मध्य पूर्व-यूरोप आर्थिक गलियारा (IMEC)",
        "concepts_en": ["Unveiled at G20 New Delhi Summit 2023", "Eastern corridor (India to Arabian Gulf) & Northern corridor (Gulf to Europe)", "Partners: India, US, UAE, Saudi Arabia, EU, France, Germany, Italy", "Clean hydrogen pipeline and digital cable integration"],
        "concepts_hi": ["जी20 नई दिल्ली शिखर सम्मेलन 2023 में घोषित", "पूर्वी गलियारा (भारत से खाड़ी) एवं उत्तरी गलियारा (खाड़ी से यूरोप)", "साझेदार: भारत, अमेरिका, यूएई, सऊदी अरब, यूरोपीय संघ आदि", "स्वच्छ हाइड्रोजन पाइपलाइन और डेटा केबल नेटवर्क"],
        "q_en": "The India-Middle East-Europe Economic Corridor (IMEC), announced during the 2023 G20 Summit, connects India to Europe via which geographic region?",
        "q_hi": "2023 जी20 शिखर सम्मेलन में घोषित 'भारत-मध्य पूर्व-यूरोप आर्थिक गलियारा' (IMEC) भारत को किस क्षेत्र के माध्यम से यूरोप से जोड़ता है?",
        "options_en": ["The Arabian Gulf and Middle East", "Central Asia and Caspian Sea", "Suez Canal maritime route only", "Southeast Asia and the Pacific"],
        "options_hi": ["अरब की खाड़ी एवं मध्य पूर्व (The Arabian Gulf & Middle East)", "मध्य एशिया एवं कैस्पियन सागर", "केवल स्वेज नहर समुद्री मार्ग", "दक्षिण-पूर्व एशिया एवं प्रशांत क्षेत्र"],
        "correct_idx": 0,
        "exp_en": "IMEC comprises two corridors: the East Corridor connecting India to the Arabian Gulf and the Northern Corridor connecting the Arabian Gulf to Europe via rail and shipping networks.",
        "exp_hi": "आईएमईसी में दो गलियारे शामिल हैं: पूर्वी गलियारा जो भारत को अरब की खाड़ी से जोड़ता है और उत्तरी गलियारा जो खाड़ी को यूरोप से रेल और बंदरगाहों के माध्यम से जोड़ता है।",
        "cue_en": "IMEC = India -> Gulf / Middle East -> Europe.",
        "cue_hi": "IMEC = भारत -> खाड़ी / मध्य पूर्व -> यूरोप।",
        "wrong_en": ["Correct route through Middle East.", "INSTC route, not IMEC.", "IMEC provides a multimodal alternative to Suez.", "Opposite geographical direction."],
        "wrong_hi": ["मध्य पूर्व से होकर जाने वाला सही मार्ग।", "यह आईएनएसटीसी का मार्ग है, आईएमईसी का नहीं।", "आईएमईसी स्वेज का विकल्प प्रदान करता है।", "विपरीत दिशा।"]
    },
    {
        "name_en": "Quad Leaders' Summit & Indo-Pacific Maritime Domain Awareness (IPMDA)",
        "name_hi": "क्वाड (Quad) शिखर सम्मेलन एवं इंडो-पैसिफिक समुद्री डोमेन जागरूकता (IPMDA)",
        "concepts_en": ["Quad members: India, USA, Japan, Australia", "IPMDA initiative to track dark shipping and IUU fishing", "Free, open and inclusive Indo-Pacific", "Malabar naval exercise"],
        "concepts_hi": ["क्वाड सदस्य: भारत, अमेरिका, जापान, ऑस्ट्रेलिया", "डार्क शिपिंग और अवैध मछली पकड़ने पर नज़र रखने हेतु आईपीएमडीए पहल", "स्वतंत्र, खुला और समावेशी हिंद-प्रशांत क्षेत्र", "मालाबार नौसैनिक संयुक्त युद्धाभ्यास"],
        "q_en": "Which four nations constitute the Quadrilateral Security Dialogue (Quad)?",
        "q_hi": "चतुर्भुज सुरक्षा संवाद (Quad) समूह में कौन से चार राष्ट्र शामिल हैं?",
        "options_en": ["India, United States, Japan, Australia", "India, United Kingdom, France, USA", "India, Russia, China, South Africa", "USA, UK, Australia, New Zealand"],
        "options_hi": ["भारत, संयुक्त राज्य अमेरिका, जापान, ऑस्ट्रेलिया", "भारत, ब्रिटेन, फ्रांस, अमेरिका", "भारत, रूस, चीन, दक्षिण अफ्रीका", "अमेरिका, ब्रिटेन, ऑस्ट्रेलिया, न्यूजीलैंड"],
        "correct_idx": 0,
        "exp_en": "The Quad is a diplomatic partnership between India, the United States, Japan, and Australia committed to supporting a free and open Indo-Pacific.",
        "exp_hi": "क्वाड भारत, संयुक्त राज्य अमेरिका, जापान और ऑस्ट्रेलिया के बीच एक कूटनीतिक और रणनीतिक साझेदारी है जिसका उद्देश्य स्वतंत्र और खुला हिंद-प्रशांत क्षेत्र सुनिश्चित करना है।",
        "cue_en": "Quad = India, US, Japan, Australia.",
        "cue_hi": "क्वाड = भारत, अमेरिका, जापान, ऑस्ट्रेलिया।",
        "wrong_en": ["Constituent members of Quad.", "France and UK are not Quad members.", "BRICS members, not Quad.", "AUKUS / Five Eyes subset."],
        "wrong_hi": ["क्वाड के चारों सदस्य राष्ट्र।", "फ्रांस और ब्रिटेन सदस्य नहीं हैं।", "ब्रिक्स समूह के देश हैं।", "ऑकस या फाइव आइज का हिस्सा हैं।"]
    },
    {
        "name_en": "COP28 Climate Summit: Loss and Damage Fund & Global Stocktake",
        "name_hi": "कॉप-28 जलवायु सम्मेलन: लॉस एंड डैमेज फंड एवं ग्लोबल स्टॉकटेक",
        "concepts_en": ["Hosted in Dubai (UAE) in December 2023", "Operationalization of the Loss and Damage Fund", "First Global Stocktake under Paris Agreement", "Call to transition away from fossil fuels"],
        "concepts_hi": ["दिसंबर 2023 में दुबई (यूएई) में आयोजित", "हानि और क्षति कोष (Loss and Damage Fund) का संचालन", "पेरिस समझौते के तहत पहला ग्लोबल स्टॉकटेक", "जीवाश्म ईंधन से स्वच्छ ऊर्जा की ओर पारगमन"],
        "q_en": "Where was the 28th UN Climate Change Conference (COP28) held, where the Loss and Damage Fund was officially operationalized?",
        "q_hi": "संयुक्त राष्ट्र का 28वां जलवायु परिवर्तन सम्मेलन (COP28) कहां आयोजित हुआ, जिसमें 'हानि और क्षति कोष' को आधिकारिक रूप से चालू किया गया?",
        "options_en": ["Dubai, United Arab Emirates (UAE)", "Sharm El-Sheikh, Egypt", "Glasgow, United Kingdom", "Baku, Azerbaijan"],
        "options_hi": ["दुबई, संयुक्त अरब अमीरात (UAE)", "शर्म अल-शेख, मिस्र", "ग्लासगो, यूनाइटेड किंगडम", "बाकू, अज़रबैजान"],
        "correct_idx": 0,
        "exp_en": "COP28 took place in Dubai, UAE, in December 2023, where countries agreed on the operationalization of the Loss and Damage Fund and concluded the first Global Stocktake.",
        "exp_hi": "दिसंबर 2023 में दुबई (यूएई) में कॉप-28 आयोजित किया गया, जहां लॉस एंड डैमेज फंड के संचालन पर ऐतिहासिक सहमति बनी।",
        "cue_en": "COP28 = Dubai, UAE (2023).",
        "cue_hi": "कॉप-28 = दुबई, यूएई (2023)।",
        "wrong_en": ["Host city of COP28.", "Host of COP27 (2022).", "Host of COP26 (2021).", "Host of COP29 (2024)."],
        "wrong_hi": ["कॉप-28 का मेजबान शहर।", "कॉप-27 का मेजबान (2022)।", "कॉप-26 का मेजबान (2021)।", "कॉप-29 का मेजबान (2024)।"]
    }
]

# S02-C4b3f8fdc (5 topics)
DATA["S02-C4b3f8fdc"] = [
    {
        "name_en": "Aditya-L1 Solar Observatory Mission & Sun-Earth Lagrange Point 1",
        "name_hi": "आदित्य-L1 सौर वेधशाला मिशन एवं सूर्य-पृथ्वी लैग्रेंज बिंदु 1",
        "concepts_en": ["First Indian space-based observatory to study the Sun", "Positioned in halo orbit around Sun-Earth L1 (1.5 million km)", "Carries 7 payloads including VELC and SUIT", "Launched by PSLV-C57 in Sept 2023"],
        "concepts_hi": ["सूर्य के अध्ययन हेतु भारत की पहली अंतरिक्ष-आधारित वेधशाला", "सूर्य-पृथ्वी एल1 के चारों ओर हेलो कक्षा में स्थित (15 लाख किमी)", "वीईएलसी और एसयूआईटी सहित 7 वैज्ञानिक पेलोड", "सितंबर 2023 में पीएसएलवी-सी57 द्वारा प्रक्षेपित"],
        "q_en": "ISRO's solar mission Aditya-L1 is positioned in a halo orbit around which gravitational equilibrium point, situated approximately 1.5 million km from Earth?",
        "q_hi": "इसरो का सौर मिशन आदित्य-L1 पृथ्वी से लगभग 15 लाख किमी दूर किस गुरुत्वाकर्षण संतुलन बिंदु (Lagrange Point) के चारों ओर हेलो कक्षा में स्थापित किया गया है?",
        "options_en": ["Lagrange Point 1 (L1)", "Lagrange Point 2 (L2)", "Lagrange Point 4 (L4)", "Lagrange Point 5 (L5)"],
        "options_hi": ["लैग्रेंज बिंदु 1 (L1)", "लैग्रेंज बिंदु 2 (L2)", "लैग्रेंज बिंदु 4 (L4)", "लैग्रेंज बिंदु 5 (L5)"],
        "correct_idx": 0,
        "exp_en": "Aditya-L1 was inserted into a halo orbit around the Sun-Earth Lagrange Point 1 (L1), allowing continuous viewing of the Sun without any occultation or eclipses.",
        "exp_hi": "आदित्य-L1 को सूर्य-पृथ्वी लैग्रेंज बिंदु 1 (L1) के चारों ओर एक हेलो कक्षा में स्थापित किया गया है, जहां से बिना किसी ग्रहण के सूर्य का निरंतर अवलोकन संभव है।",
        "cue_en": "Aditya-L1 = L1 point (1.5 million km from Earth).",
        "cue_hi": "आदित्य-L1 = L1 बिंदु (पृथ्वी से 15 लाख किमी)।",
        "wrong_en": ["Sun-Earth L1 point.", "L2 is behind Earth (used by JWST).", "L4 leads Earth in orbit.", "L5 trails Earth in orbit."],
        "wrong_hi": ["सूर्य-पृथ्वी L1 बिंदु।", "L2 पृथ्वी के पीछे है (जेम्स वेब टेलीस्कोप का स्थान)।", "L4 कक्षा में आगे चलता है।", "L5 कक्षा में पीछे चलता है।"]
    },
    {
        "name_en": "INS Vikrant & Indigenous Aircraft Carrier Capabilities",
        "name_hi": "आईएनएस विक्रांत एवं स्वदेशी विमानवाहक पोत क्षमताएं",
        "concepts_en": ["India's first indigenously built aircraft carrier (IAC-1)", "Commissioned at Cochin Shipyard in Sept 2022", "STOBAR (Short Take-Off But Arrested Recovery) configuration", "Displacement of ~45,000 tonnes"],
        "concepts_hi": ["भारत का पहला स्वदेश निर्मित विमानवाहक पोत (IAC-1)", "सितंबर 2022 में कोचीन शिपयार्ड में नौसेना में शामिल", "स्टोबार (STOBAR) विमान संचालन प्रणाली", "लगभग 45,000 टन का विस्थापन"],
        "q_en": "What is the name of India's first indigenously designed and constructed aircraft carrier, commissioned into the Indian Navy in 2022?",
        "q_hi": "भारत के पहले स्वदेश निर्मित विमानवाहक पोत (IAC-1) का क्या नाम है, जिसे 2022 में भारतीय नौसेना में शामिल किया गया?",
        "options_en": ["INS Vikrant (आईएनएस विक्रांत)", "INS Vikramaditya", "INS Viraat", "INS Vishal"],
        "options_hi": ["आईएनएस विक्रांत (INS Vikrant)", "आईएनएस विक्रमादित्य", "आईएनएस विराट", "आईएनएस विशाल"],
        "correct_idx": 0,
        "exp_en": "INS Vikrant is India's first indigenously designed and built aircraft carrier, constructed by Cochin Shipyard Limited and commissioned in September 2022.",
        "exp_hi": "आईएनएस विक्रांत (IAC-1) भारत का पहला स्वदेशी विमानवाहक पोत है, जिसे कोचीन शिपयार्ड लिमिटेड द्वारा निर्मित कर सितंबर 2022 में नौसेना में शामिल किया गया।",
        "cue_en": "Indigenous carrier = INS Vikrant.",
        "cue_hi": "पहला स्वदेशी विमानवाहक पोत = आईएनएस विक्रांत।",
        "wrong_en": ["First indigenous carrier.", "Acquired from Russia (modified Kiev class).", "Centaur class, decommissioned 2017.", "Proposed second indigenous carrier."],
        "wrong_hi": ["पहला स्वदेशी विमानवाहक पोत।", "रूस से खरीदा गया पोत।", "ब्रिटेन से लिया गया, 2017 में सेवामुक्त।", "प्रस्तावित दूसरा स्वदेशी विमानवाहक पोत।"]
    },
    {
        "name_en": "Digital Public Infrastructure: UPI Global Expansion & ONDC",
        "name_hi": "डिजिटल सार्वजनिक अवसंरचना: यूपीआई का वैश्विक विस्तार एवं ओएनडीसी",
        "concepts_en": ["Unified Payments Interface (UPI) developed by NPCI", "International linkages (Singapore PayNow, France, UAE, Sri Lanka, Mauritius)", "Open Network for Digital Commerce (ONDC) interoperable e-commerce", "India Stack model"],
        "concepts_hi": ["एनपीसीआई द्वारा विकसित एकीकृत भुगतान इंटरफेस (UPI)", "अंतर्राष्ट्रीय जुड़ाव (सिंगापुर पेनाउ, फ्रांस, यूएई, श्रीलंका, मॉरीशस)", "डिजिटल कॉमर्स हेतु ओपन नेटवर्क (ONDC)", "इंडिया स्टैक डिजिटल मॉडल"],
        "q_en": "Which umbrella organization developed and operates India's Unified Payments Interface (UPI) and RuPay network?",
        "q_hi": "भारत के एकीकृत भुगतान इंटरफेस (UPI) और रुपे (RuPay) नेटवर्क का विकास और संचालन किस शीर्ष संगठन द्वारा किया जाता है?",
        "options_en": ["National Payments Corporation of India (NPCI)", "Reserve Bank of India (RBI)", "NITI Aayog", "State Bank of India (SBI)"],
        "options_hi": ["भारतीय राष्ट्रीय भुगतान निगम (NPCI)", "भारतीय रिज़र्व बैंक (RBI)", "नीति आयोग", "भारतीय स्टेट बैंक (SBI)"],
        "correct_idx": 0,
        "exp_en": "NPCI (National Payments Corporation of India), an initiative of RBI and IBA under the Payment and Settlement Systems Act 2007, operates UPI and RuPay.",
        "exp_hi": "एनपीसीआई (भारतीय राष्ट्रीय भुगतान निगम), जो 2008 में स्थापित हुआ, यूपीआई, रुपे, आईएमपीएस और फास्टैग जैसी प्रणालियों का संचालन करता है।",
        "cue_en": "UPI & RuPay = NPCI.",
        "cue_hi": "यूपीआई और रुपे = एनपीसीआई (NPCI)।",
        "wrong_en": ["Operates UPI.", "Regulator, not direct operator.", "Policy think-tank.", "Commercial bank."],
        "wrong_hi": ["यूपीआई का संचालन करता है।", "केंद्रीय बैंक व नियामक है।", "नीतिगत थिंक-टैंक है।", "वाणिज्यिक बैंक है।"]
    },
    {
        "name_en": "National Quantum Mission & Quantum Technologies",
        "name_hi": "राष्ट्रीय क्वांटम मिशन एवं क्वांटम प्रौद्योगिकी",
        "concepts_en": ["Approved by Union Cabinet with outlay of ₹6,003 crore", "Development of intermediate scale quantum computers (50-1000 qubits)", "Quantum communication, sensing & materials", "Led by Department of Science & Technology"],
        "concepts_hi": ["केंद्रीय मंत्रिमंडल द्वारा ₹6,003 करोड़ के परिव्यय के साथ स्वीकृत", "50 से 1000 क्यूबिट वाले क्वांटम कंप्यूटरों का विकास", "क्वांटम संचार, संवेदन एवं पदार्थ", "विज्ञान एवं प्रौद्योगिकी विभाग द्वारा संचालित"],
        "q_en": "What is the fundamental unit of information in quantum computing, analogous to a classical bit?",
        "q_hi": "क्वांटम कंप्यूटिंग में सूचना की मूल इकाई क्या कहलाती है, जो पारंपरिक बाइनरी बिट के समतुल्य होती है?",
        "options_en": ["Qubit (क्वांटम बिट)", "Byte", "Tetra", "Q-dot"],
        "options_hi": ["क्यूबिट (Qubit / Quantum Bit)", "बाइट (Byte)", "टेट्रा (Tetra)", "क्यू-डॉट (Q-dot)"],
        "correct_idx": 0,
        "exp_en": "A qubit (quantum bit) is the basic unit of quantum information, capable of existing in superpositions of 0 and 1 simultaneously.",
        "exp_hi": "क्यूबिट (क्वांटम बिट) क्वांटम कंप्यूटिंग की आधारभूत इकाई है, जो सुपरपोजिशन सिद्धांत के कारण एक साथ 0 और 1 दोनों अवस्थाओं में रह सकती है।",
        "cue_en": "Quantum Bit = Qubit.",
        "cue_hi": "क्वांटम बिट = क्यूबिट।",
        "wrong_en": ["Basic unit in quantum computing.", "8 classical bits.", "Prefix or telephony term.", "Semiconductor nanostructure."],
        "wrong_hi": ["क्वांटम सूचना की मूलभूत इकाई।", "8 सामान्य बिट्स का समूह।", "रेडियो संचार प्रणाली।", "अर्धचालक नैनोकण।"]
    },
    {
        "name_en": "Deep Ocean Mission & Matsya 6000 Submersible",
        "name_hi": "डीप ओशन मिशन एवं मत्स्य-6000 पनडुब्बी (Samudrayaan)",
        "concepts_en": ["Ministry of Earth Sciences initiative (Samudrayaan project)", "Matsya 6000 manned submersible for 6,000 m ocean depth", "Exploration of polymetallic nodules in Central Indian Ocean Basin", "Ocean climate change advisory services"],
        "concepts_hi": ["पृथ्वी विज्ञान मंत्रालय की पहल (समुद्रयान परियोजना)", "6,000 मीटर की गहराई हेतु मत्स्य-6000 मानवयुक्त पनडुब्बी", "मध्य हिंद महासागर में पॉलीमेटैलिक नोड्यूल का अन्वेषण", "महासागरीय जलवायु परिवर्तन सलाहकार सेवाएं"],
        "q_en": "Under India's Deep Ocean Mission (Samudrayaan), what is the name of the indigenously developed manned submersible designed to carry three humans to a depth of 6,000 metres?",
        "q_hi": "भारत के डीप ओशन मिशन (समुद्रयान) के तहत 6,000 मीटर की गहराई तक तीन मनुष्यों को ले जाने के लिए विकसित मानवयुक्त पनडुब्बी का नाम क्या है?",
        "options_en": ["Matsya 6000 (मत्स्य 6000)", "Varuna 6000", "Samudra 6000", "Jalashwa 6000"],
        "options_hi": ["मत्स्य 6000 (Matsya 6000)", "वरुण 6000", "समुद्र 6000", "जलाश्र्व 6000"],
        "correct_idx": 0,
        "exp_en": "Matsya 6000 is a self-propelled manned submersible developed by the National Institute of Ocean Technology (NIOT) designed to carry 3 humans to a depth of 6,000 m.",
        "exp_hi": "राष्ट्रीय महासागर प्रौद्योगिकी संस्थान (NIOT) द्वारा विकसित 'मत्स्य 6000' तीन वैज्ञानिकों को 6,000 मीटर गहरे समुद्र में ले जाने में सक्षम मानवयुक्त पनडुब्बी है।",
        "cue_en": "Samudrayaan submersible = Matsya 6000.",
        "cue_hi": "समुद्रयान पनडुब्बी = मत्स्य 6000।",
        "wrong_en": ["Official name of the submersible.", "Incorrect mythical deity name.", "Generic sea name.", "Amphibious transport ship name."],
        "wrong_hi": ["पनडुब्बी का सही आधिकारिक नाम।", "काल्पनिक नाम।", "सामान्य नाम।", "भारतीय नौसेना के युद्धपोत का नाम।"]
    }
]

print("Loaded S02 successfully")
