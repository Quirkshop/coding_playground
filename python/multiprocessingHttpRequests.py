#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-laptop>
#
# Distributed under terms of the MIT license.

import concurrent.futures
import requests

URLS = [
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get',
        'http://httpbin.org/get'
]

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    print(f"Sending request to url: {url}")
    response = requests.get(url)
    return response.json()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))