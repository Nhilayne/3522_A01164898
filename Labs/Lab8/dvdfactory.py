from dvd import DVD


class DVDFactory:

    @staticmethod
    def create():
        title = input("Enter a title: ")
        call_num = input("Enter a call number: ")
        num_copies = input("Enter number of copies: ")
        release = input("Enter Release Date: ")
        region = input("Enter Region Code: ")
        return DVD(title=title, call_num=call_num, num_copies=num_copies, date=release, region=region)
