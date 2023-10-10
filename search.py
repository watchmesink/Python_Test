import webbrowser as wb

query = input("input your query ")
query.replace(' ', '+')
wb.open('https://www.google.com/search?q=' + query)

