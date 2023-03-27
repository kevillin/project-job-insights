from src.pre_built.counter import count_ocurrences


def test_counter():
    result = count_ocurrences("data/jobs.csv", "python")
    assert result == 1639

    result2 = count_ocurrences("data/jobs.csv", "javascript")
    assert result2 == 122
