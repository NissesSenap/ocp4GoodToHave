# Sidecar

Old leagecy apps might be able to be rewritten to send logs out to std-out.
To solve this you can easily put in a sidecar.

Think of that you have to mount the volume between the two containers. The original one you want to read from and the side-car that will do the tail
