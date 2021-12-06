from aws_cdk import aws_cloudwatch as cloudwatch
from aws_cdk import core as cdk

from api.infrastructure import Api
from database.infrastructure import Database


class Monitoring(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id_: str, *, database: Database, api: Api):
        super().__init__(scope, id_)

        widgets = [
            cloudwatch.SingleValueWidget(
                metrics=[api.api_gateway_http_api.metric_count()]
            ),
            cloudwatch.SingleValueWidget(
                metrics=[database.dynamodb_table.metric_consumed_read_capacity_units()]
            ),
        ]
        cloudwatch.Dashboard(self, "CloudWatchDashboard", widgets=[widgets])
