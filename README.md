**WHAT THIS REPO IS ALL ABOUT**
===================================================
Recently I had set myself for an interview process with a renowned software company for ```Dev Ops Engineer``` position. After several steps I ***was not*** able to make to the employment. However, I had learnt a great deal of thing while preparing myself and appeared for the interviews.
.
.

There was a ```code test``` step involved. Though I was (*and am*) a **PHP** guy - for the company practice and ease of ``Dev Ops`` work I had to deal with ```Python```. I was eagerly learning python and dealt with it a bit previously. The test helped me a lot in the process of learning.
.
.

In this repo I tried to include the problem set and my answers -- for the sake of future events and for the sake of improving my learning. I understand that **there exists** a great deal of **bad codes** / **bad practices**. But I will try to improve them gradually.
.
.

### ***The Problem:***

 1. ####**FIRST**: 
    Building a command line program with Python that downloads files over the network and store them on the local file system. The program will receive two inputs:

     **a.** The URL of an RSS Feed containing links to the files to be downloaded.
     
     **b.** The path to the directory where the downloaded files are going to be stored.
     
     **c.** ***Requirements***:
     - The program has to remember if a file has been downloaded previously. So if the file has been downloaded once, it skips downloading it again.
         
     - If a file has been downloaded partially, it can resume from the point where it left off.
     - The program should be able to log its activities in a text file.
     
     - The program should support both HTTP and FTP.
     
     - The program should be designed in a way so that it can be easily extended to support additional protocols
     - Bonus points if your program is capable of downloading multiple files in parallel.

    **d.** ***Sample***: 
    
     ```python downloader.py --feed=<RSS-Feed-URL> --output=<PATH-TO-DIRECTORY>```
     
 2. ####**SECOND**: 
     - Write a ``python`` script using ***boto*** that will spin up and configure a new EC2 instance on AWS. Your script should do the following tasks:
        - Create a security group called: `code-test-access`
 With the following configuration:
    ```
    Enable TCP 22 only for 222.111.77.88
    Enable TCP 80 for rest of the world
    Restrict access to all other TCP/UDP port
    ```
     - Provision an ``EC2`` instance. And use the following default parameters. Remember to accept command line parameters for them as well.
         - **AMI**: ``ami-0b9c9f62``
         - **Instance type**: ``m1.large``
         - Use a dummy AWS access-key value, secret-access-key value and key file name in your code.
         - After provisioning print the instance ID and it’s public DNS address and status.
         - Set the following tags on that instance:
        ```
        name code-test-01
        env    dev
        role   code-test-instance
        ```
         - **Bonus point:** 
            - If the script can take value for number of instances to launch and also take value for multiple availability zone name (e.g. *us-east-1b, us-east-1c*) to launch instances on those availability zones.

            - (*assume specified number of availability zone is even*) If number of instances specified to launch is equal then place them equally on multiple availability zones. And if number of instances is odd then the first availability-zone specified in the list should get priority for the extra instance.


 2. ####**THIRD**:  
    A nginx configuration like the following:
    ```
    user www-data;
    worker_processes 8;
    pid /var/run/nginx.pid;

    events {
        worker_connections 4096;
        multi_accept on;
    }

    http {
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 30;
        types_hash_max_size 2048;
        ….
        …
        ….
    }
    ```
    **Expected** - around 200 requests/second with this configuration with a system of 4 CPU core and 8 Gb of memory.
    
    **i.** What is wrong in this configuration?
    
    *ii.** What optimization is required to handle the specified amount of traffic?
    
    **iii.** Are there any external system settings needs to be tuned to achieve this? Specify exact solutions?
    
.   
.

### ***The Solution:***

####**Solution 1**:
Solution 1 is scripted at file ``downloader.py``. There are lots of validation check issues which were not implemented but which were actually required.

.
####**Solution 2**:
Solution 2 is scripted at file ``ec2provisioning.py`` and ``securitygroup.py``. There are lots of validation check issues which were not implemented but which were actually required.

.
####**Solution 3**:
Solution 3 is provided in the ``third-solution.md`` file. The file is kind of self explanatory but still there are lots of comments in all the files.
