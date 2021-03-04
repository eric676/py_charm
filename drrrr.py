import requests

url = "https://www.jzlwbao.cn/lwbaoproSvcTest//gwn/s/workFlow/search?sort=createTime-&token=b87cca0d-ce9e-4d28-aed0-d4abaabe4412"

payload="{\"projectId\": \"PJ1607419954654\",\r\n\"status\": \"?SUBMIT|CONFIRM\",\r\n\"type\": \"BUSINESS_CONTRACT\"}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
