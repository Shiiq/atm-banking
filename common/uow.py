

class UnitOfWork:

    def __int__(self, session, customer_rep, account_rep):
        self.session = session
        self.customer_rep = customer_rep
        self.account_rep = account_rep

    pass
