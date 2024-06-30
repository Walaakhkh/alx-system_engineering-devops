# using puppet to make changes to the defult ssh config file
# so that one can connect to a server without typing a password

include stdlib

file_line {
