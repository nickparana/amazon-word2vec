import pandas as pd
import Helpers

reviews_electronics_df = Helpers.get_df('data/Datasets/reviews_Electronics_5.json.gz')[['reviewerID', 'asin', 'overall']]

is_higher_3 = reviews_electronics_df['overall'] >= 3
good_reviews_electronics_df = reviews_electronics_df[is_higher_3]

meta_electronics_df = Helpers.get_df('data/Datasets/meta_Electronics.json.gz')[['asin', 'title', 'categories', 'related']]
joined_meta_reviews = pd.merge(good_reviews_electronics_df, meta_electronics_df, on='asin', how='outer')

# Remove Rows with any NaN and Save to CSV
joined_meta_reviews.dropna().to_csv('data/Datasets/merged_meta_electronics_reviews.csv')
