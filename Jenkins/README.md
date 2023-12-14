### Install Jenkins and Java

```
sudo dnf install java-11-amazon-corretto -y
sudo dnf install java-11-amazon-corretto-devel -y
java -version
sudo wget -O /etc/yum.repos.d/jenkins.repo     https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo dnf install jenkins -y
jenkins --version
sudo systemctl start jenkins
sudo systemctl status jenkins
```
