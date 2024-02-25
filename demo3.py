import os
import requests

APP_ID='1949707f-cb4e-4f86-8a3d-acf977b3330d'
SCOPES =['Files.ReadWrite']
GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'

msgrapg_access_token="eyJ0eXAiOiJKV1QiLCJub25jZSI6IjRCNU5YeVJ3QW51Umlzd2V5S1pvck5lRy1ncnR4UW9hUWNjbXcxUzgya3ciLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80MDEyN2NkNC00NWYzLTQ5YTMtYjA1ZC0zMTVhNDNhOWYwMzMvIiwiaWF0IjoxNzA4Nzk0NjE3LCJuYmYiOjE3MDg3OTQ2MTcsImV4cCI6MTcwODg4MTMxNywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQU45YWY2TjMvVGJBYjBab3VodE91N3F4N1BJeUd2SkdxRVV4OU1KVGpkQlBtVU5VVUV1bllsQWtETldHbVJZeHhHQkZRMFRQc1EwZ2tIZEFpcW1KQUpJdzJVN0lCK09aN2JBYjJWUXhldm5JPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNzk4ZTFiYjctMTFhYy00NTU5LWI1ZmMtZWVhMTNmZWFkMzRiIiwiZmFtaWx5X25hbWUiOiJOR1VZ4buETiBUUlVORyIsImdpdmVuX25hbWUiOiJISeG6vlUiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyNDA1OjQ4MDI6YjUzMjo0N2Q2OmU1NTY6YWY2YjoxOGM2OmE0NmYiLCJuYW1lIjoiTkdVWeG7hE4gVFJVTkcgSEnhur5VIiwib2lkIjoiYTI3NDc0ZWItY2M5Ni00ZjhmLWJkZTMtMmJmNjJhYmJiZGI4IiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAwRUQwNDIyN0QiLCJyaCI6IjAuQVZRQTFId1NRUE5GbzBtd1hURmFRNm53TXdNQUFBQUFBQUFBd0FBQUFBQUFBQUJVQUZnLiIsInNjcCI6IkZpbGVzLlJlYWQgRmlsZXMuUmVhZFdyaXRlIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IjRmR0lBa3hvX2ZyMjR4N0xnYkFDUXFZUk55MkpZOHZhT2pZZHdUX2t3VkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI0MDEyN2NkNC00NWYzLTQ5YTMtYjA1ZC0zMTVhNDNhOWYwMzMiLCJ1bmlxdWVfbmFtZSI6IjIwMjAwMTk5QHN0dWRlbnQuaGNtdXMuZWR1LnZuIiwidXBuIjoiMjAyMDAxOTlAc3R1ZGVudC5oY211cy5lZHUudm4iLCJ1dGkiOiJtWmhZMkJTVXpVNlNuWWJrUWFZaEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJQYXhIeloyMVVWVkJRQjNWQ2RpS0tzVUNsZ2tmV3F4eHZabUNFR0ZTOEg0In0sInhtc190Y2R0IjoxMzcyMTg2NzcwfQ.sBxpZ8OYXzFhlLhqKv0A5hW_Hq1FgWPBDc-1HB4IdOMzmJtGbl20AR5yVTUS6LJL2Ttr9_45jd4F-lhc7VkATy00xU0prwmG_v8t8luU0UyFB4kZPJ7Nu1Bqf-KiMtKqPJCjYqMhTgqqtQ8m-nn7p3oysMlgXPNZxphzhpMz8oOpENiTJG6fmWRJ6YoxMqeQcQWLn8bWpvFlPZlDcKMzNwkJyQoWh4IE5rENPkz2qac9SRSy4He4lR19fqY2It3YQXYaA5gxHi9JDKLRlyxkqF8noWLC76VuOrh9GjTuw8fBYjKc5qoEQU_KvT5_6rvoyjhq1yn0a7FUoFeumQsHUQ"
# onedrive_target_user_id = "fee2b48b-f942-40a7-9e8a-54d78dbd8397" #MediaMod 
folder_id="01SDQWOVNOPUYRLHFA4JBYAGE7WIYNXUUO" #Thi Anh Dep in 20200199 account
onedrive_target_user_id="a27474eb-cc96-4f8f-bde3-2bf62abbbdb8" #20200199

local_folder_path=r'C:/Users/Admin/Desktop/Itern-task/demo/upload'
def list_subfolders(path):
    subfolders = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            full_path = os.path.join(root, dir)
            relative_path = full_path.replace("\\", "/")
            subfolders.append(relative_path)
    return subfolders

def list_files_in_folder(path):
    return [os.path.join(path, f).replace("\\", "/") for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# def list_files_in_folder(path):
#     return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
def handle_create_child_folder(access_token,sub_folder_path):
    sub_folder_name=os.path.basename(sub_folder_path)
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"application/json",
    }
    request_body={
        "name": f"{sub_folder_name}",
        "folder": {},
    }
    response=requests.post(
        # f"{GRAPH_API_ENDPOINT}/user/{onedrive_target_user_id}/drive/items/{folder_id}/children",
        f"{GRAPH_API_ENDPOINT}/me/drive/items/{folder_id}/children",
        headers=headers,
        json=request_body,
    )
    
def get_folder_id(access_token,index):
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"application/json",
    }
    ONEDRIVE_API_ENDPOINT=f"{GRAPH_API_ENDPOINT}/me/drive/items/{folder_id}/children"
    response=requests.get(
        ONEDRIVE_API_ENDPOINT,
        headers=headers
    )
    if response ==201:
        return response.json()['value'][index]['id']
    print(f"{response.json()['value'][index]['id']}")
    

def handle_upload_file(file_path,access_token,child_folder_id):

    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"text/plain",
    }
    # path=f"{local_sub_folder}"
    path=rf"{file_path}"
    file_name=os.path.basename(file_path)
    with open(path,"rb") as upload:
        media_content=upload.read()
    response=requests.put(
        # f"{GRAPH_API_ENDPOINT}/user/{onedrive_target_user_id}/drive/items/{child_folder_id}:/{file_name}:/content",
        f"{GRAPH_API_ENDPOINT}/me/drive/items/{child_folder_id}:/{file_name}/content",
        headers=headers,
        data=media_content,
    )
    
sub_folder=list_subfolders(local_folder_path)

for index,folder in enumerate(sub_folder):
    handle_create_child_folder(msgrapg_access_token,folder)
    child_folder_id=get_folder_id(msgrapg_access_token,index)
    
    print(folder)
    
    files = list_files_in_folder(folder)
    for file in files:
        print(file)
        handle_upload_file(file,msgrapg_access_token,child_folder_id)

# print(f"{os.path.basename(path)}")
# headers={
#     "Authorization": f"Bearer {msgrapg_access_token}",
#     "Content-Type":"text/plain",
# }
# path="C:/Users/Admin/Desktop/Itern-task/demo/upload/234-GMD-htn/test2.txt"
# file_name=os.path.basename("C:/Users/Admin/Desktop/Itern-task/demo/upload/234-GMD-htn/test2.txt")
# with open(r"C:/Users/Admin/Desktop/Itern-task/demo/upload/234-GMD-htn/test2.txt","rb") as upload: #C:/Users/Admin/Desktop/Itern-task/demo/upload/234-GMD-htn/test2.txt
#         media_content=upload.read()
# response=requests.put(
# # f"{GRAPH_API_ENDPOINT}/user/{onedrive_target_user_id}/drive/items/{child_folder_id}:/{file_name}:/content",
# f"{GRAPH_API_ENDPOINT}/me/drive/items/{child_folder_id}:/{file_name}/content",
# headers=headers,
# data=media_content,
# )