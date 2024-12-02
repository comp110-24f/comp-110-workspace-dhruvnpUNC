def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx == len(scores) - 1
    if is_good:
        if is_last:
            return True
        else:
            return all_good(scores=scores, thresh=thresh, idx=idx + 1)
    else:
        return False


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "pip", "score": "7"},
]

print(all_good(scores=pack, thresh=7, idx=0))
