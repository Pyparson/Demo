import time
import os
import yaml

base_path = os.path.dirname(__file__)
p = os.path.abspath(os.path.join(base_path, "config.yaml"))
with open(p, 'r')as f:
    data = yaml.load(f)
test_list = data["TestList"]


if __name__ == '__main__':
    # base_path = os.path.dirname(__file__)
    # test_list = ['test_room.py']
    string = ""
    if len(test_list):
        for i in test_list:
            file = os.path.abspath(os.path.join(base_path, "Case", str(i)))
            string += str(file) + " "
    else:
        file_path = os.path.abspath(os.path.join(base_path, "case1"))
        string += str(file_path) + " "
    command = "pytest %s --alluredir " % string
    report = time.strftime('%Y-%m-%d_%H:%M')
    xml_path = os.path.abspath(os.path.join(base_path, "Report", str(report), "xml"))
    report_path = os.path.abspath(os.path.join(base_path, "Report", str(report), "html"))
    print(command + xml_path)
    os.system(command + xml_path)
    os.system('allure generate ' + xml_path + ' -o ' + report_path)
