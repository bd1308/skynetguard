#! /usr/bin/env python
file = open('skynetfilter','r')
domains = file.readlines()
file.close()

def sort_domains(s):
    return list(s.split('.')[-1])
domains_sorted = sorted(domains, key=sort_domains)
print(domains_sorted)

output = open('tmp_skynetallow', 'w+')
for line in domains_sorted:
    output.write(f"@@||{line.strip()}^$client=skynet,important\n")

output.write("#Default block\n")
output.write("||*.*^$client=skynet\n")
output.close()
