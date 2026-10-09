# build_curriculum/group7_s26.py
# S26: Metrology, SI Units, Physical Constants & Standard Measures (10 topics across 3 chapters)

DATA = {}

# S26-C2d838fe4 The Seven Base SI Units, Defining Constants & Redefinition (2019) (4 topics)
DATA["S26-C2d838fe4"] = [
    {
        "name_en": "The Seven Fundamental SI Base Units: Meter, Kilogram, Second, Ampere, Kelvin, Mole & Candela",
        "name_hi": "सात मूल एसआई (SI) मात्रक: मीटर, किलोग्राम, सेकंड, एम्पीयर, केल्विन, मोल एवं कैंडेला",
        "concepts_en": ["International System of Units (SI, Le Système International d'Unités): Established in 1960 by the 11th CGPM (General Conference on Weights and Measures) based on the metric MKS system", "Seven fundamental base quantities and their respective SI base units:", "1. Length: Meter (m)", "2. Mass: Kilogram (kg)", "3. Time: Second (s)", "4. Electric Current: Ampere (A)", "5. Thermodynamic Temperature: Kelvin (K - note: no degree symbol, absolute zero = 0 K = -273.15 °C)", "6. Amount of Substance: Mole (mol)", "7. Luminous Intensity: Candela (cd)", "Supplementary dimensionless units: Radian (rad - plane angle) and Steradian (sr - solid angle)"],
        "concepts_hi": ["अंतर्राष्ट्रीय मात्रक प्रणाली (SI - International System of Units): 1960 में 11वीं सीजीपीएम (CGPM) संगोष्ठी में स्थापित मीट्रिक प्रणाली", "सात मूलभूत भौतिक राशियां एवं उनके मानक एसआई मात्रक:", "1. लंबाई: मीटर (m)", "2. द्रव्यमान: किलोग्राम (kg)", "3. समय: सेकंड (s)", "4. विद्युत धारा: एम्पीयर (A)", "5. ऊष्मागतिक तापमान: केल्विन (K - ध्यान दें: केल्विन के साथ डिग्री ° नहीं लगाया जाता; परम शून्य ताप = 0 K = -273.15 °C)", "6. पदार्थ की मात्रा: मोल (mol)", "7. ज्योति तीव्रता (Luminous Intensity): कैंडेला (cd)", "दो संपूरक मात्रक: रेडियन (rad - समतल कोण) एवं स्टेरेडियन (sr - ठोस/घन कोण)"],
        "q_en": "What is the official base SI unit for the fundamental physical quantity of 'Luminous Intensity' (the perceived power of light per unit solid angle)?",
        "q_hi": "मूल भौतिक राशि 'ज्योति तीव्रता' (Luminous Intensity - प्रकाश स्रोतों की प्रदीपन शक्ति) का अंतर्राष्ट्रीय मानक एसआई (SI) मूल मात्रक क्या है?",
        "options_en": ["Candela (कैंडेला - cd)", "Lumen", "Lux", "Watt"],
        "options_hi": ["कैंडेला (Candela - cd)", "ल्यूमेन (Lumen - यह ज्योति फ्लक्स का मात्रक है)", "लक्स (Lux - यह प्रदीप्ति घनत्व का मात्रक है)", "वाट (Watt - यह शक्ति का मात्रक है)"],
        "correct_idx": 0,
        "exp_en": "The Candela (symbol: cd) is the SI base unit of luminous intensity in a given direction, defined by fixing the luminous efficacy of monochromatic radiation of frequency 540 × 10¹² Hz at 683 lm/W.",
        "exp_hi": "ज्योति तीव्रता (Luminous Intensity) का मूल एसआई मात्रक 'कैंडेला' (cd) है। (ल्यूमेन ज्योति फ्लक्स का व्युत्पन्न मात्रक है और लक्स प्रदीप्ति का मात्रक है)।",
        "cue_en": "SI base unit of luminous intensity = Candela (cd).",
        "cue_hi": "ज्योति तीव्रता का एसआई मात्रक = कैंडेला (cd)।",
        "wrong_en": ["SI base unit of luminous intensity.", "Derived unit of luminous flux (cd·sr).", "Derived unit of illuminance (lm/m²).", "Unit of power."],
        "wrong_hi": ["ज्योति तीव्रता का मूल मात्रक।", "ज्योति फ्लक्स का मात्रक (ल्यूमेन)।", "प्रदीप्ति का मात्रक (लक्स)।", "शक्ति का मात्रक।"]
    },
    {
        "name_en": "Historic 2019 Redefinition of SI Units: The Seven Defining Fundamental Constants",
        "name_hi": "2019 की ऐतिहासिक एसआई मात्रक पुनर्परिभाषा: सात अपरिवर्तनीय सार्वत्रिक भौतिक नियतांक",
        "concepts_en": ["Effective May 20, 2019 (World Metrology Day, commemorating the 1875 Metre Convention): 26th CGPM unanimously redefined all seven SI base units in terms of invariant fundamental constants of nature", "The Seven Defining Constants (exact values with zero uncertainty):", "1. Cesium hyperfine transition frequency ΔνCs = 9,192,631,770 Hz (defines the Second)", "2. Speed of light in vacuum c = 299,792,458 m/s (defines the Meter)", "3. Planck constant h = 6.62607015 × 10⁻³⁴ J·s (defines the Kilogram via Kibble balance)", "4. Elementary charge e = 1.602176634 × 10⁻¹⁹ C (defines the Ampere)", "5. Boltzmann constant k = 1.380649 × 10⁻²³ J/K (defines the Kelvin)", "6. Avogadro constant NA = 6.02214076 × 10²³ mol⁻¹ (defines the Mole)", "7. Luminous efficacy Kcd = 683 lm/W (defines the Candela)"],
        "concepts_hi": ["20 मई 2019 (विश्व मापिकी दिवस) से प्रभावी: 26वीं सीजीपीएम संगोष्ठी ने मानव इतिहास में पहली बार सातों मूल मात्रकों को प्रकृति के अपरिवर्तनीय मौलिक नियतांकों के आधार पर पुनर्परिभाषित किया", "सात निर्धारक भौतिक नियतांक (जिनके मान अब 100% सटीक व निश्चित हैं):", "1. सीज़ियम-133 की हाइपरफाइन आवृत्ति ΔνCs = 9,192,631,770 हर्ट्ज (सेकंड की परिभाषा)", "2. निर्वात में प्रकाश की चाल c = 299,792,458 मीटर/सेकंड (मीटर की परिभाषा)", "3. प्लांक नियतांक h = 6.62607015 × 10⁻³⁴ जूल·सेकंड (किबले बैलेंस द्वारा किलोग्राम की परिभाषा)", "4. मूल इलेक्ट्रॉनिक आवेश e = 1.602176634 × 10⁻¹⁹ कूलॉम (एम्पीयर की परिभाषा)", "5. बोल्ट्ज़मान नियतांक k = 1.380649 × 10⁻²³ जूल/केल्विन (केल्विन की परिभाषा)", "6. आवोगाद्रो नियतांक NA = 6.02214076 × 10²³ मोल⁻¹ (मोल की परिभाषा)", "7. चमकदार प्रभावोत्पादकता Kcd = 683 ल्यूमेन/वाट (कैंडेला की परिभाषा)"],
        "q_en": "Under the landmark 2019 redefinition of SI base units, which fundamental physical quantum constant is fixed at exactly 6.62607015 × 10⁻³⁴ J·s to define the 'Kilogram'?",
        "q_hi": "2019 की ऐतिहासिक एसआई पुनर्परिभाषा के तहत किस सार्वत्रिक क्वांटम नियतांक के मान को 6.62607015 × 10⁻³⁴ जूल-सेकंड पर स्थिर करके 'किलोग्राम' (Kilogram) को नए सिरे से परिभाषित किया गया?",
        "options_en": ["Planck Constant / h (प्लांक नियतांक)", "Boltzmann Constant", "Avogadro Constant", "Gravitational Constant"],
        "options_hi": ["प्लांक नियतांक (Planck Constant - h)", "बोल्ट्ज़मान नियतांक (Boltzmann Constant - k, यह केल्विन हेतु है)", "आवोगाद्रो नियतांक (Avogadro Constant - NA, यह मोल हेतु है)", "गुरुत्वाकर्षण नियतांक (G)"],
        "correct_idx": 0,
        "exp_en": "Since May 20, 2019, the kilogram is no longer defined by a physical prototype cylinder, but by fixing the numerical value of the Planck constant (h) using the electro-mechanical Kibble balance.",
        "exp_hi": "20 मई 2019 से पेरिस के वॉल्ट में रखे प्लैटिनम-इरीडियम सिलेंडर को हटाकर 'प्लांक नियतांक' (Planck constant, h) के सटीक मान के आधार पर किलोग्राम को परिभाषित किया गया है।",
        "cue_en": "Kilogram redefinition (2019) = Planck Constant (h = 6.62607015 × 10⁻³⁴ J·s).",
        "cue_hi": "किलोग्राम की नई परिभाषा = प्लांक नियतांक (h)।",
        "wrong_en": ["Defines the kilogram.", "Defines the kelvin.", "Defines the mole.", "Not used to define SI units due to measurement uncertainty."],
        "wrong_hi": ["किलोग्राम का निर्धारक नियतांक।", "केल्विन का नियतांक।", "मोल का नियतांक।", "गुरुत्वाकर्षण नियतांक।"]
    },
    {
        "name_en": "Retirement of the International Prototype of the Kilogram (Le Grand K) & The Kibble Balance",
        "name_hi": "अंतर्राष्ट्रीय किलोग्राम प्रोटोटाइप (ले ग्रांड के) की विदाई एवं किबले बैलेंस (Kibble Balance) तकनीक",
        "concepts_en": ["Le Grand K (The International Prototype of the Kilogram, IPK): Manufactured in London in 1879, a cylinder of 90% Platinum and 10% Iridium alloy stored under triple bell jars in a safe at the BIPM in Sèvres, France; served as the physical definition of the kilogram for 130 years (1889-2019)", "The Problem: Over a century, comparisons with official sister copies showed Le Grand K had lost or gained ~50 micrograms due to surface contamination and cleaning wear, making the standard artifact unstable", "Kibble Balance (invented by British physicist Bryan Kibble at NPL in 1975, originally called Watt Balance): Measures the ratio of mechanical power to electrical power using quantum electrical standards (Josephson effect and Quantum Hall effect), linking weight directly to the fixed Planck constant h with parts-per-billion precision"],
        "concepts_hi": ["ले ग्रांड के (Le Grand K / IPK): 1879 में 90% प्लैटिनम और 10% इरीडियम मिश्रधातु से बना एक छोटा बेलनाकार बाट, जिसे पेरिस (सेवरेस) के अंतर्राष्ट्रीय माप-तोल ब्यूरो (BIPM) में तीन कांच के जार के अंदर रखा गया था; 130 वर्षों तक (1889 से 2019) यही दुनिया का आधिकारिक 1 किलोग्राम था", "समस्या: 100 वर्षों में साफ-सफाई और सूक्ष्म टूट-फूट से इस भौतिक बाट का वजन लगभग 50 माइक्रोग्राम बदल गया था, जिससे संपूर्ण वैज्ञानिक माप प्रभावित हो रहा था", "किबले बैलेंस (Kibble Balance): ब्रिटिश वैज्ञानिक ब्रायन किबले द्वारा आविष्कृत विद्युत-चुंबकीय तुला जो क्वांटम यांत्रिकी (जोसेफसन व क्वांटम हॉल प्रभाव) द्वारा वजन को सीधे 'प्लांक नियतांक' से माप देती है, जिससे किसी भौतिक बाट की आवश्यकता समाप्त हो गई"],
        "q_en": "What precious metallic alloy was used to craft 'Le Grand K', the cylindrical artifact that served as the world's physical standard prototype kilogram for 130 years until its retirement in 2019?",
        "q_hi": "पेरिस के वॉल्ट में 130 वर्षों तक दुनिया के आधिकारिक 1 किलोग्राम के मानक के रूप में रखा गया 'ले ग्रांड के' (Le Grand K) सिलेंडर किस बहुमूल्य मिश्रधातु से निर्मित था?",
        "options_en": ["90% Platinum and 10% Iridium alloy (90% प्लैटिनम एवं 10% इरीडियम मिश्रधातु)", "Pure 24-Karat Gold", "Titanium and Tungsten alloy", "Stainless Steel and Nickel alloy"],
        "options_hi": ["90% प्लैटिनम एवं 10% इरीडियम (Platinum-Iridium alloy)", "शुद्ध 24-कैरेट सोना", "टाइटेनियम व टंगस्टन", "स्टेनलेस स्टील व निकल"],
        "correct_idx": 0,
        "exp_en": "The International Prototype of the Kilogram (IPK) was manufactured from a corrosion-resistant, high-density alloy of 90% Platinum and 10% Iridium by mass, with height equal to diameter (39 mm).",
        "exp_hi": "'ले ग्रांड के' 90% प्लैटिनम और 10% इरीडियम की मिश्रधातु से बना 39 मिलीमीटर का सिलेंडर था, जो जंग-रोधी और अत्यधिक घनत्व वाली धातु है।",
        "cue_en": "Le Grand K composition = 90% Platinum + 10% Iridium.",
        "cue_hi": "ले ग्रांड के = 90% प्लैटिनम + 10% इरीडियम।",
        "wrong_en": ["Historic composition of the IPK artifact.", "Too soft for physical standard prototype.", "Modern structural metals, not standard IPK.", "Common commercial weight material."],
        "wrong_hi": ["सही मिश्रधातु (प्लैटिनम-इरीडियम)।", "सोना अत्यधिक मुलायम होता है।", "टाइटेनियम।", "साधारण स्टील।"]
    },
    {
        "name_en": "Atomic Clocks: Cesium-133 Hyperfine Transitions & Coordinated Universal Time (UTC)",
        "name_hi": "परमाणु घड़ियां: सीज़ियम-133 हाइपरफाइन संक्रमण, लीप सेकंड एवं समन्वित सार्वत्रिक समय (UTC)",
        "concepts_en": ["Atomic definition of the Second (1967): The duration of exactly 9,192,631,770 periods of the radiation corresponding to the transition between the two hyperfine ground-state levels of the Cesium-133 atom at rest at 0 K", "Cesium fountain atomic clocks (e.g., NIST-F2, NPL India primary standard): Accurate to within 1 second in over 300 million years", "Coordinated Universal Time (UTC): Global primary time standard computed by the BIPM by averaging signals from over 450 atomic clocks worldwide (International Atomic Time / TAI adjusted for leap seconds)", "Indian Standard Time (IST): UTC+05:30; calculated from the reference longitude of 82.5° East passing through Mirzapur, Uttar Pradesh; maintained in India by CSIR-National Physical Laboratory (NPL) in New Delhi"],
        "concepts_hi": ["सेकंड की परमाणु परिभाषा (1967): सीज़ियम-133 (Cs-133) परमाणु की मूल अवस्था के दो हाइपरफाइन स्तरों के बीच संक्रमण से उत्पन्न विकिरण के ठीक 9,192,631,770 कंपनों (दोलनों) में लगने वाला समय", "सीज़ियम परमाणु घड़ी: 30 करोड़ वर्षों में 1 सेकंड से भी कम की त्रुटि; भारत में CSIR-राष्ट्रीय भौतिक प्रयोगशाला (NPL, नई दिल्ली) द्वारा मानक समय का संचालन", "समन्वित सार्वत्रिक समय (UTC): दुनिया भर की 450 से अधिक परमाणु घड़ियों के औसत द्वारा निर्धारित वैश्विक समय", "भारतीय मानक समय (IST): UTC + 5:30 घंटे; मिर्जापुर (उत्तर प्रदेश) से गुजरने वाली 82.5° पूर्वी देशांतर रेखा से निर्धारित"],
        "q_en": "The SI base unit of time, the 'Second', is defined by exactly 9,192,631,770 cycles of microwave radiation emitted by the ground-state hyperfine transition of which specific isotope?",
        "q_hi": "समय का मूल एसआई मात्रक 'सेकंड' किस विशिष्ट समस्थानिक (Isotope) के मूल अवस्था में 9,192,631,770 कंपनों की अवधि द्वारा सटीक रूप से परिभाषित किया गया है?",
        "options_en": ["Cesium-133 (सीज़ियम-133)", "Rubidium-87", "Hydrogen-1", "Carbon-12"],
        "options_hi": ["सीज़ियम-133 (Cesium-133)", "रुबिडियम-87 (Rubidium-87 - द्वितीयक परमाणु घड़ियों में प्रयुक्त)", "हाइड्रोजन-1 (मेसर घड़ी)", "कार्बन-12 (यह मोल की पुरानी परिभाषा थी)"],
        "correct_idx": 0,
        "exp_en": "Since the 13th CGPM in 1967, the SI second has been formally defined by fixing the ground-state hyperfine transition frequency of the unperturbed Cesium-133 atom at exactly 9,192,631,770 Hz.",
        "exp_hi": "सीज़ियम-133 परमाणु के 9,192,631,770 दोलनों में लगने वाले समय को 1 सेकंड माना गया है; यही सीज़ियम परमाणु घड़ियों का मूल आधार है।",
        "cue_en": "1 second = 9,192,631,770 cycles of Cesium-133.",
        "cue_hi": "1 सेकंड = सीज़ियम-133 के 9,192,631,770 कंपन।",
        "wrong_en": ["SI defining isotope for the second.", "Used in secondary portable atomic clocks.", "Used in hydrogen masers.", "Former defining isotope for the mole."],
        "wrong_hi": ["सेकंड का मानक समस्थानिक (सीज़ियम-133)।", "रुबिडियम।", "हाइड्रोजन।", "कार्बन-12।"]
    }
]

