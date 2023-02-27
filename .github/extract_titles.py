import re

result_file = 'result.txt'

with open(result_file, 'r') as f:
    lines = f.readlines()

with open(result_file, 'w') as f:
    for line in lines:
        if "200 OK" in line:
            url = re.findall(r"\[\+\] (\S+)", line)[0]
            title = httpx.get(url).html.title
            f.write(f"{url}: {title}\n")
            print(f"Found new vulnerability: {url}: {title}")
