# build_curriculum/group5_s13.py
# S13: Information Technology & Computer Science (10 topics across 3 chapters)

DATA = {}

# S13-C3b0201a3 Computer Fundamentals, Memory Hierarchy & Operating Systems (4 topics)
DATA["S13-C3b0201a3"] = [
    {
        "name_en": "Computer Architecture: Von Neumann Model, CPU, ALU & Control Unit",
        "name_hi": "कंप्यूटर संरचना: वॉन न्यूमैन मॉडल, सीपीयू (CPU), एएलयू एवं नियंत्रण इकाई (CU)",
        "concepts_en": ["John von Neumann (1945) architecture: Stored-program concept where data and instructions share the same memory bus", "Central Processing Unit (CPU) 'brain of the computer': Arithmetic Logic Unit (ALU performs arithmetic and boolean operations), Control Unit (CU coordinates instruction execution), and Registers (high-speed temporary storage)", "Machine Cycle: Fetch -> Decode -> Execute -> Store", "Moore's Law: Number of transistors on microchip doubles roughly every two years"],
        "concepts_hi": ["जॉन वॉन न्यूमैन मॉडल (1945): 'संग्रहीत प्रोग्राम संकल्पना' जहां डेटा और निर्देश एक ही मेमोरी में रहते हैं", "केंद्रीय प्रसंस्करण इकाई (CPU / कंप्यूटर का मस्तिष्क): एएलयू (ALU - अंकगणितीय व तार्किक क्रियाएं), कंट्रोल यूनिट (CU - निर्देशों का निष्पादन व नियंत्रण) एवं रजिस्टर्स (अति-तीव्र आंतरिक मेमोरी)", "मशीन चक्र: फेच (Fetch) -> डिकोड (Decode) -> निष्पादन (Execute) -> संचयन (Store)", "मूर का नियम: माइक्रोचिप पर ट्रांजिस्टर की संख्या हर 2 साल में दोगुनी हो जाती है"],
        "q_en": "In the Von Neumann computer architecture, which component of the Central Processing Unit (CPU) directs and coordinates the operations of all other hardware components?",
        "q_hi": "वॉन न्यूमैन कंप्यूटर आर्किटेक्चर में सीपीयू (CPU) का कौन सा घटक अन्य सभी हार्डवेयर घटकों के कार्यों का समन्वय और नियंत्रण करता है?",
        "options_en": ["Control Unit (CU / नियंत्रण इकाई)", "Arithmetic Logic Unit (ALU)", "Memory Data Register", "Accumulator"],
        "options_hi": ["कंट्रोल यूनिट (Control Unit - CU)", "अंकगणित तर्क इकाई (ALU)", "मेमोरी डेटा रजिस्टर", "एक्यूमुलेटर (Accumulator)"],
        "correct_idx": 0,
        "exp_en": "The Control Unit (CU) interprets instructions from memory and directs data flow through the CPU and system buses by generating timing and control signals.",
        "exp_hi": "कंट्रोल यूनिट (CU) कंप्यूटर के सभी भागों (इनपुट, आउटपुट, मेमोरी, ALU) के बीच तालमेल बैठाती है और निर्देशों को डिकोड कर सही क्रम में निष्पादित करवाती है।",
        "cue_en": "Directs CPU operations = Control Unit (CU); Calculations = ALU.",
        "cue_hi": "कार्यों का नियंत्रण = कंट्रोल यूनिट (CU); गणनाएं = एएलयू (ALU)।",
        "wrong_en": ["Directs system execution and buses.", "Performs math and logic operations.", "Holds fetched data temporarily.", "Stores intermediate ALU results."],
        "wrong_hi": ["प्रणाली संचालन का नियंत्रक।", "गणितीय व तार्किक कार्य करता है।", "डेटा अस्थाई रूप से रखता है।", "गणना के तात्कालिक परिणाम रखता है।"]
    },
    {
        "name_en": "Memory Hierarchy: Registers, Cache (L1/L2/L3), RAM, ROM & Secondary Storage",
        "name_hi": "मेमोरी पदानुक्रम: रजिस्टर्स, कैश मेमोरी (L1, L2, L3), रैम, रोम एवं द्वितीयक स्टोरेज",
        "concepts_en": ["Hierarchy ordered by speed and cost per bit: CPU Registers (fastest, smallest, inside CPU core) > Cache Memory (SRAM: L1, L2, L3) > Primary Memory (DRAM: volatile RAM) > Flash/ROM (non-volatile BIOS firmware) > Secondary Storage (SSD, HDD) > Tertiary Storage (magnetic tape)", "RAM (Random Access Memory): Volatile read-write main working memory; lost upon power-off", "ROM (Read Only Memory): Non-volatile permanent memory containing firmware (BIOS/UEFI and POST bootstrap)", "Cache Memory: Static RAM (SRAM) bridges the speed gap between high-speed CPU and slower main DRAM memory"],
        "concepts_hi": ["गति और लागत के आधार पर पदानुक्रम: सीपीयू रजिस्टर्स (सर्वाधिक तीव्र, सबसे छोटे) > कैश मेमोरी (SRAM: L1, L2, L3) > मुख्य मेमोरी (DRAM / रैम) > रोम (ROM / गैर-वाष्पशील फर्मवेयर) > द्वितीयक मेमोरी (SSD, हार्ड डिस्क)", "रैम (RAM): वाष्पशील (Volatile) मेमोरी; कंप्यूटर बंद होते ही सारा डेटा मिट जाता है", "रोम (ROM): गैर-वाष्पशील (Non-volatile); स्थायी मेमोरी जिसमें बूटस्ट्रैप लोडर व BIOS फर्मवेयर संगृहीत होता है", "कैश मेमोरी: तेज गति वाली SRAM जो सीपीयू और धीमी मुख्य रैम के बीच गति के अंतर को पाटती है"],
        "q_en": "Which of the following computer storage memories is the FASTEST in terms of access time and data transfer speed?",
        "q_hi": "डेटा स्थानांतरण और एक्सेस गति की दृष्टि से कंप्यूटर की सबसे तेज (Fastest) मेमोरी कौन सी होती है?",
        "options_en": ["CPU Registers (सीपीयू रजिस्टर्स)", "Cache Memory (L1 Cache)", "Random Access Memory (RAM)", "Solid State Drive (SSD)"],
        "options_hi": ["सीपीयू रजिस्टर्स (CPU Registers)", "कैश मेमोरी (L1 Cache)", "रैंडम एक्सेस मेमोरी (RAM)", "सॉलिड स्टेट ड्राइव (SSD)"],
        "correct_idx": 0,
        "exp_en": "CPU Registers located directly inside the processor core operate at processor clock cycle speeds (<1 nanosecond), making them the fastest memory in the entire hierarchy.",
        "exp_hi": "रजिस्टर्स सीधे सीपीयू के अंदर लगे होते हैं और प्रोसेसर की क्लॉक स्पीड पर काम करते हैं (1 नैनोसेकंड से कम); ये कंप्यूटर की सबसे तेज मेमोरी होते हैं, इसके बाद L1 कैश का स्थान आता है।",
        "cue_en": "Fastest memory = CPU Registers > Cache > RAM > SSD/HDD.",
        "cue_hi": "सबसे तेज मेमोरी = रजिस्टर्स > कैश > रैम > एसएसडी।",
        "wrong_en": ["Fastest memory in computer hierarchy.", "Second fastest (SRAM).", "Third level (DRAM).", "Secondary flash storage."],
        "wrong_hi": ["सर्वोच्च गति वाली मेमोरी।", "दूसरे स्थान पर (कैश)।", "तीसरे स्थान पर (रैम)।", "स्थायी द्वितीयक स्टोरेज।"]
    },
    {
        "name_en": "Operating System Functions: Process Management, Memory Virtualization & File Systems",
        "name_hi": "ऑपरेटिंग सिस्टम के कार्य: प्रोसेस शेड्यूलिंग, वर्चुअल मेमोरी एवं फाइल सिस्टम",
        "concepts_en": ["Operating System acts as intermediary between user applications and bare hardware", "Core functions: Process management (CPU scheduling algorithms: FCFS, Round Robin, Shortest Job First), Memory management (Paging and Segmentation)", "Virtual Memory: Uses hard drive space as simulated extension of physical RAM (paging via Page Faults) to execute programs larger than physical memory", "File Systems: FAT32, NTFS (Windows), ext4 (Linux), APFS (Apple); organize data hierarchically into files and directories with access permissions"],
        "concepts_hi": ["ऑपरेटिंग सिस्टम (OS): उपयोगकर्ता, एप्लिकेशन सॉफ्टवेयर और कंप्यूटर हार्डवेयर के बीच मध्यस्थ सॉफ्टवेयर", "प्रमुख कार्य: प्रोसेस शेड्यूलिंग (राउंड रॉबिन, एफसीएफएस), मेमोरी आवंटन, डिवाइस प्रबंधन और फाइल सिस्टम", "वर्चुअल मेमोरी (Virtual Memory): हार्ड डिस्क के एक भाग को अतिरिक्त रैम की तरह उपयोग करना, जिससे भौतिक रैम से बड़े प्रोग्राम भी चलाए जा सकें", "फाइल सिस्टम: NTFS, FAT32, ext4; फाइलों को फोल्डरों में व्यवस्थित करना और सुरक्षा अनुमतियां प्रबंधित करना"],
        "q_en": "What operating system memory management technique uses secondary hard drive space to simulate additional physical RAM, enabling execution of processes larger than available memory?",
        "q_hi": "ऑपरेटिंग सिस्टम की वह कौन सी मेमोरी तकनीक है जो हार्ड डिस्क के एक भाग का उपयोग कर अतिरिक्त रैम का आभास कराती है, जिससे रैम की क्षमता से बड़े सॉफ्टवेयर भी चल सकें?",
        "options_en": ["Virtual Memory (वर्चुअल मेमोरी / आभासी स्मृति)", "Cache Memory", "Flash Memory", "Read-Only Memory"],
        "options_hi": ["वर्चुअल मेमोरी (Virtual Memory)", "कैश मेमोरी (Cache Memory)", "फ्लैश मेमोरी", "रीड-ओनली मेमोरी (ROM)"],
        "correct_idx": 0,
        "exp_en": "Virtual Memory maps secondary storage pages to virtual addresses, enabling the OS to run large programs by swapping pages in and out of physical RAM dynamically.",
        "exp_hi": "वर्चुअल मेमोरी ऑपरेटिंग सिस्टम का एक ऐसा तंत्र है जो हार्ड डिस्क पर 'पेज फाइल' बनाकर उसे अस्थायी रैम की तरह इस्तेमाल करता है, जिससे 'Out of Memory' की समस्या नहीं आती।",
        "cue_en": "Hard disk acting as RAM extension = Virtual Memory.",
        "cue_hi": "हार्ड डिस्क का रैम की तरह उपयोग = वर्चुअल मेमोरी।",
        "wrong_en": ["Secondary-storage based memory extension.", "High-speed SRAM hardware buffer.", "Non-volatile solid-state storage.", "Permanent firmware storage."],
        "wrong_hi": ["आभासी रैम तकनीक।", "हार्डवेयर बफर कैश।", "पेन ड्राइव/एसएसडी।", "स्थायी फर्मवेयर।"]
    },
    {
        "name_en": "Open Source vs Proprietary Software, Linux Kernel Architecture & File Permissions",
        "name_hi": "ओपन सोर्स बनाम प्रोप्राइटरी सॉफ्टवेयर, लिनक्स कर्नल संरचना एवं फाइल अनुमतियां",
        "concepts_en": ["Open Source: Source code publicly accessible to inspect, modify, and distribute (Linux, Apache, Android, Python, PostgreSQL) vs Proprietary / Closed Source (Windows, macOS, MS Office)", "Linus Torvalds created Linux Kernel (1991); monolithic kernel managing hardware drivers, memory, and system calls", "GNU Project (Richard Stallman, Free Software Foundation): GPL license, user utilities bundled with Linux kernel (GNU/Linux)", "Linux file permissions: Read (r=4), Write (w=2), Execute (x=1) for Owner, Group, Others (chmod 755 = rwxr-xr-x)"],
        "concepts_hi": ["ओपन सोर्स सॉफ्टवेयर: जिसका सोर्स कोड सभी के लिए मुफ्त और संपादन योग्य उपलब्ध होता है (लिनक्स, अपाचे, एंड्रॉइड, पायथन) बनाम प्रोप्राइटरी सॉफ्टवेयर (विंडोज, एमएस ऑफिस)", "लिनस टोरवाल्ड्स ने 1991 में लिनक्स कर्नल (Linux Kernel) का निर्माण किया", "जीएनयू प्रोजेक्ट (रिचर्ड स्टालमैन): जीपीएल (GPL) फ्री सॉफ्टवेयर लाइसेंस", "लिनक्स फाइल अनुमतियां: Read (r=4), Write (w=2), Execute (x=1); 'chmod 755' का अर्थ है स्वामी को पूर्ण अधिकार (4+2+1=7) तथा ग्रुप व अन्य को केवल पढ़ने व चलाने का अधिकार (4+1=5)"],
        "q_en": "Who wrote and released the original open-source Linux operating system kernel in 1991 while a student at the University of Helsinki?",
        "q_hi": "1991 में हेलसिंकी विश्वविद्यालय में छात्र जीवन के दौरान प्रसिद्ध ओपन-सोर्स 'लिनक्स कर्नल' (Linux Kernel) का मूल कोड किसने लिखा था?",
        "options_en": ["Linus Torvalds (लिनस टोरवाल्ड्स)", "Richard Stallman", "Dennis Ritchie", "Ken Thompson"],
        "options_hi": ["लिनस टोरवाल्ड्स (Linus Torvalds)", "रिचर्ड स्टालमैन (Richard Stallman)", "डेनिस रिची (Dennis Ritchie - C भाषा के जनक)", "केन थॉम्पसन (यूनिक्स के सह-जनक)"],
        "correct_idx": 0,
        "exp_en": "Finnish software engineer Linus Torvalds created and released the initial Linux kernel in 1991, which became the cornerstone of modern servers, supercomputers, and Android.",
        "exp_hi": "लिनस टोरवाल्ड्स ने 1991 में लिनक्स कर्नल बनाया और इसे मुफ्त में जारी किया; आज दुनिया के 100% सुपरकंप्यूटर और सभी एंड्रॉइड स्मार्टफोन लिनक्स पर ही चलते हैं।",
        "cue_en": "Creator of Linux = Linus Torvalds (1991).",
        "cue_hi": "लिनक्स के जनक = लिनस टोरवाल्ड्स (1991)।",
        "wrong_en": ["Creator of Linux kernel.", "Founder of GNU Project and FSF.", "Creator of C language and Unix co-creator.", "Co-creator of Unix operating system."],
        "wrong_hi": ["लिनक्स कर्नल के निर्माता।", "जीएनयू प्रोजेक्ट के संस्थापक।", "सी प्रोग्रामिंग भाषा के जनक।", "यूनिक्स के सह-निर्माता।"]
    }
]

