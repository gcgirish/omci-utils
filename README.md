# omci-utils
This project is a collection of utilities for decoding omci messages

## Decoding "Received frame VLAN tagging operation table"
To decode "Received frame VLAN tagging operation table", use the below utility. 
```shell
python3.7 decode_vlan_tag_oper_table.py
```
You will be prompted to input a hex stream of "Received frame VLAN tagging operation table". Enter a valid hex stream.
An example stream is "f800000080000000400f000000080384".
