import re
import argparse

def extract_urls_from_file(file_path):
    try:
        # Đọc nội dung file HTML
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Regular expression để tìm href
        pattern = r'href\s*=\s*["\']([^"\']+)["\']'
        urls = re.findall(pattern, html_content)

        # In các URL tìm được
        if urls:
            print("\nURL find in file:")
            print("--------------------")
            for url in urls:
                print(url)
        else:
            print("\nNot URLs found in file !")
            print("--------------------")
    except FileNotFoundError:
        print(f"\nFile is not exist! Please check file name: {file_path}")
    except Exception as e:
        print(f"\nError: {e}")

def main():
    # Cấu hình parser cho argument dòng lệnh
    parser = argparse.ArgumentParser(description="Tool to get URLs from 'href' in index.html file.")
    parser.add_argument("-f", "--file", required=True, help="Please input path file!")
    args = parser.parse_args()

    # Gọi hàm xử lý với file được chỉ định
    extract_urls_from_file(args.file)

if __name__ == "__main__":
    main()

