# build_curriculum/group7_s23.py
# S23: Global Currencies, Trade & Commerce (12 topics across 3 chapters)

DATA = {}

# S23-C864e59f4 Indian Currency: Legal Tender, Demonetization & RBI Security Features (6 topics)
DATA["S23-C864e59f4"] = [
    {
        "name_en": "Indian Rupee Currency System: Coinage Act, Legal Tender & One Rupee Note Exception",
        "name_hi": "भारतीय रुपया मुद्रा प्रणाली: सिक्का निर्माण अधिनियम, वैध मुद्रा (लीगल टेंडर) एवं एक रुपये के नोट का अपवाद",
        "concepts_en": ["Indian Rupee (INR / ₹ symbol designed by D. Udaya Kumar in 2010 blending Devanagari 'र' and Roman capital 'R' without stem)", "Section 22 of RBI Act 1934 gives Reserve Bank of India sole right to issue banknotes in India (denominations of ₹2, ₹5, ₹10, ₹20, ₹50, ₹100, ₹200, ₹500, ₹2000 - signed by RBI Governor)", "Critical Exception: ₹1 note and all coins are issued directly by the Ministry of Finance (Government of India) under Coinage Act 2011, and the ₹1 note bears the signature of the FINANCE SECRETARY (not the RBI Governor)", "Legal Tender: Money that cannot be refused by a creditor in satisfaction of debt; limited legal tender (coins up to ₹1,000) vs unlimited legal tender (currency notes)"],
        "concepts_hi": ["भारतीय रुपया (INR / ₹ प्रतीक चिह्न 2010 में डी. उदय कुमार द्वारा देवनागरी 'र' और रोमन 'R' को मिलाकर डिजाइन किया गया)", "भारतीय रिज़र्व बैंक अधिनियम 1934 की धारा 22 के तहत ₹2 से लेकर ₹2000 तक के सभी बैंक नोट जारी करने का एकाधिकार केवल RBI के पास है (इन पर रिज़र्व बैंक के गवर्नर के हस्ताक्षर होते हैं)", "महत्वपूर्ण अपवाद: ₹1 का नोट और सभी सिक्के भारत सरकार के 'वित्त मंत्रालय' द्वारा जारी किए जाते हैं, और ₹1 के नोट पर 'वित्त सचिव' (Finance Secretary) के हस्ताक्षर होते हैं, न कि RBI गवर्नर के", "वैध मुद्रा (Legal Tender): जिसे कर्ज के भुगतान में स्वीकार करने से कोई इनकार नहीं कर सकता; सीमित वैध मुद्रा (सिक्के ₹1000 तक) बनाम असीमित वैध मुद्रा (बैंक नोट)"],
        "q_en": "Under Indian monetary law, whose official signature is affixed to the Government of India's ONE RUPEE (₹1) currency note, distinguishing it from all higher denomination banknotes?",
        "q_hi": "भारतीय मौद्रिक व्यवस्था के तहत भारत सरकार द्वारा जारी किए जाने वाले 'एक रुपये' (₹1) के करेंसी नोट पर किसके आधिकारिक हस्ताक्षर होते हैं?",
        "options_en": ["Finance Secretary of India (वित्त सचिव, भारत सरकार)", "Governor of the Reserve Bank of India", "Union Finance Minister", "Prime Minister of India"],
        "options_hi": ["वित्त सचिव (Finance Secretary, भारत सरकार)", "भारतीय रिज़र्व बैंक के गवर्नर (RBI Governor)", "केंद्रीय वित्त मंत्री", "भारत के प्रधानमंत्री"],
        "correct_idx": 0,
        "exp_en": "Under the Coinage Act and RBI Act, the ₹1 note is technically an asset issued by the Government of India rather than a promissory bank note, bearing the signature of the Union Finance Secretary.",
        "exp_hi": "एक रुपये का नोट भारत सरकार का सिक्का-समतुल्य नोट है जिस पर केंद्रीय 'वित्त सचिव' के हस्ताक्षर होते हैं, जबकि ₹2 से लेकर ₹2000 तक के सभी नोटों पर RBI गवर्नर के हस्ताक्षर होते हैं।",
        "cue_en": "₹1 note signature = Finance Secretary; other notes = RBI Governor.",
        "cue_hi": "₹1 के नोट पर हस्ताक्षर = वित्त सचिव; अन्य नोटों पर = RBI गवर्नर।",
        "wrong_en": ["Signatory of ₹1 currency note.", "Signatory of all notes from ₹2 to ₹2000.", "Head of Ministry of Finance.", "Head of Government."],
        "wrong_hi": ["₹1 के नोट के हस्ताक्षरकर्ता।", "₹2 से ₹2000 के नोटों के हस्ताक्षरकर्ता।", "वित्त मंत्रालय के राजनीतिक प्रमुख।", "शासन प्रमुख।"]
    },
    {
        "name_en": "Banknote Printing Presses & Government Mints in India: Nashik, Dewas, Salboni, Mysore",
        "name_hi": "भारत में बैंक नोट प्रिंटिंग प्रेस एवं सरकारी टकसालें: नासिक, देवास, मैसूर, सालबोनी व 4 टकसालें",
        "concepts_en": ["Four Banknote Printing Presses in India:", "1. Two under SPMCIL (Security Printing and Minting Corporation of India Ltd, GoI): CNP Nashik (Maharashtra, established 1928) and BNP Dewas (Madhya Pradesh, 1974)", "2. Two under BRBNMPL (Bharatiya Reserve Bank Note Mudran Private Ltd, wholly-owned subsidiary of RBI established 1995): Mysore (Karnataka) and Salboni (West Bengal)", "Four Government Mints (producing coins): Mumbai (Maharashtra - diamond mint mark ◆), Kolkata (West Bengal - NO mint mark), Hyderabad (Telangana - star mint mark ★), and Noida (Uttar Pradesh - round dot mint mark •)", "Security Paper Mill: Hoshangabad / Narmadapuram (Madhya Pradesh) manufactures security paper"],
        "concepts_hi": ["भारत में 4 बैंक नोट प्रिंटिंग प्रेस:", "1. दो प्रेस SPMCIL (भारत सरकार) के अधीन: नासिक (महाराष्ट्र, 1928 में स्थापित) एवं देवास (मध्य प्रदेश, 1974)", "2. दो प्रेस BRBNMPL (भारतीय रिज़र्व बैंक की सहायक कंपनी) के अधीन: मैसूर (कर्नाटक) एवं सालबोनी (पश्चिम बंगाल)", "भारत की 4 सरकारी टकसालें (सिक्का निर्माण स्थल) व उनके पहचान चिह्न:", "1. मुंबई (हीरा/डायमंड चिह्न ◆), 2. कोलकाता (कोई चिह्न नहीं), 3. हैदराबाद (तारा/स्टार चिह्न ★), 4. नोएडा (गोल बिंदु/डॉट चिह्न •)", "सिक्योरिटी पेपर मिल: नर्मदापुरम / होशंगाबाद (मध्य प्रदेश) जहां नोटों के लिए विशेष कागज बनता है"],
        "q_en": "If an Indian circulation coin has a small Five-Pointed Star (★) stamped beneath the year of manufacture, at which of the four Government of India Mints was it minted?",
        "q_hi": "यदि किसी भारतीय सिक्के पर निर्माण वर्ष (Year) के नीचे एक छोटा 'तारा' या फाइव-पॉइंटेड स्टार (★) का टकसाल चिह्न अंकित हो, तो उस सिक्के की ढलाई किस सरकारी टकसाल में हुई है?",
        "options_en": ["Hyderabad Mint (हैदराबाद टकसाल - स्टार चिह्न ★)", "Mumbai Mint (डायमंड चिह्न ◆)", "Noida Mint (डॉट चिह्न •)", "Kolkata Mint (कोई चिह्न नहीं)"],
        "options_hi": ["हैदराबाद टकसाल (Hyderabad Mint - स्टार चिह्न ★)", "मुंबई टकसाल (Mumbai Mint - डायमंड चिह्न ◆)", "नोएडा टकसाल (Noida Mint - डॉट चिह्न •)", "कोलकाता टकसाल (Kolkata Mint - कोई टकसाल चिह्न नहीं)"],
        "correct_idx": 0,
        "exp_en": "Each Indian mint has a unique mint mark: Mumbai = Diamond (◆), Hyderabad = Star (★), Noida = Solid Round Dot (•), and Kolkata = No mint mark beneath the date.",
        "exp_hi": "भारतीय सिक्कों पर टकसाल के प्रतीक: हैदराबाद = तारा (★), मुंबई = हीरा (◆), नोएडा = गोल बिंदी (•) और कोलकाता = बिना किसी निशान के।",
        "cue_en": "Coin mint marks: Hyderabad = Star; Mumbai = Diamond; Noida = Dot; Kolkata = None.",
        "cue_hi": "सिक्कों के टकसाल चिह्न: हैदराबाद = तारा; मुंबई = डायमंड; नोएडा = बिंदु; कोलकाता = कोई नहीं।",
        "wrong_en": ["Hyderabad Mint mark (Star).", "Mumbai Mint mark (Diamond).", "Noida Mint mark (Round Dot).", "Kolkata Mint mark (Blank / No mark)."],
        "wrong_hi": ["हैदराबाद का टकसाल चिह्न।", "मुंबई का चिह्न (डायमंड)।", "नोएडा का चिह्न (डॉट)।", "कोलकाता (बिना चिह्न)।"]
    },
    {
        "name_en": "Mahatma Gandhi New Banknote Series (2016): Denominations, Colors & Cultural Heritage Reverse Motifs",
        "name_hi": "महात्मा गांधी नई बैंक नोट श्रृंखला (2016): मूल्यवर्ग, रंग एवं पिछले भाग पर अंकित भारतीय सांस्कृतिक धरोहरें",
        "concepts_en": ["Mahatma Gandhi (New) Series introduced post-demonetization in November 2016, highlighting India's scientific and cultural heritage on the reverse:", "₹10: Chocolate Brown; Reverse motif is Sun Temple, Konark (Odisha)", "₹20: Greenish Yellow; Reverse motif is Ellora Caves (Maharashtra)", "₹50: Fluorescent Blue; Reverse motif is Stone Chariot of Hampi (Karnataka)", "₹100: Lavender; Reverse motif is Rani ki Vav (Queen's Stepwell at Patan, Gujarat)", "₹200: Bright Yellow; Reverse motif is Sanchi Stupa (Madhya Pradesh)", "₹500: Stone Grey; Reverse motif is Red Fort (Delhi)", "₹2000 (withdrawn in 2023): Magenta; Reverse motif was Mangalyaan (Mars Orbiter Mission)"],
        "concepts_hi": ["महात्मा गांधी (नई) बैंक नोट श्रृंखला (नवंबर 2016 से प्रारंभ); नोटों के पिछले भाग पर भारत के यूनेस्को विश्व धरोहर स्थलों व स्मारकों के रूपांकन (Motifs) अंकित हैं:", "₹10 का नोट: चॉकलेट ब्राउन रंग; कोणार्क का सूर्य मंदिर (ओडिशा)", "₹20 का नोट: हरा-पीला रंग; एलोरा की गुफाएं (महाराष्ट्र)", "₹50 का नोट: फ्लोरोसेंट नीला रंग; हम्पी का पत्थर का रथ (कर्नाटक)", "₹100 का नोट: लैवेंडर रंग; रानी की वाव (पाटन, गुजरात की सीढ़ीदार बावड़ी)", "₹200 का नोट: चमकीला पीला रंग; सांची का महान बौद्ध स्तूप (मध्य प्रदेश)", "₹500 का नोट: स्टोन ग्रे रंग; लाल किला (नई दिल्ली)", "₹2000 का नोट (2023 में चलन से वापस): मैजेंटा रंग; मंगलयान (Mangalyaan)"],
        "q_en": "Which famous UNESCO World Heritage architectural monument is featured as the primary reverse motif on the Lavender-colored Mahatma Gandhi (New) Series ₹100 banknote?",
        "q_hi": "महात्मा गांधी (नई) श्रृंखला के लैवेंडर रंग वाले ₹100 के नए बैंक नोट के पिछले भाग (Reverse) पर भारत की किस प्रसिद्ध यूनेस्को विश्व धरोहर बावड़ी का चित्र अंकित है?",
        "options_en": ["Rani ki Vav, Patan, Gujarat (रानी की वाव, पाटन, गुजरात)", "Sun Temple, Konark", "Hampi Stone Chariot", "Sanchi Stupa"],
        "options_hi": ["रानी की वाव, पाटन, गुजरात (Rani ki Vav - ₹100 के नोट पर)", "सूर्य मंदिर, कोणार्क (यह ₹10 के नोट पर है)", "हम्पी का रथ (यह ₹50 के नोट पर है)", "सांची का स्तूप (यह ₹200 के नोट पर है)"],
        "correct_idx": 0,
        "exp_en": "The reverse of the ₹100 banknote depicts 'Rani ki Vav' (Queen's Stepwell) in Patan, Gujarat, inscribed as a UNESCO World Heritage site in 2014.",
        "exp_hi": "₹100 के नए नोट के पीछे गुजरात के पाटन में स्थित 11वीं सदी की सोलंकी कालीन सीढ़ीदार बावड़ी 'रानी की वाव' का चित्र है।",
        "cue_en": "₹100 note reverse = Rani ki Vav (Patan, Gujarat).",
        "cue_hi": "₹100 के नोट पर = रानी की वाव (गुजरात)।",
        "wrong_en": ["Reverse motif on ₹100 note.", "Reverse motif on ₹10 note.", "Reverse motif on ₹50 note.", "Reverse motif on ₹200 note."],
        "wrong_hi": ["₹100 के नोट का रूपांकन।", "₹10 के नोट का रूपांकन।", "₹50 के नोट का रूपांकन।", "₹200 के नोट का रूपांकन।"]
    },
    {
        "name_en": "Advanced Anti-Counterfeiting Security Features in Currency Notes: Watermark, Security Thread & Intaglio",
        "name_hi": "बैंक नोटों में जालसाजी-रोधी सुरक्षा विशेषताएं: वॉटरमार्क, सुरक्षा धागा, ऑप्टिकली वेरिएबल इंक एवं दृष्टिहीनों हेतु पहचान चिह्न",
        "concepts_en": ["Multi-tier security features designed to prevent counterfeiting:", "1. Mahatma Gandhi Portrait & Electrotype Watermark: Visible when held against light with multi-directional shades", "2. Security Thread: Windowed color-shifting thread that transitions from green to blue when tilted; inscribed with 'भारत' and 'RBI'", "3. Optically Variable Ink (OVI): Denomination numeral '500' printed on front with color-shifting ink (shifts green to blue under tilt)", "4. Latent Image: Hidden denomination numeral visible only when held horizontally at eye level", "5. Intaglio Raised Printing: Raised tactile print of Ashoka Pillar emblem and Bleed Lines on borders (e.g., 5 bleed lines on ₹500, 4 on ₹200) enabling visually impaired persons to identify denomination by touch"],
        "concepts_hi": ["नकली नोटों की रोकथाम हेतु आधुनिक सुरक्षा विशेषताएं:", "1. वॉटरमार्क: प्रकाश के सामने रखने पर महात्मा गांधी का चित्र और सूक्ष्म इलेक्ट्रोप्रकार मूल्यवर्ग स्पष्ट दिखाई देता है", "2. सुरक्षा धागा (Security Thread): आंशिक रूप से बाहर दिखने वाला धागा, जिसे तिरछा करने पर रंग हरे से नीला बदलता है और 'भारत' व 'RBI' लिखा दिखता है", "3. ऑप्टिकली वेरिएबल इंक (OVI): ₹500 के अंक पर प्रयुक्त स्याही जो नोट झुकाने पर हरे से नीले रंग में बदल जाती है", "4. प्रच्छन्न छवि (Latent Image): नोट को आंख के स्तर पर क्षैतिज रखने पर दिखने वाला छुपा हुआ अंक", "5. उत्कीर्ण मुद्रण (Intaglio Printing) एवं ब्लीड लाइनें: उभरी हुई छपाई और किनारों पर स्पर्श रेखाएं (जैसे ₹500 पर 5 रेखाएं, ₹200 पर 4 रेखाएं) जिससे दृष्टिबाधित लोग छूकर नोट पहचान सकें"],
        "q_en": "Which optical security feature on modern high-denomination Indian banknotes causes the printed denomination numerals to change color from GREEN to BLUE when the banknote is tilted?",
        "q_hi": "आधुनिक उच्च मूल्यवर्ग के भारतीय बैंक नोटों पर वह कौन सी सुरक्षा विशेषता है, जिसके कारण नोट को तिरछा करने पर छपे हुए मूल्यवर्ग अंक का रंग हरे (Green) से बदलकर नीले (Blue) में परिवर्तित हो जाता है?",
        "options_en": ["Optically Variable Ink / Color-Shifting Ink (ऑप्टिकली वेरिएबल इंक)", "Fluorescent Fibers", "Electrotype Watermark", "Micro-lettering"],
        "options_hi": ["ऑप्टिकली वेरिएबल इंक (Optically Variable Ink - रंग बदलने वाली स्याही)", "प्रतिदीप्त फाइबर (Fluorescent Fibers)", "इलेक्ट्रोप्रकार वॉटरमार्क", "सूक्ष्म अक्षर (Micro-lettering)"],
        "correct_idx": 0,
        "exp_en": "Optically Variable Ink (OVI) printed on the denomination numeral changes color dynamically from green to blue when viewed at different tilt angles, acting as an infallible anti-copying measure.",
        "exp_hi": "ऑप्टिकली वेरिएबल इंक (रंग बदलने वाली स्याही) का प्रयोग ₹500 के नोट पर मूल्यवर्ग संख्या लिखने में किया जाता है, जो नोट को थोड़ा सा झुकाने पर हरे से नीले रंग में बदल जाती है।",
        "cue_en": "Color shift green to blue = Optically Variable Ink (OVI).",
        "cue_hi": "हरा से नीला रंग बदलना = ऑप्टिकली वेरिएबल इंक।",
        "wrong_en": ["Color-shifting security ink.", "Fibers embedded in paper visible under UV.", "Translucent watermark.", "Tiny readable lettering."],
        "wrong_hi": ["रंग बदलने वाली सुरक्षा स्याही।", "पराबैंगनी प्रकाश में दिखने वाले फाइबर।", "पारभासी वॉटरमार्क।", "माइक्रो अक्षर।"]
    },
    {
        "name_en": "History of Demonetization in India: 1946, 1978 & 2016 Economic Impact",
        "name_hi": "भारत में विमुद्रीकरण (नोटबंदी) का इतिहास: 1946, 1978 एवं 2016 के आर्थिक प्रभाव",
        "concepts_en": ["Demonetization: The official stripping of a currency unit of its status as legal tender", "First Demonetization (January 1946): British Raj government demonetized ₹1,000 and ₹10,000 notes to curb wartime black marketing and tax evasion; re-introduced in 1954 along with ₹5,000 notes", "Second Demonetization (January 16, 1978): Janata Party government under Prime Minister Morarji Desai demonetized high-denomination notes of ₹1,000, ₹5,000, and ₹10,000 via High Denomination Bank Notes (Demonetisation) Act 1978 (RBI Governor I.G. Patel had opposed it)", "Third Demonetization (November 8, 2016): Prime Minister Narendra Modi announced the withdrawal of ₹500 and ₹1,000 notes of the Mahatma Gandhi series (which constituted 86.4% of total currency in circulation by value); aims: eliminate black money, counter fake currency, choke terror financing, and promote digital payments"],
        "concepts_hi": ["विमुद्रीकरण (नोटबंदी): किसी मुद्रा इकाई की वैध मुद्रा (लीगल टेंडर) के रूप में आधिकारिक मान्यता समाप्त करना", "प्रथम विमुद्रीकरण (जनवरी 1946): ब्रिटिश सरकार द्वारा द्वितीय विश्व युद्ध के दौरान जमा किए गए काले धन पर लगाम लगाने हेतु ₹1000 और ₹10,000 के नोट बंद किए गए (1954 में पुनः चालू किए गए)", "द्वितीय विमुद्रीकरण (16 जनवरी 1978): मोरारजी देसाई की जनता पार्टी सरकार द्वारा ₹1,000, ₹5,000 और ₹10,000 के बड़े नोटों का विमुद्रीकरण किया गया (तत्कालीन RBI गवर्नर आई.जी. पटेल इससे असहमत थे)", "तृतीय विमुद्रीकरण (8 नवंबर 2016): प्रधानमंत्री नरेंद्र मोदी द्वारा राष्ट्र के नाम संबोधन में ₹500 और ₹1000 के पुराने नोटों को बंद करने की घोषणा (यह चलन में कुल मुद्रा का 86.4% था); उद्देश्य: काला धन समाप्त करना, जाली नोटों पर रोक, आतंकवाद के वित्तपोषण पर प्रहार व डिजिटल लेनदेन को बढ़ावा"],
        "q_en": "On which exact date did Prime Minister Narendra Modi announce the historic demonetization of ₹500 and ₹1,000 banknotes, withdrawing 86.4% of India's circulating currency value overnight?",
        "q_hi": "प्रधानमंत्री नरेंद्र मोदी ने किस ऐतिहासिक तारीख को रात 8 बजे राष्ट्र के नाम संबोधन में ₹500 और ₹1,000 के नोटों को बंद करने (विमुद्रीकरण) की घोषणा की थी?",
        "options_en": ["November 8, 2016 (8 नवंबर 2016)", "October 2, 2016", "December 31, 2016", "January 16, 2017"],
        "options_hi": ["8 नवंबर 2016 (November 8, 2016)", "2 अक्टूबर 2016", "31 दिसंबर 2016", "16 जनवरी 2017"],
        "correct_idx": 0,
        "exp_en": "On the evening of November 8, 2016, the Government of India announced that all ₹500 and ₹1,000 banknotes of the Mahatma Gandhi series would cease to be legal tender from midnight.",
        "exp_hi": "8 नवंबर 2016 की रात 8 बजे तत्कालीन ₹500 और ₹1000 के नोटों के विमुद्रीकरण की घोषणा की गई थी, जो आधी रात से प्रभावी हो गई थी।",
        "cue_en": "2016 Demonetization date = November 8, 2016.",
        "cue_hi": "2016 नोटबंदी की तारीख = 8 नवंबर 2016।",
        "wrong_en": ["Official date of 2016 demonetization.", "Gandhi Jayanti.", "New Year's Eve.", "Morarji Desai demonetization anniversary."],
        "wrong_hi": ["नोटबंदी की सही तारीख।", "गांधी जयंती।", "वर्ष का अंतिम दिन।", "गलत तारीख।"]
    },
    {
        "name_en": "Central Bank Digital Currency (CBDC): Digital Rupee (e₹-R and e₹-W) & Blockchain Concepts",
        "name_hi": "केंद्रीय बैंक डिजिटल मुद्रा (CBDC): डिजिटल रुपया (e₹-रिटेल एवं e₹-होलसेल) एवं सॉवरेन डिजिटल टोकन",
        "concepts_en": ["Central Bank Digital Currency (CBDC): Sovereign legal tender issued by a central bank in digital form, appearing as a direct liability on the central bank's balance sheet (unlike commercial bank deposits or decentralized cryptocurrencies)", "Digital Rupee (e₹) launched by Reserve Bank of India in 2022:", "1. Wholesale CBDC (e₹-W): Launched November 1, 2022 for secondary market transactions in government securities among designated financial institutions", "2. Retail CBDC (e₹-R): Pilot launched December 1, 2022 as an electronic token representing physical currency for general public and merchants (operates via digital token wallets with zero credit risk, interoperable with UPI QR codes)", "Advantages: Eliminates physical printing/distribution costs, prevents counterfeiting, provides real-time cross-border settlements"],
        "concepts_hi": ["केंद्रीय बैंक डिजिटल मुद्रा (CBDC): किसी देश के केंद्रीय बैंक द्वारा जारी की जाने वाली आधिकारिक कानूनी डिजिटल मुद्रा, जो सीधे केंद्रीय बैंक की बैलेंस शीट पर संप्रभु देनदारी होती है (यह बिटकॉइन या निजी क्रिप्टोकरेंसी जैसी नहीं है)", "आरबीआई द्वारा 2022 में 'डिजिटल रुपया' (e₹) का प्रायोगिक शुभारंभ:", "1. e₹-होलसेल (e₹-W): 1 नवंबर 2022 को बैंकों और वित्तीय संस्थानों के बीच सरकारी प्रतिभूतियों के निपटान हेतु शुरू", "2. e₹-रिटेल (e₹-R): 1 दिसंबर 2022 को आम जनता और व्यापारियों के लिए डिजिटल टोकन के रूप में शुरू (यह मोबाइल वॉलेट में रहता है और यूपीआई क्यूआर कोड के साथ एकीकृत है)", "लाभ: नोटों की छपाई और वितरण की विशाल लागत की बचत, सुरक्षित लेनदेन और विदेशी प्रेषण में आसानी"],
        "q_en": "What is the official nomenclature for the Central Bank Digital Currency (CBDC) launched in pilot phases by the Reserve Bank of India in late 2022?",
        "q_hi": "2022 के अंत में भारतीय रिज़र्व बैंक (RBI) द्वारा प्रायोगिक तौर पर शुरू की गई भारत की आधिकारिक केंद्रीय बैंक डिजिटल मुद्रा (CBDC) का नाम क्या रखा गया है?",
        "options_en": ["Digital Rupee / e-Rupee (डिजिटल रुपया / e₹)", "Bharat Coin", "CryptoRupee", "RBI DigiCash"],
        "options_hi": ["डिजिटल रुपया (Digital Rupee / e-Rupee - e₹)", "भारत कॉइन (Bharat Coin)", "क्रिप्टोरुपया (CryptoRupee)", "आरबीआई डिजीकैश (DigiCash)"],
        "correct_idx": 0,
        "exp_en": "The Reserve Bank of India officially designated its Central Bank Digital Currency as the 'Digital Rupee' (abbreviated as e₹, with retail variant e₹-R and wholesale variant e₹-W).",
        "exp_hi": "भारतीय रिज़र्व बैंक की डिजिटल मुद्रा का नाम 'डिजिटल रुपया' (Digital Rupee या e₹) है, जो भौतिक नोटों का डिजिटल विकल्प है और कानूनी निविदा का पूर्ण दर्जा रखता है।",
        "cue_en": "India's CBDC = Digital Rupee (e₹).",
        "cue_hi": "भारत की CBDC = डिजिटल रुपया (e₹)।",
        "wrong_en": ["Official RBI digital currency name.", "Fictitious cryptocurrency name.", "Unofficial term.", "Commercial banking product."],
        "wrong_hi": ["आरबीआई की आधिकारिक डिजिटल मुद्रा।", "काल्पनिक नाम।", "अनौपचारिक शब्द।", "वाणिज्यिक उत्पाद।"]
    }
]

