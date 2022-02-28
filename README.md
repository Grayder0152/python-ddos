# python-ddos
*beta version* 	

Program for DDOS-attacks on Russian propaganda sites.

## Installation
### Windows
#### [Install Docker on your PC](https://docs.docker.com/engine/install/)
#### Pull docker image locally:
```
 docker pull grayder/python-ddos:ddos
```
#### Launch the container:
```
 docker run --rm grayder/python-ddos:ddos
```
##### By default, the script runs in 200 streams and with logging enabled.
##### If you want to change the number of threads or disable logging, run the following command:
#
#
```
 docker run --rm grayder/python-ddos:ddos -t 1000 -wl
```
##### -t N - the program will run in N streams;
##### -wl - the program will work without logging;

#
#
#
#### use your own site list
 
```
 docker run --rm -v <full file path>:/app/site_for_attack.txt grayder/python-ddos:ddos
```

### Pure python approach
```
 git clone https://github.com/Grayder0152/python-ddos.git
```
```
 pip install -r requirements.txt
```
```
  python3 main.py
```