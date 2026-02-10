"""HolyC Language Tools"""
import re,json

class HolyCParser:
    KEYWORDS=["U0","U8","U16","U32","U64","I8","I16","I32","I64","F64",
              "Bool","if","else","while","for","switch","case","break",
              "return","class","public","extern","_extern","asm","lock"]
    BUILTINS=["Print","StrLen","StrCpy","StrCmp","MAlloc","Free","Sleep",
              "GrPrint","DocPrint","Snd","InU8","OutU8","Beep"]
    
    def tokenize(self,code):
        tokens=[]
        patterns=[
            ("COMMENT",r"//[^
]*"),("STRING",r'"[^"]*"'),
            ("NUMBER",r"\d+"),("IDENT",r"[A-Za-z_][A-Za-z0-9_]*"),
            ("OP",r"[+\-*/=<>!&|^~%]"),("PUNC",r"[{}\[\]();,.]"),
            ("WS",r"\s+"),
        ]
        combined="|".join(f"(?P<{n}>{p})" for n,p in patterns)
        for m in re.finditer(combined,code):
            kind=m.lastgroup
            if kind!="WS":
                val=m.group()
                if kind=="IDENT":
                    if val in self.KEYWORDS: kind="KEYWORD"
                    elif val in self.BUILTINS: kind="BUILTIN"
                tokens.append({"type":kind,"value":val,"pos":m.start()})
        return tokens
    
    def analyze(self,code):
        tokens=self.tokenize(code)
        stats={"keywords":0,"builtins":0,"identifiers":0,"strings":0,"comments":0,"numbers":0}
        for t in tokens: 
            if t["type"] in stats: stats[t["type"]]+=1
        functions=re.findall(r"(U0|U8|U16|U32|U64|I8|I16|I32|I64|F64|Bool)\s+(\w+)\s*\(",code)
        return {"token_count":len(tokens),"stats":stats,"functions":[{"return_type":r,"name":n} for r,n in functions]}

class TempleOSInfo:
    SPECS={"author":"Terry A. Davis","year":"2003-2017","language":"HolyC","kernel":"Single address space",
           "resolution":"640x480 16-color","features":["Ring 0 access","No networking","64-bit","JIT compiler",
           "Hymns","3D graphics","After Egypt game","DolDoc format"]}
    
    def get_info(self): return self.SPECS
