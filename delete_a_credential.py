# import sys

# delId=sys.argv[1]
# newInstantietje = Credential.objects.get(id=17)


delId=REPLACEME
newInstantietje = Credential.objects.get(id=delId)
print(newInstantietje.delete())
