import seasons
    """
    The code contains test functions for the age_in_words and main functions in the seasons module,
    including tests for valid and invalid input.
    """


def test_age_in_words():
    assert seasons.age_in_words(0) == '0 minutes'
    assert seasons.age_in_words(1) == '1 minute'
    assert seasons.age_in_words(2) == '2 minutes'
    assert seasons.age_in_words(60) == '1 hour'
    assert seasons.age_in_words(120) == '2 hours'
    assert seasons.age_in_words(1440) == '1 day'
    assert seasons.age_in_words(2880) == '2 days'
    assert seasons.age_in_words(525600) == '1 year'
    assert seasons.age_in_words(1051200) == '2 years'
    assert seasons.age_in_words(525948) == '1 year 1 minute'
    assert seasons.age_in_words(526063) == '1 year 2 minutes'
    assert seasons.age_in_words(525960) == '1 year 1 day'
    assert seasons.age_in_words(527040) == '1 year 2 days'
    assert seasons.age_in_words(536040) == '1 year 1 day 1 hour'


def test_main(monkeypatch):
    user_input = '2000-01-01'
    expected_output = '21 years 109 days'
    monkeypatch.setattr('builtins.input', lambda x: user_input)
    monkeypatch.setattr('builtins.print', lambda x: expected_output)

    seasons.main()


def test_main_invalid_input(monkeypatch, capsys):
    user_input = 'invalid'
    monkeypatch.setattr('builtins.input', lambda x: user_input)

    seasons.main()

    captured = capsys.readouterr()
    assert "Invalid date format. Please enter a date in YYYY-MM-DD format." in captured.out