# S23-C2d861ea1 Major World Currencies, Central Banks & Foreign Exchange Reserves (5 topics)
DATA["S23-C2d861ea1"] = [
    {
        "name_en": "Global Reserve Currencies & IMF Special Drawing Rights (SDR) Currency Basket",
        "name_hi": "वैश्विक रिज़र्व मुद्राएं एवं अंतर्राष्ट्रीय मुद्रा कोष (IMF) का विशेष आहरण अधिकार (SDR) बास्केट",
        "concepts_en": ["Special Drawing Rights (SDR): Supplementary international reserve asset created by the International Monetary Fund (IMF) in 1969; allocated to member nations based on IMF quotas (XDR)", "SDR Valuation Basket: Value determined daily based on a basket of five major world reserve currencies meeting export criteria and freely usable criteria:", "1. US Dollar (USD - largest weight ~43.38%)", "2. Euro (EUR - second largest weight ~29.31%)", "3. Chinese Renminbi / Yuan (RMB / CNY - included in October 2016, weight ~12.28%)", "4. Japanese Yen (JPY - weight ~7.59%)", "5. British Pound Sterling (GBP - weight ~7.44%)", "US Dollar remains dominant global reserve currency (~58% of global allocated forex reserves)"],
        "concepts_hi": ["विशेष आहरण अधिकार (SDR): अंतर्राष्ट्रीय मुद्रा कोष (IMF) द्वारा 1969 में बनाया गया अंतरराष्ट्रीय पूरक रिज़र्व परिसंपत्ति (आईएमएफ कोटा के आधार पर आवंटित)", "एसडीआर बास्केट में शामिल 5 वैश्विक मुद्राएं (SDR Currency Basket):", "1. अमेरिकी डॉलर (USD - सर्वाधिक भार ~43.38%)", "2. यूरो (EUR - दूसरा सबसे बड़ा भार ~29.31%)", "3. चीनी रॅन्मिन्बी / युआन (RMB - अक्टूबर 2016 में शामिल किया गया, भार ~12.28%)", "4. जापानी येन (JPY - भार ~7.59%)", "5. ब्रिटिश पाउंड स्टर्लिंग (GBP - भार ~7.44%)", "अमेरिकी डॉलर आज भी विश्व के कुल विदेशी मुद्रा भंडार का लगभग 58% हिस्सा रखता है"],
        "q_en": "Which major national currency was formally included in October 2016 by the International Monetary Fund (IMF) as the fifth currency in the Special Drawing Rights (SDR) elite valuation basket?",
        "q_hi": "अक्टूबर 2016 में अंतर्राष्ट्रीय मुद्रा कोष (IMF) द्वारा विशेष आहरण अधिकार (SDR) के संभ्रांत मुद्रा बास्केट में पांचवीं मुद्रा के रूप में किस देश की मुद्रा को शामिल किया गया था?",
        "options_en": ["Chinese Renminbi / Yuan (चीनी रॅन्मिन्बी / युआन)", "Indian Rupee", "Swiss Franc", "Russian Ruble"],
        "options_hi": ["चीनी रॅन्मिन्बी / युआन (Chinese Renminbi / Yuan)", "भारतीय रुपया (Indian Rupee)", "स्विस फ्रैंक (Swiss Franc)", "रूसी रूबल (Russian Ruble)"],
        "correct_idx": 0,
        "exp_en": "On October 1, 2016, the IMF added the Chinese Renminbi (Yuan) to the SDR basket alongside the US dollar, Euro, Japanese yen, and British pound, recognizing China's rise in global trade.",
        "exp_hi": "1 अक्टूबर 2016 को आईएमएफ ने चीन की मुद्रा 'रॅन्मिन्बी (युआन)' को अपने एसडीआर बास्केट में शामिल किया, जिससे वह डॉलर, यूरो, येन और पाउंड के साथ पांचवीं वैश्विक आरक्षित मुद्रा बनी।",
        "cue_en": "5th SDR basket currency (added 2016) = Chinese Renminbi (Yuan).",
        "cue_hi": "एसडीआर बास्केट में 2016 में जुड़ी 5वीं मुद्रा = चीनी युआन।",
        "wrong_en": ["Fifth SDR basket currency added in 2016.", "Not included in SDR basket.", "Safe-haven currency not in SDR basket.", "Not included in SDR basket."],
        "wrong_hi": ["2016 में शामिल चीनी मुद्रा।", "एसडीआर में शामिल नहीं।", "एसडीआर में शामिल नहीं।", "एसडीआर में शामिल नहीं।"]
    },
    {
        "name_en": "Major Central Banks of the World: Federal Reserve, ECB, Bank of England & Bank of Japan",
        "name_hi": "विश्व के प्रमुख केंद्रीय बैंक: फेडरल रिज़र्व (US), यूरोपीय सेंट्रल बैंक (ECB), बैंक ऑफ इंग्लैंड एवं बैंक ऑफ जापान",
        "concepts_en": ["Central Bank Functions: Monopoly on banknote issuance, lender of last resort, setting benchmark policy interest rates, managing national foreign exchange reserves, targeting inflation", "Federal Reserve System (The Fed, USA): Created by Federal Reserve Act 1913; 12 regional Fed Banks; governed by Federal Reserve Board of Governors; Federal Open Market Committee (FOMC) sets federal funds rate", "European Central Bank (ECB): Established 1998 in Frankfurt, Germany; sets monetary policy for the Eurozone; manages Euro currency", "Bank of England (The Old Lady of Threadneedle Street): Founded 1694 in London; one of the oldest central banks; Monetary Policy Committee (MPC) sets Bank Rate", "Bank of Japan (Nippon Ginko): Founded 1882 in Tokyo; pioneered quantitative easing (QE) and yield curve control (YCC)"],
        "concepts_hi": ["केंद्रीय बैंकों के प्रमुख कार्य: मुद्रा निर्गमन का एकाधिकार, अंतिम ऋणदाता (Lender of Last Resort), बेंचमार्क नीतिगत ब्याज दरें तय करना, मुद्रास्फीति नियंत्रण एवं विदेशी मुद्रा प्रबंधन", "फेडरल रिज़र्व (The Fed - अमेरिका): 1913 के अधिनियम द्वारा स्थापित; फेडरल ओपन मार्केट कमेटी (FOMC) वैश्विक रूप से महत्वपूर्ण ब्याज दरें तय करती है", "यूरोपीय सेंट्रल बैंक (ECB): 1998 में फ्रैंकफर्ट (जर्मनी) में स्थापित; 20 देशों के यूरोज़ोन की मौद्रिक नीति का संचालन करता है", "बैंक ऑफ इंग्लैंड (Bank of England): 1694 में लंदन में स्थापित; 'द ओल्ड लेडी ऑफ थ्रेडनीडल स्ट्रीट' के नाम से विख्यात", "बैंक ऑफ जापान: 1882 में टोक्यो में स्थापित; लंबे समय तक नकारात्मक ब्याज दर और क्वांटिटेटिव ईजिंग का प्रयोग किया"],
        "q_en": "In which German financial capital city is the headquarters of the European Central Bank (ECB), the central monetary authority of the Eurozone, situated?",
        "q_hi": "यूरोज़ोन की सर्वोच्च मौद्रिक संस्था 'यूरोपीय सेंट्रल बैंक' (ECB) का मुख्यालय जर्मनी के किस प्रमुख वित्तीय नगर में स्थित है?",
        "options_en": ["Frankfurt am Main, Germany (फ्रैंकफर्ट, जर्मनी)", "Berlin", "Brussels", "Munich"],
        "options_hi": ["फ्रैंकफर्ट, जर्मनी (Frankfurt am Main, Germany)", "बर्लिन (जर्मनी की राजधानी)", "ब्रुसेल्स (बेल्जियम - यूरोपीय संघ का प्रशासनिक मुख्यालय)", "म्यूनिख"],
        "correct_idx": 0,
        "exp_en": "The European Central Bank (ECB) has its seat in Frankfurt am Main, Germany, responsible for monetary policy and banking supervision across the 20 European Union nations that have adopted the Euro.",
        "exp_hi": "यूरोपीय सेंट्रल बैंक (ECB) का मुख्यालय फ्रैंकफर्ट (जर्मनी) में स्थित है। (यूरोपीय संघ की संसद ब्रुसेल्स और स्ट्रासबर्ग में है)।",
        "cue_en": "European Central Bank (ECB) headquarters = Frankfurt, Germany.",
        "cue_hi": "यूरोपीय सेंट्रल बैंक (ECB) मुख्यालय = फ्रैंकफर्ट, जर्मनी।",
        "wrong_en": ["Headquarters city of ECB.", "Capital of Germany.", "Administrative headquarters of European Commission.", "Capital of Bavaria."],
        "wrong_hi": ["ईसीबी का मुख्यालय नगर।", "जर्मनी की राजनीतिक राजधानी।", "यूरोपीय आयोग का मुख्यालय।", "बवेरिया की राजधानी।"]
    },
    {
        "name_en": "Foreign Exchange Reserves: Foreign Currency Assets, Gold, SDRs & Reserve Tranche Position",
        "name_hi": "विदेशी मुद्रा भंडार (Forex Reserves): विदेशी मुद्रा परिसंपत्तियां (FCA), स्वर्ण, एसडीआर एवं रिज़र्व ट्रेंच स्थिति (RTP)",
        "concepts_en": ["Foreign Exchange Reserves of India managed by the Reserve Bank of India under Section 19 of the RBI Act 1934", "Four Official Components of India's Forex Reserves:", "1. Foreign Currency Assets (FCA - largest component ~85-90%): Holdings in foreign banknotes, deposits with foreign central banks, and treasury bills in major global currencies (USD, EUR, GBP, JPY)", "2. Gold: Physical gold reserves held by RBI (stored at RBI vaults in Nagpur and Mumbai, and Bank of England vaults)", "3. Special Drawing Rights (SDR): Supplementary reserve assets held with the IMF", "4. Reserve Tranche Position (RTP): India's quota subscription with the IMF available on demand without conditionality", "India ranks among the top 4-5 countries globally with forex reserves exceeding $650 billion (2024), behind China, Japan, and Switzerland"],
        "concepts_hi": ["भारत का विदेशी मुद्रा भंडार (Forex Reserves): भारतीय रिज़र्व बैंक (RBI) द्वारा प्रबंधित; बाहरी आर्थिक झटकों से रुपये और अर्थव्यवस्था को सुरक्षा प्रदान करता है", "भारत के विदेशी मुद्रा भंडार के 4 मुख्य घटक:", "1. विदेशी मुद्रा परिसंपत्तियां (FCA - सबसे बड़ा घटक, लगभग 85-90%): प्रमुख वैश्विक मुद्राओं (डॉलर, यूरो, पाउंड, येन) में सरकारी बॉन्ड व विदेशी बैंकों में जमा", "2. स्वर्ण भंडार (Gold Reserves): आरबीआई के पास भौतिक सोने का भंडार (नागपुर व मुंबई के वॉल्ट तथा बैंक ऑफ इंग्लैंड में सुरक्षित)", "3. विशेष आहरण अधिकार (SDR): आईएमएफ के पास आरक्षित एसडीआर टोकन", "4. रिज़र्व ट्रेंच स्थिति (RTP): आईएमएफ में भारत के कोटा का वह हिस्सा जिसे आपातकाल में बिना किसी शर्त के तुरंत निकाला जा सकता है", "भारत चीन, जापान और स्विट्जरलैंड के बाद विश्व के शीर्ष 4 विदेशी मुद्रा भंडार वाले देशों में शामिल है ($650+ अरब डॉलर)"],
        "q_en": "Which of the following constitutes the LARGEST component (typically over 85%) of India's total Foreign Exchange Reserves held by the Reserve Bank of India?",
        "q_hi": "भारतीय रिज़र्व बैंक द्वारा रखे जाने वाले भारत के कुल विदेशी मुद्रा भंडार (Forex Reserves) का सबसे बड़ा घटक (सामान्यतः 85% से अधिक) कौन सा होता है?",
        "options_en": ["Foreign Currency Assets / FCA (विदेशी मुद्रा परिसंपत्तियां)", "Gold Reserves", "Special Drawing Rights (SDR)", "Reserve Tranche Position in the IMF (RTP)"],
        "options_hi": ["विदेशी मुद्रा परिसंपत्तियां (Foreign Currency Assets - FCA)", "स्वर्ण भंडार (Gold Reserves - दूसरा घटक)", "विशेष आहरण अधिकार (SDR)", "आईएमएफ में रिज़र्व ट्रेंच स्थिति (RTP)"],
        "correct_idx": 0,
        "exp_en": "Foreign Currency Assets (FCA), consisting of multi-currency assets invested in foreign government bonds and deposits, form the dominant lion's share of India's foreign exchange reserves.",
        "exp_hi": "विदेशी मुद्रा परिसंपत्तियां (FCA) भारत के विदेशी मुद्रा भंडार का सबसे विशाल हिस्सा (~85-90%) होती हैं, जिसमें मुख्य रूप से अमेरिकी डॉलर, यूरो और ब्रिटिश पाउंड में रखी संपत्तियां शामिल हैं।",
        "cue_en": "Largest forex component = Foreign Currency Assets (FCA).",
        "cue_hi": "विदेशी मुद्रा भंडार का सबसे बड़ा अंग = विदेशी मुद्रा परिसंपत्तियां (FCA)।",
        "wrong_en": ["Dominant component of forex reserves.", "Second largest component (~7-10%).", "Small multilateral reserve component.", "Emergency quota tranche with IMF."],
        "wrong_hi": ["सबसे बड़ा घटक (FCA)।", "दूसरा घटक (सोना)।", "छोटा बहुपक्षीय घटक।", "आईएमएफ ट्रेंच।"]
    },
    {
        "name_en": "Exchange Rate Regimes: Fixed, Floating, Managed Float (Dirty Float) & Currency Depreciation vs Devaluation",
        "name_hi": "विनिमय दर प्रणालियां: स्थिर दर, लचीली दर, प्रबंधित फ्लोट (डर्टी फ्लोट) एवं अवमूल्यन बनाम ह्रास",
        "concepts_en": ["Exchange Rate: Price of one currency expressed in terms of another currency", "Exchange Rate Systems: 1. Fixed / Pegged Rate (currency pegged to anchor currency like USD or gold; maintained by continuous central bank intervention), 2. Freely Floating Rate (determined purely by market forces of supply and demand without government intervention), 3. Managed Float / Dirty Float (market-driven floating rate where central bank intervenes periodically by buying/selling dollars to curb excessive volatility without targeting a specific level - followed by India/RBI)", "Depreciation vs Devaluation: Depreciation is market-driven drop in currency value due to supply-demand forces under floating regime; Devaluation is deliberate government/central bank policy decision to reduce domestic currency value under fixed regime", "Purchasing Power Parity (PPP): Theory that exchange rates adjust so identical basket of goods costs the same in different currencies (Big Mac Index)"],
        "concepts_hi": ["विनिमय दर: एक देश की मुद्रा का दूसरे देश की मुद्रा के संदर्भ में मूल्य", "विनिमय दर प्रणालियां: 1. स्थिर दर (Fixed/Pegged - सरकार द्वारा किसी अन्य मुद्रा या सोने से बांधना), 2. स्वतंत्र रूप से तैरती दर (Freely Floating - केवल बाजार की मांग और आपूर्ति द्वारा निर्धारित), 3. प्रबंधित फ्लोट / डर्टी फ्लोट (Managed Float - बाजार आधारित प्रणाली जिसमें अत्यधिक उतार-चढ़ाव को रोकने के लिए केंद्रीय बैंक डॉलर खरीदता या बेचता है - भारत की प्रणाली)", "मूल्यह्रास (Depreciation) बनाम अवमूल्यन (Devaluation): मूल्यह्रास बाजार की ताकतों से मुद्रा के मूल्य में गिरावट है; जबकि अवमूल्यन सरकार द्वारा जानबूझकर अपनी मुद्रा का आधिकारिक मूल्य घटाना है (ताकि निर्यात बढ़े और आयात घटे)", "क्रय शक्ति समता (PPP): विभिन्न देशों में समान वस्तुओं की टोकरी की क्रय क्षमता के आधार पर तुलना (बिग मैक इंडेक्स)"],
        "q_en": "What is the crucial economic difference between 'Currency Depreciation' and 'Currency Devaluation'?",
        "q_hi": "अर्थशास्त्र में 'मुद्रा का ह्रास' (Depreciation) और 'मुद्रा का अवमूल्यन' (Devaluation) के बीच क्या मूलभूत अंतर होता है?",
        "options_en": ["Depreciation is driven by market supply-demand forces under a floating regime, whereas Devaluation is a deliberate government policy action under a fixed regime (ह्रास बाजार की मांग-आपूर्ति से होता है जबकि अवमूल्यन सरकार द्वारा जानबूझकर किया जाता है)", "Depreciation increases export prices while Devaluation decreases them", "Devaluation occurs automatically while Depreciation is ordered by the central bank", "They are identical terms with no economic difference"],
        "options_hi": ["ह्रास बाजार की मांग-आपूर्ति से होता है, जबकि अवमूल्यन सरकार द्वारा जानबूझकर आधिकारिक रूप से किया जाता है", "ह्रास से निर्यात महंगा होता है जबकि अवमूल्यन से सस्ता", "अवमूल्यन स्वतः होता है जबकि ह्रास का आदेश केंद्रीय बैंक देता है", "दोनों पूर्णतः एक ही हैं"],
        "correct_idx": 0,
        "exp_en": "Under floating exchange rate systems, market forces cause currency Depreciation. Under fixed or pegged regimes, a deliberate official downward adjustment of the exchange rate by the monetary authority is called Devaluation.",
        "exp_hi": "फ्लोटिंग सिस्टम में जब बाजार में मांग घटने से रुपया गिरता है तो उसे 'मूल्यह्रास' (Depreciation) कहते हैं। जब सरकार आधिकारिक आदेश से जानबूझकर अपनी मुद्रा का मूल्य घटाती है तो उसे 'अवमूल्यन' (Devaluation) कहते हैं।",
        "cue_en": "Market force decline = Depreciation; Official government cut = Devaluation.",
        "cue_hi": "बाजार से गिरावट = मूल्यह्रास; सरकार द्वारा कटौती = अवमूल्यन।",
        "wrong_en": ["Accurate macroeconomic distinction.", "Inverted commercial effects.", "Reversed causality.", "Factually erroneous assertion."],
        "wrong_hi": ["सही आर्थिक अंतर।", "उल्टा प्रभाव।", "विपरीत कारण।", "तथ्यात्मक रूप से गलत।"]
    },
    {
        "name_en": "SWIFT Financial Messaging System, IBAN, Cross-Border Payments & Sanctions",
        "name_hi": "स्विफ्ट (SWIFT) वित्तीय संदेश प्रणाली, आईबीएएन (IBAN), सीमा-पार भुगतान एवं वित्तीय प्रतिबंध",
        "concepts_en": ["SWIFT (Society for Worldwide Interbank Financial Telecommunication): Founded in 1973; headquartered in La Hulpe, Belgium; cooperative utility owned by global member banks; overseen by G10 central banks and National Bank of Belgium", "Function: Standardized, secure financial messaging network for international funds transfers, letters of credit, and securities trade (does NOT hold funds or settle transactions itself; sends payment orders/instructions)", "BIC / SWIFT Code: 8 or 11 alphanumeric characters identifying bank, country, location, and branch (e.g., SBININBB for State Bank of India, Mumbai)", "IBAN (International Bank Account Number): Up to 34 alphanumeric characters uniquely identifying overseas accounts across Europe and Middle East", "Geopolitics: Weaponization of SWIFT (disconnection of sanctioned Iranian and Russian banks isolating them from global financial transactions); emerging alternatives: China's CIPS, Russia's SPFS, India's cross-border UPI integration"],
        "concepts_hi": ["स्विफ्ट (SWIFT): सोसाइटी फॉर वर्ल्डवाइड इंटरबैंक फाइनेंशियल टेलीकम्युनिकेशन; 1973 में स्थापित; मुख्यालय ला हुल्पे (बेल्जियम); वैश्विक बैंकों का सहकारी वित्तीय नेटवर्क", "कार्य: सुरक्षित वित्तीय संदेश (Financial Messaging) का आदान-प्रदान (यह स्वयं पैसे ट्रांसफर या जमा नहीं करता, बल्कि बैंकों के बीच सुरक्षित भुगतान आदेश/संदेश भेजता है)", "स्विफ्ट कोड (BIC): 8 या 11 अक्षरों का विशिष्ट कोड जो बैंक, देश और शाखा की पहचान करता है (जैसे स्टेट बैंक ऑफ इंडिया का SBININBB)", "आईबीएएन (IBAN): अंतरराष्ट्रीय बैंक खाता संख्या जो सीमा-पार लेनदेन में प्रयुक्त होती है", "भू-राजनीति: स्विफ्ट से किसी देश के बैंकों को बाहर करना वित्तीय बहिष्कार का सबसे कड़ा प्रतिबंध माना जाता है (जैसे ईरान और रूस पर लगाया गया); वैकल्पिक प्रणालियां: चीन का CIPS, भारत का UPI सीमा-पार विस्तार"],
        "q_en": "In which European country is the global headquarters of the Society for Worldwide Interbank Financial Telecommunication (SWIFT) located?",
        "q_hi": "विश्व भर के बैंकों के बीच सुरक्षित अंतरराष्ट्रीय लेन-देन संदेश भेजने वाली संस्था 'स्विफ्ट' (SWIFT) का वैश्विक मुख्यालय किस यूरोपीय देश में स्थित है?",
        "options_en": ["Belgium (बेल्जियम - ला हुल्पे)", "Switzerland", "United States", "United Kingdom"],
        "options_hi": ["बेल्जियम (Belgium - La Hulpe)", "स्विट्जरलैंड (Switzerland - यहां BIS स्थित है)", "संयुक्त राज्य अमेरिका (USA)", "यूनाइटेड किंगडम (UK)"],
        "correct_idx": 0,
        "exp_en": "SWIFT is organized under Belgian law and headquartered in La Hulpe, near Brussels, Belgium, regulated by the National Bank of Belgium in cooperation with major central banks.",
        "exp_hi": "स्विफ्ट (SWIFT) का वैश्विक मुख्यालय ब्रुसेल्स के पास ला हुल्पे (बेल्जियम) में स्थित है और यह बेल्जियम के कानूनों के तहत संचालित एक सहकारी संस्था है।",
        "cue_en": "SWIFT headquarters = Belgium (La Hulpe).",
        "cue_hi": "स्विफ्ट (SWIFT) का मुख्यालय = बेल्जियम।",
        "wrong_en": ["Headquarters country of SWIFT.", "Headquarters of BIS and WHO.", "Headquarters of IMF and World Bank.", "Major financial trading hub."],
        "wrong_hi": ["स्विफ्ट का मुख्यालय देश।", "बीआईएस का मुख्यालय।", "आईएमएफ व विश्व बैंक।", "वित्तीय व्यापार केंद्र।"]
    }
]

