class MockDBHelper:

    def connect(self, database='crimemap'):
        pass

    def get_all_inputs(self):
        return []

    def add_input(self):
        pass

    def clear_all(self):
        pass

    def add_crime(self, category, date, latitude, longtitude,
            description):
        pass

    def get_all_crimes(self):
        return [{
            'latitude': 42.217654242281405,
            'longtitude': 43.97156920053156,
            'date': '2020-03-01',
            'category': 'mugging',
            'description': 'mock description',
        }]
