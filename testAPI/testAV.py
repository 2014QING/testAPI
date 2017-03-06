# -*- coding:utf-8 -*-

# A simple example using the HTTP plugin

import requests
import unittest
from rwExcel import RwEXcel
import json


url = "http://10.19.4.20:6989/ivis/IntlAvSearch.json"


class AVAPITestCase(unittest.TestCase):
    def setUp(self):
        self.file = '/Users/zhaoqing/softwares/codes/testAPI/scripts/params/testAVDatas.xlsx'
        self.rwexcel = RwEXcel()

    def test_av(self):
        file=self.file
        filersname='testRs'
        rwexcel = self.rwexcel
        datas = rwexcel.read_excel_table_byindex(self.file)
        listrs = []
        for row in datas:
            #中转
            if(row['中转地']!="否"):
                data= {"caller": "hz",
                       "requesterToken": "5FFF73D3A3D6D2FF3A9AF2D366F09240",
                       "routingMaps": [{
                           "flightSegmentKeys": [
                               {
                                   "arrCity": row['中转地'],
                                   "date": self.reDate(row['旅行日期1']),
                                   "depCity": row['出发地'],
                                   "flightNo": row['航班号1']
                               },
                               {
                                   "arrCity": row['到达地'],
                                   "date": self.reDate(row['旅行日期2']),
                                   "depCity": row['中转地'],
                                   "flightNo": row['航班号2']
                               }
                           ],
                           "origDestRoutingPath": row['出发地']+"-"+row['航班号1']+"-"+self.reDate(row['旅行日期1'])+"-"+row['中转地']+"-"+row['航班号2']+"-"+self.reDate(row['旅行日期2'])+"-"+row['到达地']}],
                       "uuid": "ss"
                       }
                print("-----"+row['数据类型']+'******'+json.dumps(data))
                resp=requests.post(url,data=json.dumps(data),headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
                #print(resp.status_code)
                print(resp.json())
                listrs.append(json.dumps(resp.json()))
            #直达
            else:
                data = {"caller": "hz",
                        "requesterToken": "5FFF73D3A3D6D2FF3A9AF2D366F09240",
                        "routingMaps": [{
                            "flightSegmentKeys": [
                                {
                                    "arrCity": row['到达地'],
                                    "date": self.reDate(row['旅行日期1']),
                                    "depCity": row['出发地'],
                                    "flightNo": row['航班号1']
                                }
                            ],
                            "origDestRoutingPath": row['出发地'] + "-" + row['航班号1'] + "-" + self.reDate(
                                row['旅行日期1']) + "-" +row['到达地']}],
                        "uuid": "ss"
                        }
                print("-----" + row['数据类型'] +'******'+ json.dumps(data))
                resp = requests.post(url, data=json.dumps(data),
                                     headers={'Content-type': 'application/json', 'Accept': 'text/plain'})
                # print(resp.status_code)
                print(resp.json())
                listrs.append(json.dumps(resp.json()))
                #print(listrs)
        # 第一行是标题
        # 将结果写入excel文档中，
        rwexcel.write_excel_table_byindex(2, 22, listrs,file,filersname)

    # 将2016/12/30格式转为20161230
    def reDate(self,date):
        return (''.join(date.split('/')))

    def tearDown(self):
        pass
        # self.before()
        #self.test_av()


#if __name__ == '__main__':
   # tr = TestRunner()
    #tr.__call__()
