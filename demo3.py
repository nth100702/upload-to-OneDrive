import os
from apscheduler.schedulers.blocking import BlockingScheduler
import requests

GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'

msgrapg_access_token2 ="eyJ0eXAiOiJKV1QiLCJub25jZSI6ImU2ci10Y2J4SWtBZW5YeUpYSm9ZcHdMeW1VSDBsR21JOEYyOWY3WXNJNFUiLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80MDEyN2NkNC00NWYzLTQ5YTMtYjA1ZC0zMTVhNDNhOWYwMzMvIiwiaWF0IjoxNzA5MDgzMjg4LCJuYmYiOjE3MDkwODMyODgsImV4cCI6MTcwOTE2OTk4OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQW1VVWNLWkNNR3NvREZYeDF3WmZYSFl0cXZKUUhrSTBBd1Qya3Q3TmZiaUd3MGJYRUhNS0hSSmxqVU4rNEdnSW1RejNtNzR2NS9BZHlOdmxBcjgreWRtd1Y3eDRtSFk4TFJMTHE4RHNDbGxjPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNzk4ZTFiYjctMTFhYy00NTU5LWI1ZmMtZWVhMTNmZWFkMzRiIiwiZmFtaWx5X25hbWUiOiJOR1VZ4buETiBUUlVORyIsImdpdmVuX25hbWUiOiJISeG6vlUiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMTMuMTYxLjExOS4yMzQiLCJuYW1lIjoiTkdVWeG7hE4gVFJVTkcgSEnhur5VIiwib2lkIjoiYTI3NDc0ZWItY2M5Ni00ZjhmLWJkZTMtMmJmNjJhYmJiZGI4IiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAwRUQwNDIyN0QiLCJyaCI6IjAuQVZRQTFId1NRUE5GbzBtd1hURmFRNm53TXdNQUFBQUFBQUFBd0FBQUFBQUFBQUJVQUZnLiIsInNjcCI6IkZpbGVzLlJlYWQgRmlsZXMuUmVhZFdyaXRlIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IjRmR0lBa3hvX2ZyMjR4N0xnYkFDUXFZUk55MkpZOHZhT2pZZHdUX2t3VkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI0MDEyN2NkNC00NWYzLTQ5YTMtYjA1ZC0zMTVhNDNhOWYwMzMiLCJ1bmlxdWVfbmFtZSI6IjIwMjAwMTk5QHN0dWRlbnQuaGNtdXMuZWR1LnZuIiwidXBuIjoiMjAyMDAxOTlAc3R1ZGVudC5oY211cy5lZHUudm4iLCJ1dGkiOiJRc3hXMlJSaDkwV05tS1pmeFd2TEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJQYXhIeloyMVVWVkJRQjNWQ2RpS0tzVUNsZ2tmV3F4eHZabUNFR0ZTOEg0In0sInhtc190Y2R0IjoxMzcyMTg2NzcwfQ.pmQgbiGvzXCMTTGGAvw5Hm7mfWyCrRwsPstEOuLNFYw4OC4XSfTVr5r8vPfzCsH-6CrRSJjlpzDsPOjgONjJFd5bTy4aA3TpsDRqHm0ZYri3IXScpAuc7BmTdNhP96pG8bD4OwLt5c-QBRLKWKTOqg-ic03q7w_I-DLKajom6BywnfeYmejd3Bp_-wVz_ca0lsz-CTyEV285elsexFoL8Ocu1JxNg_Am77gJ997xojlDF3m12hJQ3yfMc9dooRBUyF_eCqkjSXIKsA5_WcABJCtctJaVR2Mo4O0c3ugbwtSSUmCSi8KcI3j58ITscu53ooPe2UZeey-Cc6fZgcwtEA"

folder_id2="01SDQWOVNOPUYRLHFA4JBYAGE7WIYNXUUO"
onedrive_target_user_id2="a27474eb-cc96-4f8f-bde3-2bf62abbbdb8" #20200199
local_folder_path=r'C:/Users/Admin/Desktop/Itern-task/demo/upload'# '/mnt/c/Users/Admin/Desktop/Itern-task/demo/upload'#
count=0
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

