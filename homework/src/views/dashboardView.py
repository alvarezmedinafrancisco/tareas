import flet as ft
def DashboardView(page, tarea_controller):
    user= page.session.get("user")
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_tareas(user["id"]):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t["titulo"], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            trailing=ft.Badge(content=ft.Text(t["estado"]),bgcolor=ft.colors.ORANGE_300)
                        ), padding=10
                )
            )
        )
    page.update()
    txt_titulo = ft.TextField(label="Nueva Tarea", expand=True)
    def add_task(e):
        success, msg = tarea_controller.guardar_nueva(user["id_usuario"], txt_titulo.value, "", "Media","trabajo")
        if success:
            txt_titulo.value = ""
            refresh()
    return ft.View("/dashboard", [
        ft.AppBar(
            title=ft.Text(f"Bienvenido, {user['nombre']}"),
            actions=[ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda e: page.go("/login"))
            ]
        ),
        ft.column([
            ft.Row([txt_titulo,ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_task)]),
            ft.divider(),
            ft.Text("mis tareas pendientes", size=20, weight="bold"),
            lista_tareass
    ], expand=True, padding=20)
    ],on_open=lambda _: refresh())