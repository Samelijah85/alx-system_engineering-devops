# Installing MySQL 5.7 and MySQL 8.0 on Ubuntu 18.04, 20.04, or Later
## Installing MySQL 5.7 on Ubuntu 20.04 LTS
#### Step 1: Add MySQL 5.7 APT Repository
1. Download the MySQL repository package:
``` bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
```
2. Install the MySQL repository package:
``` bash
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
```
3. Select Ubuntu Bionic, then MySQL Server & Cluster, followed by mysql-5.7, and confirm.
4. Update the APT repository:
``` bash
sudo apt update
```
If encountering a signature verification error, import the missing GPG key:

``` bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
```
(Replace this "467B942D3A79BD29" with your recv keys that will be display alongside with the error message)

5. Update APT again:
``` bash
sudo apt update
```

#### Step 2: Install MySQL 5.7
1. Install MySQL 5.7 using the following command:
``` bash
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
```
2. Proceed with installation and set the root password when prompted.

#### Step 3: Secure your MySQL root user account
Run the security installation command:
``` bash
sudo mysql_secure_installation
```

#### Step 4: Check MySQL version
Log in to MySQL and execute:
``` bash
mysql -u root -p
SELECT VERSION();
```

#### Step 5: Add MySQL user and set privileges
Create a MySQL user account and grant privileges.

#### Step 6: Test MySQL 5.7
Verify MySQL service status:
``` bash
sudo systemctl status mysql
```

## Installing MySQL 8.0 on Ubuntu 20.04 LTS

#### Step 1: Download and Install MySQL 8.0 APT Repository
1. Download the MySQL 8.0 repository package:
``` bash
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
```
2. Install the repository package:
``` bash
sudo dpkg -i mysql-apt-config_0.8.15-1_all.deb
```
3. Select options as prompted to configure the repository.

#### Step 2: Install MySQL 8.0
1. Install MySQL 8.0:
``` bash
sudo apt install -f mysql-client=8.0* mysql-community-server=8.0* mysql-server=8.0*
```
2. Set the root password during installation.

#### Step 3: Check MySQL version
Check the installed MySQL version:
``` bash
mysql –V
mysqladmin -u root -p version
```

#### Step 4: Create a MySQL user
Create a new MySQL user account.

