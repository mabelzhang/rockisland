#!/usr/bin/env python3

import csv
import random

pc_path = 'inputs/OrkneyPostcodes.csv'
sel_path = 'inputs/OrkneyPostcodesRandomlySelected.csv'

num_pcs = 0
num_sel = 50

fieldnames = []

# Read postcodes file first pass, to see how many there are
with open(pc_path) as pc_file:
  pc_reader = csv.DictReader(pc_file)

  # Read header row
  fieldnames = pc_reader.fieldnames

  for row in pc_reader:
    num_pcs += 1

print(f'Number of postcodes: {num_pcs:d}')

# Sanity check. Number of items selected cannot be greater than total number of
# items
if num_sel > num_pcs:
  num_sel = num_pcs

# Randomly select a subset of rows
sel_rows = random.sample(range(num_pcs), k=num_sel)
# Sort to descending order
sel_rows.sort()
print(f'Randomly selected {num_sel:d} rows')
#print(sel_rows)

# Open output file to write to
# TODO: This currently writes to csv file. AnyLogic takes Excel file as input.
# Would need third party library to write to Excel file from Python.
sel_file = open(sel_path, 'w', newline='')
sel_writer = csv.DictWriter(sel_file, fieldnames)
sel_writer.writeheader()
sel_i = 0

# Reset for second read
num_pcs = 0

# Open file again, to save the selected rows
with open(pc_path) as pc_file:
  pc_reader = csv.DictReader(pc_file)

  for row in pc_reader:
    # If this row is the next selected row
    if num_pcs == sel_rows[sel_i]:
      sel_writer.writerow(row)
      sel_i += 1

      # Done indexing sel_rows
      if sel_i >= len(sel_rows):
        break

    num_pcs += 1

sel_file.close()

print(f'Randomly selected rows written to file {sel_path:s}')

