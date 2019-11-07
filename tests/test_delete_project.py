import random
from tests.test_add_project import test_add_project


def test_delete_random_project(app):
    if len(app.project.get_project_list()) == 0:
        test_add_project(app)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects
