import city_processor
import threading
import time


class CityOverheadTimeQueue:
    def __init__(self):
        self._data_queue = list()
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        with self.access_queue_lock:
            self._data_queue.insert(0, overhead_time)
        # add to queue
        # accept overhead_time and append to data_queue list

    def get(self) -> city_processor.CityOverheadTimes:
        with self.access_queue_lock:
            data = self._data_queue[0]
            del self._data_queue[0]
            return data
        # remove an element from queue
        # queues are FIFO
        # get index 0 and use del

    def __len__(self) -> int:
        with self.access_queue_lock:
            return self._data_queue.__len__()
        # return length of data_queue


class ProducerThread(threading.Thread):

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super(ProducerThread, self).__init__()
        self._city_list = cities
        self._queue = queue

    def run(self) -> None:
        sleep_counter = 0
        for city in self._city_list:
            self._queue.put(city_processor.ISSDataRequest.get_overhead_pass(city))
            sleep_counter += 1
            if sleep_counter % 5 == 0:
                time.sleep(1)
        # executes when thread starts
        # loop over each city and add the city to the queue
        # after reading 5 cities sleep 1 second


class ConsumerThread(threading.Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        super(ConsumerThread, self).__init__()
        self._queue = queue
        self.data_incoming = True

    def run(self) -> None:
        while self.data_incoming or self._queue.__len__() > 0:
            if self._queue.__len__() < 1:
                time.sleep(0.75)
            data = self._queue.get()
            print(data)
            time.sleep(0.5)


def main():
    cities = city_processor.CityDatabase("city_locations.xlsx").city_db

    city_third = int(cities.__len__()/3)

    cities1 = cities[0: city_third]
    cities2 = cities[city_third+1: city_third*2]
    cities3 = cities[city_third*2+1: cities.__len__()]
    queue = CityOverheadTimeQueue()

    producer_one = ProducerThread(cities1, queue)
    producer_two = ProducerThread(cities2, queue)
    producer_three = ProducerThread(cities3, queue)
    consumer = ConsumerThread(queue)

    producer_one.start()
    producer_two.start()
    producer_three.start()

    consumer.start()

    producer_one.join()
    producer_two.join()
    producer_three.join()
    consumer.data_incoming = False


if __name__ == '__main__':
    main()
