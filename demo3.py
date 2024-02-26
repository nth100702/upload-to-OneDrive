import os
import requests

APP_ID='1949707f-cb4e-4f86-8a3d-acf977b3330d'
SCOPES =['Files.ReadWrite']
GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0'

msgrapg_access_token="eyJ0eXAiOiJKV1QiLCJub25jZSI6InJIUk40cEtYSmdhaThlb09Ia1R6cF96VTlpTG1BYkxYV0NPdWwxc2NVVmsiLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80MDEyN2NkNC00NWYzLTQ5YTMtYjA1ZC0zMTVhNDNhOWYwMzMvIiwiaWF0IjoxNzA4OTA5OTIwLCJuYmYiOjE3MDg5MDk5MjAsImV4cCI6MTcwODk5NjYyMCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQVkzakhJWjVEdFBqVTdOTGhCbnhmUjltVFJLajJxcldDWGxObk02ZXQ2UUZIaVJYU0RqbjQ3eEszQmQvMmh1WWwzZ2pkUjJjcGF0OTFVa2tTQXdEVEpyZElBTWV6dUlFeGQ4N2F6MUlWMDJZPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNzk4ZTFiYjctMTFhYy00NTU5LWI1ZmMtZWVhMTNmZWFkMzRiIiwiZmFtaWx5X25hbWUiOiJOR1VZ4buETiBUUlVORyIsImdpdmVuX25hbWUiOiJISeG6vlUiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMTMuMTYxLjExOS4yMzQiLCJuYW1lIjoiTkdVWeG7hE4gVFJVTkcgSEnhur5VIiwib2lkIjoiYTI3NDc0ZWItY2M5Ni00ZjhmLWJkZTMtMmJmNjJhYmJiZGI4IiwicGxhdGYiOiIzIiwicHVpZCI6IjEwMDMyMDAwRUQwNDIyN0QiLCJyaCI6IjAuQVZRQTFId1NRUE5GbzBtd1hURmFRNm53TXdNQUFBQUFBQUFBd0FBQUFBQUFBQUJVQUZnLiIsInNjcCI6IkZpbGVzLlJlYWQgRmlsZXMuUmVhZFdyaXRlIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IjRmR0lBa3hvX2ZyMjR4N0xnYkFDUXFZUk55MkpZOHZhT2pZZHdUX2t3VkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI0MDEyN2NkNC00NWYzLTQ5YTMtYjA1ZC0zMTVhNDNhOWYwMzMiLCJ1bmlxdWVfbmFtZSI6IjIwMjAwMTk5QHN0dWRlbnQuaGNtdXMuZWR1LnZuIiwidXBuIjoiMjAyMDAxOTlAc3R1ZGVudC5oY211cy5lZHUudm4iLCJ1dGkiOiJ1dnUxd1ZUbU4wQy1NM1ZlQVd3eEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJQYXhIeloyMVVWVkJRQjNWQ2RpS0tzVUNsZ2tmV3F4eHZabUNFR0ZTOEg0In0sInhtc190Y2R0IjoxMzcyMTg2NzcwfQ.goTsPED7RToLJVDTo8GvEVNXrGGCAFR-P-d7rLLxG2O7F_IdyA56kG7S3KDEUpFMAxvPvQC_Wp5o18xE4viHWsrVA5Rk1f1IhHdoUFA5K77QVPWepGe04TvySRJKoECKcQmQh08KAQlKWRX1-Az6LgZ_qK7TGGp-WU44PGV70LCDRACF0CVErGHDook6KxJAYwDqk8X-f4mEaIwK7K_m6RRM6aWe8sAbejQ1Ka-4LdWvd5tBh6mQiT8V3VZieaVwOePZ8WnyVgpbvyFqdzNtTx4JLq39XcAdElnWqe4mkLU5DHK8D3tBp53nzzjegpelKiVYRSAUNPrgpgumx_ZepA"
msgrapg_access_token2 ="EwCQA8l6BAAUs5+HQn0N+h2FxWzLS31ZgQVuHsYAAZZAkmeXVdphJ6cWSBCNnjDII1brKiKQee+KwH3OOaeAlW9SR0OeUvSXbPNMVDw6YUGtepMegKL8Riox0zAjrrawxk9BKEDjWBWgN88LZAXdhp7Sq5dZRjNoBB65rRpieGUQIkAbwSGkHO1HFYmDGV5nSR4O6MIXXO2GmI2UpcvcA7bXKUwd9BBw6MVizChLA2A7ZVyuqW6rNr3BCwNz+tB8broMnR4RJQ/2FklwP/FQ4bGp1YOs2Ip1E0EroZ42L1rDzhc7/J5OIGQ3W4+ySkduqxagqUdbbZEAaIzs79aa1umNCICPSTr/7SelKH0iKnP6+tWz0uhoYDU/fRuT+rsDZgAACDIIz6bMLsmAYAKQBe9Wk7JOKMR4AlYWJSFF6wj0MnXZ7gxDrITvaDbK3cAkdBaOHp7BuGhVRwzuW+Cn+PSxZZJG0UKLaX8jpChjSXYMVcQnqIvYnmteUcVSFhUSmudGN8s2+xtuA8wTqB25cNR3mwZYpz5QDhN83G6RYF2Se/p+hIwEC/WYULx1e40gDDPTtKUjr+cNLGYkuhZLvC9JPCNzyjbZXqvfHNvRVIvsKJ0oEwQLTEYMXz1SVs9hjmemswAxFkqPVgcgo5GmIqKZq18lq8ZS2ODKcSopnxclaPaEpVMpiENjrdpnsR0sCsWXqkueygea0HSiqRd3U7Oc1WMlKVR+8GX2Mx+oMEhKUI6DuOfXj8MZT8iwcL/OgW4tmEosukNuyt1JmWMPrxIKXvOevH2iTbcou/QxHXsgIR0vTQnLTRXf8xPnAfjbSfYriuu3saeax9+R0+TETKZyTNJqOvnc1vlz0/pkTgxpmATVMycLF8m1zwiyNNnTXcQ9V5//THX+VGqW7wxjfogW7TtDMjtul9wHf0eMalQLHjUzhTvk/Rl7RelTb2uTI0DFENLUjta9YHkk8CP3ARXD0RGmuBytLp5Uspeqey6tXo0BKrPKKaMUHeYTms/+vIfS5eAT/RX0DcNg/uMNKiaiqvtMwpEPczz3qLRxbfjkfHmnYwBJI6kwv8FS0BVV4strVx87buZrXLU4Vc3jt7G5N1ZpxFSU+0BAMB/O+XK6bXLZIeNxDHFy2/cEzjdf67JQ7rKcqHAx2QfeugKkFB87UoJoiqns5orEewcO+U28QJCaeq99Q5AkzZ2lS44C"
folder_id="01SDQWOVNOPUYRLHFA4JBYAGE7WIYNXUUO" #Thi Anh Dep in 20200199 account
folder_id2="D7E087F9238E57D0!108"
# onedrive_target_user_id = "fee2b48b-f942-40a7-9e8a-54d78dbd8397" #MediaMod 
onedrive_target_user_id="a27474eb-cc96-4f8f-bde3-2bf62abbbdb8" #20200199
onedrive_target_user_id2="d7e087f9238e57d0"
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
        # f"{GRAPH_API_ENDPOINT}/me/drive/items/{folder_id}/children",
        f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{folder_id2}/children",
        headers=headers,
        json=request_body,
    )
    
