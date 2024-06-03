import pandas as pd

# this script is trigged by changes to the data csv file
# it sorts and updates the data csv file and updates the data displayed in the README file

# read data csv into a pandas dataframe
df = pd.read_csv('data/archaeology-machine-learning-data.csv')

# sort the dataframe entries by application area and year (most recent first)
df_sorted = df.sort_values(by=['application area', 'year'], ascending=[True, False])

# write the sorted dataframe back to the data csv file
with open('data/archaeology-machine-learning-data.csv', 'w') as file:
    file.write(df_sorted.to_csv(index=False))

# identify dataframe rows containing the word 'dataset'
contains_dataset = df_sorted['task'].str.contains('dataset', case=False, na=False)

# split the datasets from the main dataframe
df_without_dataset = df[~contains_dataset]
df_with_dataset = df[contains_dataset]

# create a dictionary which contains the main dataframe data, split by application area
dfs_split = {group: group_df for group, group_df in df_without_dataset.groupby('application area')}

# add the datasets dataframe to the dfs_split dictionary
dfs_split['datasets'] = df_with_dataset

# keep only the dataframe columns needed for the README
for key, df in dfs_split.items():
    dfs_split[key] = df.drop(columns=['application area'])

# create a dictionary to map an emoji to each application area
emoji_mapping = {
    'artefact analysis': '🏺',
    'datasets': '📊',
    'ecofact analysis': '🌱',
    'natural language processing': '📚️',
    'remote sensing feature detection': '🛰️',
    'spatial predictive modelling': '🌏'
    # insert new areas in the list in alphabetical order
}

# save each application area dataframe into pretty_data dictionary
pretty_data = {}
for area, area_df in dfs_split.items():
    emoji = emoji_mapping.get(area, '')
    title = f'## {emoji} {area}\n\n'
    markdown_table = area_df.to_markdown(index=False) + '\n\n'
    pretty_data[area] = title + markdown_table

# read the content of the README file
with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

# find the start and end markers in the README content
start_marker = '<!-- START -->'
end_marker = '<!-- END -->'
start_index = readme_content.find(start_marker)
end_index = readme_content.find(end_marker)

# write pretty_data into the README.md file between the start and end markers
if start_index != -1 and end_index != -1:
    updated_readme = readme_content[:start_index + len(start_marker)] + '\n\n'
    for area, data in pretty_data.items():
        updated_readme += data
    updated_readme += readme_content[end_index:]

# write the updated content back to the README file
    with open('README.md', 'w') as readme_file:
        readme_file.write(updated_readme)
else:
    print('markers not found in README.md')