# S26-C41885f6d Derived SI Units with Special Names (Newton, Joule, Watt, Pascal) (3 topics)
DATA["S26-C41885f6d"] = [
    {
        "name_en": "Mechanical Derived Units: Newton (Force), Pascal (Pressure), Joule (Energy) & Watt (Power)",
        "name_hi": "यांत्रिक व्युत्पन्न एसआई मात्रक: न्यूटन (बल), पास्कल (दाब), जूल (ऊर्जा/कार्य) एवं वाट (शक्ति)",
        "concepts_en": ["Derived SI units are coherent algebraic combinations of base SI units:", "1. Newton (N): Unit of Force = mass × acceleration = 1 kg·m·s⁻² (force required to accelerate 1 kg by 1 m/s²)", "2. Pascal (Pa): Unit of Pressure = force / area = 1 N·m⁻² = 1 kg·m⁻¹·s⁻²; 1 standard atmospheric pressure (1 atm) = 101,325 Pa = 1.01325 bar = 760 mm of Hg (Torr)", "3. Joule (J): Unit of Work / Energy / Heat = force × distance = 1 N·m = 1 kg·m²·s⁻²; 1 calorie ≈ 4.184 J; 1 kilowatt-hour (kWh) = 3.6 × 10⁶ J (3.6 MJ)", "4. Watt (W): Unit of Power = rate of doing work = 1 J·s⁻¹ = 1 kg·m²·s⁻³; 1 Horsepower (hp, imperial) ≈ 746 Watts"],
        "concepts_hi": ["मूल मात्रकों के गुणन और भाग से बनने वाले सुसंगत व्युत्पन्न मात्रक:", "1. न्यूटन (N): बल का मात्रक = द्रव्यमान × त्वरण = 1 kg·m·s⁻² (1 किग्रा पिंड में 1 मी/से² का त्वरण उत्पन्न करने वाला बल)", "2. पास्कल (Pa): दाब और प्रतिबल का मात्रक = बल / क्षेत्रफल = 1 N/m² = 1 kg·m⁻¹·s⁻²; 1 मानक वायुमंडलीय दाब = 101,325 पास्कल = 760 मिमी पारा (टॉर)", "3. जूल (J): कार्य, ऊर्जा और ऊष्मा का मात्रक = बल × विस्थापन = 1 N·m = 1 kg·m²·s⁻²; 1 कैलोरी = 4.184 जूल; 1 यूनिट बिजली (1 kWh) = 3.6 × 10⁶ जूल", "4. वाट (W): शक्ति का मात्रक = कार्य करने की दर = 1 जूल/सेकंड = 1 kg·m²·s⁻³; 1 अश्वशक्ति (Horsepower / HP) = 746 वाट"],
        "q_en": "One mechanical Horsepower (hp), a traditional imperial unit of mechanical power still widely used in automotive and industrial engines, is equivalent to exactly how many Watts in SI units?",
        "q_hi": "ऑटोमोबाइल और औद्योगिक मोटरों में प्रयुक्त होने वाली पारंपरिक यांत्रिक 'अश्वशक्ति' (1 Horsepower - HP) कितने वाट (Watts) के बराबर होती है?",
        "options_en": ["746 Watts (746 वाट)", "1000 Watts", "550 Watts", "735.5 Watts"],
        "options_hi": ["746 वाट (746 Watts - 1 HP)", "1000 वाट (यह 1 किलोवाट है)", "550 वाट", "735.5 वाट (यह मीट्रिक हॉर्सपावर है)"],
        "correct_idx": 0,
        "exp_en": "One imperial horsepower (defined by James Watt as 550 foot-pounds per second) corresponds to approximately 745.7, rounded universally in standard physics exams to 746 Watts.",
        "exp_hi": "1 अश्वशक्ति (1 HP) = 746 वाट (Watts) होती है। जेम्स वाट ने भाप के इंजनों की क्षमता की घोड़ों से तुलना करने हेतु इस मात्रक की शुरुआत की थी।",
        "cue_en": "1 Horsepower (HP) = 746 Watts.",
        "cue_hi": "1 अश्वशक्ति (HP) = 746 वाट।",
        "wrong_en": ["Standard imperial horsepower equivalence.", "One kilowatt (1 kW).", "Foot-pounds per second definition.", "Metric horsepower (PS/CV)."],
        "wrong_hi": ["सही मान (746 वाट)।", "1 किलोवाट।", "फुट-पाउंड मान।", "मीट्रिक अश्वशक्ति।"]
    },
    {
        "name_en": "Electromagnetic Derived Units: Coulomb, Volt, Ohm, Farad, Tesla & Henry",
        "name_hi": "विद्युत एवं चुंबकीय व्युत्पन्न मात्रक: कूलॉम, वोल्ट, ओम, फैराड, टेस्ला एवं हेनरी",
        "concepts_en": ["Electromagnetic SI derived units with special eponyms:", "1. Coulomb (C): Electric charge = current × time = 1 A·s", "2. Volt (V): Electric potential difference = work / charge = 1 J·C⁻¹ = 1 kg·m²·s⁻³·A⁻¹", "3. Ohm (Ω): Electrical resistance = voltage / current = 1 V·A⁻¹ (Ohm's Law: V = IR)", "4. Farad (F): Capacitance = charge / voltage = 1 C·V⁻¹ = 1 s⁴·A²·kg⁻¹·m⁻² (1 Farad is exceptionally large, practical capacitors use μF or pF)", "5. Tesla (T): Magnetic flux density (magnetic B-field) = 1 N·A⁻¹·m⁻¹ = 1 Weber·m⁻²; 1 Tesla = 10,000 Gauss (CGS unit)", "6. Weber (Wb): Magnetic flux = 1 T·m² = 1 V·s", "7. Henry (H): Inductance = 1 Wb·A⁻¹ = 1 V·s·A⁻¹"],
        "concepts_hi": ["वैज्ञानिकों के नाम पर रखे गए विद्युत-चुंबकीय व्युत्पन्न एसआई मात्रक:", "1. कूलॉम (C): विद्युत आवेश का मात्रक = धारा × समय = 1 A·s", "2. वोल्ट (V): विद्युत विभव / विभवांतर का मात्रक = कार्य / आवेश = 1 जूल/कूलॉम", "3. ओम (Ω): विद्युत प्रतिरोध का मात्रक = विभवांतर / धारा = 1 वोल्ट/एम्पीयर (ओम का नियम: V = IR)", "4. फैराड (F): विद्युत धारिता (कैपेसिटेंस) का मात्रक = आवेश / विभव = 1 C/V (1 फैराड बहुत बड़ा मात्रक है, व्यावहारिक रूप से माइक्रोफैराड μF का उपयोग होता है)", "5. टेस्ला (T): चुंबकीय क्षेत्र की तीव्रता (चुंबकीय फ्लक्स घनत्व) = 1 वेबर/मी²; 1 टेस्ला = 10,000 गॉस (Gauss)", "6. वेबर (Wb): चुंबकीय फ्लक्स का मात्रक = 1 T·m²", "7. हेनरी (H): प्रेरकत्व (Inductance) का मात्रक"],
        "q_en": "What is the specialized SI derived unit for measuring 'Capacitance' (the ability of a system to store an electrical charge per unit potential difference)?",
        "q_hi": "किसी चालक या संधारित्र की 'विद्युत धारिता' (Capacitance - प्रति इकाई विभव पर विद्युत आवेश संचित करने की क्षमता) का विशेष एसआई व्युत्पन्न मात्रक क्या है?",
        "options_en": ["Farad (फैराड - F)", "Henry", "Tesla", "Weber"],
        "options_hi": ["फैराड (Farad - F)", "हेनरी (Henry - यह प्रेरकत्व का मात्रक है)", "टेस्ला (Tesla - यह चुंबकीय क्षेत्र का मात्रक है)", "वेबर (Weber - यह चुंबकीय फ्लक्स का मात्रक है)"],
        "correct_idx": 0,
        "exp_en": "The Farad (symbol: F), named after Michael Faraday, is the SI unit of electrical capacitance, defined as one coulomb of charge stored across a potential difference of one volt (1 F = 1 C/V).",
        "exp_hi": "विद्युत धारिता (Capacitance) का एसआई मात्रक 'फैराड' (Farad - F) है, जिसका नामकरण महान वैज्ञानिक माइकल फैराडे के सम्मान में किया गया है।",
        "cue_en": "Capacitance unit = Farad (F); Inductance unit = Henry (H).",
        "cue_hi": "धारिता का मात्रक = फैराड; प्रेरकत्व का मात्रक = हेनरी।",
        "wrong_en": ["SI unit of electrical capacitance.", "SI unit of electrical inductance.", "SI unit of magnetic flux density.", "SI unit of magnetic flux."],
        "wrong_hi": ["धारिता का सही मात्रक।", "प्रेरकत्व का मात्रक।", "चुंबकीय क्षेत्र का मात्रक।", "चुंबकीय फ्लक्स का मात्रक।"]
    },
    {
        "name_en": "Nuclear & Photometric Derived Units: Becquerel, Gray, Sievert, Lumen & Lux",
        "name_hi": "परमाणु विकिरण एवं प्रकाशमितीय व्युत्पन्न मात्रक: बेकेरल, ग्रे, सीवर्ट, ल्यूमेन एवं लक्स",
        "concepts_en": ["Radiation Metrology units (crucial distinction between source activity, absorbed dose, and biological risk):", "1. Becquerel (Bq): Radioactivity (decay rate) = 1 nuclear decay or disintegration per second (1 s⁻¹); replaces non-SI Curie (1 Ci = 3.7 × 10¹⁰ Bq)", "2. Gray (Gy): Absorbed radiation dose = energy absorbed per unit mass = 1 J·kg⁻¹ = 1 m²·s⁻² (physical physical dose absorbed by tissue)", "3. Sievert (Sv): Equivalent / Effective radiation dose = biological damage risk = 1 J·kg⁻¹ (absorbs dose multiplied by radiation weighting factor Q/WR); measure of human health hazard", "Photometric units:", "Lumen (lm): Luminous flux (total perceived light emitted = 1 cd·sr); Lux (lx): Illuminance (light falling on surface = 1 lm·m⁻²)"],
        "concepts_hi": ["परमाणु विकिरण मापिकी मात्रक (स्रोत की सक्रियता, अवशोषित मात्रा और जैविक खतरे में स्पष्ट अंतर):", "1. बेकेरल (Bq): रेडियोधर्मिता (क्षय दर) = 1 विखंडन प्रति सेकंड (1 disintegration/sec); पुराने क्यूरी मात्रक का स्थान लिया (1 Ci = 3.7 × 10¹⁰ Bq)", "2. ग्रे (Gy): अवशोषित विकिरण मात्रा = प्रति इकाई द्रव्यमान में अवशोषित ऊर्जा = 1 जूल/किग्रा (पदार्थ या ऊतक द्वारा ग्रहण की गई भौतिक मात्रा)", "3. सीवर्ट (Sv): प्रभावी जैविक विकिरण मात्रा (मानव स्वास्थ्य पर जैविक नुकसान का जोखिम) = 1 जूल/किग्रा (अवशोषित मात्रा × जैविक प्रभाव गुणांक); रेडिएशन सुरक्षा का मुख्य मात्रक", "प्रकाशमितीय मात्रक: ल्यूमेन (lm = ज्योति फ्लक्स) एवं लक्स (lx = प्रदीप्ति घनत्व = 1 ल्यूमेन/मी²)"],
        "q_en": "Which SI derived unit measures the 'Equivalent Radiation Dose' representing the stochastic biological health risk and damage of ionizing radiation to human tissue?",
        "q_hi": "मानव शरीर के ऊतकों पर आयनकारी विकिरण से होने वाले जैविक नुकसान और स्वास्थ्य जोखिम (प्रभावी विकिरण मात्रा) को मापने वाला मानक एसआई मात्रक कौन सा है?",
        "options_en": ["Sievert (सीवर्ट - Sv)", "Becquerel", "Gray", "Curie"],
        "options_hi": ["सीवर्ट (Sievert - Sv)", "बेकेरल (Becquerel - यह रेडियोधर्मी क्षय दर का मात्रक है)", "ग्रे (Gray - यह अवशोषित भौतिक विकिरण का मात्रक है)", "क्यूरी (Curie - यह गैर-एसआई पुराना मात्रक है)"],
        "correct_idx": 0,
        "exp_en": "The Sievert (Sv) is the SI unit for equivalent and effective dose, measuring the biological hazard of radiation on human health by factoring in the damaging power of different radiation types (alpha, beta, gamma).",
        "exp_hi": "विकिरण के जैविक खतरे और मानव स्वास्थ्य पर प्रभाव को 'सीवर्ट' (Sievert, Sv) में मापा जाता है। (बेकेरल नाभिकीय क्षय दर का और ग्रे अवशोषित ऊर्जा का मात्रक है)।",
        "cue_en": "Biological radiation risk unit = Sievert (Sv); Activity = Becquerel (Bq).",
        "cue_hi": "जैविक विकिरण खतरा = सीवर्ट; रेडियोधर्मी सक्रियता = बेकेरल।",
        "wrong_en": ["SI unit of biological radiation effect.", "SI unit of radioactive decay rate.", "SI unit of physically absorbed dose.", "Historical non-SI unit of radioactivity."],
        "wrong_hi": ["जैविक प्रभाव का सही मात्रक (सीवर्ट)।", "रेडियोधर्मिता का मात्रक।", "अवशोषित मात्रा का मात्रक।", "पुराना गैर-एसआई मात्रक।"]
    }
]

