import core
import modules

@core.cron(
    name="PING"
)
class PingJob(core.BaseLambdaFunction):
    def execute(
        self,
        event: core.LambdaEvent,
        context: core.DevOpsContext,
        notifier: core.SlackNotifier,
    ):
        return "PONG"

