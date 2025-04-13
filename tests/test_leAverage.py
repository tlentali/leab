from leab import after
from leab import leDataset


def test_get_size_absolute():
    data = leDataset.SampleLeAverage()
    ab_test = after.leAverage(data.A, data.B)
    assert ab_test.sample_A.confidence_interval == [
        34.75214007684581,
        81.59785992315418,
    ]


def test_get_size_absolute():
    data = leDataset.SampleLeAverage()
    ab_test = after.leAverage(data.A, data.B)
    assert ab_test.get_verdict() == "Sample A mean is greater"
