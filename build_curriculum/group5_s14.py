# build_curriculum/group5_s14.py
# S14: Space Science, Astronomy & Space Missions (7 topics across 3 chapters)

DATA = {}

# S14-Cc877e372 The Solar System, Planetary Characteristics & The Sun (3 topics)
DATA["S14-Cc877e372"] = [
    {
        "name_en": "The Sun: Solar Atmosphere (Photosphere, Chromosphere, Corona), Sunspots & Solar Flares",
        "name_hi": "सूर्य की संरचना: सौर वायुमंडल (प्रकाशमंडल, वर्णमंडल, कोरोना), सौर कलंक एवं सौर ज्वालाएं",
        "concepts_en": ["Structure of the Sun: Core (thermonuclear fusion: 4 protons into 1 Helium nucleus via p-p chain at 15 million K), Radiative Zone, Convective Zone", "Solar Atmosphere: Photosphere (visible surface ~5,500 °C, granulations), Chromosphere (thin red layer visible during total solar eclipse), Corona (outermost tenuous plasma halo extending millions of km, temperature reaches 1-3 million K; the 'Coronal Heating Mystery')", "Sunspots: Cooler, darker magnetic storm regions on photosphere (~3,800 K) following an 11-year solar cycle (Schwabe cycle)", "Solar Wind and Flares: Stream of charged particles interacting with Earth's magnetosphere causing Auroras (Aurora Borealis / Northern Lights and Aurora Australis / Southern Lights)"],
        "concepts_hi": ["सूर्य की आंतरिक संरचना: कोर (क्रोड - 1.5 करोड़ केल्विन तापमान पर प्रोटॉन-प्रोटॉन संलयन द्वारा हाइड्रोजन का हीलियम में रूपांतरण), विकिरण क्षेत्र एवं संवहन क्षेत्र", "सौर वायुमंडल: प्रकाशमंडल (Photosphere - दृश्यमान सतह, तापमान ~5500 °C), वर्णमंडल (Chromosphere - लाल पतली परत), कोरोना (Corona - केवल पूर्ण सूर्यग्रहण के समय दिखने वाला बाहरी प्रभामंडल, जिसका तापमान 10 से 30 लाख डिग्री तक पहुंच जाता है; 'कोरोना तापन समस्या')", "सौर कलंक (Sunspots): प्रकाशमंडल पर तीव्र चुंबकीय खिंचाव के कारण बने अपेक्षाकृत ठंडे काले धब्बे (~3800 K), जो 11-वर्षीय सौर चक्र का पालन करते हैं", "सौर पवन एवं सौर ज्वालाएं: पृथ्वी के चुंबकीय क्षेत्र से टकराकर ध्रुवीय ज्योति (ऑरोरा बोरियालिस व ऑरोरा ऑस्ट्रेलिस) उत्पन्न करती हैं"],
        "q_en": "Which outermost, pearly-white layer of the solar atmosphere, reaching temperatures of millions of degrees Kelvin, is normally visible to the naked eye ONLY during a total solar eclipse?",
        "q_hi": "सूर्य के वायुमंडल की वह सबसे बाहरी श्वेत परत कौन सी है, जिसका तापमान लाखों डिग्री केल्विन तक पहुंच जाता है और जो सामान्यतः केवल पूर्ण सूर्यग्रहण के समय ही नंगी आंखों से दिखाई देती है?",
        "options_en": ["Corona (कोरोना / प्रभामंडल)", "Photosphere", "Chromosphere", "Core"],
        "options_hi": ["कोरोना / प्रभामंडल (Corona)", "प्रकाशमंडल (Photosphere - यह सामान्य दिनों में दिखने वाली सतह है)", "वर्णमंडल (Chromosphere)", "सौर क्रोड (Core)"],
        "correct_idx": 0,
        "exp_en": "The solar Corona is the outermost atmospheric layer composed of highly ionized plasma at 1-3 million Kelvin, eclipsed by the bright photosphere except during total solar eclipses or when viewed via a coronagraph.",
        "exp_hi": "कोरोना (Corona) सूर्य का बाह्यतम वायुमंडल है; इसका अत्यधिक तापमान सौर भौतिकी का अनसुलझा रहस्य है और यह पूर्ण सूर्यग्रहण के समय चंद्रमा द्वारा प्रकाशमंडल को ढक लेने पर मुकुट के समान चमकता है।",
        "cue_en": "Outer solar atmosphere visible during eclipse = Corona.",
        "cue_hi": "सूर्यग्रहण में दिखने वाला बाह्य भाग = कोरोना (प्रभामंडल)।",
        "wrong_en": ["Outermost solar atmosphere visible during total eclipse.", "Visible surface layer of the Sun.", "Middle reddish atmospheric layer.", "Center of nuclear fusion."],
        "wrong_hi": ["ग्रहण में दिखने वाला बाह्य भाग।", "दृश्यमान धरातल।", "मध्यम परत।", "नाभिकीय संलयन केंद्र।"]
    },
    {
        "name_en": "Planetary Characteristics: Terrestrial vs Gas/Ice Giants & Dwarf Planet Pluto (IAU 2006)",
        "name_hi": "ग्रहों की विशेषताएं: पार्थिव (आंतरिक) बनाम गैसीय/बर्फीले (बाहरी) ग्रह एवं बौना ग्रह प्लूटो",
        "concepts_en": ["Terrestrial / Inner Planets (Rocky, dense, metallic cores): Mercury (smallest, no atmosphere, fastest orbit 88 days), Venus ('Morning/Evening Star', hottest planet ~465 °C due to runaway CO2 greenhouse effect, retrograde clockwise rotation), Earth, Mars ('Red Planet' due to iron oxide, Olympus Mons tallest volcano, Phobos and Deimos moons)", "Asteroid Belt separates Mars and Jupiter", "Jovian / Outer Giants: Jupiter (largest planet, Great Red Spot anticyclonic storm, Ganymede largest moon in solar system), Saturn (prominent ring system made of ice/rock, lowest density < water, Titan moon with nitrogen atmosphere), Uranus (ice giant rotating on its side at 98° tilt), Neptune (farthest official planet, Great Dark Spot, Triton moon)", "Dwarf Planet Pluto: Demoted by International Astronomical Union (IAU) at Prague General Assembly in August 2006 for failing the 3rd planetary criterion: 'has cleared the neighborhood around its orbit' in the Kuiper Belt"],
        "concepts_hi": ["आंतरिक / पार्थिव ग्रह (चट्टानी व सघन): बुध (सबसे छोटा, सबसे तीव्र 88 दिन की परिक्रमा), शुक्र ('भोर व सांझ का तारा', पृथ्वी की जुड़वां बहन, 96% CO2 के ग्रीनहाउस प्रभाव से सबसे गर्म ग्रह ~465 °C, दक्षिणावर्त घूर्णन), पृथ्वी, मंगल ('लाल ग्रह', सौरमंडल का सबसे ऊंचा पर्वत ओलिंपस मॉन्स, फोबोस व डिमोस उपग्रह)", "क्षुद्रग्रह पेटी (Asteroid Belt): मंगल और बृहस्पति के बीच स्थित", "बाहरी / जोवियन ग्रह (गैसीय व विशाल): बृहस्पति (सबसे बड़ा ग्रह, विशाल लाल धब्बा, सौरमंडल का सबसे बड़ा उपग्रह गैनीमीड), शनि (सुंदर वलय/रिंग्स, जल से भी कम घनत्व, टाइटन उपग्रह), अरुण / यूरेनस (अपनी धुरी पर 98° लेटा हुआ ग्रह), वरुण / नेप्च्यून (सबसे दूर, ट्राइटन उपग्रह)", "बौना ग्रह प्लूटो (यम): अगस्त 2006 में प्राग में अंतर्राष्ट्रीय खगोलीय संघ (IAU) द्वारा ग्रह का दर्जा समाप्त किया गया, क्योंकि यह अपनी कक्षा के आस-पास का क्षेत्र साफ (Clear the neighborhood) नहीं कर सका था"],
        "q_en": "Which planet in our solar system is the HOTTEST planet with surface temperatures exceeding 465 °C, owing to an extreme runaway greenhouse effect driven by a dense 96% carbon dioxide atmosphere?",
        "q_hi": "हमारे सौरमंडल का सबसे गर्म (Hottest) ग्रह कौन सा है, जिसकी सतह का तापमान 96% कार्बन डाइऑक्साइड के सघन वायुमंडल और तीव्र ग्रीनहाउस प्रभाव के कारण लगभग 465 °C तक पहुंच जाता है?",
        "options_en": ["Venus (शुक्र ग्रह)", "Mercury", "Mars", "Jupiter"],
        "options_hi": ["शुक्र ग्रह (Venus - सबसे गर्म ग्रह)", "बुध ग्रह (Mercury - सूर्य के सबसे नजदीक होने के बावजूद वायुमंडल न होने से दूसरे स्थान पर)", "मंगल ग्रह (Mars)", "बृहस्पति ग्रह (Jupiter)"],
        "correct_idx": 0,
        "exp_en": "Although Mercury is closer to the Sun, Venus is the hottest planet in the solar system (~465 °C) because its dense atmosphere of 96% CO2 traps solar heat in a runaway greenhouse effect.",
        "exp_hi": "बुध सूर्य के सबसे निकट है, किंतु वायुमंडल न होने से रातें बर्फीली होती हैं; जबकि शुक्र का सघन CO2 वायुमंडल ऊष्मा को बाहर नहीं जाने देता, जिससे शुक्र सौरमंडल का सबसे गर्म ग्रह है।",
        "cue_en": "Hottest planet = Venus (dense CO2 runaway greenhouse effect).",
        "cue_hi": "सौरमंडल का सबसे गर्म ग्रह = शुक्र (CO2 ग्रीनहाउस)।",
        "wrong_en": ["Hottest planet due to runaway greenhouse.", "Closest to Sun, but lacks insulating atmosphere.", "Cold desert planet.", "Cold gas giant."],
        "wrong_hi": ["सबसे गर्म ग्रह (शुक्र)।", "सूर्य के निकटतम किंतु रातें ठंडी।", "ठंडा लाल ग्रह।", "विशाल गैसीय ग्रह।"]
    },
    {
        "name_en": "Moons of the Solar System, Asteroids, Kuiper Belt, Oort Cloud & Comets",
        "name_hi": "सौरमंडल के प्रमुख प्राकृतिक उपग्रह (चंद्रमा), क्षुद्रग्रह, काइपर बेल्ट, ऊर्ट क्लाउड एवं धूमकेतु",
        "concepts_en": ["Major Natural Satellites: Ganymede (Jupiter - largest moon in solar system, larger than Mercury, only moon with its own magnetic field); Titan (Saturn - second largest moon, dense nitrogen-methane atmosphere, liquid methane lakes); Europa (Jupiter - smooth ice crust concealing subsurface liquid water ocean, prime target for extraterrestrial life search); Enceladus (Saturn - active water ice cryovolcanoes geysers at south pole); Io (Jupiter - most volcanically active body in solar system due to tidal heating); Moon (Earth - synchronous rotation, tidal locking)", "Kuiper Belt: Ring of icy bodies and dwarf planets (Pluto, Eris, Haumea, Makemake) beyond Neptune (30-50 AU)", "Oort Cloud: Theoretical spherical shell of trillions of icy cometary nuclei surrounding solar system up to 100,000 AU (origin of long-period comets)", "Comets: 'Dirty snowballs' of dust and ice; develop coma and ion/dust tails pointing AWAY from Sun due to solar radiation pressure and solar wind; Halley's Comet (76-year orbital period, next in 2061)"],
        "concepts_hi": ["सौरमंडल के प्रमुख उपग्रह: गैनीमीड (बृहस्पति का चंद्रमा - सौरमंडल का सबसे बड़ा उपग्रह, बुध ग्रह से भी बड़ा, अपना स्वतंत्र चुंबकीय क्षेत्र रखता है); टाइटन (शनि का उपग्रह - सघन नाइट्रोजन वायुमंडल और तरल मीथेन की झीलें); यूरोपा (बृहस्पति - बर्फ की सतह के नीचे तरल जल का महासागर, जीवन की खोज का प्रमुख केंद्र); आयो (Io - तीव्र ज्वारीय घर्षण के कारण सौरमंडल का सर्वाधिक सक्रिय ज्वालामुखीय पिंड); एन्सेलैडस (शनि - बर्फ के फव्वारे)", "काइपर बेल्ट: नेप्च्यून की कक्षा के पार (30-50 AU) बर्फीले पिंडों व बौने ग्रहों (प्लूटो, एरिस) का विशाल क्षेत्र", "ऊर्ट क्लाउड (Oort Cloud): सौरमंडल के सुदूर किनारे पर (1 लाख AU तक) फैला विशाल गोलाकार बर्फीला बादल जहां से दीर्घकालिक धूमकेतु आते हैं", "धूमकेतु (Comets): धूल, बर्फ और गैस के पिंड; सूर्य के पास आने पर सौर पवन के कारण इनकी पूंछ हमेशा 'सूर्य की विपरीत दिशा' में होती है; हैली का धूमकेतु (76 वर्ष की अवधि, अगली बार 2061 में दिखेगा)"],
        "q_en": "Which moon in the solar system is the LARGEST natural satellite, orbiting Jupiter and possessing its own internally generated magnetic field?",
        "q_hi": "बृहस्पति की परिक्रमा करने वाला सौरमंडल का सबसे बड़ा प्राकृतिक उपग्रह (चंद्रमा) कौन सा है, जो आकार में बुध ग्रह से भी बड़ा है और जिसका अपना स्वतंत्र चुंबकीय क्षेत्र है?",
        "options_en": ["Ganymede (गैनीमीड - बृहस्पति का उपग्रह)", "Titan", "Callisto", "Europa"],
        "options_hi": ["गैनीमीड (Ganymede - बृहस्पति)", "टाइटन (Titan - यह शनि का उपग्रह है, दूसरा सबसे बड़ा)", "कैलिस्टो (Callisto)", "यूरोपा (Europa)"],
        "correct_idx": 0,
        "exp_en": "Ganymede, discovered by Galileo Galilei in 1610, is the largest moon in the solar system (diameter 5,268 km), even exceeding the planet Mercury in volume, and is the only moon with an intrinsic magnetosphere.",
        "exp_hi": "गैनीमीड सौरमंडल का सबसे बड़ा उपग्रह है; इसका व्यास 5,268 किमी है जो बुध ग्रह से 8% बड़ा है। यह एकमात्र ऐसा चंद्रमा है जिसके कोर में तरल लोहे के कारण अपनी चुंबकीय ढाल है।",
        "cue_en": "Largest moon in solar system = Ganymede (Jupiter).",
        "cue_hi": "सौरमंडल का सबसे बड़ा उपग्रह = गैनीमीड (बृहस्पति)।",
        "wrong_en": ["Largest moon in solar system.", "Second largest moon (Saturn).", "Third largest moon (Jupiter).", "Ice-covered ocean moon."],
        "wrong_hi": ["सबसे बड़ा उपग्रह।", "दूसरा सबसे बड़ा (शनि का टाइटन)।", "तीसरा सबसे बड़ा उपग्रह।", "बर्फीला महासागरीय उपग्रह।"]
    }
]

