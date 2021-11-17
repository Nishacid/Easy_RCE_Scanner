# Easy RCE Scanner

Script for the automation of your Pentest or Bug Bounty recon.
It will help you find sensitive open ports, which usually leads to an `easy RCE` . 

## Sensible Ports

- IBM WebSphere : 8880
- Apache Hadoop : 8088
- Apache Spark : 6066
- Apache Solr : 8983
- Redis : 6379
- Docker : 2375, 2376
- Zoho Manageengine Desktop : 8383
- Atlassian Crowd : 4990
- Portainer : 9000
- Hashicorp Consul : 8500
- Java RMI : 1090,1098,1099,4444,11099,47001,47002,10999
- WebLogic : 7000-7004, 8000-8003, 9000-9003,9503,7070,7071
- JDWP : 45000,45001
- JMX : 8686,9012,50500
- GlassFish: 4848
- jBoss: 11111,4444,4445
- Ciso Smart Install : 4786
- HP Data Protector : 5555,5556

## Installation 

```bash
git clone https://github.com/Nishacid/Easy_RCE_Scanner.git
cd  Easy_RCE_Scanner/
pip3 install -r requirements.txt
```

## Usage

```bash
usage: main.py [-h] -ip Targeted IP
```

## Exemple 

```
╰─➤  python3 main.py -ip 192.168.13.37
[+] Port 8983 open on 192.168.13.37
[*] More information about the exploit for Apache Solr
[*] CVE-2019-17558
[*] CVE-2019-0193
[*] CVE-2019-12409
Scanning completed in : 1 seconds 425 miliseconds.
```
