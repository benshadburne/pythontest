#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Utilities for location."""

from collections import namedtuple


def known_region(region):
    """Returns true if this is a know region."""
    return region in region_to_endpoint


def get_endpoint(region):
    """Get the s3 website hosting endpoint for this region."""
    return region_to_endpoint[region]


Endpoint = namedtuple('Endpoint', ['name', 'host', 'zone'])

region_to_endpoint = {
    'us-east-2': Endpoint('US East (Ohio)',
                          'apigateway.us-east-2.amazonaws.com', 'ZOJJZC49E0EPZ'),
    'us-east-1': Endpoint('US East (N. Virginia)',
                          'apigateway.us-east-1.amazonaws.com', 'Z1UJRXOUMOOFQ8'),
    'us-west-1': Endpoint('US West (N. California)',
                          'apigateway.us-west-1.amazonaws.com', 'Z2MUQ32089INYE'),
    'us-west-2': Endpoint('US West (Oregon)',
                          'apigateway.us-west-2.amazonaws.com', 'Z2OJLYMUO9EFXC'),
    'ap-south-1': Endpoint('Asia Pacific (Mumbai)',
                           'apigateway.ap-south-1.amazonaws.com', 'Z3VO1THU9YC4UR'),
    'ap-northeast-3': Endpoint('Asia Pacific (Osaka-Local)**',
                               'apigateway.ap-northeast-3.amazonaws.com', 'Z2YQB5RD63NC85'),
    'ap-northeast-2': Endpoint('Asia Pacific (Seoul)',
                               'apigateway.ap-northeast-2.amazonaws.com', 'Z20JF4UZKIW1U8'),
    'ap-southeast-1': Endpoint('Asia Pacific (Singapore)',
                               'apigateway.ap-southeast-1.amazonaws.com', 'ZL327KTPIQFUL'),
    'ap-southeast-2': Endpoint('Asia Pacific (Sydney)',
                               'apigateway.ap-southeast-2.amazonaws.com', 'Z2RPCDW04V8134'),
    'ap-northeast-1': Endpoint('Asia Pacific (Tokyo)',
                               'apigateway.ap-northeast-1.amazonaws.com', 'Z1YSHQZHG15GKL'),
    'ca-central-1': Endpoint('Canada (Central)',
                             'apigateway.ca-central-1.amazonaws.com', 'Z19DQILCV0OWEC'),
    'cn-north-1': Endpoint('China (Beijing)',
                           'apigateway.cn-north-1.amazonaws.com.cn', 'None'),
    'cn-northwest-1': Endpoint('China (Ningxia)',
                               'apigateway.cn-northwest-1.amazonaws.com.cn', 'None'),
    'eu-central-1': Endpoint('EU (Frankfurt)',
                             'apigateway.eu-central-1.amazonaws.com', 'Z1U9ULNL0V5AJ3'),
    'eu-west-1': Endpoint('EU (Ireland)',
                          'apigateway.eu-west-1.amazonaws.com', 'ZLY8HYME6SFDD'),
    'eu-west-2': Endpoint('EU (London)',
                          'apigateway.eu-west-2.amazonaws.com', 'ZJ5UAJN8Y3Z2Q'),
    'eu-west-3': Endpoint('EU (Paris)',
                          'apigateway.eu-west-3.amazonaws.com', 'Z3KY65QIEKYHQQ'),
    'eu-north-1': Endpoint('EU (Stockholm)',
                           'apigateway.eu-north-1.amazonaws.com', 'Z2YB950C88HT6D'),
    'sa-east-1': Endpoint('South America (São Paulo)',
                          'apigateway.sa-east-1.amazonaws.com', 'ZCMLWB8V5SYIT'),
}
