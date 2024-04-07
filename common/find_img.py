import aircv as ac

from common.tools import get_project_path, sep


class FindImg:
    def img_imread(self, img_path):
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)
        confidence = float(result["confidence"])
        return confidence


if __name__ == '__main__':
    source_path = get_project_path() + sep(["img", "source.png"])
    search_path = get_project_path() + sep(["img", "search.png"])
    confidence = FindImg().get_confidence(source_path, search_path)
    print(confidence)
