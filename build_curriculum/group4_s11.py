# build_curriculum/group4_s11.py
# S11: General Science: Chemistry (10 topics across 2 chapters)

DATA = {}

# S11-C7bd7bee9 Atomic Structure, Chemical Bonding & Periodic Table (5 topics)
DATA["S11-C7bd7bee9"] = [
    {
        "name_en": "Atomic Models: Thomson, Rutherford, Bohr & Quantum Mechanical Model",
        "name_hi": "परमाणु मॉडल: थॉमसन, रदरफोर्ड, बोहर मॉडल एवं क्वांटम यांत्रिक मॉडल",
        "concepts_en": ["J.J. Thomson (1897): Discovered electron via cathode rays; Plum Pudding model", "Ernest Rutherford (1911): Gold foil alpha-particle scattering experiment; discovered tiny, dense, positively charged nucleus", "Niels Bohr (1913): Electrons revolve in discrete quantized stationary energy orbits without radiating energy (angular momentum mvr = nh/2π)", "Quantum Mechanical Model (Schrödinger): Wave mechanics; electrons described by orbital probability clouds and four quantum numbers (n, l, m, s)"],
        "concepts_hi": ["जे.जे. थॉमसन (1897): कैथोड किरणों द्वारा इलेक्ट्रॉन की खोज; तरबूज (प्लम पुडिंग) मॉडल", "अर्नेस्ट रदरफोर्ड (1911): स्वर्ण पत्री अल्फा-कण प्रकीर्णन प्रयोग; परमाणु के केंद्र में धनावेशित सघन 'नाभिक' (Nucleus) की खोज", "नील्स बोहर (1913): इलेक्ट्रॉन निश्चित क्वांटाइज्ड ऊर्जा स्तरों में बिना ऊर्जा खोए चक्कर लगाते हैं (कोणीय संवेग mvr = nh/2π)", "क्वांटम यांत्रिक मॉडल (श्रोडिंगर): तरंग यांत्रिकी; कक्षकों (Orbitals) में इलेक्ट्रॉन के पाए जाने की प्रायिकता एवं चार क्वांटम संख्याएं"],
        "q_en": "The existence of the atomic nucleus was experimentally demonstrated in 1911 through the famous gold foil alpha-particle scattering experiment conducted by:",
        "q_hi": "1911 में स्वर्ण पत्री पर अल्फा कणों के प्रकीर्णन के ऐतिहासिक प्रयोग द्वारा परमाणु के धनावेशित नाभिक (Nucleus) की खोज किसने की थी?",
        "options_en": ["Ernest Rutherford (अर्नेस्ट रदरफोर्ड)", "J.J. Thomson", "Niels Bohr", "James Chadwick"],
        "options_hi": ["अर्नेस्ट रदरफोर्ड (Ernest Rutherford)", "जे.जे. थॉमसन", "नील्स बोहर", "जेम्स चैडविक"],
        "correct_idx": 0,
        "exp_en": "Ernest Rutherford (along with Geiger and Marsden) bombarded thin gold foil with alpha particles, observing rare backward deflections that proved the existence of a dense positive nucleus.",
        "exp_hi": "रदरफोर्ड के अल्फा-कण प्रकीर्णन प्रयोग से पता चला कि अधिकांश अल्फा कण सीधे निकल गए किंतु कुछ 180 डिग्री पर वापस लौटे, जिससे परमाणु के केंद्र में अति-सूक्ष्म ठोस 'नाभिक' की खोज हुई।",
        "cue_en": "Discovered atomic nucleus = Ernest Rutherford (1911).",
        "cue_hi": "परमाणु नाभिक की खोज = अर्नेस्ट रदरफोर्ड।",
        "wrong_en": ["Discovered the atomic nucleus.", "Discovered electron (1897).", "Proposed quantized electron orbits (1913).", "Discovered neutron (1932)."],
        "wrong_hi": ["नाभिक के खोजकर्ता।", "इलेक्ट्रॉन के खोजकर्ता।", "क्वांटाइज्ड कक्षाओं का मॉडल दिया।", "न्यूट्रॉन के खोजकर्ता।"]
    },
    {
        "name_en": "Subatomic Particles: Protons, Neutrons, Electrons, Isotopes & Isobars",
        "name_hi": "अपरमाणुक कण: प्रोटॉन, न्यूट्रॉन, इलेक्ट्रॉन, समस्थानिक (Isotopes) एवं समभारिक (Isobars)",
        "concepts_en": ["Electron: Discovered by J.J. Thomson; negative charge -1.602×10⁻¹⁹ C, mass 9.109×10⁻³¹ kg", "Proton: Discovered by Eugen Goldstein (anode rays), identified by Rutherford; positive charge +1.602×10⁻¹⁹ C, mass ~1.673×10⁻²⁷ kg", "Neutron: Discovered by James Chadwick (1932); electrically neutral, mass ~1.675×10⁻²⁷ kg (heaviest subatomic particle)", "Isotopes: Same atomic number (Z), different mass number (A) (e.g., Protium ¹H, Deuterium ²H, Tritium ³H); Isobars: Same mass number (A), different atomic numbers (e.g., ⁴⁰Ar and ⁴⁰Ca)"],
        "concepts_hi": ["इलेक्ट्रॉन: थॉमसन द्वारा खोज; ऋणावेश -1.6×10⁻¹⁹ C, द्रव्यमान 9.1×10⁻³¹ किग्रा", "प्रोटॉन: गोल्डस्टीन (एनोड किरणें) व रदरफोर्ड; धनावेश +1.6×10⁻¹⁹ C, द्रव्यमान 1.673×10⁻²⁷ किग्रा", "न्यूट्रॉन: जेम्स चैडविक (1932) द्वारा खोज; विद्युत उदासीन, द्रव्यमान 1.675×10⁻²⁷ किग्रा (सबसे भारी मौलिक कण)", "समस्थानिक (Isotopes): समान परमाणु क्रमांक (Z) किंतु भिन्न द्रव्यमान संख्या (A) (जैसे हाइड्रोजन के तीन समस्थानिक: प्रोटियम, ड्यूटीरियम, ट्रिटियम)", "समभारिक (Isobars): समान द्रव्यमान संख्या किंतु भिन्न परमाणु क्रमांक (जैसे आर्गन-40 व कैल्शियम-40)"],
        "q_en": "Atoms of different chemical elements having the SAME mass number (A) but DIFFERENT atomic numbers (Z) are known in chemistry as:",
        "q_hi": "रसायन विज्ञान में विभिन्न तत्वों के वे परमाणु जिनकी द्रव्यमान संख्या (Mass Number) समान होती है किंतु परमाणु क्रमांक (Atomic Number) भिन्न होते हैं, क्या कहलाते हैं?",
        "options_en": ["Isobars (समभारिक)", "Isotopes (समस्थानिक)", "Isotones (समन्यूट्रॉनिक)", "Allotropes (अपररूप)"],
        "options_hi": ["समभारिक (Isobars)", "समस्थानिक (Isotopes)", "समन्यूट्रॉनिक (Isotones)", "अपररूप (Allotropes)"],
        "correct_idx": 0,
        "exp_en": "Isobars are nuclide species of different chemical elements having identical mass numbers (sum of protons and neutrons) but differing atomic numbers (e.g., Argon-40 and Calcium-40).",
        "exp_hi": "समभारिक (Isobars) वे परमाणु हैं जिनका भार (द्रव्यमान संख्या A) समान होता है लेकिन प्रोटॉनों की संख्या (परमाणु क्रमांक Z) भिन्न होती है।",
        "cue_en": "Same mass number = Isobars; Same atomic number = Isotopes.",
        "cue_hi": "समान द्रव्यमान = समभारिक; समान परमाणु क्रमांक = समस्थानिक।",
        "wrong_en": ["Same mass number, different atomic number.", "Same atomic number, different mass number.", "Same number of neutrons.", "Different physical forms of same element."],
        "wrong_hi": ["समान द्रव्यमान, भिन्न क्रमांक।", "समान क्रमांक, भिन्न द्रव्यमान।", "समान न्यूट्रॉन संख्या।", "एक ही तत्व के भिन्न भौतिक रूप।"]
    },
    {
        "name_en": "Chemical Bonding: Ionic, Covalent, Coordinate & Hydrogen Bonding",
        "name_hi": "रासायनिक बंधन: आयनिक (वैद्युत संयोजक), सहसंयोजक, उप-सहसंयोजक एवं हाइड्रोजन बंध",
        "concepts_en": ["Octet Rule (Lewis & Kossel): Atoms transfer or share valence electrons to achieve stable noble gas octet (8 valence electrons)", "Ionic (Electrovalent) Bond: Complete transfer of electrons from metal (cation) to non-metal (anion); strong electrostatic attraction, high melting/boiling points, conduct electricity in molten/aqueous state (e.g., NaCl, MgO)", "Covalent Bond: Mutual sharing of electron pairs between non-metals; single, double, triple bonds (e.g., H2O, CH4, CO2)", "Coordinate (Dative) Bond: Shared electron pair contributed by only one donor atom (e.g., NH4⁺, H3O⁺)", "Hydrogen Bond: Dipole attraction between hydrogen bonded to electronegative atom (F, O, N) and another electronegative atom (explains unusually high boiling point of water and DNA double-helix stability)"],
        "concepts_hi": ["अष्टक नियम (लुईस व कोसेल): उत्कृष्ट गैसों जैसा स्थाई विन्यास (8 संयोजी इलेक्ट्रॉन) पाने हेतु इलेक्ट्रॉनों का त्याग, ग्रहण या साझा करना", "आयनिक बंध: धातु से अधातु में इलेक्ट्रॉनों का पूर्ण स्थानांतरण; धनायन व ऋणायन के बीच मजबूत स्थिर-विद्युत आकर्षण; उच्च गलनांक/क्वथनांक; जलीय व गलित अवस्था में विद्युत के सुचालक (NaCl, MgO)", "सहसंयोजक बंध: अधातुओं के मध्य इलेक्ट्रॉनों का साझा (एकल, द्वि, त्रि-बंध; जैसे जल, मेथेन)", "उप-सहसंयोजक बंध: साझीदार इलेक्ट्रॉन युग्म केवल एक ही दाता परमाणु द्वारा दिया जाता है (जैसे अमोनियम आयन NH4⁺)", "हाइड्रोजन बंध: उच्च विद्युत-ऋणात्मक तत्व (F, O, N) से जुड़े हाइड्रोजन का आकर्षण (जल के उच्च क्वथनांक और डीएनए संरचना का आधार)"],
        "q_en": "Which unique intermolecular bond accounts for the surprisingly high boiling point of liquid water (100°C) and the open hexagonal lattice that makes ice less dense than water?",
        "q_hi": "जल के अप्रत्याशित रूप से उच्च क्वथनांक (100°C) तथा बर्फ के पानी पर तैरने (कम घनत्व) के लिए कौन सा विशिष्ट अंतराण्विक बंधन उत्तरदायी होता है?",
        "options_en": ["Hydrogen Bonding (हाइड्रोजन बंध)", "Covalent Bonding", "Metallic Bonding", "London Dispersion Forces"],
        "options_hi": ["हाइड्रोजन बंध (Hydrogen Bonding)", "सहसंयोजक बंध", "धात्विक बंध", "लंदन परिक्षेपण बल"],
        "correct_idx": 0,
        "exp_en": "Hydrogen bonds between the highly electronegative oxygen atom of one water molecule and the hydrogen atoms of neighboring molecules create a strong cohesive network, elevating water's boiling point and forming an open crystal lattice in ice.",
        "exp_hi": "जल के अणुओं के मध्य पाए जाने वाले मजबूत अंतराण्विक हाइड्रोजन बंध के कारण जल का क्वथनांक बहुत अधिक (100°C) होता है तथा बर्फ बनने पर जालीदार संरचना के कारण उसका घनत्व जल से कम हो जाता है।",
        "cue_en": "Water anomalies (high boiling point, floating ice) = Hydrogen Bonding.",
        "cue_hi": "जल का उच्च क्वथनांक व बर्फ का तैरना = हाइड्रोजन बंध।",
        "wrong_en": ["Responsible for water's high boiling point.", "Bonds within the molecule, not between.", "Bonds found in solid metals.", "Weak general Van der Waals attraction."],
        "wrong_hi": ["जल के असामान्य गुणों का कारण।", "अणु के भीतर का बंध।", "धातुओं का बंध।", "कमजोर आकर्षण बल।"]
    },
    {
        "name_en": "Modern Periodic Table: Mendeleev's Law, Moseley's Atomic Number & Periodic Trends",
        "name_hi": "आधुनिक आवर्त सारणी: मेंडलीफ का नियम, मोजले का परमाणु क्रमांक एवं आवर्ती प्रवृत्तियां",
        "concepts_en": ["Dmitri Mendeleev (1869): Periodic law based on atomic mass; predicted undiscovered elements (Eka-Boron = Scandium, Eka-Aluminium = Gallium, Eka-Silicon = Germanium)", "Henry Moseley (1913): Modern Periodic Law based on Atomic Number (Z); X-ray spectra proved Z is fundamental property", "Long Form Periodic Table: 7 Horizontal Periods, 18 Vertical Groups (s, p, d, f blocks)", "Periodic Trends: Atomic Radius decreases across a period (left to right) and increases down a group; Ionization Energy and Electronegativity increase across a period and decrease down a group (Fluorine is most electronegative element: 3.98 Pauling scale)"],
        "concepts_hi": ["दिमित्री मेंडलीफ (1869): परमाणु भार पर आधारित आवर्त नियम; अज्ञात तत्वों (एका-एल्युमीनियम = गैलियम, एका-सिलिकॉन = जर्मेनियम) की सफल भविष्यवाणी", "हेनरी मोजले (1913): आधुनिक आवर्त नियम - तत्वों के भौतिक व रासायनिक गुण उनके 'परमाणु क्रमांक' (Z) के आवर्ती फलन होते हैं", "दीर्घ आवर्त सारणी: 7 क्षैतिज आवर्त (Periods) एवं 18 ऊर्ध्वाधर वर्ग (Groups); s, p, d, f ब्लॉक में विभाजन", "आवर्ती प्रवृत्तियां: आवर्त में बाएं से दाएं जाने पर परमाणु त्रिज्या घटती है तथा आयनन विभव व विद्युत-ऋणात्मकता बढ़ती है; फ्लोरीन (F) पूरे आवर्त सारणी का सर्वाधिक विद्युत-ऋणात्मक तत्व है"],
        "q_en": "In the modern periodic table of elements, which chemical element possesses the HIGHEST electronegativity on the Pauling scale (value of 3.98)?",
        "q_hi": "आधुनिक आवर्त सारणी में पॉलिंग पैमाने पर किस रासायनिक तत्व की 'विद्युत-ऋणात्मकता' (Electronegativity) सर्वाधिक (3.98) होती है?",
        "options_en": ["Fluorine (फ्लोरीन - F)", "Chlorine (Cl)", "Oxygen (O)", "Cesium (Cs)"],
        "options_hi": ["फ्लोरीन (Fluorine - F)", "क्लोरीन (Chlorine - Cl)", "ऑक्सीजन (Oxygen - O)", "सीजियम (Cesium - Cs)"],
        "correct_idx": 0,
        "exp_en": "Fluorine is the most electronegative element in the periodic table (3.98 on the Pauling scale), exerting the strongest pull on shared bonding electron pairs. Chlorine has highest electron affinity.",
        "exp_hi": "फ्लोरीन (F) आवर्त सारणी का सर्वाधिक विद्युत-ऋणात्मक तत्व है। (ध्यान रहे: सर्वाधिक 'इलेक्ट्रॉन बंधुता' क्लोरीन की होती है, किंतु 'विद्युत-ऋणात्मकता' फ्लोरीन की ही सर्वाधिक होती है)।",
        "cue_en": "Highest electronegativity = Fluorine (F); Highest electron affinity = Chlorine (Cl).",
        "cue_hi": "सर्वाधिक विद्युत-ऋणात्मकता = फ्लोरीन; सर्वाधिक इलेक्ट्रॉन बंधुता = क्लोरीन।",
        "wrong_en": ["Highest electronegativity.", "Highest electron gain enthalpy (electron affinity).", "Second most electronegative element (3.44).", "Least electronegative (most electropositive)."],
        "wrong_hi": ["सर्वाधिक विद्युत-ऋणात्मक।", "सर्वाधिक इलेक्ट्रॉन बंधुता वाला।", "दूसरा सर्वाधिक विद्युत-ऋणात्मक तत्व।", "न्यूनतम विद्युत-ऋणात्मक (सर्वाधिक धनात्मक)।"]
    },
    {
        "name_en": "Radioactivity, Nuclear Isotopes in Medicine/Industry & Carbon-14 Dating",
        "name_hi": "रेडियोधर्मिता, चिकित्सा व उद्योग में रेडियोधर्मी समस्थानिक एवं कार्बन-14 डेटिंग",
        "concepts_en": ["Henri Becquerel (1896) discovered natural radioactivity; Marie and Pierre Curie discovered Polonium and Radium (Curie and Becquerel units)", "Carbon-14 Dating (Willard Libby, 1949): Half-life 5,730 years; dates organic archaeological artifacts up to ~50,000 years", "Medical Radioisotopes: Iodine-131 treats thyroid cancer; Cobalt-60 (gamma radiation) treats cancer tumors; Technetium-99m used in diagnostic organ imaging; Carbon-11/Fluorine-18 in PET scans", "Industrial: Uranium-235/Plutonium-239 for nuclear reactors; Americium-241 in smoke detectors"],
        "concepts_hi": ["हेनरी बेकेरल (1896) ने प्राकृतिक रेडियोधर्मिता की खोज की; मैरी क्यूरी व पियरे क्यूरी ने पोलोनियम व रेडियम की खोज की", "कार्बन-14 डेटिंग (विलार्ड लिब्बी, 1949): C-14 की अर्धायु 5,730 वर्ष है; लगभग 50,000 वर्ष तक के जीवाश्मों और काष्ठ नमूनों की आयु का निर्धारण", "चिकित्सा में उपयोगी समस्थानिक: आयोडीन-131 थायरॉयड (घेंघा/कैंसर) उपचार में; कोबाल्ट-60 कैंसर ट्यूमर के विकिरण उपचार में; टेक्नेशियम-99m नैदानिक इमेजिंग में", "सोडियम-24 रक्त परिसंचरण में रुकावट जांचने हेतु; आर्सेनिक-74 ट्यूमर का पता लगाने हेतु"],
        "q_en": "Which radioactive isotope is widely utilized in radiation oncology for teletherapy to destroy deep-seated malignant cancer tumors?",
        "q_hi": "कैंसर के घातक ट्यूमर को नष्ट करने हेतु विकिरण चिकित्सा (रेडियोथेरेपी) में मुख्य रूप से किस रेडियोधर्मी समस्थानिक का उपयोग किया जाता है?",
        "options_en": ["Cobalt-60 (कोबाल्ट-60)", "Iodine-131", "Carbon-14", "Sodium-24"],
        "options_hi": ["कोबाल्ट-60 (Cobalt-60)", "आयोडीन-131 (Iodine-131)", "कार्बन-14 (Carbon-14)", "सोडियम-24 (Sodium-24)"],
        "correct_idx": 0,
        "exp_en": "Cobalt-60 emits penetrating high-energy gamma rays (1.17 and 1.33 MeV), making it the gold standard radioisotope in external beam radiotherapy for cancer treatments.",
        "exp_hi": "कोबाल्ट-60 से तीव्र गामा किरणें निकलती हैं जिनका उपयोग कैंसर कोशिकाओं और ट्यूमर को नष्ट करने वाली रेडियोथेरेपी मशीनों में किया जाता है।",
        "cue_en": "Cancer radiotherapy = Cobalt-60; Thyroid cancer = Iodine-131.",
        "cue_hi": "कैंसर उपचार = कोबाल्ट-60; थायरॉयड उपचार = आयोडीन-131।",
        "wrong_en": ["Standard isotope for cancer radiotherapy.", "Used for thyroid disorders.", "Used for archaeological radiocarbon dating.", "Used to detect blood circulation clots."],
        "wrong_hi": ["कैंसर विकिरण चिकित्सा का समस्थानिक।", "थायरॉयड ग्रंथि के उपचार हेतु।", "जीवाश्मों की आयु निर्धारण हेतु।", "रक्त प्रवाह में थक्कों की जांच हेतु।"]
    }
]

