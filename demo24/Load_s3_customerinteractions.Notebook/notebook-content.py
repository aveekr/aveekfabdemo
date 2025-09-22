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

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/customerdata/customerinteractionsdemo/customerInteractions (2).csv")
# df now is a Spark DataFrame containing CSV data from "Files/customerdata/customerinteractionsdemo/customerInteractions.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# ATTENTION: AI-generated code can include errors or operations you didn't intend. Review the code in this cell carefully before running it.

# Assuming 'df' is your PySpark dataframe and you want to save it into a Delta table

# Delta table path
delta_table_path = "customer.customerinteractions"

# Write the dataframe to the Delta table
df.write.format("delta").mode("overwrite").saveAsTable(delta_table_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
