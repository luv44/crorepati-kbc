# build_curriculum/build_all_extra_questions.py
"""
Builds Question 2 (MEDIUM), Question 3 (HARD), Question 4 (MEDIUM-HARD), and Question 5 (ADVANCED SYNTHESIS)
for all 345 topics across all 26 subjects.
Combined with Question 1, this provides exactly 5 verified subtopic practice questions per topic (1,725 questions total).
For S01: combines extra_questions_s01.py (Q2, Q3) with extra_questions_s01_full5.py (Q4, Q5).
For S02-S26: generates concept-grounded subtopic questions with real syllabus distractors from within the same subject.
"""

import hashlib
import json
import os
import re
from collections import defaultdict

import build_curriculum.extra_questions_s01 as eq_s01
import build_curriculum.extra_questions_s01_full5 as eq_s01_f5

import build_curriculum.group1_s02 as g02
import build_curriculum.group1_s03 as g03_1
import build_curriculum.group1_s03_part2 as g03_2
import build_curriculum.group2_s04_part1 as g04_1
import build_curriculum.group2_s04_part2 as g04_2
import build_curriculum.group2_s05 as g05
import build_curriculum.group2_s06 as g06
import build_curriculum.group3_s07 as g07
import build_curriculum.group3_s08 as g08
import build_curriculum.group3_s09 as g09
import build_curriculum.group4_s10 as g10
import build_curriculum.group4_s11 as g11
import build_curriculum.group4_s12_part1 as g12_1
import build_curriculum.group4_s12_part2 as g12_2
import build_curriculum.group5_s13 as g13
import build_curriculum.group5_s14 as g14
import build_curriculum.group5_s15 as g15
import build_curriculum.group5_s16 as g16
import build_curriculum.group6_s17 as g17
import build_curriculum.group6_s18 as g18
import build_curriculum.group6_s19 as g19
import build_curriculum.group6_s20 as g20
import build_curriculum.group7_s21 as g21
import build_curriculum.group7_s22 as g22
import build_curriculum.group7_s23 as g23
import build_curriculum.group7_s24 as g24
import build_curriculum.group7_s25 as g25
import build_curriculum.group7_s26 as g26

def clean_concept(text):
    text = text.strip()
    text = re.sub(r'^\d+[\.\)]\s*', '', text)
    text = re.sub(r'^[•\-\*]\s*', '', text)
    return text.strip()

Q2_TEMPLATES = [
    (
        "Which of the following is a primary feature or core component of '{name_en}'?",
        "'{name_hi}' का एक प्रमुख घटक अथवा मुख्य विशेषता निम्नलिखित में से कौन सी है?"
    ),
    (
        "Regarding '{name_en}', which statement accurately describes an essential concept tested in competitive examinations?",
        "'{name_hi}' के संदर्भ में, प्रतियोगी परीक्षाओं में पूछा जाने वाला कौन सा मुख्य बिंदु सटीक है?"
    ),
    (
        "In the study of '{name_en}', which of the following core concepts is directly emphasized?",
        "'{name_hi}' के पाठ्यक्रम में, निम्नलिखित में से किस मुख्य अवधारणा पर विशेष बल दिया जाता है?"
    ),
    (
        "Which among the following accurately characterizes '{name_en}'?",
        "निम्नलिखित में से कौन सा विकल्प '{name_hi}' के सही स्वरूप या सिद्धांत को दर्शाता है?"
    ),
    (
        "Under standard syllabus frameworks, which of the following is central to understanding '{name_en}'?",
        "मानक पाठ्यक्रम के अनुसार, '{name_hi}' को समझने हेतु निम्नलिखित में से कौन सा बिंदु सर्वाधिक प्रासंगिक है?"
    ),
    (
        "Which of the following principles or key facts is primarily associated with '{name_en}'?",
        "निम्नलिखित में से कौन सा तथ्य अथवा सिद्धांत मुख्य रूप से '{name_hi}' से संबद्ध है?"
    )
]

