# coding：utf-8

import requests
import unittest
import json
from rwExcel import RwEXcel
import time
import hashlib


class openAPITestCase(unittest.TestCase):
    def setUp(self):
        self.rwexcel = RwEXcel()
        self.url0 = "http://10.100.159.135:20001/ifow/privatefare/getOpenApi.do"
        #self.url0="http://10.19.6.84:8080/ifow/privatefare/getOpenApi.do"
        self.accessKeyId = 'zXOgWOpOrFu55AGV'
        self.userAccount = 'jpfx'
        self.accessKeySecret = 'zqOnCBshkONy0POjFythaOTac0Gbr8'
        self.timestamp = int(time.time()) * 1000 + 6000000

    def testAddOW(self):
        # 新增单程54个字段
        # 修改单程，多增字段：私有运价ID
        filersname = 'testaddOW'
        file = "/Users/zhaoqing/softwares/codes/testAPI/scripts/params/testaddOW.xlsx"
        datas = self.rwexcel.read_excel_table_byindex(file)
        listrs = []
        operateType = 1
        for row in datas:
            data = {
                "content": {
                    "mainFileGroupCode": self.isTureData(row['mainFileGroupCode']),
                    "externalId": self.isTureData(row["externalId"]),
                    "productType": self.isTureData(row['productType']),
                    "airline": self.isTureData(row['airline']),
                    "addressOption": self.isTureData(row['addressOption']),
                    "depCities": self.isTureData(row['depCities']),
                    "isTransfer": self.isTureData(row['isTransfer']),
                    "transferCities": self.isTureData(row['transferCities']),
                    "arrCities": self.isTureData(row['arrCities']),
                    "cabin": self.isTureData(row['cabin']),
                    "canDepStay": self.isTureData(row['canDepStay']),
                    "saleStart": self.isTureData(row['saleStart']),
                    "saleEnd": self.isTureData(row['saleEnd']),
                    "dateRestrictGo": self.isTureData(row['dateRestrictGo']),
                    "dateRestrictGoForbid": self.isTureData(row['dateRestrictGoForbid']),
                    "advancedSaleDate": self.isTureData(row['advancedSaleDate']),
                    "timeLimitType": self.isTureData(row['timeLimitType']),
                    "weekRestrictGo": self.isTureData(row['weekRestrictGo']),
                    "minPeopleNum": self.isTureData(row['minPeopleNum']),
                    "maxPeopleNum": self.isTureData(row['maxPeopleNum']),
                    "passengerType": self.isTureData(row['passengerType']),
                    "filePrice": self.isTureData(row['filePrice']),
                    "filePriceChild": self.isTureData(row['filePriceChild']),
                    "currency": self.isTureData(row['currency']),
                    "saleRetention": self.isTureData(row['saleRetention']),
                    "saleRebase": self.isTureData(row['saleRebase']),
                    "reserveType": self.isTureData(row['reserveType']),
                    "officeNo": self.isTureData(row['officeNo']),
                    "canReimbursementVoucher": self.isTureData(row['canReimbursementVoucher']),
                    "luggageType": self.isTureData(row['luggageType']),
                    "luggageWeightsBags": self.isTureData(row['luggageWeightsBags']),
                    "canInvalid": self.isTureData(row['canInvalid']),
                    "invalidFee": self.isTureData(row['invalidFee']),
                    "remark": self.isTureData(row['remark']),
                    "status": self.isTureData(row['status']),
                    "buyTicketNotice": self.isTureData(row['buyTicketNotice']),
                    "travelType": self.isTureData(row['travelType']),
                    "segmentFlightAllow": self.isTureData(row['segmentFlightAllow']),
                    "segmentFlightDeny": self.isTureData(row['segmentFlightDeny']),
                    "segmentAirlines": self.isTureData(row['segmentAirlines']),
                    "canChange": self.isTureData(row['canChange']),
                    "changeFeeDep": self.isTureData(row['changeFeeDep']),
                    "canRefund": self.isTureData(row['canRefund']),
                    "refundFeeAllUnused": self.isTureData(row['refundFeeAllUnused']),
                    "noShowRestrict": self.isTureData(row['noShowRestrict']),
                    "noShowFee": self.isTureData(row['noShowFee']),
                    "noShowRemark": self.isTureData(row['noShowRemark'])
                }
            }
            sign0 = 'accessKeyId=' + self.accessKeyId + '&accessKeySecret=' + self.accessKeySecret + '&content=' + str(
                data["content"]) + '&operateType=' + str(operateType) + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount
            # print('#########',data['content'])
            sign = self.isSha1(sign0)
            url = self.url0 + '?accessKeyId=' + self.accessKeyId + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount + '&sign=' + sign + '&operateType=' + str(
                operateType) + '&content=' + str(data["content"])
            print('$$$$$$$$$', url)
            rsp = requests.post(url=url)
            print('',rsp.json())
            listrs.append(json.dumps(rsp.json()))
        self.rwexcel.write_excel_table_byindex(2, 56, listrs, file, filersname)

    def testEditOW(self):
        # 修改单程，多增字段：私有运价ID
        filersname = 'testEditOW'
        file = "/Users/zhaoqing/softwares/codes/testAPI/scripts/params/testEditOW.xlsx"
        datas = self.rwexcel.read_excel_table_byindex(file)
        listrs = []
        operateType = 3
        for row in datas:
            data = {
                "content": {
                    "id": self.isTureData(row['id']),
                    "mainFileGroupCode": self.isTureData(row['mainFileGroupCode']),
                    "externalId": self.isTureData(row["externalId"]),
                    "productType": self.isTureData(row['productType']),
                    "airline": self.isTureData(row['airline']),
                    "addressOption": self.isTureData(row['addressOption']),
                    "depCities": self.isTureData(row['depCities']),
                    "isTransfer": self.isTureData(row['isTransfer']),
                    "transferCities": self.isTureData(row['transferCities']),
                    "arrCities": self.isTureData(row['arrCities']),
                    "cabin": self.isTureData(row['cabin']),
                    "canDepStay": self.isTureData(row['canDepStay']),
                    "saleStart": self.isTureData(row['saleStart']),
                    "saleEnd": self.isTureData(row['saleEnd']),
                    "dateRestrictGo": self.isTureData(row['dateRestrictGo']),
                    "dateRestrictGoForbid": self.isTureData(row['dateRestrictGoForbid']),
                    "advancedSaleDate": self.isTureData(row['advancedSaleDate']),
                    "timeLimitType": self.isTureData(row['timeLimitType']),
                    "weekRestrictGo": self.isTureData(row['weekRestrictGo']),
                    "minPeopleNum": self.isTureData(row['minPeopleNum']),
                    "maxPeopleNum": self.isTureData(row['maxPeopleNum']),
                    "passengerType": self.isTureData(row['passengerType']),
                    "filePrice": self.isTureData(row['filePrice']),
                    "filePriceChild": self.isTureData(row['filePriceChild']),
                    "currency": self.isTureData(row['currency']),
                    "saleRetention": self.isTureData(row['saleRetention']),
                    "saleRebase": self.isTureData(row['saleRebase']),
                    "reserveType": self.isTureData(row['reserveType']),
                    "officeNo": self.isTureData(row['officeNo']),
                    "canReimbursementVoucher": self.isTureData(row['canReimbursementVoucher']),
                    "luggageType": self.isTureData(row['luggageType']),
                    "luggageWeightsBags": self.isTureData(row['luggageWeightsBags']),
                    "canInvalid": self.isTureData(row['canInvalid']),
                    "invalidFee": self.isTureData(row['invalidFee']),
                    "remark": self.isTureData(row['remark']),
                    "status": self.isTureData(row['status']),
                    "buyTicketNotice": self.isTureData(row['buyTicketNotice']),
                    "travelType": self.isTureData(row['travelType']),
                    "segmentFlightAllow": self.isTureData(row['segmentFlightAllow']),
                    "segmentFlightDeny": self.isTureData(row['segmentFlightDeny']),
                    "segmentAirlines": self.isTureData(row['segmentAirlines']),
                    "canChange": self.isTureData(row['canChange']),
                    "changeFeeDep": self.isTureData(row['changeFeeDep']),
                    "canRefund": self.isTureData(row['canRefund']),
                    "refundFeeAllUnused": self.isTureData(row['refundFeeAllUnused']),
                    "noShowRestrict": self.isTureData(row['noShowRestrict']),
                    "noShowFee": self.isTureData(row['noShowFee']),
                    "noShowRemark": self.isTureData(row['noShowRemark'])
                }
            }

            sign0 = 'accessKeyId=' + self.accessKeyId + '&accessKeySecret=' + self.accessKeySecret + '&content=' + str(
                data["content"]) + '&operateType=' + str(operateType) + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount
            # print('#########',data['content'])
            sign = self.isSha1(sign0)
            url = self.url0 + '?accessKeyId=' + self.accessKeyId + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount + '&sign=' + sign + '&operateType=' + str(
                operateType) + '&content=' + str(data["content"])
            print('$$$$$$$$$', url)
            rsp = requests.post(url=url)
            print('',rsp.json())
            listrs.append(json.dumps(rsp.json()))
        self.rwexcel.write_excel_table_byindex(2, 56, listrs, file, filersname)

    def testAddRT(self):
        # 新增往返60个字段
        file="/Users/zhaoqing/softwares/codes/testAPI/scripts/params/testaddRT.xlsx"
        filersname = 'testaddRT'
        datas = self.rwexcel.read_excel_table_byindex(file)
        listrs = []
        operateType = 6

        for row in datas:
            data = {
                "content": {
                    "mainFileGroupCode":self.isTureData(row['mainFileGroupCode']),
                    "externalId": self.isTureData(row["externalId"]),
                    "productType": self.isTureData(row['productType']),
                    "airline": self.isTureData(row['airline']),
                    "addressOption": self.isTureData(row['addressOption']),
                    "depCities": self.isTureData(row['depCities']),
                    "isTransfer": self.isTureData(row['isTransfer']),
                    "transferCities": self.isTureData(row['transferCities']),
                    "arrCities": self.isTureData(row['arrCities']),
                    "cabin": self.isTureData(row['cabin']),
                    "canDepStay": self.isTureData(row['canDepStay']),
                    "saleStart": self.isTureData(row['saleStart']),
                    "saleEnd": self.isTureData(row['saleEnd']),
                    "dateRestrictGo": self.isTureData(row['dateRestrictGo']),
                    "dateRestrictGoForbid": self.isTureData(row['dateRestrictGoForbid']),
                    "advancedSaleDate": self.isTureData(row['advancedSaleDate']),
                    "timeLimitType": self.isTureData(row['timeLimitType']),
                    "weekRestrictGo": self.isTureData(row['weekRestrictGo']),
                    "minPeopleNum": self.isTureData(row['minPeopleNum']),
                    "maxPeopleNum": self.isTureData(row['maxPeopleNum']),
                    "passengerType": self.isTureData(row['passengerType']),
                    "filePrice": self.isTureData(row['filePrice']),
                    "filePriceChild": self.isTureData(row['filePriceChild']),
                    "currency": self.isTureData(row['currency']),
                    "saleRetention": self.isTureData(row['saleRetention']),
                    "saleRebase": self.isTureData(row['saleRebase']),
                    "reserveType": self.isTureData(row['reserveType']),
                    "officeNo": self.isTureData(row['officeNo']),
                    "canReimbursementVoucher": self.isTureData(row['canReimbursementVoucher']),
                    "luggageType": self.isTureData(row['luggageType']),
                    "luggageWeightsBags": self.isTureData(row['luggageWeightsBags']),
                    "canInvalid": self.isTureData(row['canInvalid']),
                    "invalidFee": self.isTureData(row['invalidFee']),
                    "remark": self.isTureData(row['remark']),
                    "status": self.isTureData(row['status']),
                    "buyTicketNotice": self.isTureData(row['buyTicketNotice']),
                    "travelType": self.isTureData(row['travelType']),
                    "segmentFlightAllow": self.isTureData(row['segmentFlightAllow']),
                    "segmentFlightDeny": self.isTureData(row['segmentFlightDeny']),
                    "segmentAirlines": self.isTureData(row['segmentAirlines']),
                    "canChange": self.isTureData(row['canChange']),
                    "changeFeeDep": self.isTureData(row['changeFeeDep']),
                    "canRefund": self.isTureData(row['canRefund']),
                    "refundFeeAllUnused": self.isTureData(row['refundFeeAllUnused']),
                    "noShowRestrict": self.isTureData(row['noShowRestrict']),
                    "noShowFee": self.isTureData(row['noShowFee']),
                    "noShowRemark": self.isTureData(row['noShowRemark']),
                    #"operateSource": self.isTureData(row['operateSource']),
                    "bCanRt": self.isTureData(row['bCanRt']),
                    "canGroupFileCode": self.isTureData(row['canGroupFileCode']),
                    "canRetStay": self.isTureData(row['canRetStay']),
                    "minStay": self.isTureData(row['minStay']),
                    "maxStay": self.isTureData(row['maxStay']),
                    "weekRestrictReturn": self.isTureData(row['weekRestrictReturn']),
                    "canChangeRet": self.isTureData(row['canChangeRet']),
                    "changeFeeRet": self.isTureData(row['changeFeeRet']),
                    "canRefundPartUnused": self.isTureData(row['canRefundPartUnused']),
                    "refundFeePartUnused": self.isTureData(row['refundFeePartUnused']),
                    "dateRestrictReturn": self.isTureData(row['dateRestrictReturn']),
                    "dateRestrictReturnForbid": self.isTureData(row['dateRestrictReturnForbid'])
                }
            }


            sign0 = 'accessKeyId=' + self.accessKeyId + '&accessKeySecret=' + self.accessKeySecret + '&content=' + str(
                data["content"]) + '&operateType=' + str(operateType) + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount
            print('#########',str(int(row['NO'])),data['content'])
            sign = self.isSha1(sign0)
            url = self.url0 + '?accessKeyId=' + self.accessKeyId + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount + '&sign=' + sign + '&operateType=' + str(
                operateType) + '&content=' + str(data["content"])
            #url中&和?有特殊含义，会被截取
            print('$$$$$$$$$',url)

            rsp = requests.post(url=url)
            print(rsp.json())
            listrs.append(str(rsp.json()))
        self.rwexcel.write_excel_table_byindex(2,65, listrs, file, filersname)

    def testEditRT(self):
        #修改比新增多一个ID
        file="/Users/zhaoqing/softwares/codes/testAPI/scripts/params/testEditRT.xlsx"
        filersname = 'testEditRT'
        datas = self.rwexcel.read_excel_table_byindex(file)
        listrs = []
        operateType = 3

        for row in datas:
            data = {
                "content": {
                    "id":self.isTureData(row['id']),
                    "mainFileGroupCode":self.isTureData(row['mainFileGroupCode']),
                    "externalId": self.isTureData(row["externalId"]),
                    "productType": self.isTureData(row['productType']),
                    "airline": self.isTureData(row['airline']),
                    "addressOption": self.isTureData(row['addressOption']),
                    "depCities": self.isTureData(row['depCities']),
                    "isTransfer": self.isTureData(row['isTransfer']),
                    "transferCities": self.isTureData(row['transferCities']),
                    "arrCities": self.isTureData(row['arrCities']),
                    "cabin": self.isTureData(row['cabin']),
                    "canDepStay": self.isTureData(row['canDepStay']),
                    "saleStart": self.isTureData(row['saleStart']),
                    "saleEnd": self.isTureData(row['saleEnd']),
                    "dateRestrictGo": self.isTureData(row['dateRestrictGo']),
                    "dateRestrictGoForbid": self.isTureData(row['dateRestrictGoForbid']),
                    "advancedSaleDate": self.isTureData(row['advancedSaleDate']),
                    "timeLimitType": self.isTureData(row['timeLimitType']),
                    "weekRestrictGo": self.isTureData(row['weekRestrictGo']),
                    "minPeopleNum": self.isTureData(row['minPeopleNum']),
                    "maxPeopleNum": self.isTureData(row['maxPeopleNum']),
                    "passengerType": self.isTureData(row['passengerType']),
                    "filePrice": self.isTureData(row['filePrice']),
                    "filePriceChild": self.isTureData(row['filePriceChild']),
                    "currency": self.isTureData(row['currency']),
                    "saleRetention": self.isTureData(row['saleRetention']),
                    "saleRebase": self.isTureData(row['saleRebase']),
                    "reserveType": self.isTureData(row['reserveType']),
                    "officeNo": self.isTureData(row['officeNo']),
                    "canReimbursementVoucher": self.isTureData(row['canReimbursementVoucher']),
                    "luggageType": self.isTureData(row['luggageType']),
                    "luggageWeightsBags": self.isTureData(row['luggageWeightsBags']),
                    "canInvalid": self.isTureData(row['canInvalid']),
                    "invalidFee": self.isTureData(row['invalidFee']),
                    "remark": self.isTureData(row['remark']),
                    "status": self.isTureData(row['status']),
                    "buyTicketNotice": self.isTureData(row['buyTicketNotice']),
                    "travelType": self.isTureData(row['travelType']),
                    "segmentFlightAllow": self.isTureData(row['segmentFlightAllow']),
                    "segmentFlightDeny": self.isTureData(row['segmentFlightDeny']),
                    "segmentAirlines": self.isTureData(row['segmentAirlines']),
                    "canChange": self.isTureData(row['canChange']),
                    "changeFeeDep": self.isTureData(row['changeFeeDep']),
                    "canRefund": self.isTureData(row['canRefund']),
                    "refundFeeAllUnused": self.isTureData(row['refundFeeAllUnused']),
                    "noShowRestrict": self.isTureData(row['noShowRestrict']),
                    "noShowFee": self.isTureData(row['noShowFee']),
                    "noShowRemark": self.isTureData(row['noShowRemark']),
                    #"operateSource": self.isTureData(row['operateSource']),
                    "bCanRt": self.isTureData(row['bCanRt']),
                    "canGroupFileCode": self.isTureData(row['canGroupFileCode']),
                    "canRetStay": self.isTureData(row['canRetStay']),
                    "minStay": self.isTureData(row['minStay']),
                    "maxStay": self.isTureData(row['maxStay']),
                    "weekRestrictReturn": self.isTureData(row['weekRestrictReturn']),
                    "canChangeRet": self.isTureData(row['canChangeRet']),
                    "changeFeeRet": self.isTureData(row['changeFeeRet']),
                    "canRefundPartUnused": self.isTureData(row['canRefundPartUnused']),
                    "refundFeePartUnused": self.isTureData(row['refundFeePartUnused']),
                    "dateRestrictReturn": self.isTureData(row['dateRestrictReturn']),
                    "dateRestrictReturnForbid": self.isTureData(row['dateRestrictReturnForbid'])
                }
            }

            sign0 = 'accessKeyId=' + self.accessKeyId + '&accessKeySecret=' + self.accessKeySecret + '&content=' + str(
                data["content"]) + '&operateType=' + str(operateType) + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount
            # print('#########',data['content'])
            sign = self.isSha1(sign0)
            url = self.url0 + '?accessKeyId=' + self.accessKeyId + '&timestamp=' + str(
                self.timestamp) + '&userAccount=' + self.userAccount + '&sign=' + sign + '&operateType=' + str(
                operateType) + '&content=' + str(data["content"])
            print('$$$$$$$$$',url)
            rsp = requests.post(url=url)
            print(rsp.json())
            print(type(rsp.json()))
            listrs.append(str(rsp.json()))
        self.rwexcel.write_excel_table_byindex(2,68, listrs, file, filersname)



    def testQuery(self):
        filename="Query"
        listrs=[]
        file=""
        #operateTpe操作类型(1-新增单程 2-删除 3-修改 4-查询 5-批量修改状态 6-新增往返)
        operateType=4
        datas=self.rwexcel.read_excel_table_byindex(file)
        for row in datas:
            data = {
                "content":{
                    "id":self.isTureData(row["id"]),
                    "externalId":self.isTureData(row['externalId']),
                    "status":self.isTureData(row["status"]),
                    "productType":self.isTureData(row["productType"]),
                    "depCtiy":self.isTureData(row["depCtiy"]),
                    "arrCity":self.isTureData(row["arrCity"]),
                    "fileCode":self.isTureData(row["fileCode"]),
                    "cabin":self.isTureData(row["cabin"]),
                    "agent":self.isTureData(row["agent"]),
                    "gmtCreateStart":self.isTureData(row["gmtCreateStart"]),
                    "gmtCreateEnd": self.isTureData(row["gmtCreateEnd"]),
                    "gmtModifiedStart":self.isTureData(row["gmtModifiedStart"]),
                    "gmtModifiedEnd": self.isTureData(row["gmtModifiedEnd"]),
                    "travelType":self.isTureData(row["travelType"]),
                    "pageNum":self.isTureData(row["pageNum"]),
                    "pageSize":self.isTureData(row["pageSize"])
                }
            }
            sign0 = 'accessKeyId=' + self.accessKeyId + '&accessKeySecret=' + self.accessKeySecret + '&content=' + str(
            data["content"]) + '&operateType=' + str(operateType) + '&timestamp=' + str(
            self.timestamp) + '&userAccount=' + self.userAccount
        # print('#########',data['content'])
            sign = self.isSha1(sign0)
            url = self.url0 + '?accessKeyId=' + self.accessKeyId + '&timestamp=' + str(
            self.timestamp) + '&userAccount=' + self.userAccount + '&sign=' + sign + '&operateType=' + str(
            operateType) + '&content=' + str(data["content"])
            rsp = requests.post(url=url)
            listrs.append(json.dumps(rsp.json()))
        self.rwexcel.write_excel_table_byindex(2,15,listrs,file,filename)
        print("Query result:",listrs)

    def testDele(self):
        listrs=[]
        #id=246588124887515149
        id=246588124887515151,246588124887515152
        operateType=2
        data = {
            "content":{
            "id": id
            }
        }
        sign0 = 'accessKeyId=' + self.accessKeyId + '&accessKeySecret=' + self.accessKeySecret + '&content=' + str(
            data["content"]) + '&operateType=' + str(operateType) + '&timestamp=' + str(
            self.timestamp) + '&userAccount=' + self.userAccount
        # print('#########',data['content'])
        sign = self.isSha1(sign0)
        url = self.url0 + '?accessKeyId=' + self.accessKeyId + '&timestamp=' + str(
            self.timestamp) + '&userAccount=' + self.userAccount + '&sign=' + sign + '&operateType=' + str(
            operateType) + '&content=' + str(data["content"])
        print('&&&&&&&&&',url)
        rsp = requests.post(url=url)
        listrs.append(rsp.json())
        print(listrs)

    def testChangeStatus(self):
        filersname='testChangeStatus'
        listrs=[]
        operateType=5
        file="/Users/zhaoqing/softwares/codes/testAPI/scripts/params/testChangeStatus.xlsx"

        datas = self.rwexcel.read_excel_table_byindex(file)
        for row in datas:
            data = {
            "content":{
                "ids": self.isTureData(row['ids']),
                "statusBefore": self.isTureData(row['statusBefore']),
                "statusAfter": self.isTureData(row['statusAfter'])
            }
        }
            sign0 = 'accessKeyId=' + self.accessKeyId + '&accessKeySecret=' + self.accessKeySecret + '&content=' + str(
            data["content"]) + '&operateType=' + str(operateType) + '&timestamp=' + str(
            self.timestamp) + '&userAccount=' + self.userAccount
            print('#########',row['No'],data['content'])
            sign = self.isSha1(sign0)
            url = self.url0 + '?accessKeyId=' + self.accessKeyId + '&timestamp=' + str(
            self.timestamp) + '&userAccount=' + self.userAccount + '&sign=' + sign + '&operateType=' + str(
            operateType) + '&content=' + str(data["content"])
            rsp = requests.post(url=url)
            print(url)
            print(rsp.json())
            listrs.append(str(rsp.json()))
        print("Change status result:",listrs)
        self.rwexcel.write_excel_table_byindex(2,6, listrs, file, filersname)


    # 查询
    # 批量修改状态
    # 删除运价
    def tearDwon(self):
        pass
    # #非空转为整型
    # def isNull(self,pa):
    #     if(pa==''):
    #         return pa
    #     else:
    #         return int(pa)
    #将2017/02/25转为2017-02-25
    def isDate(self,date):
        return date.replace('/','-')

    #从Excel读取的数字全是float类型，对于输入数字但实际传递为str的参数，需将参数转为int,去掉小数点，在转为str
    # def isTureData(self, str0):
    #     if (isinstance(str0, float)):
    #         return str(int(str0))
    #     return str0
    #
    # def isTureData(self, num):
    #     if (isinstance(num, str)):
    #         return num
    #     return num

    # 测试数据为str,则直接传str
    # 测试数据为整型，需转为int
    # 判断是否是XXX.0，是，默认读取变成浮点型，需转为整型，否，则说明测试数据为浮点型
    def isTureData(self,num):
        if(isinstance(num,str)):
            return num
        if(isinstance(num,float)):
            if(str(num).split('.')[1]=='0'):
                return int(num)
            return num

    def isSha1(self,sign):
        hash = hashlib.sha1()
        hash.update(sign.encode('utf-8'))
        return hash.hexdigest()

    #def testit(self):
    #   print(self.isTureData(1.0))
    #def testit(self):
        #num=0.000009
        #print(int(str(num))[0]*str)
        #print(str.format( "%f",num))
        #print(str(0.000001).split('.'))
        #print(self.isTureData(0.000001))
