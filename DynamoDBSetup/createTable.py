import boto3
from decouple import config

if __name__ == "__main__":
    try:
        TABLE_NAME = config("RESTAURANTS_TABLE_NAME")
        dynamodb = boto3.client('dynamodb')
        if TABLE_NAME in dynamodb.list_tables()['TableNames']:
            print("\n%s table already exists" % TABLE_NAME)
        else:
            KEY_SCHEMA = [{
                "AttributeName": config("KEY_NAME"),
                "KeyType": "HASH"}]
            ATTRIBUTE_DEFINITIONS = [{
                "AttributeName": config("KEY_NAME"),
                "AttributeType": "S"}]
            PROVISIONED_THROUGHPUT = {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
            tbl_Restaurants = dynamodb.create_table(TableName=TABLE_NAME,
                                                    AttributeDefinitions = ATTRIBUTE_DEFINITIONS,
                                                    KeySchema=KEY_SCHEMA,
                                                    ProvisionedThroughput=PROVISIONED_THROUGHPUT)
            print("\n%s table created successfully" % TABLE_NAME)
    except Exception as ex:
        print("Error : ", ex.message)
