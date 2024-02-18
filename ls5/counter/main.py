import flet as ft

def main(page: ft.Page):
    page.title = "Counter"
    page.window_width=500
    page.window_height=650
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    number_input = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_in = ft.TextField(value="10", text_align=ft.TextAlign.RIGHT, width=100)
    
    def minus_click(event):
        number_input.value = str(int(number_input.value) - 1)
        page.update()
    
    def plus_click(event):
        number_input.value = str(int(number_input.value) + 1)
        page.update()
    
    def remove_click(event):
        number_input.value = str(int(number_input.value) - int(txt_in.value))
        page.update()
    
    def add_click(event):
        number_input.value = str(int(number_input.value) + int(txt_in.value))
        page.update()

    page.add(
        ft.Row(
            [   
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click, width=80), 
                number_input, 
                ft.IconButton(ft.icons.ADD, on_click=plus_click, width=80), 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [   
                ft.TextButton("Remove", on_click=remove_click, width=80),
                txt_in, 
                ft.TextButton("Add", on_click=add_click, width=80) 
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ) 

    )



if __name__ == "__main__":
    ft.app(target=main)