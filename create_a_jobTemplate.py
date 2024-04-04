import re

newObjectje = JobTemplate.objects.create(description= 'Hele goede template', name= 'De beste template', organization_id = 1, diff_mode = False, timeout = 0, survey_enabled=False, playbook='hello_world.yml', project_id=6,  inventory_id= 1, created_by_id= 1)

newIdeetje = re.search("^.*-(.*)$", str(newObjectje))

print(str(newIdeetje.group(1)))
# print(str(newIdeetje.groups()))
print(str(newObjectje))
