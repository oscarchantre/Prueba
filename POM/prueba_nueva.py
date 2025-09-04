import pytest
from playwright.sync_api import Page
from objetos import HomePage

def test_diligenciar_formulario(page):
    home = HomePage(page)
    home.open()
    home.menu()
    home.diligenciar_formulario(
        First_Name="Oscar",
        LastName="Chantre",
        email="oscar@test.com",
        mobile="3001234567",
        current_addres="Calle 123 #45-67"
    )
    home.finalizar()

    