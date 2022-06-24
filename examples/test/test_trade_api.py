#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import unittest
import sys
import os
import json
import time
import uuid


class TestOrder(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def test_order_placement(self):
        # {"code":"100001","msg":"The clientOid parameter cannot be empty."}
        ret = self.client.order_placement(
            symbol="BTCUSDTM",
            # clientOid=uuid.uuid1().hex,
            side="BUY",
            typ="LIMIT",
            price=1,
            size=1,
        )
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_single_order_cancellation(self):
        # Prepare order data for testing
        pram = dict(
            symbol="BTCUSDTM",
            clientOid=uuid.uuid1().hex,
            side="BUY",
            typ="LIMIT",
            price="1",
            size=10,
        )
        ret = self.client.order_placement(**pram)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

        if "orderId" in ret:  # successfully ordered
            ret = self.client.single_order_cancellation(
                symbol=pram["symbol"], orderId=ret["orderId"]
            )
            print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_batch_order_cancellation(self):  #
        symbol = "BTCUSDTM"
        pram = dict(
            symbol=symbol,
            clientOid=uuid.uuid1().hex,
            side="BUY",
            typ="LIMIT",
            price="1",
            size=10,
        )
        ret = self.client.order_placement(**pram)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

        pram = dict(
            symbol=symbol,
            clientOid=uuid.uuid1().hex,
            side="BUY",
            typ="LIMIT",
            price="1",
            size=10,
        )
        ret = self.client.order_placement(**pram)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

        # batch cancel order
        ret = self.client.batch_order_cancellation(symbol=symbol)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_query_transaction_records(self):
        # {"code":"400100","msg":"error.startAtInvalid"}
        ret = self.client.query_transaction_records(symbol="BTCUSDTM")
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_query_individual_orders_details(self):  # pass
        # clientOid = uuid.uuid1().hex
        # pram = dict(
        #     symbol="BTCUSDTM",
        #     clientOid=uuid.uuid1().hex,
        #     side="BUY",
        #     typ="LIMIT",
        #     price="1",
        #     size=10,
        # )
        # ret = self.client.order_placement(**pram)
        # print(json.dumps(ret, ensure_ascii=False, indent=2))
        # if "orderId" in ret:
        #     orderId = ret["orderId"]

        # ret = self.client.query_individual_orders_details(clientOid=clientOid)
        # print(json.dumps(ret, ensure_ascii=False, indent=2))

        orderId = '49629987480838144'
        ret = self.client.query_individual_orders_details(orderId=orderId)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_query_active_orders(self):  # pass
        clientOid = uuid.uuid1().hex
        pram = dict(
            symbol="BTCUSDTM",
            clientOid=uuid.uuid1().hex,
            side="BUY",
            typ="LIMIT",
            price="1",
            size=10,
        )
        ret = self.client.order_placement(**pram)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

        ret = self.client.query_active_orders(symbol="BTCUSDTM")
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_query_all_active_orders(self):  # pass
        clientOid = uuid.uuid1().hex
        pram = dict(
            symbol="BTCUSDTM",
            clientOid=uuid.uuid1().hex,
            side="BUY",
            typ="LIMIT",
            price="1",
            size=10,
        )
        ret = self.client.order_placement(**pram)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

        ret = self.client.query_all_active_orders()
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_query_historical_orders(self):
        ret = self.client.query_historical_orders(symbol="BTCUSDTM")
        print(json.dumps(ret, ensure_ascii=False, indent=2))


class TestPosition(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def test_get_the_position(self):  # pass
        ret = self.client.get_the_position(symbol="BTCUSDTM")
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_all_position(self, **kwargs):  # pass
        ret = self.client.get_all_position()
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_increase_position_margin(self):  # pass
        ret = self.client.increase_position_margin(
            symbol="BTCUSDTM", positionSide="BOTH", amount=1
        )
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_position_pnl_history(self):
        ret = self.client.position_pnl_history()
        print(json.dumps(ret, ensure_ascii=False, indent=2))


class TestFundingFees(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def test_query_funding_history(self):  # pass
        ret = self.client.query_funding_history(symbol="BTCUSDTM")
        print(json.dumps(ret, ensure_ascii=False, indent=2))