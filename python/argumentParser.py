import argparse

def parse_args():
    """
    python run.py model [--test/-t]
    if --test is defined, isTest = True
    """
    description = "Add model name to start to make the prediction.['lgb','rf','gbdt'] are supported now."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('model', metavar='MODEL')
    parser.add_argument('-t',
                        '--test',
                        dest='isTest',
                        action='store_true',
                        help='Is testing or not')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    print(args.model)
    print(args.isTest)


