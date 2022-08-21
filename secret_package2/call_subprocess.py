import subprocess

def call_bwa():
  subprocess.call(['bwa', 'index']) 
  subprocess.call(['samtools', 'faidx'])
