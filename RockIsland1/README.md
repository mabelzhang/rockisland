# Issues

- Postal codes are randomly selected in select\_postcodes.py, which currently
  writes to a csv file.
  But Anylogic takes Excel file as input.
  Would need third party library to write to Excel file from Python.

- AnyLogic Database does not automatically refresh when the postcodes input
  file is changed.
  User needs to click on Database > New > Database table, to reload the same
  file, in order for it to update. That is not sustainable for changing the
  randomly selected list of postcodes outside AnyLogic.
  Unclear if it is possible to randomly select a list from the database table
  of 800+ postcodes, inside AnyLogic, and then populate the agent using the
  selected list.
  Currently, this is all done through GUI, and it's unclear how to change
  the agent setup programmatically. Perhaps you can through these
  [functions](https://anylogic.help/anylogic/gis/agents-placement.html#agent-location-api).


# Sources

[1] List of postcodes in Orkney
https://www.doogal.co.uk/AdministrativeAreas?district=S12000023

