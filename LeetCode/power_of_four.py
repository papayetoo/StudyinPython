import re
def solution(num: int):
    num_to_bin = f'{num:b}'
    return True if re.fullmatch('^1(00)*', num_to_bin) is not None else False

if __name__ == '__main__':
    num = int(input())
    print(solution(num))