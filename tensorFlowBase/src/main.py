import argparse
import logging
import sys

logger = logging.getLogger(__name__)


def main(verbose, debug):
    """
    Runs the application.
    """
    pass


def add_args(parser):
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument('--verbose', help='Whether to run with verbose mode.',
                        default=True, type="bool", required=False)
    parser.add_argument('--debug', help='Whether to run with debug mode.',
                        default=False, type="bool", required=False)


def debug_main():
    # main()
    pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        debug_main()
        exit(0)
    parser = argparse.ArgumentParser(
        description='Generic task [Please fill out this description!]',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    add_args(parser)
    flags, unparsed = parser.parse_known_args()
    logger.info("Running with:")
    for option, value in vars(flags).items():
        logger.info("    {} -> {}".format(option, value))
    main(**vars(flags))
