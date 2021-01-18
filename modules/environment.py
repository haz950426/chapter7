import os

#返回所有环境变量
def run(**args):
    print "[*] In environment module."
    return str(os.environ)