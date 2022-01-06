import pytest
import pandas as pd
import keydecompose

class TestKeyHelper:
    self.frame = pd.DataFrame()

    # generate weighted series tests
    def test_weighted_non_unique(self):
