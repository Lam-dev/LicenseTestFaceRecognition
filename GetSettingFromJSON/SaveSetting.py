import json
def SaveSystemSetting(settingDict):
    with open('GetSettingFromJSON/systemSetting.json', 'w') as json_file:
        json.dump(settingDict, json_file)