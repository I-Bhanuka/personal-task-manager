class Expense:
    def __init__(self, amount, category, date, description=None):
        self._amount = amount
        self._category = category
        self._date = date
        self._description = description
        
    def to_dict(self):
        return {'amount':self._amount, 'category':self._category, 'date':self._date, 'description':self._description}
    

