# COMP90024_Ass2
This project presents all the works have been doen for the University of Melbourne COMP90024 team03.

# Team mumber:
    Wei Ge - 1074198
    Han Wang - 1041260 
    YanBei Jiang - 1087029
    Yiwen Zhang - 1002781
    Zening Zhang - 1078374

# Ansible-playbook:
1. - Make sure you have at least 4 instances available and at least 400GB disk space on MRC 
2. - Replace the file “unimelb-COMP90024-2022-grp-3-openrc.sh” with your own MRC configuration file by downloading it on the MRC homepage
3. - Modify the ansible configuration file at ./ansible/host_vars/nectar.yaml 
    This file contains all the configuration information about setting up the system. There are a few configuration parameters that MUST be modified.
4. - Generate your own MRC private key as shown below and save it to your own computer, change the field ssh_private_key_path to your own private key path
5. - ou might change the volume mount or number of instances created if you have a larger capacity.
6. - Run the following command
    ```sudo ./launch_instance.sh```
    ```sudo ./install_dependency.sh```
    ```sudo ./deploy.sh```
# directory structure
```
  /ansible
  /backend
  /crawler
  /data_analysis
  /frontend
  /map_reduce
```

# Videos
- https://youtu.be/dki5nmgq5hg