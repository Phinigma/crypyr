from PIL import Image

class SteganographyExtract:
    @staticmethod
    def decode(image_path):
        img = Image.open(image_path)
        width, height = img.size
        message = ""

        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                char_bits = (r & 0x1) << 7 | (g & 0x1) << 6 | (b & 0x1) << 5
                if char_bits:
                    char = chr(char_bits)
                    message += char
                    if message[-3:] == "###":
                        return message[:-3]

        return "No message found"
