
'''
Function demonstrating basic file write.
Considering this non-safe as it will overwite any existing files
'''
def nonSafeFileWrite():
    with open('unsafeWrite.txt', 'w') as handle:
        #Should remove empty lines: (len) > 1 not true for '' empty lines
        handle.writelines(line for line in open('example.txt') if len(line) > 1)

    # Verify it works
    with open('unsafeWrite.txt') as f:
        lines = f.readlines()

        print(lines)


def saferFileWrite():
    # 'x' fails if the file already exists, preventing overwriting of file on accident
    with open('saferFileWrite.txt', 'x') as handle:
        handle.writelines(line for line in open('example.txt') if len(line) > 1)

    with open('saferFileWrite.txt') as f:
        lines = f.readlines()

        print(lines)

        #print(x.rstrip() for x in lines) Returns generator rather than printing the list elements


    

if __name__ == '__main__':
    nonSafeFileWrite()
    saferFileWrite()