import requests


def detect_cms(url):
    try:
        response = requests.get(url)
        if "wp-content" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mWordPress\033[0m\n\n")
        elif "Joomla" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mJoomla\033[0m")
        elif "Drupal" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mDrupal\033[0m")
        elif "typo3conf" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mTYPO3\033[0m")
        elif "app/code/core" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mMagento\033[0m")
        elif "var/cache" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mPrestaShop\033[0m")
        elif "content/themes" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mWordPress\033[0m")
        elif "themes/jupiter" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mJupiter\033[0m")
        elif "sites/default" in response.text:
            print(f"\033[1mThe website {url} is running on \033[92mDrupal\033[0m")
        elif "modules/system" in response.text:
            print(f"\033[1;31mThe website {url} is running on \033[92mDrupal\033[0m")
        else:
            print(f"\033[91mNo CMS detected on the website {url}\033[0m \n")
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31mError: {str(e)}\033[0m")

url = input("Enter the URL of the website to detect the CMS for: ")
detect_cms(url)