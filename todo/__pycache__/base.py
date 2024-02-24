import flet as ft 


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task_input = ft.TextField(hint_text="Whats needs to be done?", on_submit=self.handle_add_task)
        self.tasks_viewport = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task_input, 
                            ft.FloatingActionButton(
                                icon=ft.icons.ADD,
                                on_click=self.handle_add_task, 
                            )
                        ]
                    ), 
                    self.tasks_viewport,
            ]
        )
    
    def handle_add_task(self, e):
        # ADD NEW TASK EVENT HANDLER
        self.tasks_viewport.controls.append(ft.Checkbox(label=self.new_task_input.value))
        self.new_task_input.value = ""
        self.update()