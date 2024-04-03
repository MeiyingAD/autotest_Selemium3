import os


def get_project_path():
    """
    获取项目目录
    :return:
    """

    project_name = "pythonProject"
    file_path = os.path.dirname(__file__)
    a = file_path[:file_path.find("common")]
    return a


def sep(path, add_sep_before=False, add_sep_after=False):
    """
    系统分隔符
    :param path: 路径列表,类型为数组
    :param add_sep_before: 是否需要在拼接的路径前加分隔符
    :param add_sep_after:   是否需要在拼接的路径后加分隔符
    :return:
    """

    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    elif add_sep_after:
        all_path = all_path + os.sep
    return all_path


if __name__ == '__main__':
    path = get_project_path()

    all_path = sep(["config", "environment.yaml"], add_sep_before=True)

    print(all_path)
