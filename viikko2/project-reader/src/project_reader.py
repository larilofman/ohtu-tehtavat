from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        poetry_toml = toml.loads(content)["tool"]["poetry"]

        name = poetry_toml["name"]
        description = poetry_toml["description"]
        dependencies = poetry_toml["dependencies"]
        dev_dependencies = poetry_toml["dev-dependencies"]

        return Project(name, description, dependencies, dev_dependencies)
