import re

m = re.match(r".*[\.](\w+|√|×)",'173.关于货币真伪鉴定，以下说法正确的是_________.ABCD')
print (m.group(1))