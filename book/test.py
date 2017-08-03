import re

m = re.search(r"(\w{1,6}|√|×)\Z",'173.关于货币真伪鉴定，以下说法正确的是_________.ABCD')
print (m.group())