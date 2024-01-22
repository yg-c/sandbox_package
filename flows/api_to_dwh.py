def extract_api() -> str:
    print('extract api')
    return 'data'


def transform_api_data(data: str) -> str:
    print('transform api data')
    return 'data'


def load_api_data(data: str):
    print('load api data')


extracted_data = extract_api()
transformed_data = transform_api_data(data=extracted_data)
load_api_data(data=transformed_data)
