# Issues

- Postal codes are randomly selected in select\_postcodes.py, which currently
  writes to a csv file.
  But Anylogic takes Excel file as input.
  Would need third party library to write to Excel file from Python.
  Currently, the csv file is manually converted to .xlsx format, so that
  AnyLogic can import it to a population agent.
  That is not sustainable for an automatic software pipeline that changes
  the randomly selected list of postcodes on demand, as it needs to be changed
  outside AnyLogic.

  Unclear if it is possible to randomly select a list from the database table
  of 800+ postcodes, inside AnyLogic, and then populate the agent using the
  selected list.
  Currently, this is all done through GUI, and it's unclear how to change
  the agent setup programmatically. Perhaps you can through these
  [functions](https://anylogic.help/anylogic/gis/agents-placement.html#agent-location-api).

- Once the python script has been run and the .xlsx made from the .csv,
  you need to manually point the AnyLogic model to the .xlsx file.
  Database -> Create or import a table... -> Import database table(s) -> 
  File: RockIsland - inputs/OrkneyPostCodesRandomlySelected.xlsx
  (select 'Update data on the model startup')

- For AnyLogic Database to automatically refresh when the postcodes input
  .xlsx file is changed, make sure in
  Database > orkney\_postcodes\_randomly\_selected, check "Update data on
  the model startup".

# Sources

[1] List of postcodes in Orkney
https://www.doogal.co.uk/AdministrativeAreas?district=S12000023

