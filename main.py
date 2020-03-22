from file import AddressFile
from formatter import PostcodeFormatter
from thread import AddressViaCepCrawlerThreadFactory, AddressWidenetCrawlerThreadFactory, AddressFSOACrawlerThreadFactory
import time

THREADS_LIMIT = 100
SLEEP_TIME = 10
FIRST_CEP = int(1001000)
THREAD_FACTORY = AddressFSOACrawlerThreadFactory

listed_addresses = AddressFile.list()

counter = 0
for postcode in range(FIRST_CEP, int(''.rjust(8, '9'))):
    if postcode not in listed_addresses:
        THREAD_FACTORY.run(
            PostcodeFormatter.postcode(postcode)
        )
        counter += 1

        if counter > 0 and counter % (THREADS_LIMIT + 1) == THREADS_LIMIT:
            time.sleep(SLEEP_TIME)
