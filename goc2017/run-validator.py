#!/usr/bin/python

import sys, subprocess, threading, os

if len(sys.argv) < 3:
  print "usage: %s test-validator run [script [invocation]]" % (sys.argv[0])
  print "example: %s boxes/tests/1.validator go run boxes/dev/soln/main.go" % (
      sys.argv[0])
  sys.exit(1)

stdin1, stdout1 = os.pipe()
stdin2, stdout2 = os.pipe()

validator = subprocess.Popen(
    [sys.argv[1]], stdout=stdout1, stdin=stdin2, close_fds=True)

solution = subprocess.Popen(
    sys.argv[2:], stdout=stdout2, stdin=stdin1, close_fds=True)

os.close(stdin1)
os.close(stdin2)
os.close(stdout1)
os.close(stdout2)

if solution.wait() != 0:
  raise Exception("script failed")
if validator.wait() != 0:
  raise Exception("validation failed")

print "test passed"
