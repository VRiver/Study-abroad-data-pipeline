from study_kit.scraper import extract_program_cards


def test_extract_program_cards_returns_structured_fields():
    html = '<div class="program-card"><h2 class="title">Data Science MSc</h2><span class="country">UK</span></div>'
    assert extract_program_cards(html) == [{"program": "Data Science MSc", "country": "UK"}]
