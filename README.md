{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww30040\viewh17760\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # convert-tahaz\
\
This repo contains scripts to parse CS2  demo files into CSVs. Contains some helper functions to reduce file size by tick.\
\
---\
\
## Files\
\
- **main_parse.py**  \
  Main script which includes the functions calls and where the whole script is run from. Has instructions on how to save files and data frame names for parsing.\
\
- **demo_parser.py**  \
  Contains the parsing function which actually reads .dem files and converts them to dataframes and csvs\
\
- **helpful_demo_functions.py**  \
  Contains one helper function, `filter_by_tick`, which lets you reduce the size of the css dataframes by keeping only every nth tick. Any additional helpful functions will be added here. \
\
---\
\
## Usage\
\
Run the main script from the terminal with this command:\
\
```bash\
python3 main_parse.py \\\
  --demos_folder path/to/demos \\\
  --output_folder path/to/save/csvs \\\
  --dataframe_typelist path/to/dataframes.txt \\\
  --df_to_filter_name grenades \\\
  --num_tick_saved 8 \\\
  --verbose\
```}