# S26-Ce9261bae SI Decimal Prefixes (Quetta to Quecto) & Metric-Imperial Conversions (3 topics)
DATA["S26-Ce9261bae"] = [
    {
        "name_en": "SI Decimal Prefixes: From Micro, Nano, Pico, Femto to Yotta, Ronna and Quetta",
        "name_hi": "एसआई दशमलव उपसर्ग: माइक्रो (10⁻⁶), नैनो, पिको, फेम्टो से लेकर योटा (10²⁴), रोना एवं क्वैटा (10³⁰)",
        "concepts_en": ["Submultiple prefixes (negative powers of 10): Deci (10⁻¹), Centi (10⁻²), Milli (10⁻³), Micro (10⁻⁶, μ), Nano (10⁻⁹, n), Pico (10⁻¹², p), Femto (10⁻¹⁵, f - Fermi size of atomic nucleus), Atto (10⁻¹⁸, a), Zepto (10⁻²¹, z), Yocto (10⁻²⁴, y), Ronto (10⁻²⁷, r, added 2022), Quecto (10⁻³⁰, q, added 2022)", "Multiple prefixes (positive powers of 10): Deka (10¹), Hecto (10²), Kilo (10³), Mega (10⁶, M), Giga (10⁹, G), Tera (10¹², T), Peta (10¹⁵, P), Exa (10¹⁸, E), Zetta (10²¹, Z), Yotta (10²⁴, Y), Ronna (10²⁷, R, added 2022), Quetta (10³⁰, Q, added 2022)", "Historic 27th CGPM (Versailles, November 2022) expansion: First additions in 31 years (since 1991) to meet data science and planetary science needs (Earth mass ≈ 6 ronnagrams, Jupiter mass ≈ 2 quettagrams)"],
        "concepts_hi": ["ऋणात्मक घात वाले सूक्ष्म उपसर्ग: डेसी (10⁻¹), सेंटी (10⁻²), मिली (10⁻³), माइक्रो (10⁻⁶, μ), नैनो (10⁻⁹, n), पिको (10⁻¹², p), फेम्टो (10⁻¹⁵, f - नाभिक का आकार फर्मी), अट्टो (10⁻¹⁸), जेप्टो (10⁻²¹), योक्टो (10⁻²⁴), रोन्टो (10⁻²⁷, r - 2022 में स्वीकृत), क्वेक्टो (10⁻³⁰, q - 2022 में स्वीकृत)", "धनात्मक घात वाले विशाल उपसर्ग: किलो (10³), मेगा (10⁶, M), गीगा (10⁹, G), टेरा (10¹², T), पेटा (10¹⁵, P), एक्सा (10¹⁸, E), ज़ेटा (10²¹), योटा (10²⁴, Y), रोना (10²⁷, R - 2022 में स्वीकृत), क्वैटा (10³⁰, Q - 2022 में स्वीकृत)", "2022 में 27वीं सीजीपीएम संगोष्ठी ने डेटा साइंस और खगोल विज्ञान की बढ़ती आवश्यकताओं के लिए 31 वर्षों बाद 4 नए उपसर्ग जोड़े"],
        "q_en": "What is the multiplicative scale factor represented by the standard SI decimal prefix 'Femto' (symbol: f), widely used to express the diameter of atomic nuclei (Femtometer / Fermi)?",
        "q_hi": "परमाणु के नाभिक के आकार (फर्मी/फेम्टोमीटर) को व्यक्त करने के लिए व्यापक रूप से प्रयुक्त होने वाले मानक एसआई दशमलव उपसर्ग 'फेम्टो' (Femto - f) का गणितीय मान 10 की कितनी घात के बराबर होता है?",
        "options_en": ["10⁻¹⁵ (दस की घात ऋण 15)", "10⁻¹² (यह पिको है)", "10⁻⁹ (यह नैनो है)", "10⁻¹⁸ (यह अट्टो है)"],
        "options_hi": ["10⁻¹⁵ (Ten raised to the power minus 15)", "10⁻¹² (Pico / पिको)", "10⁻⁹ (Nano / नैनो)", "10⁻¹⁸ (Atto / अट्टो)"],
        "correct_idx": 0,
        "exp_en": "The prefix 'femto-' represents a factor of 10⁻¹⁵ (one quadrillionth), derived from the Danish/Norwegian word 'femten' meaning fifteen. A femtometer (10⁻¹⁵ m) is universally called a Fermi.",
        "exp_hi": "फेम्टो (f) का मान 10⁻¹⁵ होता है। 1 फेम्टोमीटर (10⁻¹⁵ मीटर) को वैज्ञानिक एनरिको फर्मी के सम्मान में 1 'फर्मी' भी कहा जाता है, जो परमाणु नाभिक की त्रिज्या का पैमाना है।",
        "cue_en": "Femto = 10⁻¹⁵; Pico = 10⁻¹²; Nano = 10⁻⁹; Micro = 10⁻⁶.",
        "cue_hi": "फेम्टो = 10⁻¹⁵; पिको = 10⁻¹²; नैनो = 10⁻⁹; माइक्रो = 10⁻⁶।",
        "wrong_en": ["Femto scale factor (10⁻¹⁵).", "Pico scale factor (10⁻¹²).", "Nano scale factor (10⁻⁹).", "Atto scale factor (10⁻¹⁸)."],
        "wrong_hi": ["फेम्टो का सही मान (10⁻¹⁵)।", "पिको का मान (10⁻¹²)।", "नैनो का मान (10⁻⁹)।", "अट्टो का मान (10⁻¹⁸)।"]
    },
    {
        "name_en": "Metric vs Imperial System Conversions: Inches, Feet, Miles, Pounds, Gallons & Liters",
        "name_hi": "मीट्रिक बनाम इंपीरियल (ब्रिटिश) रूपांतरण: इंच, फीट, मील, पाउंड, गैलन एवं बैरल",
        "concepts_en": ["Length conversions:", "1 inch = exactly 2.54 cm = 0.0254 m (international yard and pound treaty 1959)", "1 foot = 12 inches = 30.48 cm; 1 yard = 3 feet = 36 inches = 0.9144 m", "1 statute mile = 1,760 yards = 5,280 feet ≈ 1.609344 km", "1 Nautical Mile (NM, maritime navigation based on one minute of latitude arc) = exactly 1,852 meters (1.852 km) ≈ 1.15 statute miles; 1 Knot = 1 Nautical Mile per hour ≈ 0.514 m/s", "Mass conversions: 1 pound (lb, avoirdupois) = 16 ounces (oz) = exactly 0.45359237 kg ≈ 453.6 g; 1 metric tonne = 1,000 kg ≈ 2,204.62 lbs", "Volume conversions: 1 US gallon = 3.785 liters; 1 Imperial (UK) gallon = 4.546 liters; 1 barrel of crude oil (bbl) = exactly 42 US gallons ≈ 158.987 liters"],
        "concepts_hi": ["लंबाई रूपांतरण:", "1 इंच = ठीक 2.54 सेमी = 0.0254 मीटर", "1 फीट = 12 इंच = 30.48 सेमी; 1 गज (Yard) = 3 फीट = 36 इंच = 0.9144 मीटर", "1 मील (Statute Mile) = 1,760 गज = 5,280 फीट ≈ 1.609 किलोमीटर", "1 समुद्री मील (Nautical Mile - नौवहन में अक्षांश के 1 मिनट का मान) = ठीक 1,852 मीटर (1.852 किमी); 1 नॉट (Knot) = 1 समुद्री मील प्रति घंटा की गति", "द्रव्यमान रूपांतरण: 1 पाउंड (lb) = 16 आउंस = ठीक 0.45359237 किग्रा ≈ 453.6 ग्राम; 1 मीट्रिक टन = 1,000 किग्रा", "आयतन रूपांतरण: 1 अमेरिकी गैलन = 3.785 लीटर; 1 ब्रिटिश (इंपीरियल) गैलन = 4.546 लीटर; कच्चे तेल का 1 बैरल (Barrel) = ठीक 42 यूएस गैलन ≈ 159 लीटर"],
        "q_en": "What is the exact standardized length of ONE NAUTICAL MILE, universally utilized in international maritime navigation and air traffic control?",
        "q_hi": "अंतर्राष्ट्रीय समुद्री नौवहन और विमानन यातायात में प्रयुक्त होने वाले 'एक समुद्री मील' (1 Nautical Mile) की मानक लंबाई कितने मीटर निर्धारित है?",
        "options_en": ["1,852 meters (1,852 मीटर / 1.852 किमी)", "1,609 meters (यह थलीय मील / Statute Mile है)", "2,000 meters", "1,500 meters"],
        "options_hi": ["1,852 मीटर (1,852 meters / 1.852 km)", "1,609 मीटर (यह सामान्य जमीनी मील है)", "2,000 मीटर", "1,500 मीटर"],
        "correct_idx": 0,
        "exp_en": "One Nautical Mile was standardized by the International Hydrographic Organization in 1929 at exactly 1,852 meters (approximately 1.1508 statute miles).",
        "exp_hi": "1 समुद्री मील (Nautical Mile) की अंतरराष्ट्रीय मानक लंबाई ठीक 1,852 मीटर (1.852 किमी) होती है, जो पृथ्वी के अक्षांश के 1 मिनट के चाप के बराबर होती है।",
        "cue_en": "1 Nautical Mile = 1,852 meters; 1 Statute Mile = 1,609 meters.",
        "cue_hi": "1 समुद्री मील = 1,852 मीटर; 1 थलीय मील = 1,609 मीटर।",
        "wrong_en": ["Standard international nautical mile.", "Standard statute land mile (1.609 km).", "Arbitrary rounded distance.", "Underestimated distance."],
        "wrong_hi": ["समुद्री मील का सही मान (1,852 मी.)।", "साधारण थलीय मील का मान।", "गलत मान।", "कम मान।"]
    },
    {
        "name_en": "Astronomical Distances & Scales: Astronomical Unit (AU), Light-Year & Parsec",
        "name_hi": "खगोलीय दूरियों के मात्रक: खगोलीय इकाई (AU), प्रकाश वर्ष (Light-Year) एवं पारसेक (Parsec)",
        "concepts_en": ["Astronomical Distances for cosmic scales beyond the solar system:", "1. Astronomical Unit (AU): Mean distance from the center of the Earth to the center of the Sun; defined by IAU in 2012 as exactly 149,597,870,700 meters ≈ 1.496 × 10¹¹ m (approx. 150 million km or 8.3 light-minutes)", "2. Light-Year (ly): Distance traversed by light in an absolute vacuum in one Julian year (365.25 days) = c × t = (299,792,458 m/s) × (31,557,600 s) ≈ 9.461 × 10¹⁵ meters ≈ 9.46 trillion kilometers (approx. 63,241 AU)", "3. Parsec (pc - Parallax of One Arcsecond): Distance at which a baseline of 1 AU subtends an angle of one arcsecond (1/3600 of a degree) = 1 AU / tan(1\") ≈ 3.0857 × 10¹⁶ meters ≈ 3.26 light-years (largest standard unit of cosmic distance used by professional astronomers; nearest star Proxima Centauri is at 1.30 pc = 4.24 ly)"],
        "concepts_hi": ["ब्रह्मांडीय दूरियों को मापने के तीन प्रमुख खगोलीय मात्रक:", "1. खगोलीय इकाई (AU - Astronomical Unit): पृथ्वी के केंद्र से सूर्य के केंद्र की औसत दूरी; अंतरराष्ट्रीय खगोलीय संघ (IAU) द्वारा निश्चित मान = 1.496 × 10¹¹ मीटर (लगभग 15 करोड़ किलोमीटर या 8.3 प्रकाश-मिनट)", "2. प्रकाश वर्ष (Light-Year): प्रकाश द्वारा निर्वात में एक जूलियन वर्ष (365.25 दिन) में तय की गई दूरी = चाल × समय ≈ 9.461 × 10¹⁵ मीटर (लगभग 9.46 लाख करोड़ किलोमीटर या 63,241 AU); यह दूरी का मात्रक है, समय का नहीं", "3. पारसेक (Parsec - पैरालैक्स सेकंड): खगोलीय दूरी का सबसे बड़ा व्यावहारिक मात्रक; वह दूरी जिस पर 1 AU का आधार 1 आर्कसेकंड का लंबन कोण बनाए = 3.0857 × 10¹⁶ मीटर ≈ 3.26 प्रकाश वर्ष (सूर्य का सबसे निकटतम तारा प्रॉक्सिमा सेंटॉरी 1.3 पारसेक या 4.24 प्रकाश वर्ष दूर है)"],
        "q_en": "Which of the following is the LARGEST astronomical unit of distance, equivalent to approximately 3.26 light-years or 3.086 × 10¹⁶ meters?",
        "q_hi": "खगोल भौतिकी में दूरी मापने का सबसे बड़ा मानक मात्रक कौन सा है, जो लगभग 3.26 प्रकाश वर्ष (3.086 × 10¹⁶ मीटर) के बराबर होता है?",
        "options_en": ["Parsec (पारसेक - Parallax Second)", "Light-Year (प्रकाश वर्ष)", "Astronomical Unit (AU)", "Fermi"],
        "options_hi": ["पारसेक (Parsec - 1 Parsec ≈ 3.26 प्रकाश वर्ष)", "प्रकाश वर्ष (Light-Year - 9.46 × 10¹⁵ मीटर)", "खगोलीय इकाई (Astronomical Unit - 1.496 × 10¹¹ मीटर)", "फर्मी (Fermi - यह नाभिक की अत्यंत छोटी दूरी है)"],
        "correct_idx": 0,
        "exp_en": "The Parsec (parallax second) is the largest standard cosmic distance unit, defined as 1 AU / tan(1 arcsecond) ≈ 3.26 light-years or 3.0857 × 10¹⁶ meters.",
        "exp_hi": "पारसेक (Parsec) खगोलीय दूरी का सबसे बड़ा मात्रक है; 1 पारसेक = 3.26 प्रकाश वर्ष = 3.086 × 10¹⁶ मीटर होता है। (प्रकाश वर्ष और AU इससे छोटे होते हैं)।",
        "cue_en": "Largest astronomical distance unit = Parsec (1 pc ≈ 3.26 ly).",
        "cue_hi": "दूरी का सबसे बड़ा खगोलीय मात्रक = पारसेक (3.26 प्रकाश वर्ष)।",
        "wrong_en": ["Largest unit (1 pc ≈ 3.26 ly).", "Smaller than parsec (9.46 × 10¹⁵ m).", "Earth-Sun distance (~1.496 × 10¹¹ m).", "Nuclear scale distance (10⁻¹⁵ m)."],
        "wrong_hi": ["सबसे बड़ा खगोलीय मात्रक।", "पारसेक से छोटा मात्रक।", "पृथ्वी-सूर्य की औसत दूरी।", "अति-सूक्ष्म दूरी का मात्रक।"]
    }
]

print("Loaded S26 successfully")
