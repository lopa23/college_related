# -*- coding: utf-8 -*-
# Hand-transcribed from the UC Office of the President public Tableau workbook:
# https://visualizedata.ucop.edu/t/Public/views/Freshmanadmissionbydiscipline/Bybroaddiscipline
# ("Freshman admission by discipline"), read live in-browser 2026-09-21/22.
# Fields per campus/year: [applicants, admits, enrollees, admit_gpa_25, admit_gpa_75, enrollee_gpa_25, enrollee_gpa_75, admit_rate_pct, yield_rate_pct]
import json

CS = {
 2023: {"UCB":[9018,375,228,4.20,4.30,4.17,4.29,4,61],"UCD":[5256,989,118,4.19,4.30,4.17,4.30,19,12],
        "UCI":[10071,1702,362,4.12,4.29,4.11,4.29,17,21],"UCLA":[11938,368,134,4.25,4.32,4.25,4.31,3,36],
        "UCR":[5558,2709,229,4.03,4.28,4.00,4.25,49,8],"UCSD":[13729,1621,496,4.19,4.31,4.14,4.31,12,31],
        "UCSB":[9821,1006,144,4.23,4.31,4.21,4.31,10,14],"UCSC":[6596,3901,562,3.96,4.26,3.80,4.17,59,14]},
 2024: {"UCB":[13437,515,343,4.20,4.30,4.17,4.30,4,67],"UCD":[6950,1175,97,4.20,4.30,4.14,4.29,17,8],
        "UCI":[9187,1874,355,4.18,4.29,4.15,4.29,20,19],"UCLA":[10530,435,143,4.25,4.30,4.25,4.32,4,33],
        "UCR":[5001,2684,214,4.03,4.27,3.95,4.22,54,8],"UCSD":[12519,1666,479,4.16,4.30,4.12,4.30,13,29],
        "UCSB":[8560,1470,174,4.25,4.31,4.23,4.32,17,12],"UCSC":[6597,4278,593,4.00,4.26,3.88,4.20,65,14]},
 2025: {"UCB":[9750,629,396,4.20,4.29,4.18,4.29,6,63],"UCD":[4893,946,74,4.20,4.30,4.20,4.28,19,8],
        "UCI":[6794,1874,311,4.17,4.29,4.14,4.28,28,17],"UCLA":[6803,498,138,4.25,4.30,4.23,4.32,7,28],
        "UCR":[5068,4111,236,3.96,4.25,3.73,4.08,81,6],"UCSD":[10785,2143,581,4.16,4.30,4.12,4.29,20,27],
        "UCSB":[5865,1989,182,4.19,4.29,4.14,4.29,34,9],"UCSC":[5952,4725,566,3.92,4.25,3.79,4.10,79,12]},
}
ENG = {
 2023: {"UCB":[26470,1893,942,4.20,4.30,4.18,4.30,7,50],"UCD":[17505,5941,898,4.09,4.29,4.00,4.27,34,15],
        "UCI":[17832,5071,1195,4.11,4.29,4.05,4.28,28,24],"UCLA":[20989,1263,579,4.25,4.32,4.25,4.33,6,46],
        "UCM":[6481,5851,628,3.59,4.15,3.34,3.95,90,11],"UCR":[7776,4767,577,3.95,4.24,3.84,4.14,61,12],
        "UCSD":[16709,2975,816,4.16,4.30,4.10,4.30,18,27],"UCSB":[10685,1919,300,4.20,4.30,4.16,4.29,18,16],
        "UCSC":[4426,2939,411,3.87,4.22,3.71,4.12,66,14]},
 2024: {"UCB":[21831,1698,906,4.21,4.30,4.19,4.30,8,53],"UCD":[16933,6354,1020,4.09,4.29,4.00,4.26,38,16],
        "UCI":[19342,5446,1106,4.14,4.29,4.10,4.28,28,20],"UCLA":[22301,1329,587,4.25,4.32,4.25,4.32,6,44],
        "UCM":[6429,5990,563,3.55,4.14,3.31,3.87,93,9],"UCR":[8486,5979,662,3.86,4.21,3.73,4.07,70,11],
        "UCSD":[18443,3102,797,4.16,4.30,4.12,4.29,17,26],"UCSB":[11873,2445,337,4.20,4.30,4.16,4.30,21,14],
        "UCSC":[5018,3450,448,3.90,4.23,3.78,4.09,69,13]},
 2025: {"UCB":[25025,1788,1002,4.20,4.30,4.18,4.29,7,56],"UCD":[17866,6935,813,4.08,4.28,4.00,4.27,39,12],
        "UCI":[20276,5387,1025,4.15,4.29,4.12,4.29,27,19],"UCLA":[23911,1591,647,4.25,4.32,4.25,4.32,7,41],
        "UCM":[11565,11206,603,3.69,4.21,3.33,3.93,97,5],"UCR":[11480,9615,992,3.84,4.22,3.66,4.01,84,10],
        "UCSD":[20205,3938,1074,4.17,4.30,4.12,4.29,19,27],"UCSB":[12679,2694,338,4.21,4.30,4.18,4.30,21,13],
        "UCSC":[5134,3961,495,3.85,4.22,3.72,4.04,77,12]},
}
CAMPUS_OVERALL_2025 = {  # from the "All" broad-discipline cross-campus table, Fall 2025
 "UCB":[126830,14360,6688,4.15,4.29,4.11,4.28,11,47],"UCD":[102988,45673,6805,4.00,4.26,3.91,4.21,44,15],
 "UCI":[124223,35658,6423,4.04,4.27,4.00,4.25,29,18],"UCLA":[145060,13659,6551,4.20,4.30,4.18,4.30,9,48],
 "UCM":[49366,46565,1982,3.55,4.15,3.27,3.90,94,4],"UCR":[70863,61312,6682,3.65,4.16,3.44,3.94,87,11],
 "UCSD":[136727,38457,7801,4.11,4.29,4.07,4.27,28,20],"UCSB":[110173,42094,5081,4.09,4.28,4.00,4.27,38,12],
 "UCSC":[66393,48122,4597,3.83,4.20,3.72,4.04,72,10],
}
CAMPUS_NAMES={"UCB":"Berkeley","UCD":"Davis","UCI":"Irvine","UCLA":"Los Angeles","UCM":"Merced","UCR":"Riverside","UCSD":"San Diego","UCSB":"Santa Barbara","UCSC":"Santa Cruz"}
FIELDS=["applicants","admits","enrollees","admit_gpa_p25","admit_gpa_p75","enrollee_gpa_p25","enrollee_gpa_p75","admit_rate_pct","yield_rate_pct"]

