import argparse
parser = argparse.ArgumentParser(description='Calculator')

parser.add_argument('num1', type=float, help='First number')
parser.add_argument('num2', type=float, help='Second number')
parser.add_argument('op', choices=["+", "-", "*"], help='Operation')

args = parser.parse_args()

if args.op == "+":
    result = args.num1 + args.num2
elif args.op == "-":
    result = args.num1 - args.num2
elif args.op == "*":
    result = args.num1 * args.num2


print(f'{args.num1} {args.op} {args.num2} = {result}')