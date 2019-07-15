import sys
import opai

def main():
    args = sys.argv
    # 女の子のお悩み相談解決ソリューションズ㈱（以下、オナソリュ）の提唱するフサフサをインスタンス名とする
    fusafusa = opai.New(args[1])
    fusafusa.show()

if __name__ == '__main__':
    main()
