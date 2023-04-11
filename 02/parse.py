import json


def parse_json(
        keyword_callback, json_str: str, required_fields=None, keywords=None
):
    if keywords is None:
        print('keywords=None')

    if required_fields is None:
        print('required_fields=None')

    if keyword_callback is None:
        print('keyword_callback=None')

    if keywords is not None and \
            required_fields is not None and \
            keyword_callback is not None:
        json_doc = json.loads(json_str)
        for key, value in json_doc.items():
            if key in required_fields:
                for keyword in keywords:
                    if keyword in value.split(' '):
                        keyword_callback(keyword, key)


# print(parse_json(
#                 keyword_callback=lambda x, y: print(len(x)+len(y)),
#                 json_str='{"key1": "word1 word2", "key2": "word2 word3"}',
#                 required_fields=["key1"],
#                 keywords=["word1"]))
