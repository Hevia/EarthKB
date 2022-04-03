def rank_index_results(
    keyphrase_rankings: dict[str, list[str]],
    topic_rankings: dict[str, list[str]],
    top_n: int = 5,
) -> list[str]:
    count_dict: dict[str, int] = {}

    # Count up keyphrase results
    for key in keyphrase_rankings.keys():
        for file in keyphrase_rankings[key]:
            if file in count_dict:
                count_dict[file] += 1
            else:
                count_dict[file] = 1

    # Count up topic results
    for topic in topic_rankings.keys():
        for file in topic_rankings[topic]:
            if file in count_dict:
                count_dict[file] += 1
            else:
                count_dict[file] = 1

    print(count_dict)
