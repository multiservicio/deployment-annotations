# Generate Grafana annotations type into InfluxDB for tracking events

In order to track events and been able to visualize them in [Grafana](http://docs.grafana.org/reference/annotations/), 
This script provides the functionality to create such events. 

## Requirements

- Influxdb Python -> https://github.com/influxdata/influxdb-python

## Usage

```
$ python annotations.py -h
usage: annotations.py [-h] [--title TITLE] [--description DESCRIPTION]
                      [--tags TAGS]

Create annotations in InfluxDB to be displayed in Grafana

optional arguments:
  -h, --help            show this help message and exit
  --title TITLE         Title of the annotation
  --description DESCRIPTION
                        Brief description of the annotation
  --tags TAGS           Comma separated tags for the annotation

```

Example: 

```
python annotations.py --title myTitle --description myDescription --tags hello,world
```

This will generate the following:

```
[{
	'measurement': 'deployments',
	'time': '2017-05-22T11:25:05.597294',
	'fields': {
		'title': 'myTitle',
		'description': 'myDescription',
		'tags': 'hello,world'
	}
}]
```

## Grafana annotations

To add the annotations just copy the image values. The query is

```
SELECT title, description, tags from deployments WHERE $timeFilter
```

<img src="images/annotations.png">


----------
Author: Pedro Diaz <pedro.diaz@tieto.com>