# S13-C8395c7f1 Networking, OSI Model, TCP/IP & DNS Protocols (4 topics)
DATA["S13-C8395c7f1"] = [
    {
        "name_en": "Network Topologies (Star, Mesh, Ring) & Guided vs Unguided Media",
        "name_hi": "नेटवर्क टोपोलॉजी: स्टार, मेश, रिंग, बस एवं गाइडेड बनाम अनगाइडेड माध्यम",
        "concepts_en": ["Star Topology: All nodes connect to a central hub/switch; most common in modern LANs; single node failure does not affect others, but hub failure disables entire network", "Mesh Topology: Every node connected to every other node (dedicated point-to-point links = n*(n-1)/2 connections); robust, fault-tolerant, high cabling cost", "Guided media: Twisted-pair cable (RJ45 connectors), Coaxial cable, Fiber-optic cable (highest bandwidth, immune to EMI)", "Unguided media: Radio waves, Microwaves (line-of-sight satellite communications), Infrared"],
        "concepts_hi": ["स्टार टोपोलॉजी: सभी कंप्यूटर एक केंद्रीय हब/स्विच से जुड़े होते हैं; सबसे लोकप्रिय टोपोलॉजी; एक तार कटने से बाकी नेटवर्क चालू रहता है", "मेश टोपोलॉजी (Mesh): प्रत्येक नोड अन्य सभी नोड्स से सीधे तारों द्वारा जुड़ा होता है [n*(n-1)/2 तार]; सर्वाधिक सुरक्षित व विश्वसनीय", "गाइडेड माध्यम (केबल): ट्विस्टेड पेयर केबल (इथरनेट / RJ45), कोएक्सियल केबल (केबल टीवी), ऑप्टिकल फाइबर (उच्चतम बैंडविड्थ, विद्युत-चुंबकीय व्यवधान से मुक्त)", "अनगाइडेड माध्यम (वायरलेस): रेडियो तरंगें (वाइफाई, ब्लूटूथ), माइक्रोवेव (उपग्रह संचार)"],
        "q_en": "In a Full Mesh network topology connecting 10 computers directly with dedicated physical point-to-point links, how many total communication cables are required?",
        "q_hi": "10 कंप्यूटरों वाले एक 'पूर्ण मेश नेटवर्क' (Full Mesh Topology) में, जहां प्रत्येक कंप्यूटर अन्य सभी से सीधे जुड़ा होता है, कुल कितने संचार केबलों की आवश्यकता होगी?",
        "options_en": ["45 cables [Formula: n*(n-1)/2 = 10*9/2]", "10 cables", "90 cables", "100 cables"],
        "options_hi": ["45 केबल [सूत्र: n*(n-1)/2 = 10*9/2 = 45]", "10 केबल", "90 केबल", "100 केबल"],
        "correct_idx": 0,
        "exp_en": "For 'n' devices in a full mesh network, the total number of duplex links required is given by n*(n-1)/2. For n=10, 10 × 9 / 2 = 45 cables.",
        "exp_hi": "मेश टोपोलॉजी में कुल लिंक की संख्या का सूत्र n*(n-1)/2 होता है। अतः 10 कंप्यूटरों हेतु: (10 × 9)/2 = 45 केबल आवश्यक होंगे।",
        "cue_en": "Full mesh connections formula = n*(n-1)/2.",
        "cue_hi": "मेश नेटवर्क लिंक सूत्र = n*(n-1)/2।",
        "wrong_en": ["Calculated using n*(n-1)/2.", "Cables required in Star or Ring topology.", "Directed links without sharing.", "Square of nodes."],
        "wrong_hi": ["सही गणितीय गणना।", "स्टार या रिंग टोपोलॉजी हेतु।", "एकदिशीय तारों की संख्या।", "वर्ग मान।"]
    },
    {
        "name_en": "OSI 7-Layer Reference Model vs TCP/IP 4-Layer Architecture",
        "name_hi": "ओएसआई (OSI) 7-स्तरीय मॉडल बनाम टीसीपी/आईपी (TCP/IP) 4-स्तरीय मॉडल",
        "concepts_en": ["OSI (Open Systems Interconnection) 7 Layers (bottom to top): 1. Physical (bits, cables, hubs), 2. Data Link (frames, MAC addresses, switches), 3. Network (packets, IP routing, routers), 4. Transport (segments, end-to-end reliability, TCP/UDP), 5. Session, 6. Presentation (encryption, compression), 7. Application (HTTP, DNS, FTP)", "Mnemonic: 'Please Do Not Throw Sausage Pizza Away'", "TCP/IP 4-Layer Model (DoD model): Network Access -> Internet (IP) -> Host-to-Host Transport (TCP/UDP) -> Application", "Data encapsulation adds headers at each descending layer (PDU: Bits -> Frames -> Packets -> Segments -> Data)"],
        "concepts_hi": ["ओएसआई (OSI) 7 परतें (नीचे से ऊपर): 1. भौतिक (Physical - बिट्स), 2. डेटा लिंक (Data Link - फ्रेम्स, मैक पता, स्विच), 3. नेटवर्क (Network - पैकेट्स, आईपी पता, राउटर), 4. ट्रांसपोर्ट (Transport - सेगमेंट्स, टीसीपी/यूडीपी), 5. सेशन, 6. प्रेजेंटेशन (एन्क्रिप्शन, डिक्रिप्शन), 7. एप्लिकेशन (HTTP, DNS)", "सूत्र: 'Please Do Not Throw Sausage Pizza Away'", "टीसीपी/आईपी 4 परतें: नेटवर्क एक्सेस -> इंटरनेट (IP) -> ट्रांसपोर्ट (TCP/UDP) -> एप्लिकेशन", "राउटर तीसरी परत (नेटवर्क लेयर) पर कार्य करता है; नेटवर्क स्विच दूसरी परत (डेटा लिंक) पर कार्य करता है"],
        "q_en": "In the standard OSI 7-layer networking model, at which layer do Network Routers operate to direct IP packets across interconnected networks?",
        "q_hi": "मानक ओएसआई (OSI) 7-स्तरीय नेटवर्किंग मॉडल में नेटवर्क राउटर (Routers) मुख्य रूप से किस परत (Layer) पर कार्य करते हैं?",
        "options_en": ["Layer 3: Network Layer (नेटवर्क लेयर)", "Layer 2: Data Link Layer", "Layer 4: Transport Layer", "Layer 7: Application Layer"],
        "options_hi": ["लेयर 3: नेटवर्क लेयर (Network Layer)", "लेयर 2: डेटा लिंक लेयर (इस पर स्विच कार्य करते हैं)", "लेयर 4: ट्रांसपोर्ट लेयर", "लेयर 7: एप्लिकेशन लेयर"],
        "correct_idx": 0,
        "exp_en": "Routers operate at Layer 3 (Network Layer) of the OSI model, using logical IP addresses to determine the optimal routing path for data packets.",
        "exp_hi": "राउटर ओएसआई मॉडल की तीसरी परत 'नेटवर्क लेयर' पर कार्य करते हैं, जहां वे लॉजिकल आईपी एड्रेस के आधार पर डेटा पैकेटों को सही गंतव्य तक पहुंचाते हैं।",
        "cue_en": "Router = Layer 3 (Network); Switch = Layer 2 (Data Link).",
        "cue_hi": "राउटर = लेयर 3 (नेटवर्क); स्विच = लेयर 2 (डेटा लिंक)।",
        "wrong_en": ["Operating layer of routers.", "Operating layer of switches and bridges.", "Operating layer of TCP and UDP.", "Operating layer of HTTP and SMTP."],
        "wrong_hi": ["राउटर की परत।", "नेटवर्क स्विच की परत।", "टीसीपी/यूडीपी की परत।", "एप्लिकेशन सॉफ्टवेयर की परत।"]
    },
    {
        "name_en": "Internet Protocol: IPv4 vs IPv6 Addressing, Subnetting & DHCP",
        "name_hi": "इंटरनेट प्रोटोकॉल: IPv4 बनाम IPv6 एड्रेस, सबनेटिंग एवं डीएचसीपी (DHCP)",
        "concepts_en": ["IPv4: 32-bit address represented in dotted-decimal notation (e.g., 192.168.1.1); provides 2³² ≈ 4.3 billion unique addresses (exhausted globally)", "IPv6: 128-bit address represented in 8 groups of 4 hexadecimal digits separated by colons (e.g., 2001:0db8::8a2e:0370:7334); provides 2¹²⁸ ≈ 3.4 × 10³⁸ addresses (practically inexhaustible)", "DHCP (Dynamic Host Configuration Protocol): Automatically assigns dynamic IP addresses, default gateways, and DNS servers to client devices joining a network", "NAT (Network Address Translation): Translates private RFC 1918 IPs to public IP"],
        "concepts_hi": ["IPv4: 32-बिट पता, दशमलव प्रणाली में लिखा जाता है (जैसे 192.168.1.1); कुल 2³² ≈ 4.3 अरब पते (अब समाप्त हो चुके हैं)", "IPv6: 128-बिट पता, हेक्साडेसिमल प्रारूप में कोलन द्वारा अलग किए 8 समूहों में (जैसे 2001:0db8::7334); कुल 2¹²⁸ ≈ 3.4 × 10³⁸ पते (असीमित)", "डीएचसीपी (DHCP): नेटवर्क से जुड़ने वाले कंप्यूटरों को स्वतः आईपी एड्रेस, सबनेट मास्क और गेटवे आवंटित करने वाला प्रोटोकॉल", "एनएटी (NAT): निजी आईपी को सार्वजनिक आईपी में बदलने की तकनीक"],
        "q_en": "What is the bit-length of an Internet Protocol Version 6 (IPv6) address, designed to replace the exhausted 32-bit IPv4 address space?",
        "q_hi": "समाप्त हो चुके 32-बिट वाले IPv4 पतों के स्थान पर लागू किए गए नए 'IPv6' इंटरनेट प्रोटोकॉल एड्रेस की लंबाई कितने बिट्स (Bits) होती है?",
        "options_en": ["128 bits (128 बिट्स)", "64 bits", "256 bits", "32 bits"],
        "options_hi": ["128 बिट्स (128 bits)", "64 बिट्स", "256 बिट्स", "32 बिट्स (यह IPv4 की लंबाई है)"],
        "correct_idx": 0,
        "exp_en": "IPv6 addresses are 128 bits long (four times the length of 32-bit IPv4), providing 340 undecillion unique addresses to support the Internet of Things (IoT).",
        "exp_hi": "IPv6 पता 128 बिट्स लंबा होता है, जो हेक्साडेसिमल अंकों में लिखा जाता है और लगभग 3.4 × 10³⁸ अद्वितीय इंटरनेट पते प्रदान करता है।",
        "cue_en": "IPv4 = 32 bits; IPv6 = 128 bits.",
        "cue_hi": "IPv4 = 32 बिट; IPv6 = 128 बिट।",
        "wrong_en": ["Length of IPv6 address.", "MAC address is 48 bits, not 64.", "Cryptographic hash size (SHA-256).", "Length of IPv4 address."],
        "wrong_hi": ["IPv6 की सही लंबाई।", "मैक एड्रेस 48 बिट का होता है।", "हैश साइज।", "IPv4 की लंबाई।"]
    },
    {
        "name_en": "Application Layer Protocols: HTTP/HTTPS, DNS Resolution, FTP & SMTP",
        "name_hi": "एप्लिकेशन लेयर प्रोटोकॉल: HTTP/HTTPS, डीएनएस (DNS) नाम समाधान, एफटीपी एवं एसएमटीपी",
        "concepts_en": ["DNS (Domain Name System): 'Phonebook of the Internet'; translates human-readable domain names (e.g., example.com) to machine IP addresses (Port 53 UDP/TCP)", "HTTP (Port 80) vs HTTPS (Port 443): HyperText Transfer Protocol Secure encrypts traffic using TLS/SSL to prevent eavesdropping and tampering", "Email protocols: SMTP (Simple Mail Transfer Protocol, Port 25/587) sends outgoing emails; POP3 (Port 110) downloads emails locally; IMAP (Port 143) syncs email folders across devices", "FTP (File Transfer Protocol, Port 20/21) for client-server file transfers"],
        "concepts_hi": ["डीएनएस (DNS): 'इंटरनेट की फोनबुक'; इंसानों द्वारा पढ़े जाने वाले वेबसाइट नामों (जैसे google.com) को मशीनी आईपी पतों में बदलता है (पोर्ट 53)", "HTTP (पोर्ट 80) बनाम HTTPS (पोर्ट 443): सिक्योर हाइपरटेक्स्ट प्रोटोकॉल जो एसएसएल/टीएलएस (SSL/TLS) एन्क्रिप्शन द्वारा सुरक्षित संचार देता है", "ईमेल प्रोटोकॉल: एसएमटीपी (SMTP - पोर्ट 25) ईमेल भेजने हेतु; आईमैप (IMAP) एवं पीओपी3 (POP3) सर्वर से ईमेल प्राप्त करने हेतु", "एफटीपी (FTP - पोर्ट 21): नेटवर्क पर फाइल अपलोड और डाउनलोड करने का प्रोटोकॉल"],
        "q_en": "Which networking protocol and distributed database system functions as the 'Phonebook of the Internet' by translating human-friendly domain names into machine-readable IP addresses?",
        "q_hi": "इंटरनेट का वह कौन सा वितरित डेटाबेस प्रोटोकॉल है, जो 'इंटरनेट की फोनबुक' की तरह कार्य करते हुए वेबसाइट नामों (डोमेन नेम) को आईपी पतों (IP Addresses) में परिवर्तित करता है?",
        "options_en": ["Domain Name System (DNS / डोमेन नेम सिस्टम)", "Dynamic Host Configuration Protocol (DHCP)", "Simple Network Management Protocol (SNMP)", "Address Resolution Protocol (ARP)"],
        "options_hi": ["डोमेन नेम सिस्टम (DNS)", "डायनामिक होस्ट कॉन्फ़िगरेशन प्रोटोकॉल (DHCP)", "एसएनएमपी (SNMP)", "एड्रेस रेजोल्यूशन प्रोटोकॉल (ARP)"],
        "correct_idx": 0,
        "exp_en": "The Domain Name System (DNS) resolves alphanumeric domain names (like wikipedia.org) to numeric IP addresses required for routing network packets.",
        "exp_hi": "डीएनएस (DNS) डोमेन नामों को आईपी एड्रेस में मैप करता है ताकि इंटरनेट ब्राउज़र सही वेब सर्वर से जुड़ सके।",
        "cue_en": "Domain name to IP = DNS (Domain Name System).",
        "cue_hi": "डोमेन नेम से आईपी एड्रेस = डीएनएस (DNS)।",
        "wrong_en": ["Translates domain names to IPs.", "Assigns IP addresses automatically.", "Monitors network device health.", "Maps IP address to MAC address on LAN."],
        "wrong_hi": ["वेबसाइट नाम को आईपी में बदलता है।", "आईपी असाइन करता है।", "नेटवर्क प्रबंधन करता है।", "आईपी को मैक पते में बदलता है।"]
    }
]

