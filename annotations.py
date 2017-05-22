import os
import datetime
import argparse

from influxdb import InfluxDBClient

INFLUX_URL = os.environ['INFLUX_URL']
INFLUX_USER = os.environ['INFLUX_USER']
INFLUX_PASSWORD = os.environ['INFLUX_PASSWORD']
INFLUX_DB = os.environ['INFLUX_DB']


class Annotation:
    def __init__(self):
        self.timestamp = datetime.datetime.utcnow().isoformat()
        self.influx_client = InfluxDBClient(
            host=INFLUX_URL,
            port=8086,
            username=INFLUX_USER,
            password=INFLUX_PASSWORD,
            database=INFLUX_DB
        )

    def create(self, title, description, tags):
        return [{
            "measurement": "deployments",
            "time": self.timestamp,
            "fields": {
                "title": title,
                "description": description,
                "tags": tags
            }
        }]

    def send(self, annotation):
        self.influx_client.write_points(annotation)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create annotations in InfluxDB to be displayed in Grafana')
    parser.add_argument('--title', type=str,
                        help='Title of the annotation')
    parser.add_argument('--description', type=str,
                        help='Brief description of the annotation')
    parser.add_argument('--tags', type=str,
                        help='Comma separated tags for the annotation')

    args = parser.parse_args()

    event = Annotation()
    annotation = event.create(title=args.title, description=args.description, tags=args.tags)
    event.send(annotation)
    print("Sent: " + str(annotation))
