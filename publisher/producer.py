
class Producer:
    pass


from sklearn.datasets import fetch_20newsgroups
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
newsgroups_interesting = fetch_20newsgroups(subset='all', categories=interesting_categories)
newsgroups_not_interesting = fetch_20newsgroups(subset='all', categories=not_interesting_categories)
def get_batches(data, batch_size=20):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
def batch_generator(data, batch_size=20):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]
gen_1 = batch_generator(newsgroups_interesting.data, 20)
gen_2 = batch_generator(newsgroups_not_interesting.data, 20)
print(next(gen_1))
print(next(gen_2))