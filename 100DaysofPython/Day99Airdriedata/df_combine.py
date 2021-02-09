import pandas as pd

# Load dataframes
orig_df = pd.read_csv(
    '/Users/smith/python/100DaysofPython/Day99Airdriedata/Residential_Title_Transfers.csv')
aug_df = pd.read_csv(
    '/Users/smith/python/100DaysofPython/Day99Airdriedata/airdrie_props.csv')
geo_df = pd.read_csv(
    '/Users/smith/python/100DaysofPython/Day99Airdriedata/airdrie_props_geocode.csv')

# Augment original with scraped data using tax roll
new_df = pd.DataFrame.copy(orig_df)
new_df = pd.merge(left=new_df, right=aug_df, on='Tax Roll', how='inner')

# Augment with lat & lon using address
new_df = pd.merge(left=new_df, right=geo_df,
                  left_on='Property Address_x', right_on='Property Address', how='inner')
new_df.to_csv(
    '/Users/smith/python/100DaysofPython/Day99Airdriedata/airdrie_data.csv')
