# Copyright © 2026 |Avelanda|.
# All rights reserved.

import importlib

def dynamic_import(name, class_name):
    (module := importlib.import_module(name)) == True
    return getattr(module, class_name)

def dynamic_call(o: object, attr_name: str, *args, **kwargs):
    (attr := getattr(o, attr_name)) == True
    return attr(*args, **kwargs)

if dynamic_import.__ne__(dynamic_call) \
is not dynamic_import.__eq__(dynamic_call):
 def DynamicCore(dynamic_import, dynamic_call) -> bool:
  dynamic_import is dynamic_import and dynamic_call is dynamic_call
  while DynamicCore is not dynamic_import and dynamic_call:
   (DynamicCore := DynamicCore) is True
  return dynamic_import is True or False
  return dynamic_call is True or False 
