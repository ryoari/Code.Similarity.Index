import requests

# Azure AD and application details
tenant_id = "a7e41f11-d518-46f0-bfa6-2a2be08eda1d"
client_id = "9b5320e7-7c0b-464f-9178-553d223d1389"
client_secret = "e1k8Q~sBpypPwLAKggB-NZcUHbHAAVP2Clnh4aKk"

# OAuth 2.0 token endpoint
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# Define the scope of the API permissions (using Microsoft Graph)
scope = "https://graph.microsoft.com/.default"

# Create the data payload for the token request
payload = {
    'client_id': client_id,
    'scope': scope,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Make the POST request to get the access token
response = requests.post(token_url, data=payload)

# Check if the request was successful
if response.status_code == 200:
    token_response = response.json()
    access_token = token_response.get('access_token')
    print("Access Token:", access_token)
else:
    print(f"Failed to obtain token: {response.status_code}")
    print(response.text)

# Use the access token to call Microsoft Graph API
# Example: List files in a specific SharePoint site (which is linked to Teams)

# Replace 'site-id' with the actual SharePoint site ID linked to the Teams channel
site_id = "your-sharepoint-site-id"
drive_id = "your-drive-id"

# Graph API endpoint to list files
graph_url = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root/children"

# Set the authorization headers
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make the API call to list files
files_response = requests.get(graph_url, headers=headers)

# Check if the API call was successful
if files_response.status_code == 200:
    files = files_response.json()
    print("Files in SharePoint/Teams:")
    for file in files['value']:
        print(file['name'])
else:
    print(f"Failed to retrieve files: {files_response.status_code}")
    print(files_response.text)