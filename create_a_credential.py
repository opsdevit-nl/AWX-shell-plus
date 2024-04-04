import re

newObjectje = Credential.objects.create(description= 'Veiligerste', name= 'veiligerste', credential_type_id= 1, organization_id= 2, **{ 'inputs': {'password': 'Heel$GoedP@@ssword3', 'username': 'test', 'become_method': '', 'become_username': ''}} )
newIdeetje = re.search("^.*-(.*)$", str(newObjectje))

print(str(newIdeetje.group(1)))
# print(str(newIdeetje.groups()))
print(str(newObjectje))