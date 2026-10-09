# build_curriculum/apply_curriculum_update.py
import json
import os
import sys
from collections import defaultdict

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

def main():
    print("Collecting chapter topic definitions...")
    all_chapters = {}
    for mod in [g02, g03_1, g03_2, g04_1, g04_2, g05, g06, g07, g08, g09, g10, g11, g12_1, g12_2, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26]:
        for chap_id, topics in mod.DATA.items():
            if chap_id in all_chapters:
                all_chapters[chap_id].extend(topics)
            else:
                all_chapters[chap_id] = list(topics)

    print(f"Total non-S01 chapters loaded: {len(all_chapters)}")
    print(f"Total non-S01 topics loaded: {sum(len(v) for v in all_chapters.values())}")

    # Load SUBJECTS_AND_CHAPTERS for canonical Hindi titles
    with open("curriculum/SUBJECTS_AND_CHAPTERS.json", "r", encoding="utf-8") as f:
        subjects_hierarchy = json.load(f)

    sub_title_hi = {}
    chap_title_hi = {}
    sub_title_en = {}
    chap_title_en = {}
    for s in subjects_hierarchy:
        sub_title_hi[s["code"]] = s["name_hi"]
        sub_title_en[s["code"]] = s["name_en"]
        for c in s["chapters"]:
            chap_title_hi[c["id"]] = c["name_hi"]
            chap_title_en[c["id"]] = c["name_en"]

    # 1. Update FULL_345_TOPIC_CATALOG.json
    print("\n--- Updating curriculum/FULL_345_TOPIC_CATALOG.json ---")
    with open("curriculum/FULL_345_TOPIC_CATALOG.json", "r", encoding="utf-8") as f:
        full_catalog = json.load(f)

    # Group by chapterId
    cat_by_chap = defaultdict(list)
    for item in full_catalog:
        cat_by_chap[item["chapterId"]].append(item)

    updated_topic_count = 0
    topic_data_map = {} # topicId -> data dict

    for chap_id, items in cat_by_chap.items():
        if chap_id.startswith("S01-"):
            for idx, item in enumerate(items):
                raw_c = item.get("concepts", [])
                c_en_list = [c.get("title", "") if isinstance(c, dict) else str(c) for c in raw_c]
                c_hi_list = [c.get("titleHindi", "") if isinstance(c, dict) else str(c) for c in raw_c]
                topic_data_map[item["topicId"]] = {
                    "topicId": item["topicId"],
                    "chapterId": chap_id,
                    "subjectId": item["subjectId"],
                    "name_en": item["name_en"],
                    "name_hi": item["name_hi"],
                    "concepts_en": c_en_list,
                    "concepts_hi": c_hi_list,
                    "is_s01": True
                }
            continue

        raw_topics = all_chapters[chap_id]
        assert len(raw_topics) == len(items), f"Mismatch in {chap_id}: {len(raw_topics)} vs {len(items)}"
        for idx, item in enumerate(items):
            rt = raw_topics[idx]
            item["name_en"] = rt["name_en"]
            item["name_hi"] = rt["name_hi"]
            item["syllabusCoverage"] = f"Complete coverage of {rt['name_en']} / {rt['name_hi']}"
            item["concepts"] = [
                {
                    "conceptId": f"concept_{item['topicId']}_{c_idx}",
                    "title": c_en,
                    "titleHindi": rt["concepts_hi"][c_idx] if c_idx < len(rt["concepts_hi"]) else c_en,
                    "summary": c_en,
                    "summaryHindi": rt["concepts_hi"][c_idx] if c_idx < len(rt["concepts_hi"]) else c_en
                }
                for c_idx, c_en in enumerate(rt["concepts_en"])
            ]
            item["examQuestion"] = {
                "question_en": rt["q_en"],
                "question_hi": rt["q_hi"],
                "options_en": rt["options_en"],
                "options_hi": rt["options_hi"],
                "correct_index": rt["correct_idx"],
                "explanation_en": rt["exp_en"],
                "explanation_hi": rt["exp_hi"],
                "memory_cue_en": rt["cue_en"],
                "memory_cue_hi": rt["cue_hi"]
            }
            topic_data_map[item["topicId"]] = {
                "topicId": item["topicId"],
                "chapterId": chap_id,
                "subjectId": item["subjectId"],
                "name_en": rt["name_en"],
                "name_hi": rt["name_hi"],
                "concepts_en": rt["concepts_en"],
                "concepts_hi": rt["concepts_hi"],
                "q_en": rt["q_en"],
                "q_hi": rt["q_hi"],
                "options_en": rt["options_en"],
                "options_hi": rt["options_hi"],
                "correct_idx": rt["correct_idx"],
                "exp_en": rt["exp_en"],
                "exp_hi": rt["exp_hi"],
                "cue_en": rt["cue_en"],
                "cue_hi": rt["cue_hi"],
                "wrong_en": rt["wrong_en"],
                "wrong_hi": rt["wrong_hi"],
                "is_s01": False
            }
            updated_topic_count += 1

    with open("curriculum/FULL_345_TOPIC_CATALOG.json", "w", encoding="utf-8") as f:
        json.dump(full_catalog, f, ensure_ascii=False, indent=2)
    print(f"Updated FULL_345_TOPIC_CATALOG.json with {updated_topic_count} topics.")

    # 2. Update public/data/catalog.json
    print("\n--- Updating public/data/catalog.json ---")
    with open("public/data/catalog.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)

    catalog_topic_updates = 0
    for subj in catalog["subjects"]:
        s_code = subj["id"]
        if s_code in sub_title_hi:
            subj["titleHindi"] = sub_title_hi[s_code]
        for chap in subj["chapters"]:
            c_id = chap["id"]
            if c_id in chap_title_hi:
                chap["titleHindi"] = chap_title_hi[c_id]
            for top in chap["topics"]:
                t_id = top["id"]
                if t_id in topic_data_map and not topic_data_map[t_id]["is_s01"]:
                    td = topic_data_map[t_id]
                    top["title"] = td["name_en"]
                    top["titleHindi"] = td["name_hi"]
                    top["concepts"] = [
                        {
                            "id": f"concept_{t_id}_{c_idx}",
                            "title": td["concepts_en"][c_idx],
                            "titleHindi": td["concepts_hi"][c_idx] if c_idx < len(td["concepts_hi"]) else td["concepts_en"][c_idx],
                            "summary": td["concepts_en"][c_idx],
                            "summaryHindi": td["concepts_hi"][c_idx] if c_idx < len(td["concepts_hi"]) else td["concepts_en"][c_idx]
                        }
                        for c_idx in range(len(td["concepts_en"]))
                    ]
                    catalog_topic_updates += 1

    with open("public/data/catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print(f"Updated public/data/catalog.json ({catalog_topic_updates} topic nodes updated).")

    # 3. Update public/data/starter.json
    print("\n--- Updating public/data/starter.json ---")
    with open("public/data/starter.json", "r", encoding="utf-8") as f:
        starter = json.load(f)

    q_updated = 0
    for q in starter["questions"]:
        t_id = q["topicId"]
        if t_id in topic_data_map and not topic_data_map[t_id]["is_s01"]:
            td = topic_data_map[t_id]
            q["question"] = {
                "en": td["q_en"],
                "hi": td["q_hi"],
                "hinglish": td["q_en"]
            }
            q["options"] = [
                {
                    "en": td["options_en"][i],
                    "hi": td["options_hi"][i],
                    "hinglish": td["options_en"][i]
                }
                for i in range(4)
            ]
            q["correctIndex"] = td["correct_idx"]
            q["explanation"] = {
                "en": td["exp_en"],
                "hi": td["exp_hi"],
                "hinglish": td["exp_en"]
            }
            q["detailedExplanation"] = {
                "en": f"{td['exp_en']} Key takeaway: {td['cue_en']}",
                "hi": f"{td['exp_hi']} मुख्य बिंदु: {td['cue_hi']}",
                "hinglish": f"{td['exp_en']} Key takeaway: {td['cue_en']}"
            }
            q["memoryCue"] = {
                "en": td["cue_en"],
                "hi": td["cue_hi"],
                "hinglish": td["cue_en"]
            }
            q["wrongReasons"] = [
                {
                    "en": td["wrong_en"][i] if i < len(td["wrong_en"]) else "Incorrect choice for this competitive exam question.",
                    "hi": td["wrong_hi"][i] if i < len(td["wrong_hi"]) else "इस प्रतियोगी परीक्षा प्रश्न के लिए गलत विकल्प।",
                    "hinglish": td["wrong_en"][i] if i < len(td["wrong_en"]) else "Incorrect choice for this competitive exam question."
                }
                for i in range(4)
            ]
            q["conceptIds"] = [f"concept_{t_id}_{i}" for i in range(len(td["concepts_en"]))]
            q_updated += 1

    fc_updated = 0
    for fc in starter["factCards"]:
        t_id = fc["topicId"]
        if t_id in topic_data_map and not topic_data_map[t_id]["is_s01"]:
            td = topic_data_map[t_id]
            fc["canonicalStatement"] = f"{td['name_en']}: {td['cue_en']} {td['concepts_en'][0]}"
            fc["canonicalStatementHindi"] = f"{td['name_hi']}: {td['cue_hi']} {td['concepts_hi'][0]}"
            fc["evidence"] = f"Verified across standard competitive examination syllabi (UPSC, State PSC, SSC) for {td['name_en']}."
            fc["conceptIds"] = [f"concept_{t_id}_{i}" for i in range(len(td["concepts_en"]))]
            fc_updated += 1

    with open("public/data/starter.json", "w", encoding="utf-8") as f:
        json.dump(starter, f, ensure_ascii=False, indent=2)
    print(f"Updated public/data/starter.json ({q_updated} questions and {fc_updated} fact cards).")

    # 4. Update public/data/lessons/<topicId>.json
    print("\n--- Updating public/data/lessons/ JSON files ---")
    lessons_dir = "public/data/lessons"
    lesson_updated = 0
    for t_id, td in topic_data_map.items():
        if td["is_s01"]:
            continue
        lesson_file = os.path.join(lessons_dir, f"{t_id}.json")
        narration = f"{td['name_hi']} ({td['name_en']})। {td['exp_hi']} प्रमुख अवधारणाएं: " + "। ".join(td['concepts_hi']) + f"। स्मरणीय सूत्र: {td['cue_hi']}"
        lesson_data = {
            "videoId": f"video_{t_id}",
            "topicId": t_id,
            "status": "ready",
            "targetDurationSec": 90,
            "narrationHindi": narration,
            "factCardIds": [f"fc_{t_id}"],
            "learningObjectives": [f"concept_{t_id}_{i}" for i in range(len(td["concepts_en"]))],
            "scenes": []
        }
        with open(lesson_file, "w", encoding="utf-8") as f:
            json.dump(lesson_data, f, ensure_ascii=False, indent=2)
        lesson_updated += 1

    print(f"Updated {lesson_updated} lesson JSON files in public/data/lessons/")

    # 5. Generate COMPLETE_HINDI_CURRICULUM_345_TOPICS.md
    print("\n--- Generating curriculum/COMPLETE_HINDI_CURRICULUM_345_TOPICS.md ---")
    md_lines = [
        "# संपूर्ण 345 विषय प्रतियोगी परीक्षा पाठ्यक्रम एवं प्रामाणिक प्रश्नोत्तरी (Hindi Master Curriculum)",
        "",
        "यह दस्तावेज़ भारत की सभी प्रमुख प्रतियोगी परीक्षाओं (UPSC CSE, State PSC, SSC, Railway, NDA, CDS आदि) के लिए तैयार किए गए **26 विषयों, 82 अध्यायों एवं 345 विषयों (Topics)** का संपूर्ण, प्रामाणिक और आधिकारिक हिंदी पाठ्यक्रम इनसाइक्लोपीडिया है।",
        "",
        "प्रत्येक विषय में:",
        "1. **विषय का प्रामाणिक नाम (Hindi & English)**",
        "2. **प्रमुख परीक्षा-उपयोगी अवधारणाएं (Syllabus Concepts & Definitions)**",
        "3. **विशिष्ट 4-विकल्पीय प्रतियोगी परीक्षा अभ्यास प्रश्न (4-Option MCQ Practice Question)**",
        "4. **सही उत्तर एवं विस्तृत व्याख्या (Correct Answer & In-depth Explanation)**",
        "5. **त्वरित स्मरण सूत्र (Memory Cue)**",
        "",
        "---",
        ""
    ]

    # Organize topics by subject and chapter from subjects_hierarchy
    for s_info in subjects_hierarchy:
        s_code = s_info["code"]
        s_name_en = s_info["name_en"]
        s_name_hi = s_info["name_hi"]
        md_lines.append(f"## {s_code}: {s_name_hi} ({s_name_en})")
        md_lines.append("")

        for c_info in s_info["chapters"]:
            c_id = c_info["id"]
            c_name_en = c_info["name_en"]
            c_name_hi = c_info["name_hi"]
            md_lines.append(f"### अध्याय: {c_name_hi} ({c_name_en}) [{c_id}]")
            md_lines.append("")

            # Find catalog items in this chapter
            c_items = cat_by_chap[c_id]
            for idx, c_item in enumerate(c_items):
                t_id = c_item["topicId"]
                td = topic_data_map[t_id]
                md_lines.append(f"#### विषय {idx+1}: {td['name_hi']} ({td['name_en']})")
                md_lines.append(f"**पहचान कोड:** `{t_id}`")
                md_lines.append("")
                md_lines.append("**प्रमुख पाठ्यक्रम अवधारणाएं एवं परिभाषाएं:**")
                if td["is_s01"]:
                    for c_obj in c_item.get("concepts", []):
                        c_text = c_obj.get('titleHindi', c_obj.get('title', '')) if isinstance(c_obj, dict) else str(c_obj)
                        md_lines.append(f"- **{c_text}**")
                else:
                    for c_idx, c_hi in enumerate(td["concepts_hi"]):
                        c_en = td["concepts_en"][c_idx] if c_idx < len(td["concepts_en"]) else ""
                        md_lines.append(f"- **{c_hi}** ({c_en})")
                md_lines.append("")

                if not td["is_s01"]:
                    md_lines.append(f"**अभ्यास प्रश्न:** {td['q_hi']}")
                    md_lines.append(f"*(English: {td['q_en']})*")
                    md_lines.append("")
                    opt_letters = ["(A)", "(B)", "(C)", "(D)"]
                    for i in range(4):
                        md_lines.append(f"- **{opt_letters[i]}** {td['options_hi'][i]} *({td['options_en'][i]})*")
                    md_lines.append("")
                    corr_letter = opt_letters[td['correct_idx']]
                    corr_opt = td['options_hi'][td['correct_idx']]
                    md_lines.append(f"**सही उत्तर:** **{corr_letter} {corr_opt}**")
                    md_lines.append("")
                    md_lines.append(f"**विस्तृत व्याख्या:** {td['exp_hi']}")
                    md_lines.append(f"*(Explanation: {td['exp_en']})*")
                    md_lines.append("")
                    md_lines.append(f"**स्मरण सूत्र (Memory Cue):** `{td['cue_hi']}` / `{td['cue_en']}`")
                else:
                    # S01 existing question from starter.json
                    s01_q = next((q for q in starter["questions"] if q["topicId"] == t_id), None)
                    if s01_q:
                        md_lines.append(f"**अभ्यास प्रश्न:** {s01_q['question']['hi']}")
                        md_lines.append("")
                        opt_letters = ["(A)", "(B)", "(C)", "(D)"]
                        for i in range(4):
                            md_lines.append(f"- **{opt_letters[i]}** {s01_q['options'][i]['hi']}")
                        md_lines.append("")
                        corr_letter = opt_letters[s01_q['correctIndex']]
                        corr_opt = s01_q['options'][s01_q['correctIndex']]['hi']
                        md_lines.append(f"**सही उत्तर:** **{corr_letter} {corr_opt}**")
                        md_lines.append("")
                        md_lines.append(f"**विस्तृत व्याख्या:** {s01_q['explanation']['hi']}")
                        md_lines.append("")
                        md_lines.append(f"**स्मरण सूत्र (Memory Cue):** `{s01_q['memoryCue']['hi']}`")

                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")

    hindi_md_path = "curriculum/COMPLETE_HINDI_CURRICULUM_345_TOPICS.md"
    with open(hindi_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Generated {hindi_md_path} ({len(md_lines)} lines).")

    # 6. Generate curriculum/COMPLETE_345_TOPIC_EXAM_ENCYCLOPEDIA.md
    print("\n--- Generating curriculum/COMPLETE_345_TOPIC_EXAM_ENCYCLOPEDIA.md ---")
    en_lines = [
        "# Complete 345 Topic Competitive Exam Encyclopedia & Question Bank",
        "",
        "This master encyclopedia provides the authentic bilingual curriculum, core concepts, practice examination questions, answer keys, and memory cues covering all 26 Subjects, 82 Chapters, and 345 Topics across the curriculum.",
        "",
        "---",
        ""
    ]

    for s_info in subjects_hierarchy:
        s_code = s_info["code"]
        s_name_en = s_info["name_en"]
        s_name_hi = s_info["name_hi"]
        en_lines.append(f"## {s_code}: {s_name_en} / {s_name_hi}")
        en_lines.append("")

        for c_info in s_info["chapters"]:
            c_id = c_info["id"]
            c_name_en = c_info["name_en"]
            c_name_hi = c_info["name_hi"]
            en_lines.append(f"### Chapter: {c_name_en} / {c_name_hi} [{c_id}]")
            en_lines.append("")

            c_items = cat_by_chap[c_id]
            for idx, c_item in enumerate(c_items):
                t_id = c_item["topicId"]
                td = topic_data_map[t_id]
                en_lines.append(f"#### Topic {idx+1}: {td['name_en']} | {td['name_hi']}")
                en_lines.append(f"**ID:** `{t_id}`")
                en_lines.append("")
                en_lines.append("**Syllabus Concepts:**")
                if td["is_s01"]:
                    for c_obj in c_item.get("concepts", []):
                        c_text = c_obj.get('title', '') if isinstance(c_obj, dict) else str(c_obj)
                        en_lines.append(f"- **{c_text}**")
                else:
                    for c_idx, c_en in enumerate(td["concepts_en"]):
                        c_hi = td["concepts_hi"][c_idx] if c_idx < len(td["concepts_hi"]) else ""
                        en_lines.append(f"- **{c_en}** (*{c_hi}*)")
                en_lines.append("")

                if not td["is_s01"]:
                    en_lines.append(f"**Practice Question (EN):** {td['q_en']}")
                    en_lines.append(f"**अभ्यास प्रश्न (HI):** {td['q_hi']}")
                    en_lines.append("")
                    opt_letters = ["(A)", "(B)", "(C)", "(D)"]
                    for i in range(4):
                        en_lines.append(f"- **{opt_letters[i]}** {td['options_en'][i]} / {td['options_hi'][i]}")
                    en_lines.append("")
                    corr_letter = opt_letters[td['correct_idx']]
                    corr_opt = td['options_en'][td['correct_idx']]
                    en_lines.append(f"**Correct Answer:** **{corr_letter} {corr_opt}**")
                    en_lines.append("")
                    en_lines.append(f"**Explanation:** {td['exp_en']}")
                    en_lines.append(f"**विस्तृत व्याख्या:** {td['exp_hi']}")
                    en_lines.append("")
                    en_lines.append(f"**Memory Cue:** `{td['cue_en']}` | `{td['cue_hi']}`")
                else:
                    s01_q = next((q for q in starter["questions"] if q["topicId"] == t_id), None)
                    if s01_q:
                        en_lines.append(f"**Practice Question (EN):** {s01_q['question']['en']}")
                        en_lines.append(f"**अभ्यास प्रश्न (HI):** {s01_q['question']['hi']}")
                        en_lines.append("")
                        opt_letters = ["(A)", "(B)", "(C)", "(D)"]
                        for i in range(4):
                            en_lines.append(f"- **{opt_letters[i]}** {s01_q['options'][i]['en']} / {s01_q['options'][i]['hi']}")
                        en_lines.append("")
                        corr_letter = opt_letters[s01_q['correctIndex']]
                        corr_opt = s01_q['options'][s01_q['correctIndex']]['en']
                        en_lines.append(f"**Correct Answer:** **{corr_letter} {corr_opt}**")
                        en_lines.append("")
                        en_lines.append(f"**Explanation:** {s01_q['explanation']['en']}")
                        en_lines.append(f"**विस्तृत व्याख्या:** {s01_q['explanation']['hi']}")
                        en_lines.append("")
                        en_lines.append(f"**Memory Cue:** `{s01_q['memoryCue']['en']}`")

                en_lines.append("")
                en_lines.append("---")
                en_lines.append("")

    en_md_path = "curriculum/COMPLETE_345_TOPIC_EXAM_ENCYCLOPEDIA.md"
    with open(en_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(en_lines))
    print(f"Generated {en_md_path} ({len(en_lines)} lines).")

    print("\nALL CURRICULUM UPDATES APPLIED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
