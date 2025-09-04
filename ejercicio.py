import re
import time
from playwright.sync_api import Page, expect
from funcion import obtener_usuarios


def test_example(page: Page) -> None:
    
    page.goto("https://demoqa.com/")
    page.get_by_role("heading", name="Forms").click()
    page.get_by_text("Practice Form").click()
    usuarios = obtener_usuarios()
    for i, usuario in enumerate(usuarios, start=1):
        page.locator("#firstName").fill(usuario["nombre"])
        page.locator("#lastName").fill(usuario["apellido"])
        page.locator("#userEmail").fill(usuario["email"])
        page.get_by_text("Male", exact=True).click()

        page.locator("#userNumber").fill("3167472539")

        # Fecha de nacimiento con formato simplificado
        page.locator("#dateOfBirthInput").click()
        page.locator("#dateOfBirthInput").fill("02 Mar 1991")
        page.keyboard.press("Enter")

        # Materia
        page.locator("#subjectsInput").fill("P")
        page.get_by_text("Computer Science", exact=True).click()

        # Hobbies
        page.get_by_text("Sports").click()
        page.get_by_text("Reading").click()
        page.get_by_text("Music").click()

        # Dirección
        page.locator("#currentAddress").fill("es una prueba automatizada")

        # Estado y ciudad
        page.get_by_text("Select State").click()
        page.get_by_text("Uttar Pradesh", exact=True).click()
        page.get_by_text("Select City").click()
        page.get_by_text("Agra", exact=True).click()

        # Enviar formulario
        page.get_by_role("button", name="Submit").click()

        # Esperar que aparezca el modal y tomar screenshot
        time.sleep(2)
        page.screenshot(path=f"C:/Users/oscar/OneDrive/Desktop/python/Ejercicios/Imagenes/final_{i}.jpg")

        # Cerrar modal
        page.locator("//button[@type='button'][contains(.,'Close')]").click()
        time.sleep(1)
