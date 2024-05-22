from locust import HttpUser,task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("http://43.135.150.180:7000/article/article-list/")
        # self.client.get("https://www.baidu.com/")