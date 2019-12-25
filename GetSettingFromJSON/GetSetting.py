import json

def GetSetting(arg):
    with open('GetSettingFromJSON/setting.json') as json_file:
        setting = json.load(json_file)
    if(arg == "--ServerImageDir"):
        return setting["ServerImageDir"]
    if(arg == "--FTPserverIP"):
        return setting["FTPserverIP"]
    if(arg == "--FTPserverPort"):
        return setting["FTPserverPort"]
    if(arg == "--FTPaccount"):
        return setting["FTPaccount"]
    if(arg == "--FTPpassword"):
        return setting["FTPpassword"]
    if(arg == "--SocketServerIP"):
        return setting["SocketServerIP"]
    if(arg == "--SocketServerPort"):
        return setting["SocketServerPort"]

def LoadSettingFromFile():
    with open('GetSettingFromJSON/systemSetting.json') as json_file:
        setting = json.load(json_file)
    return setting

def UpdateServerImageDir(dir):
    with open('GetSettingFromJSON/setting.json') as json_file:
        setting = json.load(json_file)
    setting["ServerImageDir"] = dir
    with open('GetSettingFromJSON/setting.json', 'w') as json_file:
        json.dump(setting, json_file)

def GetSystemSetting():
    try:
        with open('GetSettingFromJSON/systemSetting.json') as json_file:
            return json.load(json_file)
    except:
        return 0
            
# UpdateServerImageDir("local/abde")
# print(GetSetting("--ServerImageDir"))