def to_rows(d):
    return {str(y): {c: dict(zip(FIELDS,v)) for c,v in camp.items()} for y,camp in d.items()}

out = {
  "source": "University of California Office of the President, public Tableau workbook 'Freshman admission by discipline'",
  "source_url": "https://www.universityofcalifornia.edu/about-uc/information-center/freshman-admission-discipline",
  "workbook_url": "https://visualizedata.ucop.edu/t/Public/views/Freshmanadmissionbydiscipline/Bybroaddiscipline",
  "retrieved": "2026-09-21",
  "note": "Hand-transcribed from the live public dashboard (no CSV export available for the by-discipline breakdown; only the campus-level summary sheet exports as CSV). 'Broad discipline' categories are UC's own groupings, not individual majors — Computer Science here is UC's 'Computer Science' broad-discipline bucket, distinct from 'Engineering' (which includes ECE, ME, etc. and, per UCOP's own grouping, Berkeley's College of Chemistry). Figures are for first-time freshman (not transfer) admission. Campus abbreviations: " + ", ".join(f"{k}={v}" for k,v in CAMPUS_NAMES.items()),
  "campus_names": CAMPUS_NAMES,
  "computer_science": to_rows(CS),
  "engineering": to_rows(ENG),
  "campus_overall_2025": {c: dict(zip(FIELDS,v)) for c,v in CAMPUS_OVERALL_2025.items()},
}
json.dump(out, open("uc_by_discipline.json","w"), indent=1)
print("wrote uc_by_discipline.json")