# S23-C16cbee79 International Trade Agreements, Balance of Payments & WTO Norms (1 topic)
DATA["S23-C16cbee79"] = [
    {
        "name_en": "World Trade Organization (WTO): Marrakesh Agreement, Most Favoured Nation (MFN) & Trade Dispute Settlement",
        "name_hi": "विश्व व्यापार संगठन (WTO): मराकेश समझौता (1995), सर्वाधिक पसंदीदा राष्ट्र (MFN) एवं व्यापार विवाद समाधान",
        "concepts_en": ["World Trade Organization (WTO): Established on January 1, 1995 by the Marrakesh Agreement signed in Morocco, succeeding the General Agreement on Tariffs and Trade (GATT 1947); headquarters in Geneva, Switzerland", "Director-General: Ngozi Okonjo-Iweala (Nigeria, first woman and first African Director-General)", "Pillars of Multilateral Trading System: Trade in Goods (GATT), Trade in Services (GATS), and Intellectual Property Rights (TRIPS)", "Non-Discrimination Principles:", "1. Most Favoured Nation (MFN) Rule (Article I): Treating all other WTO members equally (any tariff concession granted to one member must immediately and unconditionally be extended to all WTO members)", "2. National Treatment Rule (Article III): Imported goods must be treated no less favorably than domestically produced goods once they clear customs", "Dispute Settlement Body (DSB): Appellate Body (currently paralyzed due to appointment blockades); Agriculture boxes (Green box - non-distorting permitted; Amber box - trade-distorting subject to limits; Blue box - production-limiting subsidies)"],
        "concepts_hi": ["विश्व व्यापार संगठन (WTO): 1 जनवरी 1995 को मोरक्को में हस्ताक्षरित 'मराकेश समझौते' द्वारा स्थापित; इसने 1947 के 'गैट' (GATT) का स्थान लिया; मुख्यालय जिनेवा (स्विट्जरलैंड)", "महानिदेशक: न्गोजी ओकोंजो-इवेला (नाइजीरिया - प्रथम महिला व प्रथम अफ्रीकी महानिदेशक)", "तीन प्रमुख कार्यक्षेत्र: वस्तुओं का व्यापार (GATT), सेवाओं का व्यापार (GATS) एवं बौद्धिक संपदा अधिकार (TRIPS)", "गैर-भेदभाव के दो मूलभूत नियम:", "1. सर्वाधिक पसंदीदा राष्ट्र (MFN - Most Favoured Nation): सभी सदस्य देशों के साथ समान व्यवहार (यदि किसी एक देश को व्यापार में कोई छूट दी जाती है तो वह बिना शर्त सभी WTO सदस्यों पर लागू होगी)", "2. राष्ट्रीय व्यवहार (National Treatment): सीमा शुल्क चुकाने के बाद आयातित विदेशी माल के साथ घरेलू माल जैसा ही समान व्यवहार करना", "कृषि सब्सिडी बॉक्स: ग्रीन बॉक्स (अनुमति प्राप्त), एम्बर बॉक्स (व्यापार विकृत करने वाली सीमित सब्सिडी), ब्लू बॉक्स"],
        "q_en": "Which foundational non-discrimination principle of the World Trade Organization (WTO) mandates that any trade concession or tariff reduction granted by a member to one nation must immediately and unconditionally be extended to all other WTO members?",
        "q_hi": "विश्व व्यापार संगठन (WTO) का वह मूलभूत गैर-भेदभाव सिद्धांत कौन सा है, जिसके तहत यदि कोई सदस्य देश किसी एक देश को कोई व्यापारिक छूट या कम टैरिफ देता है, तो उसे वही छूट बिना शर्त अन्य सभी सदस्य देशों को भी देनी होती है?",
        "options_en": ["Most Favoured Nation Principle (MFN / सर्वाधिक पसंदीदा राष्ट्र नियम)", "National Treatment Principle", "Special and Differential Treatment", "Generalized System of Preferences (GSP)"],
        "options_hi": ["सर्वाधिक पसंदीदा राष्ट्र नियम (Most Favoured Nation - MFN)", "राष्ट्रीय व्यवहार नियम (National Treatment - यह सीमा शुल्क के बाद घरेलू समानता है)", "विशेष एवं विभेदक व्यवहार (S&DT)", "सामान्यीकृत प्राथमिकता प्रणाली (GSP)"],
        "correct_idx": 0,
        "exp_en": "The Most Favoured Nation (MFN) principle (GATT Article I) forbids discrimination between trading partners: every member must accord all other WTO members the best trading terms it offers to any single country.",
        "exp_hi": "सर्वाधिक पसंदीदा राष्ट्र (MFN) का नियम यह सुनिश्चित करता है कि विश्व व्यापार में किसी एक देश के साथ पक्षपात न हो; यदि एक सदस्य देश को आयात शुल्क में राहत दी जाती है, तो वह स्वतः सभी WTO सदस्यों पर लागू हो जाती है।",
        "cue_en": "Equal treatment to all trading partners = Most Favoured Nation (MFN).",
        "cue_hi": "सभी देशों के साथ समान व्यापारिक व्यवहार = MFN नियम।",
        "wrong_en": ["GATT Article I non-discrimination rule.", "Equality between domestic and imported products (Article III).", "Special exemptions for developing nations.", "Unilateral tariff preference system outside WTO."],
        "wrong_hi": ["एमएफएन का सही नियम।", "घरेलू व विदेशी माल की समानता।", "विकासशील देशों हेतु छूट।", "एकतरफा व्यापारिक वरीयता।"]
    }
]

print("Loaded S23 successfully")
