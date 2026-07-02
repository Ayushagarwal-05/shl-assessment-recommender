from app.intent import IntentExtractor


class ConversationState:

    def __init__(self):
        self.extractor = IntentExtractor()

    def build(self, messages):
        """
        Reconstruct conversation state from all user messages.
        """

        intent = self.extractor.extract(messages)

        state = {
            "role": intent["role"],
            "purpose": intent["purpose"],
            "skills": intent["skills"],
            "compare": intent["compare"],
            "refine": intent["refine"],
            "conversation": " ".join(
                m["content"]
                for m in messages
                if m["role"] == "user"
            )
        }

        return state