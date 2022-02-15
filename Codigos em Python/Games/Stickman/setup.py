import cx_Freeze

executables = [cx_Freeze.Executable("stckmn.py")]

cx_Freeze.setup(name = "Jogo do stickman",options = {"build_exe":{"packages" : ["pygame"],"include_files" : ["images"]}},executables = executables)