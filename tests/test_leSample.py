from leab import before


def test_get_size_per_variation_absolute():
    ab_test = before.leSample(conversion_rate=20, min_detectable_effect=2)
    assert ab_test.get_size_per_variation() == 6347


def test_get_size_per_variation_relative():
    ab_test = before.leSample(
        conversion_rate=20, min_detectable_effect=2, absolute=False
    )
    assert ab_test.get_size_per_variation() == 157328


def test_get_total_size_absolute():
    ab_test = before.leSample(conversion_rate=20, min_detectable_effect=2)
    assert ab_test.get_total_size() == 12694


def test_get_total_size_relative():
    ab_test = before.leSample(
        conversion_rate=20, min_detectable_effect=2, absolute=False
    )
    assert ab_test.get_total_size() == 314656


def test_get_duration_absolute():
    ab_test = before.leSample(conversion_rate=20, min_detectable_effect=2)
    assert ab_test.get_duration(avg_daily_total_visitor=1000) == 13


def test_get_duration_relative():
    ab_test = before.leSample(
        conversion_rate=20, min_detectable_effect=2, absolute=False
    )
    assert ab_test.get_duration(avg_daily_total_visitor=1000) == 315
