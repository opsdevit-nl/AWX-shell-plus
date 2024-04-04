from pprint import pprint

for credential in Credential.objects.all():
    print(credential)

for credential in Credential.objects.values():
    pprint(credential)