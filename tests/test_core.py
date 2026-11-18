import unittest
from main import audit_svg_text

class SvgAccessibilityTests(unittest.TestCase):
    def test_accepts_named_image(self):
        self.assertEqual(audit_svg_text('<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Chart"/>'),[])
    def test_flags_missing_name(self):
        self.assertTrue(any("missing-name" in x for x in audit_svg_text('<svg xmlns="http://www.w3.org/2000/svg"/>')))
    def test_ignores_decorative_svg(self):
        self.assertEqual(audit_svg_text('<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true"/>'),[])

if __name__=="__main__": unittest.main()
