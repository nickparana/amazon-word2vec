from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import Helpers
import AmazonGetSingleProduct

asin_title_dict = Helpers.load_json_dict('data/Preprocessed/asin_title_dict/asin_title_dict.json')
model = Word2Vec.load('static/data/word2vec.model')

def get_top_n(item_to_search, top_n=5):
    return list(
        asin_title_dict[key] for key in list(tuple[0] for tuple in model.wv.most_similar(item_to_search, topn=top_n)))


def get_top_n_full(item_to_search, top_n=5):
    return list(
        AmazonGetSingleProduct.get_by_asin(key) for key in list(tuple[0] for tuple in model.wv.most_similar(item_to_search, topn=top_n)))


def plot():
    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    # create a scatter plot of the projection
    plt.scatter(result[:, 0], result[:, 1])
    words = list(model.wv.vocab)
    for i, word in enumerate(words):
        try:
            plt.annotate(asin_title_dict[word], xy=(result[i, 0], result[i, 1]))
        except:
            print('bad word')
    plt.show()
