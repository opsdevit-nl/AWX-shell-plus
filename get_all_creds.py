from awx.main.utils import decrypt_field
import yaml

def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)

decrypted = []

for cred in Credential.objects.all():
    newcred = {'name': cred.name, 'kind': cred.kind, 'inputs': {}}
    for field in cred.inputs.keys():
        newcred['inputs'][field] = decrypt_field(cred, field)
    decrypted.append(newcred)


print(yaml.dump({'credentials': decrypted}))
