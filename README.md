# PathStatusChecker
As a penetration tester, your goal is to identify and assess vulnerabilities in a system to help improve its security. The script designed to check specific paths on a list of URLs for a 200 HTTP status code.

# Scenario: Identifying Sensitive Paths and Misconfigurations

Let's say you are conducting a penetration test on a web application or a network of web servers. During the initial reconnaissance phase, you've gathered a list of potential targets (URLs) associated with the target organization. Your objective is to identify sensitive paths or misconfigurations that could pose security risks.

    Sensitive Paths Detection:

    The script comes into play when you want to check if certain sensitive paths, such as documentation (/docs, /redoc), API endpoints (/api/*), or potentially exploitable paths (/php.info), exist on the target URLs.

    Automated Assessment:

    The script automates the process of checking multiple paths on multiple URLs, saving time and allowing you to focus on analyzing the results. This is crucial, especially when dealing with a large number of URLs.

    Focus on 200 Status Codes:

    By focusing on URLs that return a 200 HTTP status code, the script filters out irrelevant paths and helps you concentrate on potential points of interest. It reduces noise in the results, making your analysis more efficient.

    Documentation and Reporting:

    After running the script, you get a clear list of URLs with sensitive paths and a 200 status code. This information is valuable for documentation and reporting, as it highlights potential security risks and areas that may require further investigation.

    Client Communication:

    When communicating your findings to the client, you can provide concrete examples of sensitive paths that were discovered. This not only demonstrates the impact of potential misconfigurations but also assists in explaining the importance of addressing these issues.

    Risk Mitigation Recommendations:

    Based on the results, you can recommend mitigation strategies and best practices to the client, such as securing sensitive paths, restricting access, or implementing proper authentication mechanisms.

In summary, the script serves as a valuable tool for automating a specific aspect of the reconnaissance phase, allowing you to efficiently identify potential security risks and provide actionable insights to improve the overall security posture of the target environment.


# URL Checker Script

## Overview

This Python script checks a list of URLs for specific paths and outputs the URLs with a 200 HTTP status code to a text file. It is designed to identify potentially sensitive paths on web servers.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- `colorama` library (`pip install colorama`)

## Usage

1. Clone the repository or download the script.
2. Install the required libraries using the following command:
   ```bash
   pip install requests colorama
   ```

## Configuration

    Modify the file_path variable to the full path of your file containing URLs.
    Modify the output_file_path variable to the desired path for the output file.
    Adjust the paths_to_check list to include or exclude specific paths.

## Example

If you have a file named urls.txt containing the following 
URLs:example.com
test.com 

https://example.com/api/postman-collection
https://test.com/redoc


## Notes

    Make sure to replace placeholder values in the script with your actual file paths and URLs.
    Use caution when checking URLs, especially on external servers, to avoid unintended consequences.
    The script uses the requests library to make HTTP requests, so ensure your environment allows internet access.

