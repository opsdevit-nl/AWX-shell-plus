import re

newObjectje = Team.objects.create(description= 'Batsukama', name= 'Batsukama', organization_id= 2)
newIdeetje = re.search("^.*-(.*)$", str(newObjectje))

print(str(newIdeetje.group(1)))
# print(str(newIdeetje.groups()))
print(str(newObjectje))
