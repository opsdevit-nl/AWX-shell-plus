
## create_a_jobTemplate
sudo /usr/local/bin/kubectl --kubeconfig=/etc/rancher/k3s/k3s.yaml -n awx exec -it awx-web-56ddf8bff9-dx9gj -- awx-manage shell_plus --quiet-load -c "$(sudo cat roles/awx_credential_dump/files/create_a_jobTemplate.py)"

## create_a_team
sudo /usr/local/bin/kubectl --kubeconfig=/etc/rancher/k3s/k3s.yaml -n awx exec -it awx-web-56ddf8bff9-dx9gj -- awx-manage shell_plus --quiet-load -c "$(sudo cat roles/awx_credential_dump/files/create_a_team.py)"

## create_an_organization
sudo /usr/local/bin/kubectl --kubeconfig=/etc/rancher/k3s/k3s.yaml -n awx exec -it awx-web-56ddf8bff9-dx9gj -- awx-manage shell_plus --quiet-load -c "$(sudo cat roles/awx_credential_dump/files/create_an_organization.py)"

## get_all_creds (secrets unencrypted)
sudo /usr/local/bin/kubectl --kubeconfig=/etc/rancher/k3s/k3s.yaml -n awx exec -it awx-web-56ddf8bff9-dx9gj -- awx-manage shell_plus --quiet-load -c "$(sudo cat roles/awx_credential_dump/files/get_all_creds.py)"

## list_all_creds (secrets encrypted)
sudo /usr/local/bin/kubectl --kubeconfig=/etc/rancher/k3s/k3s.yaml -n awx exec -it awx-web-56ddf8bff9-dx9gj -- awx-manage shell_plus --quiet-load -c "$(sudo cat roles/awx_credential_dump/files/list_all_creds.py)"

## create_a_credential
sudo /usr/local/bin/kubectl --kubeconfig=/etc/rancher/k3s/k3s.yaml -n awx exec -it awx-web-56ddf8bff9-dx9gj -- awx-manage shell_plus --quiet-load -c "$(sudo cat roles/awx_credential_dump/files/create_a_credential.py)"

## delete_a_credential (id 4)
sudo /usr/local/bin/kubectl --kubeconfig=/etc/rancher/k3s/k3s.yaml -n awx exec -it awx-web-56ddf8bff9-dx9gj -- awx-manage shell_plus --quiet-load -c "$(echo "$(sudo cat roles/awx_credential_dump/files/delete_a_credential.py) " | sed 's/REPLACEME/4/g')"