def get_folder_id(folder_id,access_token,index):
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"application/json",
    }
    ONEDRIVE_API_ENDPOINT=f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{folder_id}/children"  #f"{GRAPH_API_ENDPOINT}/me/drive/items/{folder_id}/children"
    response=requests.get(
        ONEDRIVE_API_ENDPOINT,
        headers=headers
    )
    return response.json()['value'][index]['id']
    
def handle_upload_file(file_path,access_token,child_folder_id):

    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type":"application/json",
    }

    file_name=os.path.basename(file_path)
    raw_path=os.path.normpath(file_path)
    with open(raw_path,"rb") as upload :
        media_content=upload.read()
    response=requests.put(
        #f"{GRAPH_API_ENDPOINT}/me/drive/items/{child_folder_id}:/{file_name}:/content",
        f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id}/drive/items/{child_folder_id}:/{file_name}:/content",
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
        f"{GRAPH_API_ENDPOINT}/me/drive/items/{child_folder_id}:/{file_name}:/createUploadSession",
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
            elif response.status_code == 409 :
                item_id=get_folder_id(child_folder_id,msgrapg_access_token2,index)

                handle_upload_error(item_id,access_token,upload_url)
            else :
                print("something went wrong dude")

def handle_upload_error(item_id,access_token,upload_url):
    headers1 = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(
        f"https://graph.microsoft.com/v1.0/me/drive/items/{item_id}",
        headers=headers1
    )

    etag = response.json()['value'][index]["eTag"]
    ctag = response.json()['value'][index]["cTag"]
    headers2={
        "Content-Type": "application/json",
        "If-Match": {etag or ctag}
    }
    body ={
        "@microsoft.graph.conflictBehavior": "rename",
        "@microsoft.graph.sourceUrl": f"{upload_url}"
    }
    response2=requests.put(
        f"{GRAPH_API_ENDPOINT}/users/{onedrive_target_user_id2}/drive/items/{item_id}",
        headers=headers2,
        json=body,
    )

sub_folder=list_subfolders(local_folder_path)

for index,folder in enumerate(sub_folder):
    handle_create_child_folder(msgrapg_access_token2,folder)
    child_folder_id=get_folder_id(folder_id2,msgrapg_access_token2,index)
    print(f"Folder: {os.path.basename(folder)}")
    files = list_files_in_folder(folder)
    for i,file in enumerate(files):
        folder_size=os.path.getsize(folder)
        file_size=os.path.getsize(files[i])
        print(f"File: {os.path.basename(file)} / size: {file_size}")
        if folder_size < 262144000 and file_size < 52428800 : # 250 Mb
            handle_upload_file(files[i],msgrapg_access_token2,child_folder_id)
        if 262144000 <= folder_size < 524288000: # 250 Mb to 500 Mb
            if file_size < 52428800 :
                handle_upload_file(files[i],msgrapg_access_token2,child_folder_id)
            else :
                handle_upload_large_file(file_size,files[i],msgrapg_access_token2,child_folder_id)
