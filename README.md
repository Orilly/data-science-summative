This repository is for our data science group summative assessment, investigating the question ***What economic indicators best predict happiness globally?***

The repo contains the following:
- **main.ipynb** - notebook containing our main report (alongside data analysis code)
- **dashboard.py** - file for pyshiny dashboard - a secondary application, interactive dashboard displaying linear regression data + data visualisation for the economic indicators discussed in our report
- **requirements.txt** - includes required modules
- **data/** - main data folder, containing datasets downloaded from theglobaleconomy.com
- **old_data/** - folder including original data downloaded for the project
- **old_cleaning.ipynb** - original data cleaning notebook

To run the code for this project:
- download github repo and run 'pip install -r requirements.txt'
- open main.ipynb in a jupyter environment and run all cells
- to launch pyshiny dashboard, run 'shiny run --reload --launch-browser dashboard.py'

Student ID numbers of group members:
- 24000103464
- 24000112264
- 24000102504
