import pandas as pd

from study_kit.cleaning import clean_programs


def test_clean_programs_standardizes_fields_and_extracts_ielts():
    raw = pd.DataFrame([
        {
            "school": "University A",
            "country": "USA",
            "degree": "Master's",
            "ielts_text": "IELTS 6.5 overall",
            "tuition_text": "$42,000 per year",
        },
        {
            "school": "University A",
            "country": "United States",
            "degree": "Master",
            "ielts_text": None,
            "tuition_text": "USD 42000/year",
        },
    ])

    cleaned = clean_programs(raw)

    assert cleaned.loc[0, "country"] == "United States"
    assert cleaned.loc[0, "degree"] == "Master"
    assert cleaned.loc[0, "ielts_min"] == 6.5
    assert cleaned.loc[0, "tuition_usd"] == 42000
    assert len(cleaned) == 1
