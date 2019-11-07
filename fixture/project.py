from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage_overview_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, '/manage_overview_page')]").click()

    def go_to_manage_projects_page(self):
        wd = self.app.wd
        self.go_to_manage_overview_page()
        wd.find_element_by_xpath("//a[contains(@href, '/manage_proj_page')]").click()

    def create(self, project):
        wd = self.app.wd
        self.go_to_manage_overview_page()
        self.go_to_manage_projects_page()
        wd.find_element_by_xpath("//button[@class='btn btn-primary btn-white btn-round']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@class='btn btn-primary btn-white btn-round']").click()
        self.go_to_manage_projects_page()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)

    def get_project_list(self):
        wd = self.app.wd
        self.go_to_manage_overview_page()
        self.go_to_manage_projects_page()
        projects_name = []
        for project_name in wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]"):
            name = project_name.text
            projects_name.append(Project(name=name))
        return list(projects_name)

    def delete(self, project_name):
        self.go_to_manage_overview_page()
        self.go_to_manage_projects_page()
        self.go_to_edit_page(project_name)
        self.delete_project()
        self.confirm_project_deletion()

    def go_to_edit_page(self, project_name):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit')][contains(text(), '%s')]" % project_name).click()

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@class='btn btn-primary btn-sm btn-white btn-round']").click()

    def confirm_project_deletion(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@class ='btn btn-primary btn-white btn-round']").click()
