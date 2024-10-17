#! /usr/bin/env python
file = open('skynetfilter','r')
domains = file.readlines()
file.close()

file2 = open('skynetredirects','r')
redirects = file2.readlines()
file.close()

def sort_domains(s):
    return list(s.split('.')[-1])
domains_sorted = sorted(domains, key=sort_domains)
print(domains_sorted)

output = open('tmp_skynetallow', 'w+')
for line in domains_sorted:
    if '#' not in line:
        output.write(f"@@||{line.strip()}^$client=skynet,important\n")

for line in redirects:
    if '#' not in line:
        output.write(f"@@||{line.split(',')[0]}^$dnsrewrite=NOERROR;CNAME;{line.split(',')[1]},client=skynet,important\n")

output.write("#Default block\n")
output.write("||*.*^$client=skynet\n")
output.close()
