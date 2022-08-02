import argparse
import os






















if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--test_only",
        action="store_true",
        help="if true, will load the trained model and run test only",
    )
    parser.add_argument(
        "--convert_bpe",
        action="store_true",    #这种你只要不明确写出来，就不是true值
        help="if true, will convert the bpe encode result to word level.",
    )
    parser.add_argument(
        "--lambda_x",
        default=2.0,
        help="if true, will convert the bpe encode result to word level.",
    )

    args = parser.parse_args()
    print(args.test_only)
    print(args.convert_bpe)
    print(args.lambda_x)



