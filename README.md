# Program I made for my co-worker and myself to speed up process of
# uploading pictures to the company's database.
# Previous process requaired to upload photos to the website,
# uploading them back, cutting the suffix from file name that website
# added, cropping the picture and adding (if necessary) numbers for
# parts on bottom of the picture. All of this had to be done manually
# and one by one (to some extent obviously).
#
# This program speed up our process and only part that still needs to
# be done manually and on one by one basis is uploading pictures to
# server.
#
# NOTE: For now the files in use are Parts.py (main script) and
# Test_Parts.py (contains functions for adding the parts numbers).
# The program adds numbers to the bottom of the pictures by looking at
# how file name ends for example if it ends on p2 that indicates 2 parts
# article, p3 means 3 part article. this works up to 6 parts as I
# simply don't need more.