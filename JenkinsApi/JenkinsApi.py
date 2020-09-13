import jenkins
import csv
import sys
import os

def start_service():
    j = jenkins.Jenkins('http://192.168.1.111:8080', username='jenkins',password='11q!!Q')
    return j

def create_node(name,hostIP,port):
    j.create_node(
        name,
        numExecutors=1,
        nodeDescription=None,
        remoteFS='/home/build/jenkins',
        labels=name,
        exclusive=True,
        launcher=jenkins.LAUNCHER_SSH,
        launcher_params={
            'port': port,
            'credentialsId': '613873f3-f919-49cb-ac25-6c5855964c60',
            'host': hostIP
        }
    )

def csv_info():
    with open('node_info.csv') as f:
        csv_reader = csv.DictReader(f)
        return [res for res in csv_reader]

def create_nodes(list_info):
    for i in list_info:
        if not j.node_exists(i['name']):
            create_node(i['name'], i['hostIP'], i['port'])
            if j.node_exists(i['name']):
                print('节点创建成功:%s' % i['name'])
            else:
                print('节点创建失败：%s' % i['name'])

if __name__ == "__main__":
    # 调用jenkins服务
    j = start_service()
    # 批量创建节点
    list_info = csv_info()
    create_nodes(list_info)
    