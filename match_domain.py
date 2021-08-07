# _*_ coding: utf-8 _*_
# @Author   : ArmandHe
# @Time     : 2021/8/4 11:21
# @Project  : match_domain
# @File     : match_domain.py
# @SoftWare : PyCharm

from os import system
from os import listdir
import requests

for filename in listdir("../chengdu"):
    system(f"python3 subdomain_find.py < ../chengdu/{filename} > ../chengdure/{filename}.txt")