# S11-C917a7c20 Acids, Bases, Salts, Metals, Non-Metals & Organic Compounds (5 topics)
DATA["S11-C917a7c20"] = [
    {
        "name_en": "Acids, Bases, pH Scale & Buffer Solutions",
        "name_hi": "अम्ल, क्षार, पीएच (pH) पैमाना एवं बफर विलयन",
        "concepts_en": ["Arrhenius: Acids produce H⁺ ions in water; Bases produce OH⁻ ions; Bronsted-Lowry: Acid is proton donor, base is proton acceptor; Lewis: Acid is electron-pair acceptor, base is electron-pair donor", "pH Scale (Sørensen 1909): pH = -log₁₀[H⁺]; pH 7 neutral, <7 acidic, >7 alkaline/basic", "Natural indicators: Litmus (lichen extract, turns red in acid, blue in base), turmeric, phenolphthalein (colorless in acid, pink in base)", "Natural acids: Formic/Methanoic acid in ant stings, Acetic acid in vinegar (5-8%), Citric acid in citrus fruits, Lactic acid in sour milk/curd, Tartaric acid in tamarind, Oxalic acid in tomatoes"],
        "concepts_hi": ["आर्रेनियस सिद्धांत: अम्ल जलीय विलयन में H⁺ देते हैं, क्षार OH⁻ देते हैं; ब्रान्स्टेड-लॉरी: अम्ल प्रोटॉन दाता, क्षार प्रोटॉन ग्राही; लुईस सिद्धांत: अम्ल इलेक्ट्रॉन युग्म ग्राही, क्षार इलेक्ट्रॉन युग्म दाता", "पीएच पैमाना (सोरेन्सन, 1909): pH = -log[H⁺]; pH 7 उदासीन, <7 अम्लीय, >7 क्षारीय (मानव रक्त का pH 7.35 से 7.45)", "प्राकृतिक सूचक: लिटमस (लाइकेन से प्राप्त; अम्ल में लाल, क्षार में नीला), हल्दी, फिनॉल्फथलीन (अम्ल में रंगहीन, क्षार में गुलाबी)", "प्राकृतिक अम्ल: चींटी के डंक में फॉर्मिक (मेथेनोइक) अम्ल, सिरके में एसीटिक अम्ल, नींबू में साइट्रिक अम्ल, दही में लैक्टिक अम्ल, इमली में टार्टरिक अम्ल, टमाटर में ऑक्सालिक अम्ल"],
        "q_en": "The painful irritation and burning sensation caused by the sting of an ant or a nettle leaf is due to the injection of which organic acid?",
        "q_hi": "लाल चींटी के काटने या बिच्छू-बूटी (Nettle) के डंक से होने वाली तीव्र जलन और दर्द किस कार्बनिक अम्ल के स्राव के कारण होता है?",
        "options_en": ["Methanoic Acid / Formic Acid (मेथेनोइक / फॉर्मिक अम्ल)", "Acetic Acid", "Tartaric Acid", "Lactic Acid"],
        "options_hi": ["मेथेनोइक अम्ल / फॉर्मिक अम्ल (Methanoic / Formic Acid)", "एसीटिक अम्ल", "टार्टरिक अम्ल", "लैक्टिक अम्ल"],
        "correct_idx": 0,
        "exp_en": "Ant venom contains methanoic acid (formic acid, HCOOH), which causes acute pain and inflammation, neutralized by applying a mild base like baking soda or calamine lotion.",
        "exp_hi": "चींटी और मधुमक्खी के डंक में फॉर्मिक अम्ल (मेथेनोइक अम्ल, HCOOH) होता है, जिसके प्रभाव को बेकिंग सोडा या कैलामाइन घोल (क्षार) लगाकर शांत किया जा सकता है।",
        "cue_en": "Ant sting = Formic Acid (Methanoic acid).",
        "cue_hi": "चींटी का डंक = फॉर्मिक अम्ल।",
        "wrong_en": ["Acid in ant venom.", "Acid in vinegar.", "Acid in tamarind and grapes.", "Acid in sour milk and curd."],
        "wrong_hi": ["चींटी के डंक का अम्ल।", "सिरके का अम्ल।", "इमली का अम्ल।", "दही का अम्ल।"]
    },
    {
        "name_en": "Common Industrial & Household Chemicals: Bleaching Powder, Plaster of Paris & Soda",
        "name_hi": "प्रमुख औद्योगिक व घरेलू रसायन: ब्लीचिंग पाउडर, प्लास्टर ऑफ पेरिस, बेकिंग व वाशिंग सोडा",
        "concepts_en": ["Baking Soda: Sodium Hydrogen Carbonate (NaHCO3), antacid, leavening agent releasing CO2 in bread/cakes, fire extinguishers", "Washing Soda: Sodium Carbonate Decahydrate (Na2CO3·10H2O), used in glass/soap manufacture and removing permanent hardness of water", "Bleaching Powder: Calcium Hypochlorite / Oxychloride (CaOCl2), prepared by reacting chlorine with dry slaked lime Ca(OH)2; disinfectant in water treatment and textile bleaching", "Plaster of Paris: Calcium Sulphate Hemihydrate (CaSO4·½H2O), made by heating gypsum (CaSO4·2H2O) to 373 K; sets into hard mass for orthopedic casts, statues, false ceilings"],
        "concepts_hi": ["बेकिंग सोडा (खाने का सोडा): सोडियम हाइड्रोजन कार्बोनेट (NaHCO3); एंटासिड, ब्रेड व केक में CO2 गैस उत्पन्न कर स्पंजी बनाना, अग्निशामक यंत्र", "वाशिंग सोडा (धावन सोडा): सोडियम कार्बोनेट डेकाहाइड्रेट (Na2CO3·10H2O); कांच व साबुन उद्योग, जल की स्थायी कठोरता दूर करना", "ब्लीचिंग पाउडर (विरंजक चूर्ण): कैल्शियम ऑक्सीक्लोराइड (CaOCl2); बुझे चूने Ca(OH)2 पर क्लोरीन की क्रिया से निर्मित; पेयजल को कीटाणुरहित करना व वस्त्र विरंजन", "प्लास्टर ऑफ पेरिस (POP): कैल्शियम सल्फेट हेमीहाइड्रेट (CaSO4·½H2O); जिप्सम (CaSO4·2H2O) को 373 K (100°C) पर गर्म करने से बनता है; टूटी हड्डियों के प्लास्टर व मूर्तियों में उपयोगी"],
        "q_en": "What is the correct chemical formula and chemical name of 'Plaster of Paris' (POP), widely used for setting fractured bones and creating decorative mouldings?",
        "q_hi": "टूटी हड्डियों को जोड़ने के लिए प्लास्टर चढ़ाने तथा मूर्तियां बनाने में प्रयुक्त 'प्लास्टर ऑफ पेरिस' (POP) का सही रासायनिक सूत्र और नाम क्या है?",
        "options_en": ["Calcium Sulphate Hemihydrate (CaSO4·½H2O)", "Calcium Sulphate Dihydrate (CaSO4·2H2O)", "Calcium Carbonate (CaCO3)", "Calcium Oxychloride (CaOCl2)"],
        "options_hi": ["कैल्शियम सल्फेट हेमीहाइड्रेट (CaSO4·½H2O)", "कैल्शियम सल्फेट डाइहाइड्रेट (CaSO4·2H2O - यह जिप्सम है)", "कैल्शियम कार्बोनेट (CaCO3 - संगमरमर/चूना पत्थर)", "कैल्शियम ऑक्सीक्लोराइड (CaOCl2 - ब्लीचिंग पाउडर)"],
        "correct_idx": 0,
        "exp_en": "Plaster of Paris is Calcium Sulphate Hemihydrate (CaSO4·½H2O). When mixed with water, it re-hydrates back into gypsum (CaSO4·2H2O), setting into a hard solid mass.",
        "exp_hi": "प्लास्टर ऑफ पेरिस का रासायनिक नाम कैल्शियम सल्फेट हेमीहाइड्रेट (अर्ध-हाइड्रेट) है जिसका सूत्र CaSO4·½H2O है। पानी मिलाने पर यह पुनः जिप्सम बनकर कड़ा हो जाता है।",
        "cue_en": "Plaster of Paris = CaSO4·½H2O (Gypsum = CaSO4·2H2O).",
        "cue_hi": "प्लास्टर ऑफ पेरिस = CaSO4·½H2O (जिप्सम = CaSO4·2H2O)।",
        "wrong_en": ["Chemical formula of Plaster of Paris.", "Formula of Gypsum.", "Formula of Limestone / Marble.", "Formula of Bleaching Powder."],
        "wrong_hi": ["प्लास्टर ऑफ पेरिस का सूत्र।", "जिप्सम का सूत्र।", "चूना पत्थर / संगमरमर।", "विरंजक चूर्ण (ब्लीचिंग पाउडर)।"]
    },
    {
        "name_en": "Metals, Non-Metals, Metalloids & Reactivity Series (Corrosion & Galvanization)",
        "name_hi": "धातु, अधातु, उपधातु, सक्रियता श्रेणी एवं संक्षारण (गैल्वनीकरण)",
        "concepts_en": ["Reactivity Series (descending order): K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au > Pt (Potassium and Sodium stored in kerosene)", "Corrosion of Iron (Rusting): Requires both oxygen and water (moisture); chemically Hydrated Ferric Oxide (Fe2O3·xH2O); mass of iron INCREASES upon rusting", "Galvanization: Coating steel or iron with a thin layer of Zinc (Zn) to prevent rusting, even if scratch occurs (sacrificial anode protection)", "Liquid elements at room temperature: Mercury (metal) and Bromine (non-metal); Gallium and Cesium melt in human palm (~30°C)"],
        "concepts_hi": ["सक्रियता श्रेणी: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au (पोटेशियम और सोडियम अत्यधिक क्रियाशील होने के कारण केरोसिन में रखे जाते हैं)", "लोहे पर जंग लगना (Rusting): ऑक्सीजन और नमी दोनों अनिवार्य; रासायनिक रूप से जलयोजित फेरिक ऑक्साइड (Fe2O3·xH2O); जंग लगने पर लोहे का भार 'बढ़' जाता है", "गैल्वनीकरण (यशदलेपन): लोहे को जंग से बचाने हेतु उस पर 'जस्ते' (Zinc) की पतली परत चढ़ाना", "कमरे के तापमान पर द्रव तत्व: पारा (पारा एकमात्र द्रव धातु है) और ब्रोमीन (एकमात्र द्रव अधातु है); गैलियम हथेली की गर्मी से पिघल जाती है"],
        "q_en": "In the metallurgical process of 'Galvanization' used to prevent iron and steel from rusting, which metal is coated over the iron surface?",
        "q_hi": "लोहे और इस्पात को जंग (संक्षारण) से बचाने के लिए 'गैल्वनीकरण' (यशदलेपन) की प्रक्रिया में किस धातु की पतली परत चढ़ाई जाती है?",
        "options_en": ["Zinc (जस्ता / Zn)", "Tin (टिन / Sn)", "Copper (तांबा / Cu)", "Lead (सीसा / Pb)"],
        "options_hi": ["जस्ता / जिंक (Zinc - Zn)", "टिन (Tin - Sn)", "तांबा (Copper - Cu)", "सीसा (Lead - Pb)"],
        "correct_idx": 0,
        "exp_en": "Galvanization involves coating iron with molten zinc. Zinc is more reactive than iron, so even if the surface is scratched, zinc acts as a sacrificial anode, oxidizing first to shield the iron.",
        "exp_hi": "गैल्वनीकरण में लोहे पर जस्ते (जिंक) की परत चढ़ाई जाती है; जिंक हवा से क्रिया कर जिंक ऑक्साइड की सुरक्षात्मक परत बना लेता है जिससे लोहे का संपर्क ऑक्सीजन व नमी से कट जाता है।",
        "cue_en": "Galvanization = Coating iron with Zinc (Zn).",
        "cue_hi": "गैल्वनीकरण = लोहे पर जस्ते (जिंक) का लेप।",
        "wrong_en": ["Metal used in galvanization.", "Used in tinning (canning food containers).", "Forms brass when alloyed with zinc.", "Heavy toxic metal."],
        "wrong_hi": ["यशदलेपन में प्रयुक्त धातु।", "टिनिंग (डिब्बे के लेपन) में प्रयुक्त।", "तांबा।", "सीसा।"]
    },
    {
        "name_en": "Allotropes of Carbon: Diamond, Graphite, Fullerenes & Graphene",
        "name_hi": "कार्बन के अपररूप: हीरा, ग्रेफाइट, फुलरीन (बकीबॉल) एवं ग्राफीन",
        "concepts_en": ["Diamond: Tetrahedral sp³ hybridization; each C bonded to 4 others in rigid 3D covalent network; hardest natural substance, electrical insulator, excellent thermal conductor", "Graphite: Hexagonal planar layers sp² hybridization; each C bonded to 3 others; free delocalized pi electrons make it an excellent electrical conductor; soft, slippery layers held by weak Van der Waals forces (used in pencil leads and solid lubricants)", "Fullerenes (Buckminsterfullerene C60): Geodesic spherical cage containing 20 hexagons and 12 pentagons (Kroto, Smalley, Curl Nobel Prize 1996)", "Graphene: Single 2D hexagonal atomic monolayer of carbon; exceptionally strong (200× stronger than steel), ballistic electrical conductivity"],
        "concepts_hi": ["हीरा (Diamond): sp³ संकरण, समचतुष्फलकीय 3D दृढ़ जाल; प्रत्येक कार्बन 4 अन्य कार्बनों से जुड़ा; प्रकृति का सबसे कठोरतम ज्ञात पदार्थ, विद्युत का कुचालक, ऊष्मा का सुचालक", "ग्रेफाइट (Graphite): sp² संकरण, षट्कोणीय परतदार संरचना; प्रत्येक कार्बन 3 अन्य कार्बनों से जुड़ा; एक मुक्त गतिशील इलेक्ट्रॉन की उपस्थिति के कारण 'विद्युत का उत्तम सुचालक'; परतों के बीच कमजोर वांडर वाल्स बल होने से चिकना व मुलायम (पेंसिल की लेड व शुष्क स्नेहक)", "फुलरीन (बकमिनिस्टर फुलरीन C60): 60 कार्बनों का फुटबॉल जैसा पिंजड़ा (20 षट्कोण व 12 पंचकोण); 1996 का नोबेल पुरस्कार", "ग्राफीन (Graphene): कार्बन परमाणुओं की एकल द्वि-आयामी (2D) षट्कोणीय चादर; इस्पात से 200 गुना मजबूत व अतिचालक"],
        "q_en": "Why is Graphite an exceptional electrical conductor while Diamond, another pure allotrope of carbon, is an electrical insulator?",
        "q_hi": "ग्रेफाइट विद्युत का एक उत्कृष्ट सुचालक क्यों है, जबकि शुद्ध कार्बन का ही दूसरा अपररूप हीरा विद्युत का पूर्ण कुचालक होता है?",
        "options_en": ["Graphite has delocalized free electrons due to sp² hybridization, while diamond has all 4 valence electrons locked in sp³ covalent bonds", "Graphite contains metallic impurities", "Diamond possesses an ionic crystal lattice", "Graphite undergoes spontaneous ionization"],
        "options_hi": ["ग्रेफाइट में sp² संकरण के कारण स्वतंत्र (डिलोकलाइज्ड) इलेक्ट्रॉन होते हैं, जबकि हीरे में सभी 4 इलेक्ट्रॉन sp³ बंधों में बंधे होते हैं", "ग्रेफाइट में धातु की अशुद्धियां पाई जाती हैं", "हीरे में आयनिक क्रिस्टल जालक होता है", "ग्रेफाइट स्वतः आयनित हो जाता है"],
        "correct_idx": 0,
        "exp_en": "In graphite, each carbon bonds to only 3 adjacent carbons in hexagonal planes, leaving one free valence electron per atom that moves freely through the sheets to conduct electricity.",
        "exp_hi": "ग्रेफाइट में प्रत्येक कार्बन केवल तीन कार्बनों से जुड़ता है, जिससे प्रत्येक परमाणु पर एक मुक्त इलेक्ट्रॉन बच जाता है जो परत के आर-पार स्वतंत्र गति कर विद्युत धारा प्रवाहित करता है। हीरे में सभी 4 इलेक्ट्रॉन बंधे होते हैं।",
        "cue_en": "Graphite conducts electricity due to free delocalized electrons (sp²).",
        "cue_hi": "ग्रेफाइट सुचालक है = मुक्त इलेक्ट्रॉन (sp² संकरण)।",
        "wrong_en": ["Fundamental electronic reason for conductivity.", "Graphite is pure carbon.", "Diamond is purely covalent.", "It does not ionize."],
        "wrong_hi": ["विद्युत चालकता का सही इलेक्ट्रॉनिक कारण।", "ग्रेफाइट शुद्ध कार्बन है।", "हीरा सहसंयोजक है, आयनिक नहीं।", "यह आयनित नहीं होता।"]
    },
    {
        "name_en": "Hydrocarbons, Synthetic Polymers & Soaps vs Detergents",
        "name_hi": "हाइड्रोकार्बन, संश्लेषित बहुलक (पॉलिमर) एवं साबुन बनाम अपमार्जक (Detergents)",
        "concepts_en": ["Alkanes (Saturated, C_n H_2n+2; Methane CH4 'Marsh Gas' major component of CNG and Biogas), Alkenes (C_n H_2n), Alkynes (C_n H_2n-2, Ethyne/Acetylene in welding)", "Polymers: Addition polymers (Polythene, Teflon / PTFE used in non-stick cookware, Polyvinyl Chloride PVC); Condensation polymers (Nylon-6,6, Bakelite thermosetting plastic for electrical switches)", "Soaps: Sodium/potassium salts of long-chain fatty acids (stearic, palmitic acid); form scum (insoluble precipitate) in hard water containing Ca²⁺ and Mg²⁺ ions", "Detergents: Sodium salts of alkyl benzene sulphonates; do NOT form scum and lather effectively even in hard water"],
        "concepts_hi": ["एल्केन (संतृप्त, C_n H_2n+2): मेथेन (CH4) को 'मार्श गैस' कहते हैं (सीएनजी और बायोगैस का मुख्य घटक); एल्कीन (असंतृप्त द्वि-बंध); एल्काइन (त्रि-बंध, एसिटिलीन वेल्डिंग में प्रयुक्त)", "बहुलक (Polymers): टेफ्लॉन (PTFE - नॉन-स्टिक बर्तनों की कोटिंग में); बेकेलाइट (थर्मोसेटिंग प्लास्टिक, बिजली के स्विच व बर्तनों के हैंडल बनाने में); नायलॉन-6,6", "साबुन (Soaps): लंबी श्रृंखला वाले वसीय अम्लों के सोडियम/पोटेशियम लवण; कठोर जल (कैल्शियम व मैग्नीशियम लवण) में झाग नहीं देते बल्कि मैल (Scum) बनाते हैं", "अपमार्जक (Detergents / सर्फ): सल्फोनिक अम्लों के सोडियम लवण; कठोर जल में भी आसानी से भरपूर झाग देते हैं"],
        "q_en": "Which heat-resistant, chemically inert fluoropolymer is coated onto domestic cookware to manufacture non-stick frying pans?",
        "q_hi": "घरेलू रसोई के 'नॉन-स्टिक' (ना चिपकने वाले) बर्तनों पर किस रासायनिक रूप से अक्रिय बहुलक (पॉलिमर) की परत चढ़ाई जाती है?",
        "options_en": ["Teflon (Polytetrafluoroethylene / PTFE)", "Bakelite", "PVC (Polyvinyl Chloride)", "Polystyrene"],
        "options_hi": ["टेफ्लॉन / पीटीएफई (Teflon / PTFE)", "बेकेलाइट (Bakelite)", "पीवीसी (PVC)", "पॉलीस्टायरीन (Polystyrene)"],
        "correct_idx": 0,
        "exp_en": "Teflon (polytetrafluoroethylene or PTFE) has an extremely low coefficient of friction and high heat resistance, making it the universal choice for non-stick cooking surfaces.",
        "exp_hi": "टेफ्लॉन (पॉलीटेट्राफ्लोरोएथिलीन / PTFE) पर तेल या पानी नहीं चिपकता और यह उच्च तापमान सह सकता है; इसलिए नॉन-स्टिक फ्राइंग पैन पर इसका लेप किया जाता है।",
        "cue_en": "Non-stick cookware coating = Teflon (PTFE).",
        "cue_hi": "नॉन-स्टिक बर्तन कोटिंग = टेफ्लॉन।",
        "wrong_en": ["Coating for non-stick utensils.", "Thermosetting plastic for electrical plugs.", "Plastic used for water pipes and raincoats.", "Used for styrofoam cups and packaging."],
        "wrong_hi": ["नॉन-स्टिक बर्तनों का बहुलक।", "बिजली के स्विचों का थर्मोसेटिंग प्लास्टिक।", "पानी के पाइपों का प्लास्टिक।", "पैकिंग थर्माकोल।"]
    }
]

print("Loaded S11 successfully")
