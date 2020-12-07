from requests import get
from pathlib import Path
from os import unlink
from random import randint
from svglib.svglib import svg2rlg
from reportlab.graphics.renderPDF import drawToFile
from PyPDF2 import PdfFileMerger
from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from sys import platform
from time import sleep


def get_browser():
    current_dir = Path(__file__).parent.absolute()

    if platform == "darwin":
        chromedriver_path = str(
            current_dir.joinpath("chromedriver/macos/chromedriver").absolute())
    elif "win" in platform:
        chromedriver_path = str(current_dir.joinpath(
            "chromedriver/windows/chromedriver.exe").absolute())
    else:
        chromedriver_path = str(
            current_dir.joinpath("chromedriver/linux/chromedriver").absolute())

    return Chrome(options=ChromeOptions(), executable_path=chromedriver_path)


def main(browser):
    url = input("Введите URL из почты:")
    output_file_name = input("Введите имя выходного файла:")
    random_int = randint(10 ** 5, 2 * 10 ** 5)

    browser.get(url)
    name_input = browser.find_element_by_id(
        "_".join([""] + url.split("/")[-2:] + ["join", "name"])
    )
    name_input.send_keys("Downloader {}".format(random_int))
    name_input.parent.find_element_by_tag_name("button").click()

    while True:
        try:
            current_slide = browser.find_element_by_tag_name("image")
            break
        except NoSuchElementException:
            print("Встреча не активна, повторяем через 5 секунд...")
            sleep(5)

    main_path = "/".join(
        current_slide.get_attribute("xlink:href").split("/")[:-1])
    slide = 1

    pdf_merger = PdfFileMerger()
    print("Начало скачивания")
    while True:
        slide_response = get(join(main_path, str(slide)))
        if slide_response.status_code != 200:
            print("Скачано и склеено слайдов: {}".format(slide - 1))
            break
        svg_file_name = "./temp_file_{}_{}.svg".format(random_int, slide)
        with open(svg_file_name, "wb") \
                as slide_file:
            slide_file.write(slide_response.content)
        svg_slide = svg2rlg(svg_file_name)
        pdf_file_name = svg_file_name.replace("svg", "pdf")
        drawToFile(svg_slide, pdf_file_name)
        pdf_merger.append(pdf_file_name)
        unlink(svg_file_name)
        unlink(pdf_file_name)
        print("Скачан слайд: {}".format(slide))
        slide += 1

    output_pdf_file_name = "{}.pdf".format(output_file_name)
    pdf_merger.write(open(output_pdf_file_name, "wb"))
    print("Результат записан в файл: {}".format(output_pdf_file_name))


if __name__ == "__main__":
    b = get_browser()
    try:
        main(b)
        b.quit()
    except (NoSuchElementException, KeyboardInterrupt):
        print("Завершение работы!")
        b.quit()
