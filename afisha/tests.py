from django.test import TestCase
import urllib
import requests

imgUrl = "https://sxodim.com/uploads/posts/2022/04/01/optimized/365accf67f76599663f7ae61f0f33339_352x198-q-85.jpg"



print(imgUrl[imgUrl.find(":") + 50:])
# p = requests.get(imgUrl)
# out = open("static\img\img1.jpg", "wb")
# out.write(p.content)
# out.close()