# S14-C268685b0 Historic Space Missions: Apollo, Voyagers & Space Telescopes (2 topics)
DATA["S14-C268685b0"] = [
    {
        "name_en": "Historic Human Spaceflight: Yuri Gagarin, Apollo 11 Moon Landing & Neil Armstrong",
        "name_hi": "ऐतिहासिक मानव अंतरिक्ष मिशन: यूरी गगारिन (प्रथम मानव), अपोलो 11 चंद्र अवतरण एवं नील आर्मस्ट्रांग",
        "concepts_en": ["First Human in Space: Soviet cosmonaut Yuri Gagarin orbited Earth on Vostok 1 on April 12, 1961 (commemorated globally as International Day of Human Space Flight)", "First Woman in Space: Soviet cosmonaut Valentina Tereshkova aboard Vostok 6 on June 16, 1963", "First Spacewalk (EVA): Alexei Leonov on Voskhod 2 (1965)", "Apollo 11 Moon Landing: NASA mission launched on Saturn V rocket; Lunar Module 'Eagle' landed on the Sea of Tranquility (Mare Tranquillitatis) on July 20, 1969; Neil Armstrong became the first human to step onto the lunar surface, uttering: 'That's one small step for [a] man, one giant leap for mankind'; joined by Buzz Aldrin, while Michael Collins piloted the Command Module Columbia in lunar orbit", "Rakesh Sharma: First Indian citizen in space aboard Soviet Soyuz T-11 on April 3, 1984 (famous response to Indira Gandhi: 'Saare Jahan Se Achha')"],
        "concepts_hi": ["अंतरिक्ष में जाने वाले प्रथम मानव: सोवियत अंतरिक्ष यात्री यूरी गगारिन ने 12 अप्रैल 1961 को 'वोस्तोक 1' से पृथ्वी की परिक्रमा की (प्रतिवर्ष 12 अप्रैल को 'मानव अंतरिक्ष उड़ान दिवस')", "अंतरिक्ष में जाने वाली प्रथम महिला: सोवियत संघ की वेलेंटीना तेरेश्कोवा (16 जून 1963, वोस्तोक 6)", "प्रथम स्पेसवॉक: एलेक्सी लियोनोव (1965)", "अपोलो 11 चंद्र अवतरण (20 जुलाई 1969): नासा के सैटर्न 5 रॉकेट से प्रक्षेपित; चंद्र मॉड्यूल 'ईगल' चंद्रमा के 'प्रशांत महासागर' (सी ऑफ ट्रैंक्विलिटी) पर उतरा; नील आर्मस्ट्रांग चंद्रमा की सतह पर कदम रखने वाले पहले मानव बने ('मनुष्य का यह छोटा सा कदम, मानव जाति के लिए एक विशाल छलांग है'); बज़ एल्ड्रिन उनके साथ थे, जबकि माइकल कोलिन्स मुख्य मॉड्यूल में रहे", "राकेश शर्मा: 3 अप्रैल 1984 को सोवियत संघ के सोयुज टी-11 से अंतरिक्ष जाने वाले पहले भारतीय नागरिक बने (इंदिरा गांधी के पूछने पर कहा: 'सारे जहां से अच्छा हिन्दोस्तां हमारा')"],
        "q_en": "On which historic date did Apollo 11's Lunar Module 'Eagle' touch down on the lunar surface at the Sea of Tranquility, making Neil Armstrong the first human to walk on the Moon?",
        "q_hi": "नासा के अपोलो 11 मिशन का लूनर मॉड्यूल 'ईगल' चंद्रमा के 'सी ऑफ ट्रैंक्विलिटी' (शांत सागर) पर किस ऐतिहासिक तारीख को उतरा, जिससे नील आर्मस्ट्रांग चंद्रमा पर कदम रखने वाले पहले इंसान बने?",
        "options_en": ["July 20, 1969 (20 जुलाई 1969)", "April 12, 1961", "October 4, 1957", "April 3, 1984"],
        "options_hi": ["20 जुलाई 1969 (July 20, 1969)", "12 अप्रैल 1961 (इस दिन यूरी गगारिन अंतरिक्ष में गए थे)", "4 अक्टूबर 1957 (स्पुतनिक 1 का प्रक्षेपण)", "3 अप्रैल 1984 (राकेश शर्मा का अंतरिक्ष मिशन)"],
        "correct_idx": 0,
        "exp_en": "On July 20, 1969, Apollo 11 astronauts Neil Armstrong and Buzz Aldrin landed the lunar module Eagle on the Moon, inaugurating crewed lunar exploration.",
        "exp_hi": "20 जुलाई 1969 को अमेरिकी अंतरिक्ष यात्री नील आर्मस्ट्रांग ने चंद्रमा पर पहला कदम रखकर इतिहास रचा था; इस अभियान की सफलता ने अमेरिका को अंतरिक्ष होड़ में विजय दिलाई।",
        "cue_en": "First Moon landing = July 20, 1969 (Apollo 11, Neil Armstrong).",
        "cue_hi": "चंद्रमा पर पहला कदम = 20 जुलाई 1969 (अपोलो 11)।",
        "wrong_en": ["Apollo 11 Moon landing date.", "Yuri Gagarin first human spaceflight.", "Sputnik 1 first artificial satellite launch.", "Rakesh Sharma first Indian in space."],
        "wrong_hi": ["अपोलो 11 चंद्र अवतरण।", "यूरी गगारिन का मिशन।", "स्पुतनिक 1 प्रक्षेपण।", "राकेश शर्मा का मिशन।"]
    },
    {
        "name_en": "Deep Space Explorers & Observatories: Voyager 1 & 2, Hubble & James Webb Space Telescope (JWST)",
        "name_hi": "गहरे अंतरिक्ष के अन्वेषक एवं वेधशालाएं: वॉयजर 1 व 2, हबल एवं जेम्स वेब स्पेस टेलीस्कोप (JWST)",
        "concepts_en": ["Voyager Program: NASA twin probes launched in 1977 to explore outer gas giants; carry the Golden Record (sounds, images, and greetings in 55 languages curated by Carl Sagan); Voyager 1 crossed heliopause into Interstellar Space in August 2012 (most distant human-made object from Earth, >160 AU); Voyager 2 entered interstellar space in 2018 (only probe to visit Uranus and Neptune)", "Hubble Space Telescope (HST): Launched 1990 into low Earth orbit (540 km); 2.4-meter mirror observing in ultraviolet, visible, and near-infrared; calculated expansion rate of universe (Hubble constant) and confirmed supermassive black holes at galaxy centers", "James Webb Space Telescope (JWST): Launched on December 25, 2021 on Ariane 5 rocket; stationed at Sun-Earth Lagrange Point 2 (L2, 1.5 million km from Earth); 6.5-meter gold-coated beryllium primary mirror operating in infrared; peers back 13.5 billion years to image first stars/galaxies formed after Big Bang and analyzes exoplanet atmospheres"],
        "concepts_hi": ["वॉयजर मिशन (Voyager 1 & 2): नासा द्वारा 1977 में प्रक्षेपित; इनमें 'गोल्डन रिकॉर्ड' संलग्न है (कार्ल सागन द्वारा संकलित पृथ्वी की ध्वनियां व 55 भाषाओं में शुभकामनाएं); वॉयजर 1 अगस्त 2012 में सौरमंडल की सीमा (हेलियोपॉज) पार कर 'अंतरतारकीय अंतरिक्ष' (Interstellar Space) में प्रवेश करने वाला मानव निर्मित सबसे दूर स्थित पिंड बन गया (>24 अरब किमी दूर)", "हबल स्पेस टेलीस्कोप (HST): 1990 में पृथ्वी की निचली कक्षा में स्थापित 2.4 मीटर दर्पण वाला टेलीस्कोप; पराबैंगनी व दृश्य प्रकाश में ब्रह्मांड की अद्भुत तस्वीरें", "जेम्स वेब स्पेस टेलीस्कोप (JWST): 25 दिसंबर 2021 को एरियन 5 रॉकेट से प्रक्षेपित; पृथ्वी से 15 लाख किमी दूर 'सूर्य-पृथ्वी लैग्रेंज बिंदु 2' (L2) पर स्थित; 6.5 मीटर चौड़ा सोने की परत चढ़ा बेरिलियम दर्पण; अवरक्त (Infrared) प्रकाश में बिग बैंग के तुरंत बाद बनी पहली आकाशगंगाओं और दूरस्थ बाह्यग्रहों का अध्ययन करता है"],
        "q_en": "At which gravitationally stable orbital position, located approximately 1.5 million kilometers from Earth on the night side, is the revolutionary James Webb Space Telescope (JWST) permanently stationed?",
        "q_hi": "पृथ्वी से लगभग 15 लाख किलोमीटर दूर सूर्य की विपरीत दिशा में स्थित वह कौन सा गुरुत्वाकर्षण की दृष्टि से संतुलित 'लैग्रेंज बिंदु' (Lagrange Point) है, जहां क्रांतिकारी जेम्स वेब स्पेस टेलीस्कोप (JWST) को तैनात किया गया है?",
        "options_en": ["Sun-Earth Lagrange Point 2 / L2 (सूर्य-पृथ्वी लैग्रेंज बिंदु 2)", "Sun-Earth Lagrange Point 1 / L1", "Low Earth Orbit (550 km)", "Geostationary Orbit (35,786 km)"],
        "options_hi": ["सूर्य-पृथ्वी लैग्रेंज बिंदु 2 (L2 - 15 लाख किमी दूर)", "सूर्य-पृथ्वी लैग्रेंज बिंदु 1 (L1 - यहां भारत का आदित्य-L1 स्थित है)", "लो अर्थ ऑर्बिट (यहां हबल टेलीस्कोप स्थित है)", "भू-स्थैतिक कक्षा (Geostationary Orbit)"],
        "correct_idx": 0,
        "exp_en": "The James Webb Space Telescope operates in a halo orbit around the Sun-Earth L2 point, where the combined gravitational pull of the Sun and Earth keeps the spacecraft in a constant cool shadow shield from solar glare.",
        "exp_hi": "जेम्स वेब टेलीस्कोप को सूर्य-पृथ्वी लैग्रेंज बिंदु 2 (L2) पर स्थापित किया गया है ताकि इसकी विशाल सनशील्ड सूर्य, पृथ्वी और चंद्रमा की ऊष्मा को पूरी तरह रोक सके और इसके इंफ्रारेड कैमरे शून्य से 233 डिग्री नीचे ठंड में काम कर सकें। (भारत का आदित्य L1 बिंदु पर है)।",
        "cue_en": "James Webb Telescope location = Sun-Earth L2 point (1.5 million km).",
        "cue_hi": "जेम्स वेब टेलीस्कोप = L2 बिंदु (15 लाख किमी)।",
        "wrong_en": ["Stationed location of JWST.", "Location of solar observatories like Aditya-L1.", "Orbit of Hubble Space Telescope.", "Orbit of weather and communication satellites."],
        "wrong_hi": ["जेम्स वेब का L2 स्थान।", "आदित्य-L1 का सौर स्थान।", "हबल का निचला कक्ष।", "संचार उपग्रह कक्षा।"]
    }
]

