from email.policy import default
import sortify
import sys

config = "default" if len(sys.argv) < 2 else sys.argv[1]
log = 1 if len(sys.argv) < 3 else sys.argv[2]
sortify.sort(config, log)