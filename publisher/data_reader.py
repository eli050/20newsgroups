from sklearn.datasets import fetch_20newsgroups


class DataReader:
    """Reads data from 20 Newsgroups dataset and provides batches
     of interesting and not interesting categories."""
    interesting_categories = [
        'alt.atheism',
        'comp.graphics',
        'comp.os.ms-windows.misc',
        'comp.sys.ibm.pc.hardware',
        'comp.sys.mac.hardware',
        'comp.windows.x',
        'misc.forsale',
        'rec.autos',
        'rec.motorcycles',
        'rec.sport.baseball',
    ]
    not_interesting_categories = [
        'rec.sport.hockey',
        'sci.crypt',
        'sci.electronics',
        'sci.med',
        'sci.space',
        'soc.religion.christian',
        'talk.politics.guns',
        'talk.politics.mideast',
        'talk.politics.misc',
        'talk.religion.misc',
    ]
    def __init__(self):
        """Initializes the DataReader by loading the dataset."""
        self.newsgroups_interesting = fetch_20newsgroups(subset='all',
                                categories=DataReader.interesting_categories)
        self.newsgroups_not_interesting = fetch_20newsgroups(subset='all',
                                categories=DataReader.not_interesting_categories)

    def read_interesting_data(self):
        """Reads a batch of interesting data."""
        return next(self._batch_generator(self.newsgroups_interesting.data))

    def read_not_interesting_data(self):
        """Reads a batch of not interesting data."""
        return next(self._batch_generator(self.newsgroups_not_interesting.data))

    @staticmethod
    def _batch_generator(data, batch_size=20):
        """Yields batches of data."""
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]

