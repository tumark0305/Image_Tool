import os,subprocess
from tqdm import tqdm

class Image_Tool:
    def __init__(self):
        self.current_path = f"{os.getcwd()}".replace("\\","/")
        self.home_path = os.path.expanduser("~").replace("\\","/")
        self.desktop_path = f"{self.home_path}/Desktop"
    @staticmethod
    def NEF_convert_TIFF(_in,_out):
        cmd = [
            "darktable-cli",  # 使用完整路徑
            _in,
            _out,
            "--core",
            "--conf","plugins/imageio/format/tiff/bpp=16",
            "--conf","plugins/imageio/format/tiff/compress=0",
            "--conf","plugins/imageio/format/tiff/shortfile=0",
        ]
        try:
            subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.DEVNULL,  # 隱藏標準輸出
                stderr=subprocess.DEVNULL   # 隱藏錯誤輸出
            )
        except subprocess.CalledProcessError as e:
            print(f"fail: {_in},error: {e}")
        return None
    def Nikon_all_toTIFF(self):
        print(self.desktop_path)
        _input_dir = f"{self.desktop_path}/DCIM"
        #_dir_name = input("input file name: date event >>>")
        _dir_name = "0504_PF42"
        _output_dir = f"{self.desktop_path}/{_dir_name}"
        os.makedirs(f"{_output_dir}", exist_ok=True)
        for _sub_dir in os.listdir(_input_dir):
            os.makedirs(f"{_output_dir}/{_sub_dir}", exist_ok=True)
            for _file in tqdm(os.listdir(f"{_input_dir}/{_sub_dir}"),desc=f"Working on folder {_sub_dir}"):
                if _file.lower().endswith(".nef"):
                    _input_path = f"{_input_dir}/{_sub_dir}/{_file}"
                    _file_name = os.path.splitext(_file)[0] + ".tiff"
                    _output_path = f"{_output_dir}/{_sub_dir}/{_file_name}"
                    Image_Tool.NEF_convert_TIFF(_input_path,_output_path)
        return None