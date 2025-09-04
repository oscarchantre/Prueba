from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.android.nativekey import AndroidKey

import time

# 1. Define capacidades
caps = {
    "platformName": "Android",
    "deviceName": "RF8X10L80GP",  # Reemplaza con el nombre de tu dispositivo si es físico
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.youtube",
    "appActivity": "com.google.android.youtube.HomeActivity",
    "noReset": True
}

# 2. Carga capacidades en opciones modernas
options = UiAutomator2Options().load_capabilities(caps)

# 3. Inicia el driver (¡NO uses desired_caps aquí!)
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

# 4. Espera unos segundos
time.sleep(10)

# 5. Validación básica
print("App actual:", driver.current_package)
boton = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Buscar"]')
boton.click()
campo = driver.find_element(AppiumBy.ID, "com.google.android.youtube:id/search_edit_text")
campo.send_keys("Los del fuego - Despues de ti\n")
driver.press_keycode(66)  # 66 es el código para Enter

# Swipe de abajo hacia arriba
driver.swipe(start_x=500, start_y=1500, end_x=500, end_y=500, duration=800)



boton1 = driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Los del Fuego - Despues de ti │ Video Lyric 2021 - 3 minutos y 38 segundos - Ir al canal - Los del Fuego - 40 millones de vistas - hace 4 años - reproducir video"]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView[1]')
boton1.click()
time.sleep(1000)

 

# 6. Finaliza sesión
#driver.quit()
