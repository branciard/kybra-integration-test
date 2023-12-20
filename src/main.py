from kybra import query,ic,void

import iscc_core as iscccore

metaCodet= {}

@query
def test() -> void:
   ic.print("test call")
   meta_code = iscccore.gen_meta_code(name="ISCC Test Document!")
   ic.print(meta_code)
