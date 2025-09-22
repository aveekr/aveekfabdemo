# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
from synapse.ml.mlflow import get_mlflow_env_config
from trident_token_library_wrapper import PyTridentTokenLibrary

mlflow_env_configs = get_mlflow_env_config()
mwc_token = PyTridentTokenLibrary.get_mwc_token(mlflow_env_configs.workspace_id, mlflow_env_configs.artifact_id, 2)

auth_headers = {
    "Authorization" : "MwcToken {}".format(mwc_token)
}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests

def print_chat_result(messages, response_code, response):
    print("==========================================================================================")
    print("| OpenAI Input    |")
    for msg in messages:
        if msg["role"] == "system":
            print("[System] ", msg["content"])
        elif msg["role"] == "user":
            print("Q: ", msg["content"])
        else:
            print("A: ", msg["content"])
    print("------------------------------------------------------------------------------------------")
    print("| Response Status |", response_code)
    print("------------------------------------------------------------------------------------------")
    print("| OpenAI Output   |")
    if response.status_code == 200:
        print(response.json()["choices"][0]["message"]["content"])
    else:
        print(response.content)
    print("==========================================================================================")


deployment_name = "gpt-4o" # deployment_id could be one of {gpt-4o or gpt-4o-mini}
openai_url = mlflow_env_configs.workload_endpoint + f"cognitive/openai/openai/deployments/{deployment_name}/chat/completions?api-version=2025-04-01-preview"
payload = {
    "messages": [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"}
    ]
}

response = requests.post(openai_url, headers=auth_headers, json=payload)
print_chat_result(payload["messages"], response.status_code, response)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
