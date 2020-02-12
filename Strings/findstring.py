import re


# Window Sliding Technique
def count_substring(string, substring):
    return len([i for i in range(len(string)) if
                string[i:i + len(substring)] == substring])  # len(re.findall(f'(?={substring})', f'{string}'))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
