import re

newObjectje = Organization.objects.create(description= 'SDZ', name= 'SDZ', created_by_id= 1)
newIdeetje = re.search("^.*-(.*)$", str(newObjectje))

print(str(newIdeetje.group(1)))
# print(str(newIdeetje.groups()))
print(str(newObjectje))
