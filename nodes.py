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

NODE_CLASS_MAPPINGS = {
    "CenterCalculation": CenterCalculationNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CenterCalculation": "Center Calculation"
}
