def pytesseracttest():
    try:
        import Image
    except ImportError:
        from PIL import Image
    import pytesseract

    # print(pytesseract.image_to_string(Image.open('test.png')))
    # print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='chi_sim'))
    # print(pytesseract.image_to_string(Image.open('test-european.jpg')))
    print(pytesseract.image_to_string(Image.open('testc2.png'), lang='chi_sim'))


if __name__ == "__main__":
    pytesseracttest()
