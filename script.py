import json
import requests
import subprocess
start_k = 2
finish_k = 1180
for k in range(start_k, finish_k):
	req = 'https://api.github.com/search/repositories?q=+language:kotlin&page=%d' % k
	print(req)
	response = requests.get(req)
	json_file = response.json()
	#number = json_file["total_count"]
	start = 0
	finish = 30
	print(len(json_file["items"]))
	for i in range(start, finish):
		arr = json_file["items"][i]
		id = arr["id"]
		full_name = arr["full_name"]
		name = arr["name"]
		str = "curl -L https://api.github.com/repos/%s/zipball > %s_%s.zip" % (full_name, name, id)

		print(str)
		p = subprocess.Popen(str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		print(out)
		print(err)

		print("Done!")
		print("=====")

