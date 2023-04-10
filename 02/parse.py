import json


def parse_json(
        keyword_callback, json_str: str, required_fields=None, keywords=None
):
    if keywords is None:
        print('keywords=None')

    json_doc = json.loads(json_str)
    for key, value in json_doc.items():
        if required_fields is not None and key in required_fields:
            if keywords is not None:
                for keyword in keywords:
                    if keyword in value.split(' '):
                        keyword_callback(keyword, key)
        elif required_fields is None:
            print('required_fields=None')
            break


# print(parse_json(
#                 keyword_callback=lambda x, y: print(len(x)+len(y)),
#                 json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
#                 required_fields=["key1"],
#                 keywords=["word1"]))
