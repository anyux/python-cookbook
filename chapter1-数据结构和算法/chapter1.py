from collections import deque

def search(lines,pattern,histroy=5):
    previous_line= deque(maxlen=histroy)
    for line in lines:
        if pattern in line:
            yield line,previous_line
        previous_line.append(line)

if __name__ == '__main__':
    with open('input.txt','r') as f:
        for line,previous_line in search(f,'python',5):
            for pline in previous_line:
                print(pline,end='')
            print(line,end='')
            print('-'*20)