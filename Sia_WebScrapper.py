import asyncio
import os

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://dninfoa.unal.edu.co/")
    await page.get_by_text("Sistema de información Académica", exact=True).click()
    async with page.expect_popup() as page1_info:
        await page.get_by_role("link", name="Portal de Servicios Académicos", exact=True).click()
    page1 = await page1_info.value
    await page1.get_by_placeholder("Usuario").click()
    await page1.get_by_placeholder("Usuario").fill(os.environ['USER'])
    await page1.get_by_placeholder("Contraseña").click()
    await page1.get_by_placeholder("Contraseña").fill(os.environ['PASSWORD'])
    await page1.get_by_role("button", name="Iniciar Sesión").click()
    await page1.get_by_role("heading", name="Buscador de cursos").get_by_text("Buscador de cursos").click()
    async with page1.expect_popup() as page2_info:
        await page1.get_by_role("link", name="Buscador de cursos").click()
    page2 = await page2_info.value
    await page2.wait_for_timeout(5000)
    await page2.goto("https://sia.unal.edu.co/Catalogo/facespublico/public/servicioPublico.jsf?taskflowId=task-flow-AC_CatalogoAsignaturas")

    await page2.get_by_role("combobox", name="Nivel de estudio").select_option("0")
    await page2.get_by_role("link", name="Logo Universidad").click()
    await page2.wait_for_timeout(2000)
    await page2.get_by_role("combobox", name="Sede").select_option("2")
    await page2.get_by_role("link", name="Logo Universidad").click()
    await page2.wait_for_timeout(2000)
    await page2.get_by_role("combobox", name="Facultad").select_option("7")
    await page2.get_by_role("link", name="Logo Universidad").click()
    await page2.wait_for_timeout(2000)
    await page2.get_by_role("combobox", name="Plan de estudios").select_option("3")
    await page2.get_by_role("link", name="Logo Universidad").click()
    await page2.wait_for_timeout(2000)
    await page2.get_by_role("combobox", name="Tipología de asignatura").select_option("0")
    await page2.get_by_role("link", name="Logo Universidad").click()
    await page2.wait_for_timeout(2000)
    await page2.get_by_role("button", name="Mostrar").click()
    await page2.wait_for_timeout(6000)
    await page2.get_by_role("link", name="Logo Universidad").click()
    await page2.wait_for_timeout(15000)

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())