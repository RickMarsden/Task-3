import re

# Open the input and output files
with open('onelinefile.txt', 'r') as infile, open('Filename2.csv', 'w') as outfile:
  # Read the contents of the input file
  contents = infile.read()
  
  # Split the contents into individual records using a regular expression
  records = re.split(r'(\d+[A-Za-z]*\d*\.\d*[A-Za-z]*)', contents)
  
  # Iterate over the records
  for record in records:
    # Split each record into fields using a regular expression
    fields = re.split(r'(\d+)\s*([A-Za-z]*)\s*(\d*\.\d*)\s*([A-Za-z]*)', record)
    
    # Write the fields to the output file, separated by commas
    outfile.write(','.join(fields) + '\n')
    