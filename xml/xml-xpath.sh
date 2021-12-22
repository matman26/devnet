#!/bin/sh

# More info can be seen on the article https://www.baeldung.com/linux/evaluate-xpath
# Make sure you have libxml2 installed for xmllint

echo "-- Get all book items under /books"
xpath='/books'
output=$(xmllint --xpath $xpath dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get all books titles"
xpath='/books/book/title'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get books from category 'linux'"
xpath='/books/book[@category="linux"]'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get list of authors from books in category 'linux'"
xpath='/books/book[@category="linux"]/author'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get book whose id is 1"
xpath='/books/book[@id="1"]'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get title for books in french"
xpath='/books/book/title[@lang="fr"]'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get all data for books in french. Notice /.. goes up one 
   level in the tree"
xpath='/books/book/title[@lang="fr"]/..'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get author for books in french."
xpath='/books/book/title[@lang="fr"]/../author'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get books published after 2004. Notice we don't use the @
   symbol as we're not using a tag attribute."
xpath='/books/book[year>2004]'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"

echo "------------------------------------------------------------"
echo
echo "-- Get books titles from books published by George. Notice text()
   returns the text value inside the author tag, and contains checks
   whether or not 'George' is contained within the return of text()"
xpath='/books/book/author[contains(text(),"George")]/../title'
output=$(xmllint --xpath $xpath  dummy-data.xml)
echo -e "xpath = $xpath \n$output"
