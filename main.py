import json

with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

with open('synced_contacts.json') as file:
    synced_contacts_json = json.load(file) 

contacts_whofollow_back=[]
for following in following_json["relationships_following"]:
  contacts_whofollow_back.append(following["string_list_data"][0]["value"])

for followers in followers_json["relationships_followers"]:
    if followers["string_list_data"][0]["value"] in contacts_whofollow_back:
        contacts_whofollow_back.remove(followers["string_list_data"][0]["value"])


for synced in synced_contacts_json["contacts_contact_info"]:
  if synced["media_map_data"][0]["value"] in contacts_whofollow_back:
    contacts_whofollow_back.append(synced["string_list_data"][0]["value"])

for user in contacts_whofollow_back:
  print(user)
