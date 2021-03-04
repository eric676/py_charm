import requests

url = "https://www.jzlwbao.cn/lwbaoproSvcTest/gwn/s/materialRequirment/save?token=b87cca0d-ce9e-4d28-aed0-d4abaabe4412"

payload="{\r\n\"companyId\": \"B1605491388778\",\r\n\"materialType\": \"MATERIEL\",\r\n\"name\": \"测试823\",\r\n\"projectId\": \"PJ1607419954654\",\r\n\"supplierQualificationList\": []\r\n\r\n\r\n\r\n\r\n\r\n}"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
