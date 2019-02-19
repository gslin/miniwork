#!/usr/bin/env python3

from confluent_kafka import Consumer, KafkaError
import sys

def main():
    c = Consumer({'bootstrap.servers': sys.argv[1], 'group.id': 'default'})
    c.subscribe(['test'])
    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print('Consumer error: {}'.format(msg.error()))
            continue

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()

if '__main__' == __name__:
    main()
