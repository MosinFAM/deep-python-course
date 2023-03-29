import json


# def keyword_callback(word):
#     return len(word)


def parse_json(
        keyword_callback, json_str: str, required_fields=None, keywords=None
):
    json_doc = json.loads(json_str)
    for key, value in json_doc.items():
        if required_fields is not None and key in required_fields:
            if keywords is not None:
                for keyword in keywords:
                    if keyword in value:
                        keyword_callback(keyword)


# print(parse_json(
#                 keyword_callback=lambda x: print(len(x)),
#                 json_str='{"key1": "Word1 word2", "key2": "word2 word3"}',
#                 required_fields=["key1"],
#                 keywords=["word2"]))
