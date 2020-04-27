Pipeline:

url -> feed -> titles with articles -> with title hashes
 -> filter out seen ones -> add remaining ones to db
 -> classify -> sort by classification -> output to screen

fetch_feed(url)
parse_feed()
hash_titles()
remove_seen()
fetch_bodies()
classify()
sort()
output()
mark_new_as_seen()
