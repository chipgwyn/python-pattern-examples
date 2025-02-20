# Simple macro example

```
pip install jinja2
pip install pyyaml
```

`# python3 render.py`

## output

```
{'interfaces': [{'name': 'eth0', 'ip': '10.22.34.0/24'}, {'name': 'eth1', 'ip': '10.21.34.0/24'}, {'name': 'eth2', 'ip': '10.22.34.0/24'}]}


# Here are our interfaces
!
interface eth0
    ip address 10.22.34.0/24
!
interface eth1
    ip address 10.21.34.0/24
!
interface eth2
    ip address 10.22.34.0/24
!
# and now we're done
```


