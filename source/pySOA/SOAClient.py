import SOAPpy
#Connect to the server
server = SOAPpy.SOAPProxy("http://localhost:8080/")
swort= raw_input("Geben Sie ihr gesuchtes Thema ein: ")
suchwort= swort.strip()
print server.search(suchwort)
