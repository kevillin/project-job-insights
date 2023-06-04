from counter import count_ocurrences


def test_counter():
    result = count_ocurrences("data/jobs.csv", "python")
    assert result == verifica_ocurrencias("data/jobs.csv", "python")

    result2 = count_ocurrences("data/jobs.csv", "javascript")
    assert result2 == 122


print(verifica_ocurrencias("data/jobs.csv", "python"))
