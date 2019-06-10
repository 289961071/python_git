#!/usr/bin/python
# coding=utf-8
# 李路
from locust import task, HttpLocust, TaskSet


class WebsiteTasks(TaskSet):
    @task(1)
    def d1(self):
        self.client.get('/')

    @task(1)
    def d2(self):
        self.client.get("/wechatapp")


class WebUserLocust(HttpLocust):
    task_set = WebsiteTasks
    host = "https://ceshi.com"
    min_wait = 0
    max_wait = 0
