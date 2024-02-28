_D='Unauthorized'
_C='127.0.0.1'
_B='GET'
_A=True
from flask import Flask,make_response,request,session
from msal import ConfidentialClientApplication

import webbrowser
import logging
CLIENT_SECRET = "IuJ8Q~PwSVCBsRAXpn~sDjetTm8SxV3fwIyrSc.u"
APPLICATION_ID = "de229405-a5c5-4dbc-b936-d82b0273ab05"
TENTANT_ID = "40127cd4-45f3-49a3-b05d-315a43a9f033"
SCOPES = ["https://graph.microsoft.com/.default"]
REDIRECT_URI = "http://localhost:5000/auth" 
user_id = "a27474eb-cc96-4f8f-bde3-2bf62abbbdb8" 
authority = f"https://login.microsoftonline.com/{TENTANT_ID}"

folder_id2="01SDQWOVNOPUYRLHFA4JBYAGE7WIYNXUUO"
onedrive_target_user_id2="a27474eb-cc96-4f8f-bde3-2bf62abbbdb8" #20200199
local_folder_path= r'C:/Users/Admin/Desktop/Itern-task/demo/upload'

msal_app=ConfidentialClientApplication(
    client_id=APPLICATION_ID,
    client_credential=CLIENT_SECRET,
    authority=authority,
)
def init_msal_app():A=ConfidentialClientApplication(
            APPLICATION_ID,
            authority=authority,
            client_credential=CLIENT_SECRET);return A
def get_auth_code_flow(app):
    A=app.initiate_auth_code_flow(scopes=SCOPES,redirect_uri=REDIRECT_URI);
    B=A['auth_uri'];return A,B
def get_auth_response(auth_url):webbrowser.open(auth_url)
def get_token(app,auth_code_flow,auth_response):
    A=app.acquire_token_by_auth_code_flow(auth_code_flow=auth_code_flow,auth_response=auth_response,scopes=SCOPES);B=A['access_token'];return B

confidential_client_app=init_msal_app()
auth_code_flow,auth_url=get_auth_code_flow(confidential_client_app)
app=Flask(__name__)
app.secret_key=CLIENT_SECRET
auth_response=get_auth_response(auth_url)
@app.route('/auth',methods=[_B])
def auth():
        D='msgraph_access_token';C='Authorization code not found';B='msgraph_auth_response'
        if request.remote_addr!=_C:return _D,401
        session.clear();
        if request.args.get('code')is not None:A=request.args;session[B]=A
        else:logging.error(C);return make_response(({'error':'auth_error','error_description':C},400))
        A=session.get(B);E=get_token(confidential_client_app,auth_code_flow,A);session[D]=E;
        return make_response(({'auth_response':session.get(B),'access_token':session.get(D)},200))




