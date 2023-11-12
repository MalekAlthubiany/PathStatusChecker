import os
import requests
from colorama import init, Fore, Style

# Initialize colorama for colored output
init()


def colored_status_code(status_code):
    if status_code == 200:
        return f"{Fore.GREEN}{status_code}{Style.RESET_ALL}"
    elif status_code == 404:
        return f"{Fore.RED}{status_code}{Style.RESET_ALL}"
    else:
        return str(status_code)


def check_status(url):
    try:
        response = requests.get(url, verify=False)
        return response.status_code
    except requests.RequestException as e:
        return -1


def main():
    # Replace 'urls.txt' with the actual file name containing URLs
    file_path = '~/Desktop/urls.txt' #1 --- > Modify this 
    output_file_path = '~/Desktop/wp-sitemap.xml.txt'  #2 --- >Modify this 

    # Expand the user directory for proper file paths
    file_path = os.path.expanduser(file_path)
    output_file_path = os.path.expanduser(output_file_path)

    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]

     paths_to_check = ['/doc', '/redoc', '/api/redocs', '/php.info', '/docs', '/api.docs', '/v3/api-docs',
                      '/v1/api-docs', '/v2/api-docs', '/api/redoc', 'api/v1/datasets', '/api/version', '/api/v2',
                      '/api/v1', '/api/postman', '/api/redoc-ui', '/api/swagger-ui', '/api/openapi', '/api/swagger',
                      '/api/postman-collection', '/api/graphql', '/api/graphql-playground'] #3 --- > Modify this

    urls_200 = set()  # Use a set to store unique URLs with 200 status code

    for url in urls:
        https_url = f"https://{url}"
        print(f"\nChecking URLs for {https_url}:")
        url_200_found = False

        for path in paths_to_check:
            full_url = https_url + path
            status_code = check_status(full_url)
            print(f"{full_url} returned {colored_status_code(status_code)}")

            if status_code == 200:
                url_200_found = True
                urls_200.add(full_url)  # Use add() for sets

        if url_200_found:
            print(f"{https_url} has at least one path with a 200 status code")

    # Save unique URLs with 200 status code to a text file on the desktop
    with open(output_file_path, 'w') as output_file:
        for url in urls_200:
            output_file.write(f"{url}\n")


if __name__ == "__main__":
    main()
