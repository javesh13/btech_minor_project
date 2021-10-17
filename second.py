import third as dm
import binascii
client = {}
ip = {}
port = {}


def process_client(c, i, p):
	data = "a"
	while len(data) > 0:
		data = c.recv(2048)
		datas = data.decode()
		datas = datas.split("28")
		datas = datas[1:]
		for i in range(len(datas)):
			datas[i] = "28" + datas[i]
		for item in datas:
			dm.process_data(c, item)
