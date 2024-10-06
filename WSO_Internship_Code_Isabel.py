# Import necessary libraries
import os
import requests
from bs4 import BeautifulSoup

def fetch_all_text(urls, headers):
    """Fetches and combines text content from a list of URLs."""
    all_text_content = ''
    for url in urls:
        response = requests.get(url, headers=headers)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the website
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract text content from the website
            text_content = soup.get_text()
            # Append the text content to the all_text_content string
            all_text_content += text_content + ' '  # Add a space to separate articles
            print(f'Successfully fetched content from: {url}')
        else:
            print(f'Failed to retrieve content from: {url}')
    return all_text_content

def process_text(text, stop_words):
    """Processes text by converting to lowercase, removing punctuation, and splitting into words."""
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~+-=|''' 
    for p in punctuation:
        text = text.replace(p, '')
    # Split text into words
    words = text.split()
    # Exclude stop words
    words = [word for word in words if word not in stop_words]
    return words

def count_word_frequencies(words):
    """Counts the frequency of each word in the list."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def filter_words_by_count(word_counts, min_count):
    """Filters words that appear more than min_count times."""
    over_threshold = [(word, count) for word, count in word_counts.items() if count > min_count]
    return over_threshold

def print_word_counts(word_counts):
    """Prints the word counts in a formatted table."""
    # Sort the list by count in descending order
    word_counts.sort(key=lambda x: x[1], reverse=True)
    # Print the table header
    print('-' * 30)
    print(f'{"Word":<20}{"Count":<10}')
    print('-' * 30)
    # Print each word and its count
    for word, count in word_counts:
        print(f'{word:<20}{count:<10}')

def main():
    # Define a list of common words to exclude
    common_words = [
        'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an',
        'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being',
        'below', 'between', 'both', 'but', 'by', 'can', 'could', 'did', 'do', 'does',
        'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had',
        'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him',
        'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself',
        'just', 'like', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not',
        'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours',
        'ourselves', 'out', 'over', 'own', 'same', 'she', 'should', 'so', 'some',
        'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves',
        'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too',
        'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when',
        'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'would', 'you',
        'your', 'yours', 'yourself', 'yourselves', 'also', 'than', 'then', 'do',
        'its', 'over', 'only', 'will', 'does', 'did', 'because', 'any', 'having',
        'both', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
        'can', 'cannot', 'could', 'would', 'should', 'might', 'must', 'shall', 'may'
    ]

    # Define a list of URLs to scrape = can add more
    urls = [
        'https://www.wallstreetoasis.com/resources/skills/finance/income',
        'https://www.investopedia.com/terms/i/income.asp',
        'https://corporatefinanceinstitute.com/resources/accounting/income-vs-revenue-vs-earnings/',
        'https://www.bea.gov/data/income-saving/personal-income',
        'https://www.dictionary.com/browse/income'
    ]

    # Define headers with a user-agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/58.0.3029.110 Safari/537.3'
    }

    # Fetch and combine text from all URLs
    all_text_content = fetch_all_text(urls, headers)

    # Process the text
    words = process_text(all_text_content, common_words)

    # Count word frequencies
    word_counts = count_word_frequencies(words)

    # Filter words that appear more than 10 times
    over_10 = filter_words_by_count(word_counts, 10)

    # Print the word counts
    print_word_counts(over_10)

if __name__ == '__main__':
    main()
