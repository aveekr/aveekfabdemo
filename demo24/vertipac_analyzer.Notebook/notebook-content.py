# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "dde69492-6b2e-46d8-ae00-5317e55ca6ee",
# META       "default_lakehouse_name": "test1234",
# META       "default_lakehouse_workspace_id": "eebc13dd-b560-4280-aeb3-c6d342982b7e",
# META       "known_lakehouses": [
# META         {
# META           "id": "dde69492-6b2e-46d8-ae00-5317e55ca6ee"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

%pip install semantic-link-labs

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import sempy_labs as labs

dataset = 'customer360' # Enter the name or ID of your semantic model
workspace = None # Enter the name or ID of the workspace in which the semantic model resides

x = labs.vertipaq_analyzer(dataset=dataset, workspace=workspace)
x = labs.vertipaq_analyzer(dataset=dataset, workspace=workspace, export='table') # Setting export='table' will export the results to delta tables in the lakehouse attached to the notebook
x = labs.vertipaq_analyzer(dataset=dataset, workspace=workspace, export='zip') # Setting export='zip' will export the results to a .zip file in the lakehouse attached to the notebook.

# Note that this function returns a dictionary of dataframes which is captured above as the parameter 'x'. You can view this as such:
for name, df in x.items():
    print(name)
    display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
