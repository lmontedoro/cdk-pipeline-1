from aws_cdk import Stack
from constructs import Construct

from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class PipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline_id = "SamplePipeline"

        # TODO Update accordingly
        codestar_connection_arn = "arn:aws:codestar-connections:us-east-1..."
        repo_string = "your_user/cdk-pipeline-1"

        # Git Connection
        source_action = CodePipelineSource.connection(
            repo_string,
            branch="release",
            connection_arn=codestar_connection_arn,
        )

        CodePipeline(
            self,
            f"{pipeline_id}-stacks",
            pipeline_name=pipeline_id,
            synth=ShellStep(
                "Synth",
                input=source_action,
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth",
                ],
            ),
        )
