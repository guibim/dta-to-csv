import os
import pandas as pd

# Path to the Downloads folder on Windows
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# File names
input_filename = "xxxxx.dta"
output_filename = "xxxxx.csv"

# Full paths
input_path = os.path.join(downloads, input_filename)
output_path = os.path.join(downloads, output_filename)

print(f"Reading file: {input_path}")

# Read .dta file
df = pd.read_stata(input_path)

# Convert to CSV
df.to_csv(output_path, index=False)

print("✔ Conversion completed!")
print(f"CSV created at: {output_path}")
