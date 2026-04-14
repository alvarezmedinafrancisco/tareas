import flet as ft
from controllers.usercontroller import AuthController
from controllers.tareacontroller import TareaController
from src.views.loginView import LoginView
from src.views.dashboardView import DashboardView

def main(page: ft.Page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, auth_ctrl, task_ctrl))
            
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("error Ruta no encontrada")])
            )
        page.update()
        
    page.on_route_change = route_change
    page.go("/")
    
if __name__ == "__main__":
    ft.run(main)