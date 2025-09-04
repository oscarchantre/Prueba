import re
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://demoqa.com/")

    def menu(self):
       self.page.locator("//h5[contains(.,'Forms')]").click()
       self.page.get_by_text("Practice Form").click()

    def diligenciar_formulario(self, First_Name, LastName, email, mobile, current_addres):
        self.page.get_by_role("textbox", name="First Name").click()
        self.page.get_by_role("textbox", name="First Name").fill(First_Name)
        self.page.get_by_role("textbox", name="First Name").press("Tab")
        self.page.get_by_role("textbox", name="Last Name").fill(LastName)
        self.page.get_by_role("textbox", name="name@example.com").click()
        self.page.get_by_role("textbox", name="name@example.com").fill(email)
        self.page.get_by_text("Male", exact=True).click()
        self.page.get_by_role("textbox", name="Mobile Number").click()
        self.page.get_by_role("textbox", name="Mobile Number").fill(mobile)
        self.page.locator("#dateOfBirthInput").click()
        self.page.get_by_role("combobox").nth(1).select_option("1991")
        self.page.locator("div").filter(has_text=re.compile(r"^JanuaryFebruaryMarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecember$")).get_by_role("combobox").select_option("2")
        self.page.get_by_role("option", name="Choose Saturday, March 2nd,").click()
        self.page.locator(".subjects-auto-complete__value-container").click()
        self.page.locator("#subjectsInput").fill("Esto es una prueba")
        self.page.get_by_text("Sports").click()
        self.page.get_by_role("textbox", name="Current Address").click()
        self.page.get_by_role("textbox", name="Current Address").fill(current_addres)
        self.page.get_by_text("Select State").click()
        self.page.get_by_text("NCR", exact=True).click()
        self.page.get_by_text("Select City").click()
        self.page.get_by_text("Delhi", exact=True).click()

    def finalizar(self):
        self.page.get_by_role("button", name="Submit").click()
        self.page.get_by_role("button", name="Close").click()