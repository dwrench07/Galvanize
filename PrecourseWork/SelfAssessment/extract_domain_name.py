import re


def domain_name(url):
    pattern = re.compile(r'([\/\/^w][-\w]?)')
    domain = re.search(pattern, url)
    print(domain)
    return domain[1]

assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"
