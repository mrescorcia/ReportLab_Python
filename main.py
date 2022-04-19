from reportlab.pdfgen import canvas

def run():

    c = canvas.Canvas("./src/tests.pdf")

    c.save()

if __name__ == '__main__':
    run()