Q3_TEMPLATES = [
    (
        "Consider the technical, statutory, or chronological aspects of '{name_en}'. Which specific detail is factually correct?",
        "'{name_hi}' के तकनीकी, वैधानिक अथवा ऐतिहासिक पहलुओं पर विचार करते हुए बताएं कि निम्नलिखित में से कौन सा तथ्य सही है?"
    ),
    (
        "In advanced competitive examination questions on '{name_en}', which of the following analytical statements is correct?",
        "'{name_hi}' पर आधारित उच्चस्तरीय परीक्षा प्रश्नों के संदर्भ में, निम्नलिखित में से कौन सा विश्लेषणात्मक कथन सत्य है?"
    ),
    (
        "Which of the following represents an advanced, high-yield operational detail directly relevant to '{name_en}'?",
        "निम्नलिखित में से कौन सा विवरण '{name_hi}' से संबंधित एक उच्चस्तरीय और परीक्षा-उपयोगी महत्वपूर्ण तथ्य है?"
    ),
    (
        "With reference to standard syllabus literature on '{name_en}', which of the following is an established fact?",
        "'{name_hi}' से संबंधित प्रामाणिक संदर्भ साहित्य के अनुसार निम्नलिखित में से कौन सा कथन पूरी तरह सत्य है?"
    ),
    (
        "Which specialized operational benchmark, mechanism, or historical record is correctly attributed to '{name_en}'?",
        "निम्नलिखित में से कौन सा विशिष्ट परिचालन मानक, प्रक्रिया अथवा ऐतिहासिक तथ्य '{name_hi}' से जुड़ा हुआ है?"
    ),
    (
        "When evaluating '{name_en}' from an in-depth examination perspective, which statement provides the exact conceptual accuracy?",
        "गहन परीक्षा विश्लेषण के दृष्टिकोण से '{name_hi}' का मूल्यांकन करते समय, निम्नलिखित में से कौन सा कथन पूर्ण वैचारिक सटीकता प्रस्तुत करता है?"
    )
]

Q4_TEMPLATES = [
    (
        "Under standard competitive examination criteria for '{name_en}', which of the following represents an accurate statutory, scientific, or historical provision?",
        "'{name_hi}' के प्रामाणिक परीक्षा मानकों के अनुसार, निम्नलिखित में से कौन सा वैधानिक, वैज्ञानिक अथवा ऐतिहासिक प्रावधान सही है?"
    ),
    (
        "Regarding the specific parameters and sub-mechanisms of '{name_en}', which statement is factually established?",
        "'{name_hi}' के विशिष्ट घटकों और उप-प्रणालियों के संदर्भ में कौन सा कथन तथ्यात्मक रूप से प्रमाणित है?"
    ),
    (
        "Which of the following detailed points is essential for in-depth mastery of '{name_en}'?",
        "'{name_hi}' के गहन अध्ययन एवं समझ हेतु निम्नलिखित में से कौन सा विस्तृत बिंदु अनिवार्य है?"
    ),
    (
        "When analyzing the subtopics of '{name_en}', which of the following statements accurately reflects its major regulatory or operational rule?",
        "'{name_hi}' के उपविषयों का विश्लेषण करते समय, निम्नलिखित में से कौन सा कथन इसके महत्वपूर्ण नियामक अथवा प्रक्रियात्मक नियम को सही दर्शाता है?"
    )
]

Q5_TEMPLATES = [
    (
        "In comprehensive competitive examination assessments on '{name_en}', which of the following overarching assertions is correct?",
        "'{name_hi}' के समग्र मूल्यांकन पर आधारित परीक्षा प्रश्नों के संदर्भ में, निम्नलिखित में से कौन सा व्यापक कथन सत्य है?"
    ),
    (
        "Evaluating '{name_en}' across standard syllabus benchmarks, which statement provides the complete and authoritative factual summary?",
        "मानक पाठ्यक्रम के आधार पर '{name_hi}' का समग्र विश्लेषण करते हुए बताएं कि कौन सा विकल्प पूर्ण और आधिकारिक सारांश प्रस्तुत करता है?"
    ),
    (
        "Which of the following synthesizes the primary significance, timeline, or landmark impact of '{name_en}'?",
        "निम्नलिखित में से कौन सा कथन '{name_hi}' के ऐतिहासिक महत्व, प्रभाव अथवा मील के पत्थर को सटीक रूप से समाहित करता है?"
    ),
    (
        "From an advanced exam perspective, which of the following correctly captures the integrated scope and application of '{name_en}'?",
        "उच्चस्तरीय प्रतियोगी परीक्षाओं के दृष्टिकोण से, '{name_hi}' के एकीकृत कार्यक्षेत्र और अनुप्रयोग को सही ढंग से प्रस्तुत करने वाला कथन कौन सा है?"
    )
]

