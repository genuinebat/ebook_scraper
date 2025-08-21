import os
from ebooklib import epub
from PIL import Image
import io

book = epub.EpubBook()

book.set_identifier("TBATE")
book.set_title("The Beginning After The End")
book.set_language("en")

book.add_author("TurtleMe")
b = io.BytesIO()
cover_img.save(b, "png")
b_cover_img = b.getvalue()
book.add_item(cover)

chaps = []

txt_files_dir = "./text_files/"
txt_files = os.listdir(txt_files_dir)

for f in txt_files:
    src = open(txt_files_dir + f, "r", encoding="utf-8").readlines()

    content = ""
    for item in src:
        content += "<p>" + item + "</p>"

    f_name = f[:-4]

    chap = epub.EpubHtml(uid="C" + f_name[7:].strip(), title=f_name, file_name="chap_" + f_name[7:].strip() + ".xhtml")
    chap.content=u"<html><head></head><body>" + "<div>" + content + "</div></body></html>"

    book.add_item(chap)
    chaps.append(chap)

book.toc = tuple(chaps)

book.spine = chaps

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

epub.write_epub("./epub_files/TBATE.epub", book, {})