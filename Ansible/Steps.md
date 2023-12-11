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
