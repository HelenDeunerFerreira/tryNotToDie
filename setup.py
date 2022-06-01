import cx_Freeze
executables = [cx_Freeze.Executable(
    script="main.py", icon="assets/logo.png")]

cx_Freeze.setup(
    name="try not to die",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets"]
                           }},
    executables=executables
)
