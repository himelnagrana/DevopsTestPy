__author__ = 'himel'

import urllib
import ftplib
import urlparse
import argparse
import os
import time


class Fileviahttp():  # http downloader class
    def downloadfile(self, feedurl, outputdirectory, filewithextension):
        urllib.urlretrieve(feedurl, outputdirectory + filewithextension)    # downloading and saving the file
        return ''


class Fileviaftp():  # ftp downloader class
    def downloadfile(self, feedurl, outputdirectory, filewithextension):
        ftp = ftplib.FTP()
        ftp.retrbinary('RETR %s' % feedurl, outputdirectory + filewithextension)    # downloading and saving the file
        return ''


class Downloadfactory():  # Factory class for selecting downloader depending on protocol
    def downloadandsave(self, feedurl, outputdirectory):
        path, filewithextension = os.path.split(feedurl)  # getting the file extension with name
        protocol = urlparse.urlparse(feedurl).scheme    # getting the protocol from file url

        if protocol == 'http' or protocol == 'https':
            httpdownloader = Fileviahttp()    # http downloader class
            httpdownloader.downloadfile(feedurl, outputdirectory, filewithextension)
        elif protocol == 'ftp':
            ftpdownloader = Fileviaftp()    # ftp downloader class
            ftpdownloader.downloadfile(feedurl, outputdirectory, filewithextension)

        return outputDirectory+filewithextension


class Helper():
    def log(self, status, source, destinationfile):
        now = (time.strftime("%Y-%m-%d %H:%M:%S"))

        if status == 'success':
            logtext = "[" + now + "] source:" + source + " destination:" + destinationfile + "\r\n"
        else:
            logtext = "[" + now + "] source:" + source + " already downloaded\r\n"

        f = open('process.log', 'a+')   # process log is the log for the whole process
        f.write(logtext)
        f.close()

        f2 = open('file.log', 'a+')     # file log is the log file which stores file url on successful download
        f2.write(source)
        f2.close()


    def checkfile(self, feedurl):
        logfile = 'file.log'
        if os.path.isfile(logfile) and os.access(logfile, os.R_OK):     # checking if file exists
            with open(logfile) as f:    # checking file exists or not
                for line in f:
                    if line == feedurl:  # checking if the url is entered anytime or not
                        return True

            return False
        else:
            f = open('process.log', 'a+')
            f.close()
            return False







# Getting input for feed and output directory
parser = argparse.ArgumentParser()
parser.add_argument('--feed')
parser.add_argument('--output')

args = parser.parse_args()
feedUrl = args.feed
outputDirectory = args.output

# Checking if the same file is downloaded previously
helper = Helper()
filexist = helper.checkfile(feedUrl)

if filexist:
    # file exists - so log and show user a msg
    helper.log('failure', feedUrl, '')  # logging
    print "File already downloaded"

else:
    # file doesn't exist
    downloader = Downloadfactory()  # instantiating the factory class
    filename = downloader.downloadandsave(feedUrl, outputDirectory)
    helper.log('success', feedUrl, filename)  # logging
    print "File downloaded and saved successfully"
