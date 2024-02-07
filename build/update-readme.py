import pandas as pd

# read csv content into a pandas dataframe
df = pd.read_csv('data/archaeology-machine-learning-data.csv')

# sort the dataframe entries by year from highest to lowest value
df_sorted = df.sort_values(by='year', ascending=False)

# split the dataframe by application area
dfs_split = {group: group_df for group, group_df in df_sorted.groupby('application area')}

# create a dictionary to map an emoji to each application area
emoji_mapping = {
    'remote sensing': '🛰️',
    'site distribution modelling': '🌏',
    'new area': '📊',
    # add more areas
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
start_marker = '<!-- START DATA -->'
end_marker = '<!-- END DATA -->'
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
