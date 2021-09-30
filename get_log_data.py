#Importing the modules
import re
import mysql.connector

#---------------------------
log_folder = "/var/log/rsyslog_remote/mikrotik/"
list_log_filename = [ "input.log", "output.log", "forward.log", "user.log", "log.log", "filter.log", "script.log" ]

#---------------------------
regex_input   = "([a-zA-Z0-9 :]+) (.+) input: in:(.+) out:(.+), src-mac (.+), proto ([a-zA-Z]+), (.+):([0-9]+)->(.+):([0-9]+), len ([0-9]+)"
regex_output  = "([a-zA-Z0-9 :]+) (.+) output: in:(.+) out:(.+), proto ([a-zA-Z]+), (.+):([0-9]+)->(.+):([0-9]+), len ([0-9]+)"
regex_forward = "([a-zA-Z0-9 :]+) (.+) forward: in:(.+) out:(.+), src-mac (.+), proto ([a-zA-Z]+), (.+):([0-9]+)->(.+):([0-9]+), len ([0-9]+)"
regex_user    = "([a-zA-Z0-9 :]+) (.+) user (.+)"
regex_log     = "([a-zA-Z0-9 :]+) (.+) log (.+)"
regex_filter  = "([a-zA-Z0-9 :]+) (.+) filter (.+)"
regex_script  = "([a-zA-Z0-9 :]+) (.+) script (.+)"

list_regex = [ regex_input, regex_output, regex_forward, regex_user, regex_log, regex_filter, regex_script ]

#---------------------------
name_input   = [ "DateTime", "DeviceName", "In", "Out", "src-mac", "Protocol", "src-ip", "src-port", "dst-ip", "dst-port", "len" ]
name_output  = [ "DateTime", "DeviceName", "In", "Out", "Protocol", "src-ip", "src-port", "dst-ip", "dst-port", "len" ]
name_forward = [ "DateTime", "DeviceName", "In", "Out", "src-mac", "Protocol", "src-ip", "src-port", "dst-ip", "dst-port", "len" ]
name_user    = [ "DateTime", "DeviceName", "UserInfo" ]
name_log     = [ "DateTime", "DeviceName", "LogInfo" ]
name_filter  = [ "DateTime", "DeviceName", "FilterInfo" ]
name_script  = [ "DateTime", "DeviceName", "ScriptInfo" ]

list_name = [name_input, name_output, name_forward, name_user, name_log, name_filter, name_script ]

#---------------------------

table_name = "logs_db"
#
mySQL_query_input = """ (DateTime, DeviceName, In_, Out_, src_mac, Protocol, src_ip, src_port, dst_ip, dst_port, len)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

#---------------------------
def get_log_data(select_name, select_regex, log_data):
    matches = re.finditer(select_regex, log_data, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        #print ("Match {matchNum}: {match}".format(matchNum = matchNum, match = match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            #print ("Group {groupNum}: {group}".format(groupNum = groupNum, group = match.group(groupNum)))
            print ("{name}: {group}".format(name = select_name[groupNum-1], group = match.group(groupNum)))

        print ("---------------")


#---------------------------

def insert_log_to_DB(select_table, select_name, select_regex, log_data):
  try:
      connection = mysql.connector.connect(
        host='localhost',
        database='users_db',
        user='root',
        password='root'
      )

      cursor = connection.cursor()
      mySQL_insert_query = "INSERT INTO " + select_table + mySQL_query_input

      print("Insert data to DB (table: " + table_name + ") ...")

      #Find data from source
      #log_data = []
      matches = re.finditer(select_regex, log_data, re.MULTILINE)
      for matchNum, match in enumerate(matches, start=1):
          for groupNum in range(0, len(match.groups())):
              print (match.group(groupNum))
              #log_data.append(match.group(groupNum))
          #record = tuple(log_data)
          #print (record)

          #cursor.execute(mySQL_insert_query, record)
          #connection.commit()

  except mysql.connector.Error as error:
      print("Failed to insert into MySQL table {}".format(error))

  finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#---------------------------
#---------------------------

index_file = 0

#Open log-file
log_file = open(list_log_filename[index_file] , "r")
print ("Select log-file: {}".format(list_log_filename[index_file]))

#Parse input log-file
#get_log_data(list_name[index_file], list_regex[index_file], log_file.read())
insert_log_to_DB("input", list_name[index_file], list_regex[index_file], log_file.read())

#---------------------------
