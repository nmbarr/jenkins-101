import argparse

def hello(name="World"):
    return "Hello %s!" % name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hello greeting script')
    parser.add_argument('name', nargs='?', default='World', help='Name to greet (default: World)')
    args = parser.parse_args()
    
    result = hello(args.name)
    print(result)