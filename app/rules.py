class RuleEngine:
    """
    Handles business rules for the SHL recommendation agent.
    """

    UNSUPPORTED_SKILLS = {
        "rust",
        "golang",
        "go language",
        "elixir",
        "haskell",
    }

    OFF_TOPIC_KEYWORDS = [
        "salary",
        "resume",
        "cv",
        "cover letter",
        "legal",
        "law",
        "contract",
        "interview tips",
        "career advice",
        "visa",
        "immigration",
    ]

    PROMPT_INJECTION = [
        "ignore previous",
        "ignore all",
        "system prompt",
        "developer prompt",
        "repeat your instructions",
        "reveal your prompt",
        "forget previous",
    ]

    def check_unsupported_skill(self, conversation):
        conversation = conversation.lower()

        for skill in self.UNSUPPORTED_SKILLS:
            if skill in conversation:
                return skill

        return None

    def needs_clarification(self, state):
        """
        Don't ask for clarification if the user is comparing
        or refining existing recommendations.
        """

        if state["compare"]:
            return False
        
        if state["refine"]:
            return False
        
        return state["role"] is None

    def is_comparison(self, state):
        return state["compare"]

    def is_refinement(self, state):
        return state["refine"]

    def is_off_topic(self, conversation):
        conversation = conversation.lower()

        return any(
            keyword in conversation
            for keyword in self.OFF_TOPIC_KEYWORDS
        )

    def is_prompt_injection(self, conversation):
        conversation = conversation.lower()

        return any(
            keyword in conversation
            for keyword in self.PROMPT_INJECTION
        )

    def should_end(self, messages):
        if not messages:
            return False

        last = messages[-1]["content"].lower()

        confirmations = [
            "thanks",
            "thank you",
            "perfect",
            "looks good",
            "great",
            "that's all",
            "done"
        ]

        return any(word in last for word in confirmations)