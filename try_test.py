file_name="test.csv"
default_file="data.csv"

try:
    file=open(file_name)
except IOError:
    file=open(default_file)
except:
    print 'There was some other problem'
    
print file.readline()
