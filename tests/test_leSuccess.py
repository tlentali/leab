from leab import after
from leab import leDataset


def test_get_confidence_interval():
    data = leDataset.SampleLeSuccess()
    ab_test = after.leSuccess(data.A, data.B, confidence_level=0.95)
    assert ab_test.sample_A.confidence_interval == [
        8.526343659939133,
        22.13718821096384,
    ]


def test_get_p_value():
    data = leDataset.SampleLeSuccess()
    ab_test = after.leSuccess(data.A, data.B, confidence_level=0.95)
    assert ab_test.p_value == 0.25870176105718934


def test_get_verdict():
    data = leDataset.SampleLeSuccess()
    ab_test = after.leSuccess(data.A, data.B, confidence_level=0.95)
    assert ab_test.get_verdict() == "No significant difference"
