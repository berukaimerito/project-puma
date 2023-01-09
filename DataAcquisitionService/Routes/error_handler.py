class ErrorHandler:
    def handle_rabbitmq_connection_error(self, request, exc):
        return {"error": "error connecting to RabbitMQ"}

    def handle_rabbitmq_channel_error(self, request, exc):
        return {"error": "error creating RabbitMQ channel"}

    def handle_value_error(self, request, exc):
        return {"error": "invalid value"}
