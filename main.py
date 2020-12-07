from requests import get
from os.path import join
from os import unlink
from random import randint
from svglib.svglib import svg2rlg
from reportlab.graphics.renderPDF import drawToFile
from PyPDF2 import PdfFileMerger

output_file_name = "2020_12_07_Программирование"
main_path = "https://webinar6.bmstu.ru/bigbluebutton/presentation/" + \
            "23656d33bc34f55baba465c736a3cddebc417261-1607325733350/" + \
            "23656d33bc34f55baba465c736a3cddebc417261-1607325733350/" + \
            "4623b7333979ba0e4a0abad911db4ecf3b51ed2c-1607325811614/svg"

if input("Использовать тестовые данные (да/нет)?").lower() != "да":
    main_path = input("Введите ссылку до номера слайда:")
    output_file_name = input("Введите имя выходного файла:")

slide = 1
random_int = randint(10 ** 5, 2 * 10 ** 5)
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
