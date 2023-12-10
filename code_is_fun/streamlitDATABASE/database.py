from deta import Deta


DETA_KEY = "a04lqpjq_akNCVLnn18h2Yu4mQoL7c52eZN7Pjz1Z"

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("monthly_reports")


def insert_period(period, incomes, expenses, comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({
        "key": period,
        "incomes": incomes,
        "expenses": expenses,
        "comment": comment
    })

def fetch_all_periods():
    """Return a dict of all periods"""
    res = db.fetch()
    return res.items

def get_period(period):
    """If not found return None"""
    return db.get(period)
