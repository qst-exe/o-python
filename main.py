import sys
import opai

def main():
    args = sys.argv
    p = opai.New(args[1])
    p.show()

if __name__ == '__main__':
    main()
