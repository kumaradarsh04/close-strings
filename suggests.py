class Suggestion:

    def __init__(self, wordlist: list[str], sort=False, reverse=False):

        self.keywords = sorted(wordlist, reverse=reverse) if sort else wordlist
        self.positions_dict = {}

        self._make_pair()

    def possible_keys(self, chars: str) -> list[str]:
        """
        Returns all possible suggestions out of the
        self.keywords which contains 'chars'
        """

        result = []

        # first check that if the first character of chars is possible to find in keywords
        if chars[0] in self.positions_dict.keys():
            indices = self.positions_dict[chars[0]]
            idx1, idx2 = indices[0], indices[1]

            for k in range(idx1, idx2 + 1):
                if chars == self.keywords[k][0:len(chars)]:
                    result.append(self.keywords[k])

        return result

    suggest_keys = possible_keys
    suggest_words = possible_keys

    def has_possibility(self, chars: str):
        """
        Returns true if there is at least 1 possible
        suggestion from self.keywords which contains 'chars'
        """""
        return len(self.possible_keys(chars)) > 0

    def update(self, newlist: list[str], sort=False, reverse=False):
        """ Creates new set of keywords using newlist and old keywords are deleted """

        self.positions_dict = {}
        self.keywords = sorted(newlist, reverse=reverse) if sort else newlist
        self._make_pair()

    def _make_pair(self):
        for i in range(len(self.keywords)):
            char = self.keywords[i][0]

            if not char in self.positions_dict.keys():
                self.positions_dict[char] = [i, i]
            elif char in self.positions_dict.keys():
                self.positions_dict[char][1] += 1
