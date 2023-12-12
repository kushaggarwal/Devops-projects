## Steps to apply Ansible project

1. Create the ssh key file in .ssh location for ansible to remotely access the hosts

   ```
   cd ~/.ssh
   vi anisble_keys
   ```

2. Add the private key file contents downloaded from the aws console

3. Go to the root directory by running `cd` command

4. Create the ansible folder and add the ansible.cfg and hosts file inside it (refer the files in the same folder and change the server IP address with respect to the instances launched by you on the console)

   ```
   mkdir ansible
   cd ansible
   touch ansible.cfg hosts
   ```

5. Check connectivity to the instance by running `ansible servers -m ping`

6. Create the ansible playbooks for nginx, git and creation of file to apply them on the adjoining servers mentioned in the hosts file ( Please find the ansible playbook in the Playbooks folder present in the same directory)

7. Apply the ansible playbooks over the hosts by running the below command

   ` ansible-playbook -i hosts git.yml -u ec2_user`

   You can replace the name of the playbook as per the one you created, please find the reference below for the attributes in the command

   host => the hosts file having the list of our public IP address
   git.yml => name of the ansible playbook we wish to apply
   -u ec2-user => the user on which or using which we want to apply our configuration

   NOTE: If you are using the nginx playbook make sure to create the index.html in the ansible folder for ansible to copy it to the remote server

#### Helpful links

- Anisble modules - https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html
- Ansible official documentation - https://docs.ansible.com/
