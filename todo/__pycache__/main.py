import flet as ft 
from base import TodoApp
    
def main(page: ft.Page):
    page.title = "TODO List v1.0.0"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    app = TodoApp()
    page.add(app)

if __name__ == "__main__":
    ft.app(target=main)
