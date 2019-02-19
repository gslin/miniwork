#!/usr/bin/env python3

from kafka import KafkaConsumer
import sys

def main():
    consumer = KafkaConsumer('test', bootstrap_servers=[sys.argv[1]], request_timeout_ms=1000)
    for msg in consumer:
        print('%s:%d:%d key=%s value=%s' % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))

if '__main__' == __name__:
    main()
