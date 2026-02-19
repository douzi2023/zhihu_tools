import configparser


class Config:
    def __init__(self) -> None:
        self.config = configparser.ConfigParser()
        self.config.read("..\config.ini")

    # 获取config.ini配置文件
    def get(self, section, key) -> str:
        return self.config.get(section, key)

    # 获取config.ini环境变量
    def getEnviroments(self) -> dict:

        envoromentDict = {}
        #print("正在读取 config.ini ...")
        #print("所有选项：", self.config.sections())
        #print("Default 节下的所有选项：", self.config.options("Default"))
        envoromentDict["Cookie"] = self.get("Default", "Cookie")
        envoromentDict["User-Agent"] = self.get("Default", "User-Agent")
        envoromentDict["Host"] = self.get("Default", "Host")
        return envoromentDict
