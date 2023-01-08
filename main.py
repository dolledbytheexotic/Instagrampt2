import json
with open('pending_follow_requests.json') as file:
    not_following_yet_= json.load(file)
not_following=[]
for notfollowing in not_following_yet_["relationships_follow_requests_sent"]:
    not_following.append(notfollowing["string_list_data"][0]["value"])
if notfollowing in not_following_yet_["relationships_follow_requests_sent"]:
 not_following.remove(notfollowing["string_list_data"][0]["value"]) 

for user in not_following:
  print(user)