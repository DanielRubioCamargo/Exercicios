from importlib.resources import Package
import cx_Freeze

executables = [cx_Freeze.Executable("dino.py")]

cx_Freeze.setup(name = "Jogo do dinossaurinho",options = {"build_exe":{"packages" : ["pygame"],"include_files" : ["imagens","sons"]}},executables = executables)