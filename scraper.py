# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://beta.companieshouse.gov.uk/company/04503188")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)

# Select a tag on the page
name = root.cssselect('title')

# print the title
for companyname in name:
    print companyname.text

# Find a second thing
index = root.cssselect('dt')

for companyindex in index:
    print companyindex.text
    
record = { "companyindex" : companyindex.text } # column name and value
scraperwiki.sqlite.save(["companyindex"], record) # save the records one by one

# Find a third thing
address = root.cssselect('dd')

for companyaddress in address:
    print companyaddress.text
    



# # # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
# #
# # # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# # You don't have to do things with the ScraperWiki and lxml libraries.
# # You can use whatever libraries you want: https://morph.io/documentation/python
# # All that matters is that your final data is written to an SQLite database
# # called "data.sqlite" in the current working directory which has at least a table
# # called "data".
