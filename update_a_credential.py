# import sys

# delId=sys.argv[1]
# newInstantietje = Credential.objects.get(id=17)


# updateId=REPLACEME

updateId=26
# updateInstantietje = Credential.objects.filter(id=updateId).update(name="veiligersterrrst", **{ 'inputs': {'password': 'Supernieuwpw12'}})
updateInstantietje = Credential.objects.filter(id=updateId).update(name="veiligersterrrst", **{ 'inputs': {'password': 'SupernieuwPWnogbeter21', 'username': 'test', 'become_method': '', 'become_username': ''}})
print(updateInstantietje)