# S14-Cc150b231 ISRO Launch Vehicles, Chandrayaan, Mangalyaan & Gaganyaan (2 topics)
DATA["S14-Cc150b231"] = [
    {
        "name_en": "ISRO Evolution & Launch Vehicle Family: SLV-3, ASLV, PSLV (Workhorse), GSLV & LVM3 (Fat Boy)",
        "name_hi": "इसरो (ISRO) का विकास एवं प्रक्षेपण यान परिवार: एसएलवी-3, पीएसएलवी (कार्यअश्व), जीएसएलवी एवं एलवीएम3 (बाहुबली)",
        "concepts_en": ["Indian Space Research Organisation (ISRO): Founded on August 15, 1969 under Department of Space; headquarters in Bengaluru, Karnataka; visionary founder Dr. Vikram Sarabhai ('Father of Indian Space Programme'); first satellite Aryabhata launched on April 19, 1975 using Soviet Kosmos-3M", "Launch Vehicle Hierarchy:", "1. SLV-3: India's first experimental launch vehicle; successfully put Rohini satellite into orbit in 1980 under Project Director Dr. A.P.J. Abdul Kalam", "2. PSLV (Polar Satellite Launch Vehicle): 'Workhorse of ISRO'; 4-stage vehicle alternating solid (HTPB) and liquid (UDMH/N2O4 Vikas engine) fuels; historic world record of launching 104 satellites in a single mission (PSLV-C37 in 2017)", "3. GSLV (Geosynchronous Satellite Launch Vehicle): 3-stage vehicle with indigenous Cryogenic Upper Stage (CE-7.5 burning liquid hydrogen at -253 °C and liquid oxygen at -183 °C)", "4. LVM3 (Launch Vehicle Mark 3 / 'Bahubali' / 'Fat Boy'): Heavy-lift 3-stage rocket with two massive S200 solid strap-ons, L110 core liquid stage, and C25 cryogenic stage; launched Chandrayaan-2, Chandrayaan-3, and designated for Gaganyaan"],
        "concepts_hi": ["भारतीय अंतरिक्ष अनुसंधान संगठन (ISRO): 15 अगस्त 1969 को अंतरिक्ष विभाग के अधीन स्थापित; मुख्यालय बेंगलुरु (कर्नाटक); संस्थापक डॉ. विक्रम साराभाई ('भारतीय अंतरिक्ष कार्यक्रम के जनक'); भारत का पहला उपग्रह 'आर्यभट्ट' 19 अप्रैल 1975 को सोवियत रॉकेट से छोड़ा गया", "प्रक्षेपण यानों का विकास:", "1. SLV-3: भारत का पहला प्रायोगिक रॉकेट; 1980 में रोहिणी उपग्रह का सफल प्रक्षेपण (परियोजना निदेशक डॉ. ए.पी.जे. अब्दुल कलाम)", "2. PSLV (ध्रुवीय उपग्रह प्रक्षेपण यान): 'इसरो का वर्कहॉर्स' (Workhorse of ISRO); 4-चरणीय रॉकेट (ठोस-तरल-ठोस-तरल, विकास इंजन); 2017 में PSLV-C37 द्वारा एक ही उड़ान में 104 उपग्रह छोड़कर विश्व रिकॉर्ड बनाया", "3. GSLV: तीन चरणीय रॉकेट जिसमें भारत का स्वदेशी क्रायोजेनिक अपर स्टेज इंजन (CE-7.5) लगा है", "4. LVM3 ('बाहुबली' / पूर्व नाम GSLV Mk III): भारत का सबसे भारी और शक्तिशाली रॉकेट; दो S200 ठोस बूस्टर, L110 तरल कोर और C25 क्रायोजेनिक इंजन; इसी ने चंद्रयान-2, चंद्रयान-3 को लॉन्च किया और गगनयान हेतु मानव-रेटेड (HLVM3) है"],
        "q_en": "Which reliable four-stage rocket of ISRO, alternating between solid and liquid propellant stages, is widely celebrated as the 'Workhorse of ISRO' for launching Chandrayaan-1, Mangalyaan, and a record 104 satellites in one flight?",
        "q_hi": "ठोस और तरल प्रणोदकों के चार चरणों वाले इसरो के किस अत्यधिक विश्वसनीय रॉकेट को 'इसरो का वर्कहॉर्स' (Workhorse of ISRO) कहा जाता है, जिसने चंद्रयान-1, मंगलयान और एक साथ 104 उपग्रहों का सफल प्रक्षेपण किया?",
        "options_en": ["Polar Satellite Launch Vehicle / PSLV (ध्रुवीय उपग्रह प्रक्षेपण यान)", "Geosynchronous Satellite Launch Vehicle (GSLV)", "Launch Vehicle Mark 3 (LVM3)", "Satellite Launch Vehicle-3 (SLV-3)"],
        "options_hi": ["ध्रुवीय उपग्रह प्रक्षेपण यान (PSLV - Polar Satellite Launch Vehicle)", "भू-समकालिक उपग्रह प्रक्षेपण यान (GSLV)", "लॉन्च व्हीकल मार्क 3 (LVM3 / बाहुबली)", "उपग्रह प्रक्षेपण यान-3 (SLV-3)"],
        "correct_idx": 0,
        "exp_en": "The PSLV has achieved over 55 successful launches, earning the title 'Workhorse of ISRO' for its unmatched reliability in launching earth observation satellites, planetary probes (Chandrayaan-1 and Mars Orbiter Mission), and commercial foreign payloads.",
        "exp_hi": "पीएसएलवी (PSLV) इसरो का सबसे भरोसेमंद और सर्वाधिक सफल रॉकेट है; इसने 2008 में चंद्रयान-1 और 2013 में मंगलयान को अंतरिक्ष में भेजा था और 95% से अधिक सफलता दर दर्ज की है।",
        "cue_en": "Workhorse of ISRO = PSLV (Polar Satellite Launch Vehicle).",
        "cue_hi": "इसरो का वर्कहॉर्स = पीएसएलवी (PSLV)।",
        "wrong_en": ["Workhorse rocket of ISRO (PSLV).", "Heavy geo-orbit rocket with cryogenic stage.", "Heaviest rocket ('Bahubali').", "India's first historical launch vehicle (1980)."],
        "wrong_hi": ["इसरो का वर्कहॉर्स रॉकेट।", "क्रायोजेनिक युक्त रॉकेट।", "सबसे भारी रॉकेट (LVM3)।", "पहला ऐतिहासिक रॉकेट।"]
    },
    {
        "name_en": "Lunar & Interplanetary Triumphs: Chandrayaan-3 Moon South Pole Landing, Mangalyaan & Gaganyaan",
        "name_hi": "चंद्र व अंतरग्रहीय विजय: चंद्रयान-3 (चंद्रमा के दक्षिणी ध्रुव पर तिरंगा), मंगलयान एवं गगनयान मानव मिशन",
        "concepts_en": ["Chandrayaan-1 (2008): Launched via PSLV-C11; Moon Impact Probe detected water molecules (H2O/OH) on lunar soil", "Mangalyaan / Mars Orbiter Mission (MOM, 2013): Launched via PSLV-C25; India became first nation in the world to reach Martian orbit in its very FIRST maiden attempt on September 24, 2014, and first Asian nation to reach Mars, executed at frugal budget of $74 million (featured on old ₹2000 note)", "Chandrayaan-3 Historic Triumph (August 23, 2023): Launched July 14, 2023 via LVM3-M4; Lander 'Vikram' with Rover 'Pragyan' made a flawless soft landing near the Lunar South Pole (69.37° S, 32.35° E) at 18:04 IST; INDIA BECAME FIRST COUNTRY IN HUMAN HISTORY TO LAND NEAR LUNAR SOUTH POLE, and 4th country to achieve a soft lunar landing (after USSR, USA, China); landing site named 'Shiv Shakti Point'; August 23 officially declared 'National Space Day'", "Aditya-L1 (September 2023): India's first solar space observatory stationed at Sun-Earth L1", "Gaganyaan: India's indigenous human spaceflight mission aiming to send 3 astronauts to a 400 km low Earth orbit for 3 days and return safely"],
        "concepts_hi": ["चंद्रयान-1 (2008): चंद्रमा पर जल के अणुओं (H2O) की खोज की", "मंगलयान (MOM, 2013): 24 सितंबर 2014 को मंगल की कक्षा में प्रवेश; भारत अपने पहले ही प्रयास में मंगल पर पहुंचने वाला विश्व का पहला देश तथा मंगल पर पहुंचने वाला पहला एशियाई देश बना (मात्र $74 मिलियन की रिकॉर्ड किफायती लागत)", "चंद्रयान-3 की ऐतिहासिक विजय (23 अगस्त 2023): 14 जुलाई को LVM3-M4 रॉकेट से प्रक्षेपित; लैंडर 'विक्रम' और रोवर 'प्रज्ञान' ने शाम 6:04 बजे चंद्रमा के दक्षिणी ध्रुव के पास सफल सॉफ्ट लैंडिंग की; भारत चंद्रमा के दक्षिणी ध्रुव पर उतरने वाला विश्व का पहला देश बना, और चंद्रमा पर उतरने वाला विश्व का चौथा देश बना; लैंडिंग स्थल का नाम 'शिव शक्ति पॉइंट' रखा गया; 23 अगस्त को प्रतिवर्ष 'राष्ट्रीय अंतरिक्ष दिवस' घोषित किया गया", "आदित्य-L1 (सितंबर 2023): भारत की पहली सौर वेधशाला जो L1 बिंदु पर स्थापित है", "गगनयान: भारत का पहला मानव अंतरिक्ष मिशन, जिसके तहत भारतीय अंतरिक्ष यात्रियों को 400 किमी की कक्षा में 3 दिनों के लिए भेजा जाएगा"],
        "q_en": "On which historic date did ISRO's Chandrayaan-3 lander 'Vikram' successfully soft-land near the Moon's South Pole, making India the FIRST country in human history to land in the lunar south polar region, commemorated as 'National Space Day'?",
        "q_hi": "इसरो के चंद्रयान-3 के लैंडर 'विक्रम' ने चंद्रमा के दक्षिणी ध्रुव के पास किस ऐतिहासिक तारीख को सफल सॉफ्ट लैंडिंग की, जिससे भारत चंद्रमा के दक्षिणी ध्रुव पर पहुंचने वाला विश्व का पहला देश बना और जिसे 'राष्ट्रीय अंतरिक्ष दिवस' घोषित किया गया?",
        "options_en": ["August 23, 2023 (23 अगस्त 2023 - राष्ट्रीय अंतरिक्ष दिवस)", "July 14, 2023", "September 2, 2023", "September 24, 2014"],
        "options_hi": ["23 अगस्त 2023 (August 23, 2023 - राष्ट्रीय अंतरिक्ष दिवस)", "14 जुलाई 2023 (इस दिन चंद्रयान-3 लॉन्च हुआ था)", "2 सितंबर 2023 (आदित्य-L1 का प्रक्षेपण)", "24 सितंबर 2014 (मंगलयान के मंगल पर पहुंचने की तारीख)"],
        "correct_idx": 0,
        "exp_en": "On August 23, 2023 at 18:04 IST, Chandrayaan-3's Vikram lander touched down near the lunar south pole, making India the 4th nation to achieve a soft lunar landing and the very 1st at the south pole. August 23 is now celebrated as National Space Day.",
        "exp_hi": "23 अगस्त 2023 को भारत ने चंद्रमा के दुर्गम दक्षिणी ध्रुव पर तिरंगा फहराकर इतिहास रच दिया; प्रधानमंत्री ने इस लैंडिंग स्थल को 'शिव शक्ति पॉइंट' नाम दिया और 23 अगस्त को 'राष्ट्रीय अंतरिक्ष दिवस' घोषित किया।",
        "cue_en": "Chandrayaan-3 Moon landing = August 23, 2023 (National Space Day).",
        "cue_hi": "चंद्रयान-3 लैंडिंग = 23 अगस्त 2023 (राष्ट्रीय अंतरिक्ष दिवस)।",
        "wrong_en": ["Historic Chandrayaan-3 landing date.", "Launch date of Chandrayaan-3.", "Launch date of Aditya-L1 solar mission.", "Mars Orbiter Mission orbital insertion date."],
        "wrong_hi": ["चंद्रयान-3 की लैंडिंग तिथि।", "चंद्रयान-3 का प्रक्षेपण दिन।", "आदित्य-L1 का प्रक्षेपण दिन।", "मंगलयान की मंगल कक्षा तिथि।"]
    }
]

print("Loaded S14 successfully")
