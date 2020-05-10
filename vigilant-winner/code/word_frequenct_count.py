import operator
import string
import sys
from collections import defaultdict


def lines_from_file(filename):
    """ a generator yielding lines from filename """
    with open(filename) as file_handler:
        for _line in file_handler:
            yield _line.strip('\n')


def words_from_line(lines):
    """ a generator yielding word from lines """
    for _line in lines:
        for _word in _line.split(' '):
            if _word not in string.whitespace:
                yield _word


def get_words_count(filename):
    word_count = defaultdict(int)
    lines = lines_from_file(filename)
    words = words_from_line(lines)
    for word in words:
        word_count[word] += 1
    return word_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("error: filename is required")
        print("-> word_count.py <filename> <top-N-word>")
        sys.exit()
    top_n_words = int(sys.argv[2]) if len(sys.argv) > 2 else None
    word_count = sorted(get_words_count(sys.argv[1]).items(),
                        key=operator.itemgetter(1), reverse=True)
    if top_n_words:
        print(word_count[:top_n_words], end='\n')
    else:
        print(word_count, end='\n')
