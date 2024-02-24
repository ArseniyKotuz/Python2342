import flet as ft

class Task(ft.UserControl):
    def __init__(self, task_name):
        super.__init__()
        self.task_name = task_name
    
    def build(self):
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_input = ft.TextField(expand=1, value="")


        self.controls_viewport = [
            self.edit_input,
            ft.Row(
                spacing=0,
                controls=[
                    ft.IconButton(
                        icon=ft.icons.CREATE, 
                        tooltip="Edit Task", 
                        on_click=self.handle_edit,
                    ), 
                    ft.IconButton(
                        icon=ft.icons.DELETE, 
                        tooltip="DELETE Task", 
                        # on_click=self.handle_delete,
                    ), 
                ] 
            )
        ]

        self.display_viewport = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=self.controls_viewport,
        )

        self.display_viewport_edit = ft.Row(
            visible=True, 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, 
            vertical_alignment=ft.CrossAxisAlignment.CENTER, 
            controls=[
                self.edit_input, 
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN, 
                    tooltip="Upgrade Task", 
                    on_click=self.handle_save,
                )
            ]
        )

        return ft.Column(controls=[self.display_viewport, self.display_viewport_edit])

    def handle_edit(self):
        self.display_task.visible=False
        self.edit_input.visible=True
        self.edit_input.value= self.display_task.label
        self.update()
    
    def handle_save(self):
        self.display_task.visible=True
        self.edit_input.visible=False
        self.edit_input.value= self.display_task.value
        self.update()