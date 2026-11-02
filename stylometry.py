"""Text shape measurements; higher style scores mean more likely AI."""

import re
import statistics
import string


def sentences(text: str) -> list[str]:
    return [p for p in re.split(r"(?<=[.!?])\s+", text.strip()) if p.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_length_spread(text: str) -> float:
    lengths = [len(words(sentence)) for sentence in sentences(text)]
    if len(lengths) < 2 or not sum(lengths):
        return 0.0
    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    tokens = words(text)
    return len(set(tokens)) / len(tokens) if tokens else 0.0


def punctuation_density(text: str) -> float:
    return sum(c in string.punctuation for c in text) / len(text) if text else 0.0


def style_signal(text: str) -> float:
    # Short samples lack enough shape to support a useful style estimate.
    if len(sentences(text)) < 2 or len(words(text)) < 10:
        return 0.5
    regularity = 1 - min(sentence_length_spread(text), 1)
    repetition = 1 - type_token_ratio(text)
    sparse_punctuation = 1 - min(punctuation_density(text) / 0.1, 1)
    return round((regularity + repetition + sparse_punctuation) / 3, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or "The system works well. It handles most cases correctly and provides good results."
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}")
