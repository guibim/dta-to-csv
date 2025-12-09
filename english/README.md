# `.dta` to `.csv` File Converter

This project provides a simple Python script to convert Stata (`.dta`) files into `.csv` format, which is widely used for statistical analysis, spreadsheets, and data processing tools.

The script automatically uses the **Windows Downloads folder** as the default input and output location.

---

## Requirements

Install Python and the required libraries:

```bash
pip install pandas pyreadstat
```

##How to Use

Place your .dta file inside the Windows Downloads folder.

Edit the script and replace:

```bash
input_filename = "xxxxx.dta"
output_filename = "xxxxx.csv"
```

Run the script:
#python converter.py

The .csv file will be automatically generated inside the Downloads folder.
