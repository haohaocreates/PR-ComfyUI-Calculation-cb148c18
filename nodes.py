import io
import pyqrcode
from PIL import Image
from torchvision.transforms import ToTensor

class CenterCalculationNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "outer_with": ("INT", {"default": 0}),
                "outer_height": ("INT", {"default": 0}),
                "inner_with": ("INT", {"default": 0}),
                "inner_height": ("INT", {"default": 0}),
                "x_position": ("FLOAT", {"default": 0.0, "min": -1.0, "max": 1.0,}),
                "y_position": ("FLOAT", {"default": 0.0, "min": -1.0, "max": 1.0,}),
            },
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "INT", "INT", )
    RETURN_NAMES = ("outer_with", "outer_height", "inner_with", "inner_height", "inner_x", "inner_y", )

    FUNCTION = "center_calc"

    CATEGORY = "Calculation"

    def center_calc(self, outer_with: int, outer_height: int, inner_with: int, inner_height: int, x_position: float, y_position: float):
        center_x = (outer_with - inner_with) / 2
        center_y = (outer_height - inner_height) / 2
        center_x += x_position * center_x
        center_y += y_position * center_y
        return (outer_with, outer_height, inner_with, inner_height, int(center_x), int(center_y), )


class CreateQRCodeNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "content": ("STRING", {"default": ""}),
            },
            "optional": {
                "error": (["L", "M", "Q", "H"], {"default": "L"}),
                "version": ("INT", {"default": 3, "min": 1, "max": 40}),
                "mode": (["numeric", "alphanumeric", "kanji", "binary"], {"default": "binary"}),
                "encoding": ("STRING", {"default": "iso-8859-1"}),
                "scale": ("INT", {"default": 5, "min": 1}),
                "module_color_R": ("INT", {"default": 0, "min": 0, "max": 255}),
                "module_color_G": ("INT", {"default": 0, "min": 0, "max": 255}),
                "module_color_B": ("INT", {"default": 0, "min": 0, "max": 255}),
                "module_color_A": ("INT", {"default": 255, "min": 0, "max": 255}),
                "background_R": ("INT", {"default": 255, "min": 0, "max": 255}),
                "background_G": ("INT", {"default": 255, "min": 0, "max": 255}),
                "background_B": ("INT", {"default": 255, "min": 0, "max": 255}),
                "background_A": ("INT", {"default": 255, "min": 0, "max": 255}),
                "quiet_zone": ("INT", {"default": 4, "min": 0}),
            },
        }

    RETURN_TYPES = ("IMAGE", )

    FUNCTION = "create_qr_code"

    CATEGORY = "Calculation"

    def create_qr_code(self, 
                       content, error, version, mode, encoding, 
                       scale, module_color_R, module_color_G, module_color_B, module_color_A, 
                       background_R, background_G, background_B, background_A, quiet_zone):
        code = pyqrcode.create(content=content, error=error, version=version, mode=mode, encoding=encoding)
        img_io = io.BytesIO()
        code.png(img_io, scale=scale, 
                 module_color=(module_color_R, module_color_G, module_color_B, module_color_A), 
                 background=(background_R, background_G, background_B, background_A), quiet_zone=quiet_zone)
        img_io.seek(0)
        img_tensor = ToTensor()(Image.open(img_io))
        return (img_tensor, )


NODE_CLASS_MAPPINGS = {
    "CenterCalculation": CenterCalculationNode,
    "CreateQRCode": CreateQRCodeNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CenterCalculation": "Center Calculation",
    "CreateQRCode": "Create QR Code",
}

