import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from nullsec_holyc.core import HolyCParser,TempleOSInfo

class TestParser(unittest.TestCase):
    def test_tokenize(self):
        p=HolyCParser()
        r=p.tokenize("U0 Main() { Print(\"Hello\"); }")
        self.assertTrue(any(t["type"]=="KEYWORD" for t in r))
    def test_analyze(self):
        p=HolyCParser()
        r=p.analyze("U0 Main() { I64 x=42; Print(\"Hi\"); }")
        self.assertGreater(r["token_count"],0)
        self.assertEqual(len(r["functions"]),1)

class TestTemplOS(unittest.TestCase):
    def test_info(self):
        t=TempleOSInfo()
        self.assertEqual(t.get_info()["author"],"Terry A. Davis")

if __name__=="__main__": unittest.main()
