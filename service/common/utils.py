# service/common/utils.py
# Counter storage
COUNTERS = {}


def reset_counters():
    """Reset the counters dictionary."""
    global COUNTERS
    COUNTERS = {}
