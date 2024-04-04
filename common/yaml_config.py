import yaml
from tools import get_project_path, sep


class GetConf:
    def __init__(self):
        project_dir = get_project_path()
        with open(project_dir + sep(['config', 'environment.yaml'], add_sep_before=True), "r",encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            print(self.env)

    def get_username_password(self):
        return self.env["username"], self.env["password"]

    def get_url(self):
        return self.env["url"]
if __name__ == '__main__':
    GetConf().get_username_password()
