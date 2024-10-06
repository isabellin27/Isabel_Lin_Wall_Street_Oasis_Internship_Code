__Web Scraping and Word Frequency Analysis Tool__

Overview:

This Python script fetches text data from a list of specified URLs, processes the text by removing common stop words and punctuation, and then calculates the frequency of each word. The script is particularly useful for analyzing the most common words in articles or text-heavy websites for SEO.

Features:
- Web scraping: Fetches HTML content from a list of URLs using the requests library.
- Text extraction: Uses BeautifulSoup to extract and clean text from the HTML content.
- Text processing: Converts text to lowercase, removes punctuation, and filters out common stop words.
- Word frequency analysis: Counts the occurrences of each word in the processed text.
- Word filtering: Filters out words that appear fewer than a specified number of times (e.g., less than 10).
- Formatted output: Prints the word frequencies in a table format, sorted in descending order.
Prerequisites
- To run this code, you'll need to have the following Python libraries installed: requests and beautifulsoup4 using pip:

How to use:
1. Edit the URL List: Update the urls list in the script to include the web pages you want to scrape. You can add or remove URLs as needed:

2. Adjust stop words: You can modify the list of common_words to exclude different stop words based on your specific needs.

3. Change word frequency threshold: To adjust the minimum number of occurrences a word must have to appear in the final table, change the value of min_count in the filter_words_by_count function:

4. Run the Script: After updating the URLs, you can run the script by executing the following command in your terminal: python script_name.py

5. View Results: The script will print a table showing the most frequent words from the scraped content that appear more than 10 times (this threshold can be adjusted in the filter_words_by_count function).

Word                Count     
------------------------------
income              52        
revenue             23        
earnings            15        
...
