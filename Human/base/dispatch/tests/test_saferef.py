from dispatch.saferef import *

try:
    import unittest2 as unittest
except:
    import unittest


def Function(obj):
    pass


class Class(object):
    def __call__(self, obj):
        pass


class Classfunc(object):
    def x(self):
        pass


class TestSaferefForFunction(unittest.TestCase):
    def setUp(self):
        self.sources = []
        self.refs = []
        self.closureCount = 0
        for x in range(self.count):
            source = self.get_source()
            referant = self.get_referant(source)
            ref = safeRef(referant, self._closure)

            self.sources.append(source)
            self.refs.append(ref)

    def tearDown(self):
        del self.sources
        del self.refs

    def get_source(self):
        return Function

    def get_referant(self, source):
        # By default, referant == source
        return source

    @property
    def count(self):
        return 1

    def testIn(self):
        """Test the "in" operator for safe references (cmp)"""
        for source in self.sources[:50]:
            self.assertIn(
                safeRef(self.get_referant(source)),
                self.refs
            )

    def testValid(self):
        """Test that the references are valid (return instance methods)"""
        for ref in self.refs:
            self.assertTrue(ref())

    def testShortCircuit(self):
        """Test that creation short-circuits to reuse existing references"""
        sd = {}
        for ref in self.refs:
            sd[ref] = 1
        for source in self.sources:
            if hasattr(source, 'x'):
                # self.assertTrue(sd.has_key(safeRef(source.x)))
                self.assertTrue(safeRef(source.x) in sd)
            else:
                # self.assertTrue(sd.has_key(safeRef(source)))
                self.assertTrue(safeRef(source) in sd)

    def testRepresentation(self):
        """Test that the reference object's representation works
        
        XXX Doesn't currently check the results, just that no error
            is raised
        """
        repr(self.refs[-1])

    def _closure(self, ref):
        """Dumb utility mechanism to increment deletion counter"""
        self.closureCount += 1


class TestSaferefForClass(TestSaferefForFunction):
    def get_source(self):
        return Class()

    @property
    def count(self):
        return 3  # 30


class TestSaferefForClassfunc(TestSaferefForFunction):
    def get_source(self):
        return Classfunc()

    def get_referant(self, source):
        return source.x

    @property
    def count(self):
        return 5  # 5000


def getSuite():
    cases = [
        TestSaferefForFunction,
        TestSaferefForClass,
        TestSaferefForClassfunc,
    ]
    suite = unittest.TestSuite()
    for case in cases:
        suite.addTests(unittest.loadTestsFromTestCase(case))
    return suite


if __name__ == "__main__":
    unittest.main()