# S13-C21e5550f Cybersecurity, Cryptography, Cloud Computing & AI Basics (2 topics)
DATA["S13-C21e5550f"] = [
    {
        "name_en": "Cybersecurity & Cryptography: Malware, Phishing, Ransomware & Public-Key Encryption",
        "name_hi": "साइबर सुरक्षा एवं क्रिप्टोग्राफी: मैलवेयर, फ़िशिंग, रैनसमवेयर एवं सार्वजनिक-कुंजी एन्क्रिप्शन (RSA)",
        "concepts_en": ["Malware types: Viruses (require host file), Worms (self-replicating, propagate across networks), Trojan Horses (disguised as benign software), Ransomware (encrypts victim's files and demands ransom in cryptocurrency, e.g., WannaCry)", "Phishing: Social engineering attacks using deceptive emails/websites to harvest credentials; Spear Phishing targets specific executives", "Symmetric Encryption (Single private key shared by sender and receiver: AES, DES) vs Asymmetric / Public-Key Encryption (Pair of keys: Public key encrypts, Private key decrypts; RSA, Diffie-Hellman, ECC)", "Digital Signatures: Provide Authentication, Integrity, and Non-repudiation using sender's private key"],
        "concepts_hi": ["मैलवेयर के प्रकार: वायरस (होस्ट फाइल की जरूरत), वर्म (नेटवर्क पर स्वतः फैलने वाले), ट्रोजन हॉर्स (हानिरहित दिखने वाले धोखेबाज प्रोग्राम), रैनसमवेयर (फाइलों को एन्क्रिप्ट कर फिरौती मांगना, जैसे वानाक्राई)", "फ़िशिंग (Phishing): नकली ईमेल या फर्जी वेबसाइटों द्वारा गोपनीय पासवर्ड व ओटीपी चुराना", "सममित क्रिप्टोग्राफी (Symmetric): एक ही गुप्त कुंजी से एन्क्रिप्शन व डिक्रिप्शन (AES) बनाम असममित (Asymmetric / Public Key): दो कुंजियां - सार्वजनिक कुंजी एन्क्रिप्ट करती है और निजी कुंजी डिक्रिप्ट करती है (RSA)", "डिजिटल हस्ताक्षर: प्रेषक की निजी कुंजी द्वारा प्रमाणित हस्ताक्षर जो अखंडता व गैर-अस्वीकृति सुनिश्चित करते हैं"],
        "q_en": "In Public-Key (Asymmetric) Cryptography, which cryptographic key is utilized by the recipient to decrypt a confidential message encrypted by the sender using the recipient's public key?",
        "q_hi": "असममित (पब्लिक-की) क्रिप्टोग्राफी में प्रेषक द्वारा प्राप्तकर्ता की सार्वजनिक कुंजी (Public Key) से एन्क्रिप्ट किए गए गोपनीय संदेश को पढ़ने हेतु प्राप्तकर्ता द्वारा किस कुंजी का उपयोग किया जाता है?",
        "options_en": ["The recipient's Private Key (प्राप्तकर्ता की निजी कुंजी)", "The sender's Public Key", "The sender's Private Key", "A shared session secret passkey"],
        "options_hi": ["प्राप्तकर्ता की निजी गुप्त कुंजी (Recipient's Private Key)", "प्रेषक की सार्वजनिक कुंजी", "प्रेषक की निजी कुंजी", "साझा पासवर्ड कुंजी"],
        "correct_idx": 0,
        "exp_en": "In asymmetric encryption, a message encrypted with a user's Public Key can ONLY be decrypted by the corresponding matching Private Key, known solely to the recipient.",
        "exp_hi": "पब्लिक की क्रिप्टोग्राफी में डेटा को किसी की पब्लिक की से कोई भी लॉक (एन्क्रिप्ट) कर सकता है, लेकिन उसे खोलने (डिक्रिप्ट) की चाबी केवल प्राप्तकर्ता की अपनी सीक्रेट 'प्राइवेट की' (निजी कुंजी) के पास होती है।",
        "cue_en": "Encrypt with Public Key -> Decrypt with matching Private Key.",
        "cue_hi": "पब्लिक की से एन्क्रिप्ट -> प्राइवेट की से डिक्रिप्ट।",
        "wrong_en": ["Sole key capable of decryption.", "Used to verify digital signatures.", "Used to sign outgoing messages.", "Concept of symmetric cryptography."],
        "wrong_hi": ["डिक्रिप्शन की एकमात्र कुंजी।", "डिजिटल हस्ताक्षर सत्यापन में प्रयुक्त।", "हस्ताक्षर बनाने में प्रयुक्त।", "सिमेट्रिक एन्क्रिप्शन का तरीका।"]
    },
    {
        "name_en": "Cloud Computing Models (IaaS, PaaS, SaaS) & Artificial Intelligence Foundations",
        "name_hi": "क्लाउड कंप्यूटिंग मॉडल (IaaS, PaaS, SaaS) एवं कृत्रिम बुद्धिमत्ता (AI) के मूल सिद्धांत",
        "concepts_en": ["Cloud Service Models: Infrastructure as a Service (IaaS: AWS EC2, Azure VMs - virtual servers, storage, raw networking), Platform as a Service (PaaS: Google App Engine, Heroku - runtime environment, databases for developers), Software as a Service (SaaS: Gmail, Salesforce, Microsoft 365 - end-user web applications)", "Cloud Deployment: Public, Private, Hybrid (combines on-premises private cloud with public cloud)", "AI and Machine Learning: Supervised learning (labeled training data, classification/regression), Unsupervised learning (clustering, dimensionality reduction), Reinforcement learning (rewards and penalties)", "Deep Learning & Neural Networks: Multi-layered Artificial Neural Networks (ANN), Transformers and Large Language Models (LLMs)"],
        "concepts_hi": ["क्लाउड सेवा मॉडल: (1) आईएएएस (IaaS): बुनियादी ढांचा (वर्चुअल सर्वर, स्टोरेज, जैसे AWS, Azure); (2) पाएएएस (PaaS): विकास मंच (डेवलपर्स हेतु रनटाइम, डेटाबेस); (3) साएस (SaaS): पूर्ण सॉफ्टवेयर एप्लिकेशन (जैसे जीमेल, एमएस 365, गूगल डॉक्स)", "क्लाउड डिप्लॉयमेंट: पब्लिक, प्राइवेट एवं हाइब्रिड क्लाउड", "आर्टिफिशियल इंटेलिजेंस (AI) व मशीन लर्निंग: सुपरवाइज्ड लर्निंग (लेबल डेटा), अनसुपरवाइज्ड लर्निंग (बिना लेबल पैटर्न पहचान), रीइन्फोर्समेंट लर्निंग (इनाम और दंड)", "डीप लर्निंग: बहु-स्तरीय न्यूरल नेटवर्क, ट्रांसफॉर्मर मॉडल एवं लार्ज लैंग्वेज मॉडल (LLMs)"],
        "q_en": "Web-based applications such as Google Workspace (Docs/Sheets), Microsoft 365, and Gmail represent which delivery model of Cloud Computing?",
        "q_hi": "गूगल डॉक्स, माइक्रोसॉफ्ट 365 और जीमेल जैसे वेब ब्राउज़र पर सीधे चलने वाले एंड-यूजर सॉफ्टवेयर क्लाउड कंप्यूटिंग के किस सेवा मॉडल का प्रतिनिधित्व करते हैं?",
        "options_en": ["Software as a Service (SaaS / सॉफ्टवेयर एज़ अ सर्विस)", "Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Network as a Service (NaaS)"],
        "options_hi": ["सॉफ्टवेयर एज़ अ सर्विस (SaaS)", "इंफ्रास्ट्रक्चर एज़ अ सर्विस (IaaS)", "प्लेटफ़ॉर्म एज़ अ सर्विस (PaaS)", "नेटवर्क एज़ अ सर्विस (NaaS)"],
        "correct_idx": 0,
        "exp_en": "Software as a Service (SaaS) delivers complete applications over the internet accessible via web browsers without requiring users to install, manage, or maintain underlying hardware or operating systems.",
        "exp_hi": "सॉफ्टवेयर एज़ अ सर्विस (SaaS) में उपयोगकर्ता को सीधे इंटरनेट पर बना-बनाया सॉफ्टवेयर मिलता है (जैसे जीमेल या गूगल डॉक्स), जहां सर्वर, डेटाबेस व कोडिंग का सारा प्रबंधन सेवा प्रदाता करता है।",
        "cue_en": "End-user web apps (Gmail, Office 365) = SaaS.",
        "cue_hi": "सीधे इस्तेमाल होने वाले क्लाउड सॉफ्टवेयर = SaaS।",
        "wrong_en": ["End-user applications delivery.", "Provides raw compute, VMs, storage.", "Provides development environment/runtimes.", "Network connectivity provisioning."],
        "wrong_hi": ["सॉफ्टवेयर सेवा मॉडल।", "हार्डवेयर व सर्वर मॉडल।", "डेवलपर्स हेतु प्लेटफॉर्म।", "नेटवर्क कनेक्टिविटी।"]
    }
]

print("Loaded S13 successfully")
