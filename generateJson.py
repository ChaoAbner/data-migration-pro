import uuid
import json

data = {
    "uid": "",
    "resourceUid": "0becd49aa2444b7db4c7aa80ac4c130b",
    "dataName": "chart",
    "content": '{"unitCode":"Learning to learn","word":"chart","wordDesc":"n.表格，图表","phoneticSymbol":""}',
    "resourceType": '1',
    "operatorUid": "fc0eb4795d3e41b09419dfbee695db10"
}


def get_uuid():
    uid = str(uuid.uuid4())
    return uid.replace('-', '')


def generate_data():
    res = []
    for i in range(5000):
        list = []
        list.append(get_uuid())
        list.append(data['resourceUid'])
        list.append(data['dataName'])
        list.append(data['content'])
        list.append(data['resourceType'])
        list.append(data['operatorUid'])
        res.append("(" + ','.join(list) + ")")
    file = open('/Users/user/Desktop/ttt.txt', 'w')
    for r in res:
        file.write(r)
    print(res)


if __name__ == '__main__':
    print(generate_data())