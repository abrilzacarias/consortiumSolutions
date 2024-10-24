# context_processors.py
# aca se establece una variable global en el proyecto
def grupos_usuario(request):
    if request.user.is_authenticated:
        grupos = request.user.groups.values_list('name', flat=True)
    else:
        grupos = []
    return {'grupos_usuario': grupos}
