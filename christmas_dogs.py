import arrow
import csv
from toot_it_out import send_toot, send_media


DOG_LIST_FILE = 'dog_list.txt'
DOG_LIST = []
XMAS_DOGS_LIST = []


def get_time():
    """ Gets time and returns a dictionary """
    utc = arrow.utcnow()
    local = utc.to('US/Pacific')
    # Get UNIX Epoc
    timestamp = int(local.timestamp())
    # Get human time
    json_date = local.for_json()
    today = local.format('YYYY-MM-DD')
    day = local.format('DD')
    time_dict = {
        'timestamp': timestamp,
        'datestamp': json_date,
        'today': today,
        'day': int(day)
    }
    return time_dict


def fill_toot_text(_daily_dog):
    """ Formulate toot based on dog """
    toot_text = f"""
    Today's Christmas Dog:
    
    {_daily_dog}
    
    #HappyHolidays
    #ChristmasDogs #StableDiffusion #AiArt

    """
    return toot_text


def make_dog_entry(_day, _dog, _text, _img):
    """ creates a daily entry for dog """
    entry = {
        "day": _day,
        "dog": _dog,
        "toot_text": _text,
        "toot_img": f"./dogs/{_img}"
    }
    XMAS_DOGS_LIST.append(entry)


def main():
    # get the date
    _today = get_time()
    with open('xmas.csv', 'r') as f:
        for line in csv.reader(f):
            # print(line)
            dog = line[0]
            img = line[1]
            day = line[2]
            make_dog_entry(
                _day=int(day),
                _dog=dog,
                _text=fill_toot_text(_daily_dog=dog),
                _img=img
            )
    # Get today's dog
    for dog in XMAS_DOGS_LIST:
        if _today['day'] == dog['day']:
            # matched dog to day
            # Post media to server, return media_id
            media_response = send_media(
                media_file=dog['toot_img'],
                description=dog['dog']
            )
            # post text + media_id [get toot_id in response]
            toot_response = send_toot(
                status=dog['toot_text'],
                media_ids=media_response['id']
            )


if __name__ == '__main__':
    main()
