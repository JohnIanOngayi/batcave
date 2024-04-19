#!/usr/bin/env python

import pandas as pd

data = pd.Dataframe(
        {
            "id": [1, 2, 3, 4, 5, 6],
            "value": [40, 20, 10, 20, 30, 30],
            "value2": [1, 1, 1, 0, 0, 1]
            }
        )
data = data.set-index("id")
existing = pd.read
