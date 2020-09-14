def solution(new_id):
    answer = ''
    validChar = '0123456789abcdefghijklmnopqrstuwxyz_-.'
    # 1단계
    new_id = new_id.lower()
    tmp = ''
    # 2단계
    for ch in new_id:
        if ch in validChar:
            tmp += ch
    # 3단계
    new_id = tmp
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if len(new_id) >= 2:
        if new_id[0] == '.' and new_id[-1] == '.':
            new_id = new_id[1:-1]
        elif new_id[0] == '.':
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:-1]
    else:
        if new_id[0] == '.':
            new_id = ''
    # 5단계
    if new_id == '':
        new_id += 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15] if new_id[14] != '.' else new_id[:14]
    elif len(new_id) <= 2:
        # 7단계
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id
    return answer


if __name__ == '__main__':
    print(solution('a.'))