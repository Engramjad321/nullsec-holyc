from nullsec_holyc.core import HolyCParser,TempleOSInfo
p=HolyCParser()
code="U0 Main() { I64 i; for(i=0;i<10;i++) Print(\"Hello %d\\n\",i); }"
result=p.analyze(code)
print(f"Tokens: {result['token_count']}")
print(f"Functions: {result['functions']}")
t=TempleOSInfo()
print(f"\nTempleOS: {t.get_info()['author']}")
