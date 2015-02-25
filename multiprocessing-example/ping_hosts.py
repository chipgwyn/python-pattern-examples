#!/usr/bin/env python

import time
from subprocess import PIPE,Popen
from multiprocessing.dummy import Pool as ThreadPool 

def runCommand(args):
  p = Popen(args, stdout=PIPE, stderr=PIPE)
  out, err = p.communicate()
  return out

def pingHost(host):
  args = ['ping', '-c', '10', host]
  return runCommand(args)

def importHosts(filename):
  hosts = []
  with open(filename, 'r') as f:
    for line in f:
      if '.' in line:
        line = line.rstrip()
        hosts.append(line)
  return hosts

def getHost(linesFromPing):
  return linesFromPing[0].split()[1]

def getStats(linesFromPing, type):
  """ types are min/avg/max/stddev """
  statLine = linesFromPing[-2]
  statLineParts = statLine.split()
  statTypes = statLineParts[1].split('/')
  statMeasurements = statLineParts[3].split('/')
  stats = dict(zip(statTypes,statMeasurements))
  return stats[type]

def printResults(results):
  for pingSession in results:
    lines = pingSession.split('\n')
    host = getHost(lines)
    avg  = getStats(lines, 'avg')
    print 'Host: {}, Avg Response: {}'.format(host, avg)


if __name__ == '__main__':

  print "Ping 3 hosts 10 times"
  hosts = importHosts('hosts.lst')
  
  # Parallel Version:
  startTime = time.time()
  print "Running in parallel..."
  pool = ThreadPool() 
  results = pool.map(pingHost, hosts)
  pool.close()
  pool.join()
  printResults(results)
  print 'Took {:.2f} seconds'.format(time.time() - startTime)

  # Non-parallel Version:
  startTime = time.time()
  print "Running one at a time..."
  results = map(pingHost, hosts)
  printResults(results)
  print 'Took {:.2f} seconds'.format(time.time() - startTime)
