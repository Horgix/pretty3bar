# Pretty3bar

Smal program which takes i3status/py3status JSON output as stream input, and
print it on stdout. Rationale is being able to test without an X server running
and without touching local configuration

# How to use

  py3status -c ~/.i3status.conf -i /home/horgix/work/my-py3status-modules | ./pretty3bar.py
