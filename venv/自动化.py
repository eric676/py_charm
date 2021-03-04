import requests

res = requests.post(

'https://www.jzlwbao.cn/lwbaoproSvcDev//gwn/s/workFlow/search?sort=createTime-&token=b87cca0d-ce9e-4d28-aed0-d4abaabe4412'

)
if res.status_code == 200:
    print('status_code测试通过')
else:
    print('status_code测试不通过')
