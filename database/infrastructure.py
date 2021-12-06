from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import core as cdk


class Database(cdk.Construct):
    def __init__(
        self,
        scope: cdk.Construct,
        id_: str,
        *,
        dynamodb_billing_mode: dynamodb.BillingMode
    ):
        super().__init__(scope, id_)

        partition_key = dynamodb.Attribute(
            name="username", type=dynamodb.AttributeType.STRING
        )
        self.dynamodb_table = dynamodb.Table(
            self,
            "DynamoDbTable",
            billing_mode=dynamodb_billing_mode,
            partition_key=partition_key,
            removal_policy=cdk.RemovalPolicy.DESTROY,
        )
