#!/usr/bin/env python3
"""
HolyC Parser and Transpiler
Converts HolyC code to C for analysis.
"""

import re
import sys

class HolyCParser:
    """Parse HolyC source code."""
    
    # HolyC type mappings
    TYPE_MAP = {
        'U0': 'void',
        'I8': 'int8_t',
        'U8': 'uint8_t',
        'I16': 'int16_t',
        'U16': 'uint16_t',
        'I32': 'int32_t',
        'U32': 'uint32_t',
        'I64': 'int64_t',
        'U64': 'uint64_t',
        'F64': 'double',
        'Bool': 'bool',
    }
    
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.pos = 0
    
    def tokenize(self):
        """Tokenize HolyC source."""
        patterns = [
            ('COMMENT', r'//[^\n]*'),
            ('STRING', r'"[^"]*"'),
            ('NUMBER', r'\b\d+\b'),
            ('HEX', r'0x[0-9A-Fa-f]+'),
            ('IDENT', r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
            ('OP', r'[+\-*/=<>!&|^~%]'),
            ('DELIM', r'[(){}\[\];,:]'),
            ('WS', r'\s+'),
        ]
        
        combined = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns)
        
        for match in re.finditer(combined, self.source):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WS':
                self.tokens.append((kind, value))
    
    def transpile_to_c(self):
        """Convert HolyC to C."""
        output = []
        output.append('#include <stdint.h>')
        output.append('#include <stdbool.h>')
        output.append('#include <stdio.h>')
        output.append('')
        
        # Process tokens
        i = 0
        while i < len(self.tokens):
            kind, value = self.tokens[i]
            
            if kind == 'IDENT' and value in self.TYPE_MAP:
                # Type conversion
                output.append(self.TYPE_MAP[value])
            elif kind == 'COMMENT':
                output.append(value)
            else:
                output.append(value)
            
            i += 1
        
        return ' '.join(output)


def main():
    if len(sys.argv) < 2:
        print("Usage: holyc_parser.py <file.hc>")
        sys.exit(1)
    
    with open(sys.argv[1], 'r') as f:
        source = f.read()
    
    parser = HolyCParser(source)
    parser.tokenize()
    
    c_code = parser.transpile_to_c()
    print(c_code)


if __name__ == '__main__':
    main()
