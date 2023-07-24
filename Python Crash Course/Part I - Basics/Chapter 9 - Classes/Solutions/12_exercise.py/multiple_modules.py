from admin import Admin

adm = Admin('alonso', 'camarena', 'camarenaai', 'ai_dev@python.org', 'mexico')
adm_privileges = ["can add post", "can delete post", "can ban user"]
adm.privileges.privileges = adm_privileges
adm.describe_user()
adm.privileges.show_privileges()