__author__ = ['[Nasrudin Salim](http://nasrudinsalim.com)']
__date__ = '2019.12.24'

"""
Generates the README for
[nasdin/Good-Tech-Companies-Singapore](https://github.com/Nasdin/Good-Tech-Companies-Singapore)
Parses the config.yaml to recreate the README each time.
The README consists of a dynamically generated table that consists of a few dynamic values found off GlassDoor 
or PayScale.
If there is a link provided, it will use those links to scrape the data.
"""

import yaml
import datetime
from generate import make_table_headers

today = datetime.datetime.today().strftime('%d %b %Y')

README_PATH = "README.md"
CONFIG_PATH = 'config.yaml'

intro = f'''
# Good-tier Tech companies in Singapore
### Updated: {today}
This project uses a config.yaml and a python script to automatically regenerate this README file.

### To contribute:
1. Fork repository
2. Edit config.yaml 
3. Run create_readme.py, which will generate new README.md
4. Open a pull request!

'''

with open(CONFIG_PATH) as f:
    data = yaml.load(f)
    columns_mapping = data.pop('COLUMNS')

table_headers = make_table_headers(columns_mapping.values())

# Structure of readme is more readable if its created via a list
readme_content = '\n'.join([intro,
                            "## List of companies",
                            f"Data updated at {today}",
                            '\n',
                            table_headers,
                            '\nCoded by: [Nasrudin Salim](http://nasrudinsalim.com)'])

print(readme_content)

with open(README_PATH, 'w') as f:
    f.write(readme_content)
