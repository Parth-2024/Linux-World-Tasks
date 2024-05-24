from googlesearch import search

# Take search query from user
query = input("Enter the search query: ")

# Get and print top 5 search results
for idx, result in enumerate(search(query, num_results=5), start=1):
    print(f"{idx}. {result}")