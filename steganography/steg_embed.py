from PIL import Image

class SteganographyEmbed:
    @staticmethod
    def encode(image_path, message, output_path):
        img = Image.open(image_path)
        encoded_img = img.copy()
        width, height = img.size
        idx = 0

        message += '###'  # Delimiter to indicate the end of the message

        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))

                if idx < len(message):
                    ascii_value = ord(message[idx])
                    new_r = (r & 0xFE) | ((ascii_value >> 7) & 0x1)
                    new_g = (g & 0xFE) | ((ascii_value >> 6) & 0x1)
                    new_b = (b & 0xFE) | ((ascii_value >> 5) & 0x1)
                    encoded_img.putpixel((col, row), (new_r, new_g, new_b))
                    idx += 1
                else:
                    encoded_img.putpixel((col, row), (r, g, b))

        encoded_img.save(output_path)
        return output_path
