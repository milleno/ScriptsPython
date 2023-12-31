import boto3
client = boto3.client('iam',aws_access_key_id="X",aws_secret_access_key="X",aws_session_token="X")
users = client.list_users()
user_list = []
for key in users['Users']:
    result = {}
    Policies = []
    Groups=[]

    result['userName']=key['UserName']
    List_of_Policies =  client.list_attached_user_policies(UserName=key['UserName'])
    #client.list_user_policies - lista polices inline

    result['Policies'] = List_of_Policies['AttachedPolicies']

    List_of_Groups =  client.list_groups_for_user(UserName=key['UserName'])

    for Group in List_of_Groups['Groups']:
        Groups.append(Group['GroupName'])
    result['Groups'] = Groups

    List_of_MFA_Devices = client.list_mfa_devices(UserName=key['UserName'])

    if not len(List_of_MFA_Devices['MFADevices']):
        result['isMFADeviceConfigured']=False   
    else:
        result['isMFADeviceConfigured']=True    
    user_list.append(result)

for key in user_list:
    print (key)