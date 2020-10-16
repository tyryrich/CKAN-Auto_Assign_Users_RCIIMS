from ckanapi import RemoteCKAN

### Set Authentication Information ### 

CKAN_URL = '' #e.g. https://demo.ckan.org/
CKAN_APIKEY = '' #e.g. '294813e2-2690-4967-9dd3-313c26e27f93'

### Remote Connect to CKAN ###

ckan = RemoteCKAN(address=CKAN_URL, apikey=CKAN_APIKEY)

### Get list of organizations ###

rciims_org_list = []
rciims_orgs = ckan.action.organization_list(all_fields=True, limit=100000)

for org in rciims_orgs:
  rciims_org_list.append(org['name'])

### Get list of RCIIMS users ###

rciims_user_id_list = []
rciims_users = ckan.action.user_list()

for user in rciims_users:
  rciims_user_id_list.append(user['id'])

### Get list of members for each organization ###

org_list_w_members = []

for org in rciims_org_list:
  org_list_w_members.append({'name': org, 'members':ckan.action.member_list(id='rciims', object_type='user')}) 

### Add users not in rciims org to org ###

for org in org_list_w_members:
  members_in_org_list = []

  if org['name'] == 'rciims':
    for member in org['members']:
      members_in_org_list.append(member[0])

    for user in rciims_user_id_list:
      if user not in members_in_org_list:
        ckan.action.organization_member_create(id=org['name'], username=user, role='member')

### Get list of groups ###

rciims_group_list = []
rciims_groups = ckan.action.group_list(all_fields=True, limit=100000)

for group in rciims_groups:
  rciims_group_list.append(group['name'])

### Get list of members for each group ###

group_list_w_members = []

for group in rciims_group_list:
  group_list_w_members.append({'name': group, 'members':ckan.action.member_list(id=group, object_type='user')}) 

### Add users not in groups to groups ###

for group in group_list_w_members:
  members_in_group_list = []

  for member in group['members']:
    members_in_group_list.append(member[0])

  for user in rciims_user_id_list:
    if user not in members_in_group_list:
      ckan.action.group_member_create(id=group['name'], username=user, role='member')
