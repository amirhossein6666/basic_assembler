# memory instruction
MI = {"AND": ["0", "8"], "ADD": ["1", "9"], "LDA": ["2", "A"], "STA": ["3", "B"],
       "BUN": ["4", "C"], "BSA": ["5", "D"], "ISZ": ["6", "E"]}
# register instruction
RI = {"CLA": 0x7800, "CLE": 0x7400, "CMA": 0x7200, "CME": 0x7100, "CIR": 0x7080, "CIL": 0x7040, "INC": 0x7020,
           "SPA": 0x7010, "SNA": 0x7008, "SZA": 0x7004, "SZE": 0x7002, "HLT": 0x7001, "INP": 0xF800, "OUT": 0xF400,
           "SKI": 0xF200, "SKO": 0xF100, "ION": 0xF080, "IOF": 0xF040}
PREUDOMSTRUCTION = ["ORG", "HEX", "DEC", "END"]
