
import os

# Define the folder structure
folders = ['data/raw', 'data/processed', 'data/staging', 'config', 'scripts']

# Create the folders if they don't exist
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        
# Create empty files in each folder
raw_file = open("data/raw/raw_data.txt", "w")
raw_file.close()

processed_file = open("data/processed/processed_data.txt", "w")
processed_file.close()

staging_file = open("data/staging/staging_data.txt", "w")
staging_file.close()

config_file = open("config/config.yaml", "w")
config_file.close()

script_file = open("scripts/script.py", "w")
script_file.close()