def folder_exists(folder_name, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(
        f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{folder_id2}/children",
        headers=headers,
    )
    folders = [item for item in response.json()['value'] if 'folder' in item]
    return any(folder['name'] == folder_name for folder in folders)

def handle_create_child_folder(access_token,sub_folder_path):
    sub_folder_name=os.path.basename(sub_folder_path)
    if not folder_exists(sub_folder_name,access_token):
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type":"application/json",
        }
        request_body={
            "name": f"{sub_folder_name}",
            "folder": {},
        }
        response=requests.post(
            f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{folder_id2}/children",
            headers=headers,
            json=request_body,
        )


def get_folder_id(folder_id,access_token,index):
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"application/json",
    }
    ONEDRIVE_API_ENDPOINT=f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{folder_id}/children"
    response=requests.get(
        ONEDRIVE_API_ENDPOINT,
        headers=headers
    ) 
    if response.status_code==401:
        return print("Unauthorized")
    else:
        print(response.status_code)
        return response.json()['value'][index]['id']

def file_exists(file_name, access_token, folder_id):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(
        f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{folder_id}/children",
        headers=headers,
    )
    files = [item for item in response.json()['value'] if 'file' in item]
    return any(file['name'] == file_name for file in files)

def handle_upload_file(file_path,access_token,child_folder_id):
    file_name = os.path.basename(file_path)
    if not file_exists(file_name, access_token, child_folder_id):
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type":"application/json",
        }

        file_name=os.path.basename(file_path)
        raw_path=os.path.normpath(file_path)
        with open(raw_path,"rb") as upload :
            media_content=upload.read()
        response=requests.put(
            f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{child_folder_id}:/{file_name}:/content",
            headers=headers,
            data=media_content,
        )
  
def handle_upload_large_file(file_size,file_path,access_token,child_folder_id):
    file_name=os.path.basename(file_path)
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"application/json",
    }
    body = {
        "item": {
            "@microsoft.graph.conflictBehavior": "rename",
        }
    }
    response=requests.post(
        f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{child_folder_id}:/{file_name}:/createUploadSession",
        headers=headers,
        json=body,
    )
    try:
        upload_url=response.json()['uploadUrl']
    except Exception as e:
        raise Exception(str(e))
    
    raw_path=os.path.normpath(file_path)
    with open(raw_path, "rb") as f:
        chunk_size = 320 * 1024  # 320 KiB
        for i in range(0, file_size, chunk_size):
            chunk_data = f.read(chunk_size)
            start_index = i
            end_index = min(i + chunk_size, file_size) - 1
            headers2 = {
                "Content-Length": str(chunk_size),
                "Content-Range": f"bytes {start_index}-{end_index}/{file_size}"
            }
            response = requests.put(upload_url, headers=headers2, data=chunk_data)
            print(response.status_code)
            if response.status_code==202 or response.status_code == 201:
                print("everything is alright")
            else :
                print("something went wrong ")

def scheduled_task(path,access_token,folder_id):
    sub_folder=list_subfolders(path)

    for index,folder in enumerate(sub_folder):
        handle_create_child_folder(access_token,folder)
        child_folder_id=get_folder_id(folder_id,access_token,index)
        print(f"Folder: {os.path.basename(folder)}")
        files = list_files_in_folder(folder)
        for i,file in enumerate(files):
            file_size=os.path.getsize(files[i])
            print(f"File: {os.path.basename(file)} / size: {file_size}")
            if file_size < 262144000: # 250 Mb
                handle_upload_file(files[i],access_token,child_folder_id)
            if 262144000 <= file_size < 524288000: # 250 Mb to 500 Mb
                handle_upload_large_file(file_size,files[i],access_token,child_folder_id)

sched = BlockingScheduler()
sched.add_job(scheduled_task, 'interval', hours=1, args=[local_folder_path, msgrapg_access_token2, folder_id2])
sched.start()
