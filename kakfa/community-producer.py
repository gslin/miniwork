#!/usr/bin/env python3

from kafka import KafkaProducer
import sys

def main():
    producer = KafkaProducer(bootstrap_servers=[sys.argv[1]], api_version=(0, 10, 1))

if '__main__' == __name__:
    main()
