from playwright.sync_api import sync_playwright
import requests

def puerto_disponible():
    try:
        response = requests.get("http://localhost:9222/json", timeout=3)
        return response.status_code == 200
    except:
        return False

def test_navegar_a_youtube_desde_movil():
    if not puerto_disponible():
        print("No se detecta conexión CDP con el móvil. Verifica adb forward.")
        return

    with sync_playwright() as p:
        # Conectar al navegador Chrome en el móvil
        browser = p.chromium.connect_over_cdp("http://localhost:9222")

        # Usa el contexto actual o crea uno nuevo
        context = browser.contexts[0] if browser.contexts else browser.new_context()

        # Abre nueva pestaña en el móvil
        page = context.new_page()

        # Ir a YouTube
        page.goto("https://m.youtube.com")  # versión móvil

        # Esperar que cargue algo visible
       # page.wait_for_selector("text=Inicio", timeout=10000)

        # Captura para validar
        page.screenshot(path="C:/Users/oscar/OneDrive/Desktop/python/Ejercicios/Imagenes/youtube.jpg")
        print("YouTube abierto en el móvil. Título:", page.title())

        browser.close()
