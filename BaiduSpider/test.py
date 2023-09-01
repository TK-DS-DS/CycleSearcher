import requests
from bs4 import BeautifulSoup


def baidu_search(query, num_results=10):
    # 构建搜索URL
    search_url = f"http://www.baidu.com/s?wd={query}&pn=0"

    # 发起HTTP请求
    response = requests.get(search_url)

    print(response.text)

    # 检查响应状态码
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML页面
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取搜索结果
        results = []
        result_divs = soup.find_all('div', class_='result-op')
        # for result_div in result_divs[:num_results]:
        #     result = {}
        #     # title = result_div.h3.get_text()
        #     link = result_div.h3.a['href']
        #     # snippet = result_div.find('div', class_='c-abstract').get_text()
        #     # result['title'] = title
        #     result['link'] = link
        #     # result['snippet'] = snippet
        #     results.append(result)
        print(result_divs)

        return results
    else:
        print("Failed to retrieve search results.")
        return []


if __name__ == "__main__":
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of results you want: "))

    search_results = baidu_search(query, num_results)
    # print(search_results)
    if search_results:
        print(f"Top {len(search_results)} search results for '{query}':\n")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. {result['title']}")
            print(f"   Link: {result['link']}")
            print(f"   Snippet: {result['snippet']}\n")
    else:
        print("No search results found.")
