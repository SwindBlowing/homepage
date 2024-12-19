from PIL import Image
import os

def convert_cmyk_to_rgb(directory):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 仅处理.jpg 和 .png 文件
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(directory, filename)
            try:
                # 打开图片
                with Image.open(file_path) as img:
                    # 检查是否是 CMYK 模式
                    if img.mode == 'CMYK':
                        print(f"Converting {filename} from CMYK to RGB...")
                        # 转换为 RGB 模式
                        rgb_img = img.convert('RGB')
                        # 保存回原文件（可以另存为避免覆盖）
                        rgb_img.save(file_path)
                        print(f"{filename} has been converted to RGB.")
                    else:
                        print(f"{filename} is already in {img.mode} mode.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# 替换为目标目录的路径
directory_path = "."
convert_cmyk_to_rgb(directory_path)
