import torch
import numpy as np
from PIL import Image
import base64
import io

class ETN_LoadMaskBase64:
    """
    A custom node for loading mask images from base64 data.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask": ("STRING", {"default": "", "multiline": True}),
            },
        }

    RETURN_TYPES = ("MASK",)
    RETURN_NAMES = ("mask",)
    FUNCTION = "load_mask"
    OUTPUT_NODE = False
    CATEGORY = "mask"

    def load_mask(self, mask):
        if not mask:
            # 如果没有提供 base64 数据，返回一个空白掩码
            empty_mask = np.zeros((64, 64), dtype=np.float32)
            return (torch.from_numpy(empty_mask),)

        try:
            # 解码 base64 数据
            image_data = base64.b64decode(mask)
            
            # 将二进制数据转换为 PIL Image
            mask_image = Image.open(io.BytesIO(image_data))
            
            # 转换为灰度图
            if mask_image.mode != 'L':
                mask_image = mask_image.convert('L')
            
            # 转换为 numpy 数组
            mask_array = np.array(mask_image).astype(np.float32) / 255.0
            
            # 转换为 PyTorch tensor
            mask_tensor = torch.from_numpy(mask_array)
            
            return (mask_tensor,)
            
        except Exception as e:
            print(f"Error loading mask: {str(e)}")
            # 发生错误时返回空白掩码
            empty_mask = np.zeros((64, 64), dtype=np.float32)
            return (torch.from_numpy(empty_mask),) 