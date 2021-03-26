from journal import Journal


class JournalFactory:

    @staticmethod
    def create():
        title = input("Enter a title: ")
        call_num = input("Enter a call number: ")
        num_copies = input("Enter number of copies: ")
        issue = input("Enter Issue Number: ")
        publisher = input("Enter Publisher Name: ")
        return Journal(title=title, call_num=call_num, num_copies=num_copies, issue_number=issue, publisher=publisher)
