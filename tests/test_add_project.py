from model.project import Project
import string
import random
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + "  "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(3, maxlen))])


def test_add_project(app):
    old_projects = app.project.get_project_list()
    new_project = Project(name=random_string("Name:", 10))
    app.project.create(new_project)
    new_projects = app.project.get_project_list()
    old_projects.append(new_project)
    assert sorted(old_projects) == sorted(new_projects)


def clear_string(s):
    return re.sub("  ", " ", s)


def clean(project):
    return Project(name=clear_string(project.name.strip()))
