# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "aeaa409d-8af6-474a-83db-b0c2403b0a77",
# META       "default_lakehouse_name": "bronze",
# META       "default_lakehouse_workspace_id": "eebc13dd-b560-4280-aeb3-c6d342982b7e",
# META       "known_lakehouses": [
# META         {
# META           "id": "aeaa409d-8af6-474a-83db-b0c2403b0a77"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
df_sale = spark.sql("SELECT * from fact_sale")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
