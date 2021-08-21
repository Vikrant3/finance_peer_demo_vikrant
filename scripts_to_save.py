from demo_app.models import FinancePeerUserData
from demo_app.fp_data import data
list_to_save = []


def save_finace_peer_data():
    for d in data:
        fpd = FinancePeerUserData(user_id=d['userId'], item_id=d['id'], title=d['title'], body=d['body'])
        list_to_save.append(fpd)
    FinancePeerUserData.objects.bulk_create(list_to_save, batch_size=500)
