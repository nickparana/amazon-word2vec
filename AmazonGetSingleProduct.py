import Helpers


full_metadata_df = Helpers.get_df('data/Datasets/meta_Electronics.json.gz')


def get_by_asin(asin: str):
    product = full_metadata_df.loc[full_metadata_df['asin'] == asin][
        ['asin', 'title', 'categories', 'brand', 'price', 'imUrl', 'description']]
    return product.to_json(orient='records')
