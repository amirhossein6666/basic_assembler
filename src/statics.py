# memory instruction
MI = {"AND": ["0", "8"], "ADD": ["1", "9"], "LDA": ["2", "A"], "STA": ["3", "B"],
      "BUN": ["4", "C"], "BSA": ["5", "D"], "ISZ": ["6", "E"]}
# register instruction
RI = {"CLA": "7800", "CLE": "7400", "CMA": "7200", "CME": "7100", "CIR": "7080", "CIL": "7040", "INC": "7020",
      "SPA": "7010", "SNA": "7008", "SZA": "7004", "SZE": "7002", "HLT": "7001", "INP": "F800", "OUT": "F400",
      "SKI": "F200", "SKO": "F100", "ION": "F080", "IOF": "F040"}
PREUDOMSTRUCTION = ["ORG", "HEX", "DEC", "END"]
