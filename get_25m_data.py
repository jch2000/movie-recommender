import requests
import zipfile
import os

url = 'https://files.grouplens.org/datasets/movielens/ml-25m.zip'
zip_fname = './ml-25m.zip'

# Downloading zip file from url
req = requests.get(url)
print('Zip Downloaded')

# Writing file to local file system
with open(zip_fname, 'wb') as output_file:
    output_file.write(req.content)

# Writing file to local file system to folder
with zipfile.ZipFile(zip_fname, 'r') as zipped:
    zipped.extractall('./')
print('Data Unzipped')

# Removing zip file
os.unlink(zip_fname)
