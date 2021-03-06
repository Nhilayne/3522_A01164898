"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def get_highest_bid(self):
        return self._highest_bid

    def get_highest_bidder_name(self):
        return self._highest_bidder.name

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for bidder in self.bidders:
            if bidder is not self._highest_bidder:
                bidder(self, self._highest_bid)

    def accept_bid(self, bid, bidder):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid > self._highest_bid:
            self._highest_bidder = bidder
            self._highest_bid = bid
            self._notify_bidders()


class Bidder:

    def __init__(self, name, budget=100, bid_probability=0.35, bid_increase_perc=1.1):
        self.name = name
        self.bid_probability = bid_probability
        self.budget = budget
        self.bid_increase_perc = bid_increase_perc
        self.highest_bid = 0

    def __call__(self, auctioneer, highest_bid):
        bidding = random.random() < self.bid_probability
        if bidding is True:
            if highest_bid * self.bid_increase_perc <= self.budget:
                self.highest_bid = highest_bid * self.bid_increase_perc
                print(str(self.name) + " bids " + str(self.highest_bid))
                auctioneer.accept_bid(self.highest_bid, self)
            elif highest_bid < self.budget:
                self.highest_bid = self.budget
                print(str(self.name) + " bids " + str(self.highest_bid))
                auctioneer.accept_bid(self.highest_bid, self)

    def __str__(self):
        return self.name


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self._auctioneer = Auctioneer()
        for bidder in bidders:
            self._auctioneer.register_bidder(bidder)

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        self._auctioneer.accept_bid(start_price, None)
        print("------------------")
        print(self._auctioneer.get_highest_bidder_name() + " wins a brand new " + item + " with a bid of $" +
              str(self._auctioneer.get_highest_bid()))


def main():
    bidders = []

    # bidders.append(Bidder("Jojo", 3000, random.random(), 1.2))
    # bidders.append(Bidder("Melissa", 7000, random.random(), 1.5))
    # bidders.append(Bidder("Priya", 15000, random.random(), 1.1))
    # bidders.append(Bidder("Kewei", 800, random.random(), 1.9))
    # bidders.append(Bidder("Scott", 4000, random.random(), 2))

    while True:
        try:
            num_bidders = int(input("Please enter the number of bidders you would like to add: "))
            break
        except ValueError:
            print("Invalid input")

    for i in range(0, num_bidders):
        try:
            name = input("Please enter Bidder's name (string): ")
            budget = int(input("Please enter Bidder's budget (int): "))
            bid_percent = float(input("Please enter Bidder's bidding chance (float 0.0 - 1.0): "))
            bid_increase = float(input("Please enter Bidder's bid increase multiplier (float 1.0 or higher): "))
            bidders.append(Bidder(name, budget, bid_percent, bid_increase))
        except ValueError:
            print("Invalid Input detected. Generating John Doe Bidder")
            bidders.append(Bidder("John Doe #" + str(i), 1500, 0.33, 1.1))

    auction_item = input("What is being auctioned: ")
    try:
        starting_price = int(input("What is the starting bid: "))
    except ValueError:
        print("Invalid price detected, setting starting bid at 100")
        starting_price = 100

    print("\n\nStarting Auction for " + auction_item + "!!")
    print("------------------")
    print("Starting bid is " + str(starting_price))
    my_auction = Auction(bidders)
    my_auction.simulate_auction(auction_item, starting_price)


if __name__ == '__main__':
    main()
