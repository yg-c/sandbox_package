def extract_db() -> str:
    print('extract db')
    return 'data'


def transform_db_data(data: str) -> str:
    print('transform db data')
    return 'data'


def load_db_data(data: str):
    print('load db data')


extracted_data = extract_db()
transformed_data = transform_db_data(data=extracted_data)
load_db_data(data=transformed_data)
