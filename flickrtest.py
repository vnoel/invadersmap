#!/usr/bin/env python
#encoding:utf-8

# if proxy is needed
# export HTTP_PROXY='129.104.38.6:8080'

import flickrapi
from flickrapi import FlickrError

api_key = 'e298505a9f7974fd63613f6112449754'

flickr = flickrapi.FlickrAPI(api_key)

sets = flickr.photosets_getList(user_id='51035596640@N01')

psets = sets.find('photosets').findall('photoset')

for pset in psets:
    title = pset.find('title').text
    if 'Space Invaders' in title:
        print 'Found space invaders set'    
        si_id = pset.attrib['id']

photos = flickr.photosets_getPhotos(api_key=api_key, photoset_id=si_id)
print len(photos[0])
photolist = photos[0].findall('photo')

noloc = 0

for photo in photolist:
    pid = photo.attrib['id']
    try:
        geoinfo = flickr.photos_geo_getLocation(api_key=api_key, photo_id=pid)
        location = geoinfo[0][0]
        print location.attrib['longitude'],' ', location.attrib['latitude'],',', photo.attrib['title']
    except FlickrError:
        # print photo.attrib['title'], 'photo has no location information'
        noloc += 1
        
        
print len(photolist), ' photos'
print noloc, ' photos without location info'
    
