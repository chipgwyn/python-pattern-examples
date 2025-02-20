Simple example of using jinja2 templates

Uses the values in a CSV file, 'values.csv' and outputs a file based on the template 'config.tmpl'.
The template is rendered into a file based on the values from the csv file and placed into the 'output/' dir.

```
#> ./generate.py
#> cat output/core1.cfg 
!
hostname core1
!
interface Loopback0
 ipv4 address 10.0.0.1/32
 ipv6 address  2001:db8::1/128
!
interface Ethernet0
 description UNUSED
 switchport mode trunk
 switchport trunk allow vlan 42-90
!
interface Ethernet1
 description UNUSED
 switchport mode trunk
 switchport trunk allow vlan 42-90
!
interface Ethernet2
 description UNUSED
 switchport mode trunk
 switchport trunk allow vlan 42-90
!
end

```