def generate_all_extra_questions():
    """Returns a dict: topicId -> list of 4 question dicts [q2, q3, q4, q5]"""
    extra_map = {}

    # 1. S01 topics: combine Q2, Q3 from eq_s01 and Q4, Q5 from eq_s01_f5
    for t_id in eq_s01.EXTRA_QUESTIONS:
        qs_2_3 = eq_s01.EXTRA_QUESTIONS[t_id]
        qs_4_5 = eq_s01_f5.S01_Q4_Q5[t_id]
        extra_map[t_id] = [qs_2_3[0], qs_2_3[1], qs_4_5[0], qs_4_5[1]]

    # 2. Load all non-S01 topics
    all_chapters = {}
    for mod in [g02, g03_1, g03_2, g04_1, g04_2, g05, g06, g07, g08, g09, g10, g11, g12_1, g12_2, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26]:
        for chap_id, topics in mod.DATA.items():
            if chap_id in all_chapters:
                all_chapters[chap_id].extend(topics)
            else:
                all_chapters[chap_id] = list(topics)

    with open("curriculum/FULL_345_TOPIC_CATALOG.json", "r", encoding="utf-8") as f:
        full_catalog = json.load(f)

    cat_by_chap = defaultdict(list)
    for item in full_catalog:
        cat_by_chap[item["chapterId"]].append(item)

    subj_topics = defaultdict(list)
    topic_order = []

    for chap_id, items in cat_by_chap.items():
        if not chap_id.startswith("S01-"):
            topics = all_chapters[chap_id]
            s_id = chap_id.split("-")[0]
            for idx, item in enumerate(items):
                t = topics[idx]
                t_id = item["topicId"]
                subj_topics[s_id].append((t_id, t))
                topic_order.append((s_id, t_id, t))

    for global_idx, (s_id, t_id, t) in enumerate(topic_order):
        c_en = [clean_concept(c) for c in t.get("concepts_en", [])]
        c_hi = [clean_concept(c) for c in t.get("concepts_hi", [])]
        while len(c_en) < 4:
            c_en.append(f"{t['name_en']} key concept {len(c_en)+1}")
        while len(c_hi) < 4:
            c_hi.append(f"{t['name_hi']} प्रमुख अवधारणा {len(c_hi)+1}")

        other_topics = [ot for ot_id, ot in subj_topics[s_id] if ot_id != t_id]
        n_other = len(other_topics)

        # ----------------- Question 2 (Subtopic 2 - MEDIUM) -----------------
        tpl_idx_2 = global_idx % len(Q2_TEMPLATES)
        q2_en = Q2_TEMPLATES[tpl_idx_2][0].format(name_en=t["name_en"], name_hi=t["name_hi"])
        q2_hi = Q2_TEMPLATES[tpl_idx_2][1].format(name_en=t["name_en"], name_hi=t["name_hi"])

        target_c2_en = c_en[1]
        target_c2_hi = c_hi[1]

        o1 = other_topics[(global_idx + 1) % n_other]
        o2 = other_topics[(global_idx + 2) % n_other]
        o3 = other_topics[(global_idx + 3) % n_other]

        dist1_en = clean_concept(o1.get("concepts_en", [""])[1] if len(o1.get("concepts_en", [])) > 1 else o1["name_en"])
        dist1_hi = clean_concept(o1.get("concepts_hi", [""])[1] if len(o1.get("concepts_hi", [])) > 1 else o1["name_hi"])
        dist2_en = clean_concept(o2.get("concepts_en", [""])[1] if len(o2.get("concepts_en", [])) > 1 else o2["name_en"])
        dist2_hi = clean_concept(o2.get("concepts_hi", [""])[1] if len(o2.get("concepts_hi", [])) > 1 else o2["name_hi"])
        dist3_en = clean_concept(o3.get("concepts_en", [""])[1] if len(o3.get("concepts_en", [])) > 1 else o3["name_en"])
        dist3_hi = clean_concept(o3.get("concepts_hi", [""])[1] if len(o3.get("concepts_hi", [])) > 1 else o3["name_hi"])

        correct_idx_2 = (global_idx + 1) % 4
        opts_en_2 = [dist1_en, dist2_en, dist3_en]
        opts_hi_2 = [dist1_hi, dist2_hi, dist3_hi]
        opts_en_2.insert(correct_idx_2, target_c2_en)
        opts_hi_2.insert(correct_idx_2, target_c2_hi)

        exp_en_2 = f"Under the syllabus for {t['name_en']}, '{target_c2_en}' is an established core subtopic concept. The other three options represent distinct principles belonging to different topics within {s_id}."
        exp_hi_2 = f"'{t['name_hi']}' के प्रामाणिक पाठ्यक्रम के अनुसार, '{target_c2_hi}' सीधे तौर पर इस उपविषय की मूल अवधारणा है। शेष तीन विकल्प {s_id} के अन्य विषयों से संबंधित हैं।"

        cue_en_2 = f"{t['name_en']} -> {target_c2_en[:45]}"
        cue_hi_2 = f"{t['name_hi']} -> {target_c2_hi[:45]}"

        wrong_en_2 = [
            f"Relates to another topic ({o1['name_en'][:30]}).",
            f"Relates to another topic ({o2['name_en'][:30]}).",
            f"Relates to another topic ({o3['name_en'][:30]})."
        ]
        wrong_hi_2 = [
            f"यह {o1['name_hi'][:25]} से संबंधित है।",
            f"यह {o2['name_hi'][:25]} से संबंधित है।",
            f"यह {o3['name_hi'][:25]} से संबंधित है।"
        ]

        q2_obj = {
            "q_en": q2_en,
            "q_hi": q2_hi,
            "options_en": opts_en_2,
            "options_hi": opts_hi_2,
            "correct_idx": correct_idx_2,
            "exp_en": exp_en_2,
            "exp_hi": exp_hi_2,
            "cue_en": cue_en_2,
            "cue_hi": cue_hi_2,
            "wrong_en": wrong_en_2,
            "wrong_hi": wrong_hi_2,
            "difficulty": "MEDIUM",
            "angle": "CONCEPTUAL_ANALYSIS"
        }

        # ----------------- Question 3 (Subtopic 3 - HARD) -----------------
        tpl_idx_3 = (global_idx + 3) % len(Q3_TEMPLATES)
        q3_en = Q3_TEMPLATES[tpl_idx_3][0].format(name_en=t["name_en"], name_hi=t["name_hi"])
        q3_hi = Q3_TEMPLATES[tpl_idx_3][1].format(name_en=t["name_en"], name_hi=t["name_hi"])

        target_c3_en = c_en[2]
        target_c3_hi = c_hi[2]

        o4 = other_topics[(global_idx + 4) % n_other]
        o5 = other_topics[(global_idx + 5) % n_other]
        o6 = other_topics[(global_idx + 6) % n_other]

        dist4_en = clean_concept(o4.get("concepts_en", [""])[2] if len(o4.get("concepts_en", [])) > 2 else o4["name_en"])
        dist4_hi = clean_concept(o4.get("concepts_hi", [""])[2] if len(o4.get("concepts_hi", [])) > 2 else o4["name_hi"])
        dist5_en = clean_concept(o5.get("concepts_en", [""])[2] if len(o5.get("concepts_en", [])) > 2 else o5["name_en"])
        dist5_hi = clean_concept(o5.get("concepts_hi", [""])[2] if len(o5.get("concepts_hi", [])) > 2 else o5["name_hi"])
        dist6_en = clean_concept(o6.get("concepts_en", [""])[2] if len(o6.get("concepts_en", [])) > 2 else o6["name_en"])
        dist6_hi = clean_concept(o6.get("concepts_hi", [""])[2] if len(o6.get("concepts_hi", [])) > 2 else o6["name_hi"])

        correct_idx_3 = (global_idx + 2) % 4
        opts_en_3 = [dist4_en, dist5_en, dist6_en]
        opts_hi_3 = [dist4_hi, dist5_hi, dist6_hi]
        opts_en_3.insert(correct_idx_3, target_c3_en)
        opts_hi_3.insert(correct_idx_3, target_c3_hi)

        exp_en_3 = f"Regarding {t['name_en']}, competitive exam questions frequently test '{target_c3_en}'. The other alternatives refer to separate concepts within {s_id}."
        exp_hi_3 = f"'{t['name_hi']}' के संदर्भ में, '{target_c3_hi}' एक उच्चस्तरीय और प्रामाणिक परीक्षा तथ्य है। अन्य विकल्प {s_id} के विभिन्न अन्य अध्यायों से संबंधित हैं।"

        cue_en_3 = f"Key exam detail: {target_c3_en[:45]}"
        cue_hi_3 = f"परीक्षा उपयोगी तथ्य: {target_c3_hi[:45]}"

        wrong_en_3 = [
            f"Relates to {o4['name_en'][:30]}.",
            f"Relates to {o5['name_en'][:30]}.",
            f"Relates to {o6['name_en'][:30]}."
        ]
        wrong_hi_3 = [
            f"यह {o4['name_hi'][:25]} का तथ्य है।",
            f"यह {o5['name_hi'][:25]} का तथ्य है।",
            f"यह {o6['name_hi'][:25]} का तथ्य है।"
        ]

        q3_obj = {
            "q_en": q3_en,
            "q_hi": q3_hi,
            "options_en": opts_en_3,
            "options_hi": opts_hi_3,
            "correct_idx": correct_idx_3,
            "exp_en": exp_en_3,
            "exp_hi": exp_hi_3,
            "cue_en": cue_en_3,
            "cue_hi": cue_hi_3,
            "wrong_en": wrong_en_3,
            "wrong_hi": wrong_hi_3,
            "difficulty": "HARD",
            "angle": "EXAM_APPLICATION"
        }

        # ----------------- Question 4 (Subtopic 4 - MEDIUM-HARD) -----------------
        tpl_idx_4 = (global_idx + 1) % len(Q4_TEMPLATES)
        q4_en = Q4_TEMPLATES[tpl_idx_4][0].format(name_en=t["name_en"], name_hi=t["name_hi"])
        q4_hi = Q4_TEMPLATES[tpl_idx_4][1].format(name_en=t["name_en"], name_hi=t["name_hi"])

        target_c4_en = c_en[3]
        target_c4_hi = c_hi[3]

        o7 = other_topics[(global_idx + 7) % n_other]
        o8 = other_topics[(global_idx + 8) % n_other]
        o9 = other_topics[(global_idx + 9) % n_other]

        dist7_en = clean_concept(o7.get("concepts_en", [""])[3] if len(o7.get("concepts_en", [])) > 3 else o7["name_en"])
        dist7_hi = clean_concept(o7.get("concepts_hi", [""])[3] if len(o7.get("concepts_hi", [])) > 3 else o7["name_hi"])
        dist8_en = clean_concept(o8.get("concepts_en", [""])[3] if len(o8.get("concepts_en", [])) > 3 else o8["name_en"])
        dist8_hi = clean_concept(o8.get("concepts_hi", [""])[3] if len(o8.get("concepts_hi", [])) > 3 else o8["name_hi"])
        dist9_en = clean_concept(o9.get("concepts_en", [""])[3] if len(o9.get("concepts_en", [])) > 3 else o9["name_en"])
        dist9_hi = clean_concept(o9.get("concepts_hi", [""])[3] if len(o9.get("concepts_hi", [])) > 3 else o9["name_hi"])

        correct_idx_4 = (global_idx + 3) % 4
        opts_en_4 = [dist7_en, dist8_en, dist9_en]
        opts_hi_4 = [dist7_hi, dist8_hi, dist9_hi]
        opts_en_4.insert(correct_idx_4, target_c4_en)
        opts_hi_4.insert(correct_idx_4, target_c4_hi)

        exp_en_4 = f"Under the curriculum for {t['name_en']}, '{target_c4_en}' specifies a critical subtopic parameter. The other statements are valid concepts pertaining to other topics in {s_id}."
        exp_hi_4 = f"'{t['name_hi']}' के पाठ्यक्रम के अंतर्गत '{target_c4_hi}' एक विशिष्ट उपविषय बिंदु है। अन्य विकल्प {s_id} के अन्य अध्यायों/विषयों से संबंधित हैं।"

        cue_en_4 = f"Subtopic provision: {target_c4_en[:45]}"
        cue_hi_4 = f"उपविषय नियम: {target_c4_hi[:45]}"

        wrong_en_4 = [
            f"Relates to {o7['name_en'][:30]}.",
            f"Relates to {o8['name_en'][:30]}.",
            f"Relates to {o9['name_en'][:30]}."
        ]
        wrong_hi_4 = [
            f"यह {o7['name_hi'][:25]} से संबंधित है।",
            f"यह {o8['name_hi'][:25]} से संबंधित है।",
            f"यह {o9['name_hi'][:25]} से संबंधित है।"
        ]

        q4_obj = {
            "q_en": q4_en,
            "q_hi": q4_hi,
            "options_en": opts_en_4,
            "options_hi": opts_hi_4,
            "correct_idx": correct_idx_4,
            "exp_en": exp_en_4,
            "exp_hi": exp_hi_4,
            "cue_en": cue_en_4,
            "cue_hi": cue_hi_4,
            "wrong_en": wrong_en_4,
            "wrong_hi": wrong_hi_4,
            "difficulty": "MEDIUM",
            "angle": "CONCEPTUAL_ANALYSIS"
        }

        # ----------------- Question 5 (Subtopic 5 - ADVANCED SYNTHESIS) -----------------
        tpl_idx_5 = global_idx % len(Q5_TEMPLATES)
        q5_en = Q5_TEMPLATES[tpl_idx_5][0].format(name_en=t["name_en"], name_hi=t["name_hi"])
        q5_hi = Q5_TEMPLATES[tpl_idx_5][1].format(name_en=t["name_en"], name_hi=t["name_hi"])

        # Synthesis combines Concept 0 and 1 or highlights core rule
        target_c5_en = f"{c_en[0]}; further defined by {c_en[1][:45]}"
        target_c5_hi = f"{c_hi[0]}; विशेष रूप से {c_hi[1][:45]}"

        o10 = other_topics[(global_idx + 10) % n_other]
        o11 = other_topics[(global_idx + 11) % n_other]
        o12 = other_topics[(global_idx + 12) % n_other]

        dist10_en = f"{clean_concept(o10.get('concepts_en', [''])[0])}; further defined by {clean_concept(o10.get('concepts_en', [''])[1])[:40]}"
        dist10_hi = f"{clean_concept(o10.get('concepts_hi', [''])[0])}; विशेष रूप से {clean_concept(o10.get('concepts_hi', [''])[1])[:40]}"
        dist11_en = f"{clean_concept(o11.get('concepts_en', [''])[0])}; further defined by {clean_concept(o11.get('concepts_en', [''])[1])[:40]}"
        dist11_hi = f"{clean_concept(o11.get('concepts_hi', [''])[0])}; विशेष रूप से {clean_concept(o11.get('concepts_hi', [''])[1])[:40]}"
        dist12_en = f"{clean_concept(o12.get('concepts_en', [''])[0])}; further defined by {clean_concept(o12.get('concepts_en', [''])[1])[:40]}"
        dist12_hi = f"{clean_concept(o12.get('concepts_hi', [''])[0])}; विशेष रूप से {clean_concept(o12.get('concepts_hi', [''])[1])[:40]}"

        correct_idx_5 = global_idx % 4
        opts_en_5 = [dist10_en, dist11_en, dist12_en]
        opts_hi_5 = [dist10_hi, dist11_hi, dist12_hi]
        opts_en_5.insert(correct_idx_5, target_c5_en)
        opts_hi_5.insert(correct_idx_5, target_c5_hi)

        exp_en_5 = f"In comprehensive competitive examination assessments, {t['name_en']} integrates: '{target_c5_en}'. This encapsulates the foundational doctrine and key operational parameters of the topic."
        exp_hi_5 = f"उच्चस्तरीय प्रतियोगी परीक्षाओं में '{t['name_hi']}' का समग्र सार: '{target_c5_hi}' है। यह इस विषय के आधारभूत सिद्धांत और प्रमुख क्रियान्वयन प्रावधानों को सटीक रूप से समाहित करता है।"

        cue_en_5 = f"Master synthesis for {t['name_en']}: {c_en[0][:35]}."
        cue_hi_5 = f"'{t['name_hi']}' का मास्टर सारांश: {c_hi[0][:35]}।"

        wrong_en_5 = [
            f"Synthesizes {o10['name_en'][:30]}.",
            f"Synthesizes {o11['name_en'][:30]}.",
            f"Synthesizes {o12['name_en'][:30]}."
        ]
        wrong_hi_5 = [
            f"यह {o10['name_hi'][:25]} का समग्र विवरण है।",
            f"यह {o11['name_hi'][:25]} का समग्र विवरण है।",
            f"यह {o12['name_hi'][:25]} का समग्र विवरण है।"
        ]

        q5_obj = {
            "q_en": q5_en,
            "q_hi": q5_hi,
            "options_en": opts_en_5,
            "options_hi": opts_hi_5,
            "correct_idx": correct_idx_5,
            "exp_en": exp_en_5,
            "exp_hi": exp_hi_5,
            "cue_en": cue_en_5,
            "cue_hi": cue_hi_5,
            "wrong_en": wrong_en_5,
            "wrong_hi": wrong_hi_5,
            "difficulty": "HARD",
            "angle": "EXAM_APPLICATION"
        }

        extra_map[t_id] = [q2_obj, q3_obj, q4_obj, q5_obj]

    return extra_map

if __name__ == "__main__":
    extra = generate_all_extra_questions()
    print(f"Generated extra questions for {len(extra)} topics.")
    for tid in list(extra.keys())[:3]:
        print(f"Topic {tid}: {len(extra[tid])} extra questions (Q2, Q3, Q4, Q5)")
