from kybra import query

import iscc_core as iscccore

@query
def testIscccoreLib() -> str:
   # meta_code = iscc_core.gen_meta_code("test")
    # ic.print(f"Meta-Code:     {meta_code['iscc']}")
    # ic.print(f"Structure:     {iscc_core.iscc_explain(meta_code['iscc'])}\n")
    # ic.print("test Iscc Lib")
    return iscccore.gen_meta_code("test")
