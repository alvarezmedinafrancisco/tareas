import flet as ft
def LoginView(page, auth_controller):
    email_input= ft.Textfield(label = "Correo electrónico", width=350,border_radius=10)
    pass_input= ft.TextField(label = "Contraseña", password=True, can_reveal_password=True, width=350,border_radius=10)
    
    def login_click(e):
        user, msg= auth_controller.login(email_input.value, pass_input.value)
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else:
            page.snack_bar = ft.Snackbar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
        return ft.View("/",[
            ft.AppBar(title=ft.Text("SIGE - Login"), bgcolor=ft.colors.BLUE_GREY_900, color="white"),
            ft.Column([
                ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.colors.BLUE),
                ft.Text("Acceso al sistema", size=24, weight="bold"),
                email_input,
                pass_input,
                ft.ElevatedButton("Iniciar sesión", on_click=login_click, width=350),
                ft.TextButton("crear una cuenta nueva", on_click=lambda _: page.go("/register"))
            
            
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)])