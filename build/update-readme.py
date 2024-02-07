import pandas as pd

# Read the updated CSV file
df = pd.read_csv('data/archaeology-machine-learning-data.csv')

# Select the columns you want to display in the README as a table
selected_columns = df[['title', 'authors', 'year', 'data type', 'technique', 'paper', 'code', 'data']]

# Convert the selected columns to Markdown format
markdown_table = selected_columns.to_markdown(index=False)

# Read the content of the README file
with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

# Find the start and end markers in the README content
start_marker = '<!-- START_TABLE -->'
end_marker = '<!-- END_TABLE -->'
start_index = readme_content.find(start_marker)
end_index = readme_content.find(end_marker)

if start_index != -1 and end_index != -1:
    # Update the README content with the Markdown table
    updated_readme = readme_content[:start_index + len(start_marker) + 1] + '\n' + markdown_table + '\n' + readme_content[end_index:]
    
    # Write the updated content back to the README file
    with open('README.md', 'w') as readme_file:
        readme_file.write(updated_readme)
else:
    print('markers not found in README.md file')
