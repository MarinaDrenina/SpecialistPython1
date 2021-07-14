# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла

def log(text, file="files/log.txt"):
    f = open(file, "a", encoding="UTF-8")
    f.write("\n"+text)
    f.close()
    return

log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
