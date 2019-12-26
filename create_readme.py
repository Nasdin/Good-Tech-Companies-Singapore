__author__ = ['[Nasrudin Salim](http://nasrudinsalim.com)']
__date__ = '2019.12.26'

"""
Generates the README for
[nasdin/Good-Tech-Companies-Singapore](https://github.com/Nasdin/Good-Tech-Companies-Singapore)
Parses the config.yaml to recreate the README each time.
The README consists of a dynamically generated table that consists of data we can get from GlassDoor or PayScale.
Which is input into config.yaml, then this create_readme.py is run to generate a new README.md
"""

import yaml
import datetime
from generate import make_table_headers, parse_row_data, row_data_to_row_markdown

today = datetime.datetime.today().strftime('%d %b %Y')

README_PATH = "README.md"
CONFIG_PATH = 'config.yaml'

intro = f'''
# Good-tier Tech companies in Singapore
### Updated: {today}
This project uses a [config.yaml](config.yaml) and a python [script](generate.py) to \
automatically [regenerate](create_readme.py) this [README](README.md) file.

### To contribute:
1. Fork repository
2. Edit [config.yaml](config.yaml)
3. Run [create_readme.py](create_readme.py), which will generate new README.md
4. Open a pull request!


#### Definitions
1. __Flexible hours__

>Choose own work hours, flexible entry and exit times or the ability to take time whenever during a workday
for personal appointments without consuming leaves. Or to work at home on any moment's notice
2. __Mid-level__
    
>Someone who is in their mid to late 20s. Past the junior phase and has 2-4 years experience.
But 5 years and above can command a much higher salary; they would have "senior" or "lead" in their titles.

3. __Striked through__

>This company has fallen below certain standards and is in the grey area of a good tier tech company

4. __Very good pantry__

> Generally means a never ending flowing pantry, topped up DAILY with premium ice cream of any kind, drinks, bars, 
magnum ice-cream, free flow alcohol. Milo, coconut water etc. Non-junk snacks, Good would be similar but slightly lower. 
Use your imagination to figure out the other ranges.


'''

with open(CONFIG_PATH) as f:
    data = yaml.load(f)
    columns_mapping = data.pop('COLUMNS')

table_headers = make_table_headers(columns_mapping.values())

company_rows = [row_data_to_row_markdown(*parse_row_data(
    key=company, data=company_data, columns_mapping=columns_mapping)
                                         ) for company, company_data in data.items()]

# Structure of readme is more readable when its created via a list
readme_content = '\n'.join([intro,
                            "## List of companies",
                            f"Data updated at {today}",
                            '\n',
                            table_headers,
                            *company_rows,
                            f'\nCoded by: {"&".join(__author__)}'])

with open(README_PATH, 'w') as f:
    f.write(readme_content)
