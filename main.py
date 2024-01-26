import flet as ft

def main(page: ft.Page):
    page.title = 'Login Screen'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def btn_click(e):
        if all([name_input.value, pass_input.value]):
            dlg = ft.AlertDialog(
                title=ft.Text('Bem Vindo ' + name_input.value)
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

        page.appbar = ft.AppBar(title=ft.Text('Login Screen'), center_title=True)
        name_input = ft.TextField(
            label='Nome', autofocus=True, hint_text='Digite seu nome'
        )
        pass_input = ft.TextField(
            label='Senha', password=True, can_reveal_password=True
        )
        submit_btn = ft.ElevatedButton(
            text='Enviar', width=600, on_click=btn_click
        )
        page.update()
        page.add(name_input, pass_input, submit_btn)

ft.app(target=main)
