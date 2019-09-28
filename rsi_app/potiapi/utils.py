from rsi_app.potiapi.models import Extract as ExtractModel

def create_transaction(date, account, value, description=None):
    new_extract = ExtractModel(
        date=date, value=value, account=account, description=description
    )
    new_extract.save_to_db()