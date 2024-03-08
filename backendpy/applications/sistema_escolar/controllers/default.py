# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
from repository.student_repository import student_repository
estudiantes_repository = student_repository(db)


# ---- example index page ----
def index():
    grid = SQLFORM.grid(db.salones, orderby=db.salones.nombre, create=False, editable=False, deletable=False, user_signature=False)
    response.flash = T("Hello World")
    grid_html = grid
    return dict(mensaje="Hola desde MiApp")#dict(grid=grid)
#dict(message=T('Welcome to web2py!'))

def pg():
    print("Hola mundo")

def register_student():
    """
    Registers a new student
    """
    try:
        name = request.post_vars.name
        lastname = request.post_vars.email
        ege= request.post_vars.ege
        print(name)
        student_id = estudiante_repository.create(nombre, correo)

        response.status = 200
        response.body = json.dumps({'id': student_id})
    except Exception as e:
        response.status = 500
        response.body = json.dumps({'error': str(e)})

    return response    

def register():
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'  # Reemplaza con la URL de tu frontend
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    id = request.post_vars.id
    name = request.post_vars.name
    age = request.post_vars.age
    gender = request.post_vars.gender
    estudiante_id = estudiantes_repository.create(id, name, age, gender)
    #print(estudiante_id)

    # Lógica para registrar al estudiante y otras operaciones en el backend

    return response.json({'message': 'Estudiante registrado exitosamente'})


# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
