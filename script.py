import globalsettings  
from libTstPyPaths import module

print("A Global var: {}".format(globalsettings.EX_VAR))

print("SCRIPT - prj_files.dir_root = {}".format(globalsettings.prj_files.dir_root))
module.tst_fun()

print("SCRIPT - prj_files.dir_data  = {}".format(globalsettings.prj_files.dir_data))
print("SCRIPT - prj_files.dir_raw   = {}".format(globalsettings.prj_files.dir_raw))
print("SCRIPT - prj_files.dir_clean = {}".format(globalsettings.prj_files.dir_clean))

print("SCRIPT - prj_settings.dir_clean = {}".format(globalsettings.prj_const.my_pi))

print("SCRIPT - prj_cfg.dir_clean = {}".format(globalsettings.prj_cfg.compression))